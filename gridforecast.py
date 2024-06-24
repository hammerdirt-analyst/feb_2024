"""
gridforecast.py
hammerdirt 2024
Author: Roger Erismann

NOTE: This module is a work in progress.

Implementation of a grid forecast using a Dirichlet-Multinomial conjugate. The module provides functions to
make reports and forecasts based on the likelihood and prior data. The module provides functions to
compute the posterior distribution, sample from the posterior, compute percentiles, compute the highest density
interval, compute the expected average, and compute the probability of x. The module also provides functions to
compute the descriptive statistics of the forecasted samples.

A Bayesian method is used because of how the data is collected. Each sample is an observation made by an individual that
can make mistakes, has an unknown amount of experience or physical limitations that we may not be aware of. Furthermore,
objects are difficult to identify due to erosion and decomposition. All of these factors contribute to the uncertainty
present in the data.

The land-use is an essential factor in the forecast. The land-use is used to weight the prior data. Comparing strictly on
a temporal scale assumes that the same types of locations was sampled from one epoch to another. This is not the case.
We note that comparing results on land use values is more appropriate than limiting the comparison to temporal or spatial
values. In simple terms, we are comparing apples to apples and not apples to oranges.
"""
import pandas as pd
import numpy as np
from scipy.stats import dirichlet, multinomial
from collections import defaultdict

import session_config
from session_config import index_range, max_range
import geospatial
import reports


def forecast_weighted_prior(landuse_of_interest, feature_variables, landuse_from_other, likelihood_data):
    # make a prior that is comprised of random samples that are weighted by the
    # land use of interest. Make the posterior and draw samples
    weights = land_use_weights(landuse_of_interest, feature_variables)
    g, w = select_prior_data_by_feature_weight(landuse_from_other, weights, feature_variables)
    posterior_by_weight, c = posterior_dirichlet_counts(likelihood_data, g['pcs/m'].values)
    sample_values, adist, summary = dirichlet_posterior(posterior_by_weight)

    return sample_values, adist, summary, g


def make_report_objects(df):
    # make a survey report and a landuse report
    # from filtered data
    this_report = reports.SurveyReport(dfc=df)

    # generate the parameters for the landuse report
    target_df = this_report.sample_results
    features = geospatial.collect_topo_data(locations=target_df.location.unique())

    # make a landuse report
    this_land_use = geospatial.LandUseReport(target_df, features)

    return this_report, this_land_use


def summary_of_forecasted_samples(vals):
    # calculate the quantiles, number of samples, average and highest density interval
    quantiles = np.quantile(vals, session_config.report_quantiles)
    nsamples = len(vals)
    average = np.mean(vals)
    highest_densitiy = hdi(vals)
    return {'range': quantiles, 'nsamples': nsamples, 'average': average, 'hdi': highest_densitiy}


def dirichlet_posterior(counts, nsamples: int = 100, **kwargs):
    # make a dirichlet distribution from counts
    # sample from the distribution, and return the samples
    # along with a summary of the samples
    adist = dirichlet(counts)
    posterior_samples = multinomial.rvs(nsamples, p=adist.rvs(1)[0])
    sample_len = len(counts)
    this_grid = index_range[:sample_len]
    sample_values = np.repeat([*this_grid[:-1], this_grid[-1] + .1], posterior_samples)
    summary = summary_of_forecasted_samples(sample_values)
    return sample_values, adist, summary


def land_use_weights(a_land_use_report, feature_variables):
    # the number of samples per feature and category divided by the number of unique samples
    wghts = a_land_use_report.n_samples_per_feature()[feature_variables]
    dvsr = a_land_use_report.df_cat.sample_id.nunique()
    weights = wghts/dvsr
    return  weights


def hdi(samples, cred_mass=.95):
    # calculate the highest density interval
    sorted_samples = np.sort(samples)
    n_samples = len(sorted_samples)
    n_cred_samples = int(np.floor(cred_mass * n_samples))

    # the intervals that include the desired number of samples
    interval_widths = sorted_samples[n_cred_samples:] - sorted_samples[:n_samples - n_cred_samples]

    # the shortest interval
    min_idx = np.argmin(interval_widths)
    hdi_min = sorted_samples[min_idx]
    hdi_max = sorted_samples[min_idx + n_cred_samples]

    return hdi_min, hdi_max


def the_number_of_samples_required(weights, feature_columns, samples_needed=100):
    # the number of samples required for each feature and magnitude
    # based on the weights from the likelihood data.

    required = defaultdict(int)
    weights['magnitude'] = weights.index
    for feature in feature_columns:
        for i, row in weights.iterrows():
            required[(feature, row['magnitude'])] = int(row[feature] * samples_needed)

    return required


def select_prior_data_by_feature_weight(odata, weights, feature_columns, samples_needed=100):
    # select the prior data based on the weights from the likelihood
    # from a set of data that does not include the likelihood data.
    required_samples = the_number_of_samples_required(weights, feature_columns, samples_needed=samples_needed)
    new_samples = pd.DataFrame()
    left_to_sample = odata.copy()
    selected_samples = set()

    # iterate through each feature and magnitude to collect the required samples
    for feature, magnitude in required_samples.keys():
        remaining_samples = required_samples[(feature, magnitude)]

        if remaining_samples > 0:
            # filter the data for the given feature and magnitude
            # print(magnitude)
            feature_data = left_to_sample[
                (left_to_sample[feature] == magnitude) & (~left_to_sample.index.isin(selected_samples))]

            # ensure we do not sample more than available
            available_samples = len(feature_data)
            if remaining_samples > available_samples:
                remaining_samples = available_samples

            # collect the required samples
            if remaining_samples > 0:
                sampled_feature_data = feature_data.sample(n=remaining_samples, replace=False)

                # add the indices of the selected samples to the set
                selected_samples.update(sampled_feature_data.index)

                # append the sampled data to the new_samples dataframe
                new_samples = pd.concat([new_samples, sampled_feature_data])

                # remove selected samples from the remaining sample data
                left_to_sample = left_to_sample.drop(sampled_feature_data.index)

                # update the remaining requirements
                for f in feature_columns:
                    if f != feature:
                        for m in sampled_feature_data[f].unique():
                            remaining_samples = required_samples[(f, m)]
                            selected_samples_count = sampled_feature_data[sampled_feature_data[f] == m].shape[0]
                            required_samples[(f, m)] = max(0, remaining_samples - selected_samples_count)

    new_samples = new_samples.reset_index(drop=True)
    # print(new_samples.columns)

    # weights of the newly sampled data
    
    new_weights = new_samples[feature_columns].apply(lambda x: x.value_counts(normalize=True)).fillna(0)
    return new_samples, new_weights


def create_mask(data, query_params):
    # create a boolean mask for the data based on query parameters including date range.
    # initialize the mask to True for all rows
    mask = pd.Series([True] * len(data))

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
    # filter the data based on the query parameters including date range.

    if 'date' in datai.columns:
        datai['date'] = pd.to_datetime(datai['date'])
    else:
        raise KeyError("The dataframe does not contain a 'date' column")

    # mask using the create_mask function
    mask = create_mask(datai, query_params)
    # Apply the mask to the dataframe
    filtered_data = datai[mask].copy()

    return filtered_data, filtered_data.location.unique()


def check_params(params, data, logger):
    # check if the query parameters are valid and return the filtered data
    # and unique locations if the query is valid. Otherwise, return an error message.
    # and empty arrays.

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
    # returns the resolution of the grid based off the max_range
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
    # the extent of the grid is determined by the max of the two distributions
    # the distribution with the lower max is extended to the higher max
    # the new grid is updated with 0.01 where there were no records
    hrmn_counts = np.array(
        [np.sum((higher_max > x) & (higher_max <= x + .1)) for x in index_range[index_range <= h_limit]])
    lrmn_counts = np.array(
        [np.sum((lower_max > x) & (lower_max <= x + .1)) for x in index_range[index_range <= h_limit]])

    hzero = sum(higher_max == 0)
    lzero = sum(lower_max == 0)
    zeroes = lzero + hzero

    # update prior with likelihood to get posterior counts
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
    # utility function to make reports and forecasts. The function checks the likelihood and prior parameters
    # and returns the reports and forecasts if the parameters are valid. Otherwise, the function returns any available
    # reports and a boolean flag indicating that a forecast was not made.

    comments = ''
    make_forecast = True
    ldi, l_locations, c = check_params(likelihood_params, ldata.copy(), logger)
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        this_report, this_land_use = 'No likelihood', 'No likelihood'
    else:
        this_report, this_land_use = make_report_objects(ldi)
    pdf, p_locations, c = check_params(prior_params, ldata.copy(), logger)
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        prior_report, prior_land_use = 'No prior', 'No prior'
    else:
        prior_report, prior_land_use = make_report_objects(pdf)

    if make_forecast:
        prr = prior_report.sample_results.groupby('sample_id')['pcs/m'].sum()

        lkl = this_report.sample_results.groupby('sample_id')['pcs/m'].sum()

        # consider all values
        i = MulitnomialDirichlet('comb', prr, lkl, logger)

        # limit to the 99th percentile
        h, c = posterior_dirichlet_counts(lkl, prr, max_range=max_range)
        comments += c
    else:
        i = 'no forecast'
        h = 'no forecast'
        comments += 'No forecast was made.'
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
    """ A class to implement the Multinomial-Dirichlet conjugate. The class is initialized with the code, prior data,
    and likelihood data. The class computes the grid, prior, likelihood, posterior parameters, and posterior distribution.
    The class can sample from the posterior, compute percentiles, compute the highest density interval, compute the expected
    average, and compute the probability of x. The class also provides descriptive statistics.

    The code parameter is used to identify the group of objects included in the prior and likelihood data.
    """
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
        logger.info("Initialized MultinomialDirichlet")

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

        posterior_samples = self.posterior_dist.rvs(1000)
        mp = np.mean(posterior_samples, axis=0)
        bin_index = np.digitize([x], self.grid)
        return mp, bin_index, posterior_samples

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
