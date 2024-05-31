""" Dirichlet-Multinomial Distribution

"""

import pandas as pd
import numpy as np
from scipy.stats import dirichlet, multinomial
from collections import defaultdict

import session_config
from session_config import index_range, max_range
import geospatial
import reports



columns =  [
    'sample_id',
    'code',
    'quantity',
    'pcs/m',
    'feature_name',
    'location',
    'parent_boundary',
    'city',
    'canton',
    'feature_type',
    'date'
]


def make_report_objects(df):


    # make a report for the likelihood data
    this_report = reports.SurveyReport(dfc=df)
    # print('making prior')

    # generate the parameters for the landuse report
    target_df = this_report.sample_results
    features = geospatial.collect_topo_data(locations=target_df.location.unique())

    # make a landuse report
    this_land_use = geospatial.LandUseReport(target_df, features)

    return this_report, this_land_use


def summary_of_forecasted_samples(vals):
    quantiles = np.quantile(vals, session_config.report_quantiles)
    nsamples = len(vals)
    average = np.mean(vals)
    highest_densitiy = hdi(vals)
    return {'range': quantiles, 'nsamples': nsamples, 'average': average, 'hdi': highest_densitiy}


def dirichlet_posterior(counts, nsamples: int = 100, **kwargs):
    adist = dirichlet(counts)

    posterior_samples = multinomial.rvs(nsamples, p=adist.rvs(1)[0])
    sample_len = len(counts)
    this_grid = index_range[:sample_len]
    sample_values = np.repeat([*this_grid[:-1], this_grid[-1] + .1], posterior_samples)
    summary = summary_of_forecasted_samples(sample_values)
    return sample_values, adist, summary

def land_use_weights(a_land_use_report, feature_variables):
    wghts = a_land_use_report.n_samples_per_feature()[feature_variables]
    dvsr = a_land_use_report.df_cat.sample_id.nunique()
    weights = wghts/dvsr
    return  weights
def hdi(samples, cred_mass=.95):
    # Sort the samples
    sorted_samples = np.sort(samples)

    # Calculate the number of included samples in the interval
    n_samples = len(sorted_samples)
    n_cred_samples = int(np.floor(cred_mass * n_samples))

    # Compute the width of intervals that include the desired number of samples
    interval_widths = sorted_samples[n_cred_samples:] - sorted_samples[:n_samples - n_cred_samples]

    # Find the shortest interval
    min_idx = np.argmin(interval_widths)

    # Return the HDI
    hdi_min = sorted_samples[min_idx]
    hdi_max = sorted_samples[min_idx + n_cred_samples]

    return hdi_min, hdi_max

def the_number_of_samples_required(weights, feature_columns, samples_needed=100):
    required = defaultdict(int)
    weights['magnitude'] = weights.index
    for feature in feature_columns:
        for i, row in weights.iterrows():
            required[(feature, row['magnitude'])] = int(row[feature] * samples_needed)
    return required


def select_prior_data_by_feature_weight(odata, weights, feature_columns, samples_needed=100):
    required_samples = the_number_of_samples_required(weights, feature_columns, samples_needed=samples_needed)
    new_samples = pd.DataFrame()
    left_to_sample = odata.copy()
    selected_samples = set()

    # Iterate through each feature and magnitude to collect the required samples
    for feature, magnitude in required_samples.keys():
        remaining_samples = required_samples[(feature, magnitude)]

        if remaining_samples > 0:
            # Filter the data for the given feature and magnitude
            feature_data = left_to_sample[
                (left_to_sample[feature] == magnitude) & (~left_to_sample.index.isin(selected_samples))]

            # Ensure we do not sample more than available
            available_samples = len(feature_data)
            if remaining_samples > available_samples:
                remaining_samples = available_samples

            # Collect the required samples
            if remaining_samples > 0:
                sampled_feature_data = feature_data.sample(n=remaining_samples, replace=False)

                # Add the indices of the selected samples to the set
                selected_samples.update(sampled_feature_data.index)

                # Append the sampled data to the new_samples dataframe
                new_samples = pd.concat([new_samples, sampled_feature_data])

                # Remove selected samples from the remaining sample data
                left_to_sample = left_to_sample.drop(sampled_feature_data.index)

                # Update the remaining requirements for other features in the selected samples
                for f in feature_columns:
                    if f != feature:
                        for m in sampled_feature_data[f].unique():
                            remaining_samples = required_samples[(f, m)]
                            selected_samples_count = sampled_feature_data[sampled_feature_data[f] == m].shape[0]
                            required_samples[(f, m)] = max(0, remaining_samples - selected_samples_count)

    # Reset the index of the sampled data
    new_samples = new_samples.reset_index(drop=True)

    # Calculate the weights of the newly sampled data
    new_weights = new_samples[feature_columns].apply(lambda x: x.value_counts(normalize=True)).fillna(0)
    return new_samples, new_weights


def create_mask(data, query_params):
    """
    Create a boolean mask for the data based on query parameters including date range.

    Parameters:
    data (pd.DataFrame): The input dataframe.
    query_params (dict): Dictionary of query parameters where key is the column name and value is the filter value.

    Returns:
    pd.Series: A boolean mask for the dataframe.
    """
    # Initialize the mask to True for all rows
    mask = pd.Series([True] * len(data))

    # Apply query parameters to the mask
    for key, value in query_params.items():
        if key == 'date_range':
            start_date = pd.to_datetime(value['start'])
            end_date = pd.to_datetime(value['end'])
            mask &= (data['date'] >= start_date) & (data['date'] <= end_date)
        elif key in data.columns:
            mask &= (data[key] == value)
        else:
            raise KeyError(f"Key '{key}' not found in data columns")

    return mask


def filter_data(datai, query_params):
    """
    Filter the data based on the query parameters including date range.

    Parameters:
    data (pd.DataFrame): The input dataframe to filter.
    query_params (dict): Dictionary of query parameters where key is the column name and value is the filter value.

    Returns:
    pd.DataFrame: The filtered dataframe.
    """
    # Ensure the 'date' column is of datetime type
    if 'date' in datai.columns:
        datai['date'] = pd.to_datetime(datai['date'])
    else:
        raise KeyError("The dataframe does not contain a 'date' column")

    # Create the mask using the create_mask function
    mask = create_mask(datai, query_params)

    # Apply the mask to the dataframe
    filtered_data = datai[mask]

    return filtered_data, filtered_data.location.unique()


def check_params(params, data, logger):

    try:
        a, b = filter_data(data, query_params=params)
        if len(b) == 0:
            message = "No survey results found."
            logger.error(message)
            return [], [], message
        message = 'ok'
        logger.info(f'query {message}')
        return a, b, message

    except Exception as e:
        message = f"An error occurred: {str(e)}. Please check your query parameters and try again."
        logger.error(message)
        return [], [], message


def grid_resolution_range(l, p, max_range: float = .99):
    if len(l) == 0:
        this_limit = 0
    else:
        this_limit = round(np.quantile(l, max_range), 1)

    if len(p) == 0:
        prior_limit = 0
    else:
        prior_limit = round(np.quantile(p, max_range), 1)

    return this_limit, prior_limit


def extend_the_prior_or_likelihood(higher_max, lower_max, h_limit, l_limit, comment: str = "no comment",
                                   grid_scale: int = 10):
    hrmn_counts = np.array(
        [np.sum((higher_max > x) & (higher_max <= x + .1)) for x in index_range[index_range <= h_limit]])
    lrmn_counts = np.array(
        [np.sum((lower_max > x) & (lower_max <= x + .1)) for x in index_range[index_range <= h_limit]])

    hzero = sum(higher_max == 0)
    lzero = sum(lower_max == 0)
    zeroes = lzero + hzero

    # Update prior with likelihood to get posterior counts
    posterior_counts_x = hrmn_counts + lrmn_counts
    posterior_counts_i = np.array([zeroes, *posterior_counts_x])

    posterior_counts = np.where(posterior_counts_i > 0, posterior_counts_i, .01)

    return posterior_counts, comment
def posterior_dirichlet_counts(regional_likelihood, regional_prior, max_range: float = .99, grid_scale: int = None):
    # the regional likelihood and prior come from the previously excluded
    # data, either by geography or use type. The logic here is we are using
    # the data we have on hand from similar locations but not in same

    this_limit, prior_limit = grid_resolution_range(regional_likelihood, regional_prior, max_range=max_range)

    comments = "Making the posterior counts, "

    if this_limit > 0 and prior_limit > 0:
        comments += 'this is the regional likelihood and prior, '
        if this_limit >= prior_limit:
            comments += 'The likelihood has a higher max, '
            posterior, c = extend_the_prior_or_likelihood(regional_likelihood, regional_prior, this_limit, prior_limit,
                                                          comment=comments)
            return posterior, c
        if this_limit < prior_limit:
            comments += 'The regional prior has a higher max. '
            posterior, c = extend_the_prior_or_likelihood(regional_prior, regional_likelihood, prior_limit, this_limit,
                                                          comment=comments)
            return posterior, c
    if this_limit == 0 or prior_limit == 0:
        if this_limit > 0:
            comments += 'The prior limit is zero. The prior at each value on the grid is 0.01. Consider using a different prior. '
            posterior, c = extend_the_prior_or_likelihood(regional_likelihood, regional_prior, this_limit, prior_limit,
                                                          comment=comments)
            return posterior, c
        elif prior_limit > 0:
            comments += 'The likelihood limit is zero. The likelihood at each value on the grid is 0.01. '
            posterior, c = extend_the_prior_or_likelihood(regional_prior, regional_likelihood, this_limit, prior_limit,
                                                          comment=comments)
            return posterior, c
        else:
            comments += 'there were no records for that query check the survey report for the most common objects we are assuming a uniform distribution on the range of 0-10'
            posterior = np.ones(100)
            return posterior, comments


def reports_and_forecast(likelihood_params: dict, prior_params: dict, ldata: pd.DataFrame,
                         feature_columns: [] = None, samples_needed: int = 100, other_data: pd.DataFrame = None, logger = None):
    comments = ''
    ldi, l_locations, c = check_params(likelihood_params, ldata.copy(), logger)
    if c != 'ok':
        return [], c
    this_report, this_land_use = make_report_objects(ldi)
    comments += c

    pdf, p_locations, c = check_params(prior_params, ldata.copy(), logger)
    comments += c

    if c == 'No survey results found.':
        use_case = prior_params['feature_type']
        odf = other_data[
            (other_data['feature_type'] == use_case) & (~other_data.sample_id.isin(this_report.df.sample_id.unique()))].copy()
        other_report, other_land_use = make_report_objects(odf)
        d = other_land_use.df_cat[~other_land_use.df_cat.location.isin(l_locations)].copy()
        weights = this_land_use.n_samples_per_feature()[feature_columns] / this_report.number_of_samples
        if len(ldi) < 100:
            new_data, weights = select_prior_data_by_feature_weight(d, weights, feature_columns, samples_needed=len(ldi))
        else:
            new_data, weights = select_prior_data_by_feature_weight(d, weights, feature_columns, samples_needed=samples_needed)

        prior_report, prior_land_use = make_report_objects(new_data)
    else:
        prior_report, prior_land_use = make_report_objects(pdf)

        # collect the results from the prior and the likelihood
    prr = prior_report.sample_results.groupby('sample_id')['pcs/m'].sum()
    lkl = this_report.sample_results.groupby('sample_id')['pcs/m'].sum()

    # consider all values
    i = MulitnomialDirichlet('comb', prr, lkl, logger)

    # limit to the 99th percentile
    h, c = posterior_dirichlet_counts(lkl, prr, max_range=max_range)
    comments += c
    results = dict(
        this_report=this_report,
        this_land_use=this_land_use,
        prior_report=prior_report,
        prior_land_use=prior_land_use,
        posterior_no_limit=i,
        posterior_99=h,
        comments=comments
    )

    return results


class MulitnomialDirichlet:
    def __init__(self, code, prior_data, likelihood_data, logger):
        if len(prior_data) == 0 or len(likelihood_data) == 0:
            logger.error("Prior data or likelihood data cannot be empty.")
            raise ValueError("Prior data or likelihood data cannot be empty.")

        self.code = code
        self.prior_data = prior_data
        self.likelihood_data = likelihood_data
        self.grid = self.compute_grid()
        self.prior = self.compute_counts(self.prior_data)
        self.likelihood = self.compute_counts(self.likelihood_data)
        self.posterior_params = self.compute_posterior_params()
        self.posterior_dist = dirichlet(self.posterior_params)
        logger.info(f"Initialized MultinomialDirichlet")

    def compute_grid(self):
        max_value = round(max(self.prior_data.max(), self.likelihood_data.max()), 1)
        return np.arange(0, max_value, 0.01)

    def compute_counts(self, data):
        counts, _ = np.histogram(data,
                                 bins=np.append(self.grid, self.grid[-1] + 0.1))
        return counts

    def compute_posterior_params(self):
        post_counts = self.likelihood + self.prior
        post_counts = np.where(post_counts > 0, post_counts, 0.01)
        return post_counts

    def sample_posterior(self, num_samples=100):
        adist_samples = self.posterior_dist.rvs(1)[0]
        posterior_samples = multinomial.rvs(num_samples, adist_samples)
        sample_values = np.repeat(self.grid, posterior_samples)
        return sample_values

    def compute_percentiles(self, percentiles=[5, 25, 50, 75, 95]):
        samples = self.sample_posterior(1000)
        return np.percentile(samples, percentiles)

    def compute_hdi(self, credibility_mass=0.95):
        samples = self.sample_posterior(1000)
        sorted_samples = np.sort(samples)
        ci_idx_inc = int(np.floor(credibility_mass * len(sorted_samples)))
        n_cis = len(sorted_samples) - ci_idx_inc
        ci_width = sorted_samples[ci_idx_inc:] - sorted_samples[:n_cis]
        min_ci_width_idx = np.argmin(ci_width)
        hdi_min = sorted_samples[min_ci_width_idx]
        hdi_max = sorted_samples[min_ci_width_idx + ci_idx_inc]
        return hdi_min, hdi_max

    def compute_expected_average(self):
        return self.posterior_dist.mean()

    def probability_of_x(self, x):
        if x < 0 or x > self.grid.max():
            raise ValueError("x must be within the range of the grid.")

        posterior_samples = self.posterior_dist.rvs(10000)
        mp = np.mean(posterior_samples, axis=0)
        bin_index = np.digitize([x], self.grid)[0] - 1
        return mp[bin_index]

    def get_descriptive_statistics(self):
        average = np.mean(self.sample_posterior())
        hdi_min, hdi_max = self.compute_hdi()
        percentiles = self.compute_percentiles()
        max_observed = max(self.prior_data.max(), self.likelihood_data.max())
        stats_dict = {
            "code": self.code,
            "average": average,
            "hdi": (hdi_min, hdi_max),
            "range": percentiles,
            "max_observed": max_observed
        }
        return stats_dict
