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
import session_config
import geospatial
import reports


def forecast_weighted_prior(land_use_profile, catalog_data, bin_labels, weighted_columns, likelihood_data, **kwargs):
    # make a prior that is comprised of random samples that are weighted by the
    # land use of interest. Make the posterior and draw samples
    g = weighted_prior(land_use_profile, catalog_data, bin_labels, weighted_columns, **kwargs)
    amodel = MulitnomialDirichlet('weighted prior', likelihood_data, g['pcs/m'])
    sample_values = amodel.sample_posterior()
    summary = amodel.get_descriptive_statistics()

    return sample_values, amodel, summary, g


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

def weighted_prior(land_use_profile, catalog_data, bin_labels, columns, ncols=1):
    sampled_data = []
    for feature in columns[:ncols]:
        for i in bin_labels:
            v = land_use_profile.loc[i, feature]
            if v > 0:
                sampler = catalog_data[catalog_data[feature] == i]
                samples = sampler.sample(v, replace=True)
                sampled_data.append(samples)
    sampled_data_df = pd.concat(sampled_data).drop_duplicates().reset_index(drop=True)
    return sampled_data_df


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
        raise KeyError("The dataframe does not contain a 'date' column ")

    # mask using the create_mask function
    mask = create_mask(datai, query_params)
    # Apply the mask to the dataframe
    filtered_data = datai[mask].copy()

    return filtered_data, filtered_data.location.unique()


def check_params(params, data):
    # check if the query parameters are valid and return the filtered data
    # and unique locations if the query is valid. Otherwise, return an error message.
    # and empty arrays.

    try:
        a, b = filter_data(data, query_params=params)
        if len(b) == 0:
            message = "No survey results found. "
            return [], [], message
        message = 'ok'
        return a, b, message

    except Exception as e:
        message = f"An error occurred: {str(e)}. Please check your query parameters and try again. "
        return [], [], message


def reports_and_forecast(likelihood_params: dict, prior_params: dict, ldata: pd.DataFrame,
                         feature_columns: [] = None, samples_needed: int = 100, other_data: pd.DataFrame = None):
    # utility function to make reports and forecasts. The function checks the likelihood and prior parameters
    # and returns the reports and forecasts if the parameters are valid. Otherwise, the function returns any available
    # reports and a boolean flag indicating that a forecast was not made.

    comments = ''
    make_forecast = True
    ldi, l_locations, c = check_params(likelihood_params, ldata.copy())
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        this_report, this_land_use = 'No likelihood', 'No likelihood'
    else:
        this_report, this_land_use = make_report_objects(ldi)
    pdf, p_locations, c = check_params(prior_params, ldata.copy())
    comments += f' {c}'
    if c != 'ok':
        make_forecast = False
        prior_report, prior_land_use = 'No prior', 'No prior'
    else:
        prior_report, prior_land_use = make_report_objects(pdf)

    if make_forecast:
        prr = prior_report.sample_results.groupby('sample_id')['pcs/m'].sum()

        lkl = this_report.sample_results.groupby('sample_id')['pcs/m'].sum()
        max_range = np.quantile(lkl.values, .99)

        # consider all values
        i = MulitnomialDirichlet('max value', prr, lkl)

        # limit to the 99th percentile
        limited = lkl[lkl <= max_range]
        h  = MulitnomialDirichlet('99th percentile', limited, prr)
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

    def __init__(self, code, prior_data, likelihood_data, nsamples=100):
        if len(prior_data) == 0 or len(likelihood_data) == 0:
            raise ValueError("Prior data or likelihood data cannot be empty.")

        self.code = code
        self.prior_data = prior_data
        self.likelihood_data = likelihood_data
        self.grid = self.compute_grid()
        self.prior = self.compute_counts(self.prior_data)
        self.likelihood = self.compute_counts(self.likelihood_data)
        self.posterior_params = self.compute_posterior_params()
        self.posterior_dist = dirichlet(self.posterior_params)
        self.posterior_samples = self.sample_posterior(nsamples)

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
        # print(adist_samples[:2])
        # print(sum(adist_samples))
        posterior_samples = multinomial.rvs(num_samples, adist_samples)
        sample_values = np.repeat(self.grid, posterior_samples)
        return sample_values

    def compute_percentiles(self, percentiles=[5, 25, 50, 75, 95]):
        samples = self.posterior_samples
        return np.percentile(samples, percentiles)

    def compute_hdi(self, credibility_mass=0.95):
        samples = self.posterior_samples
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
        equal_to_greater_than_x = np.sum(mp[bin_index[0]:])
        less_than_x = np.sum(mp[:bin_index[0]])
        results = {
            "less_than_x": less_than_x,
            "equal_to_greater_than_x": equal_to_greater_than_x
        }
        return pd.DataFrame([results])

    def get_descriptive_statistics(self):
        average = np.mean(self.posterior_samples)
        hdi_min, hdi_max = self.compute_hdi()
        percentiles = self.compute_percentiles()
        q_labels = {session_config.quantile_labels[i]: percentiles[i] for i in range(len(percentiles))}
        max_observed = max(self.prior_data.max(), self.likelihood_data.max())
        stats_dict = {
            "code": self.code,
            "average": average,
            **{'hdi min': hdi_min, 'hdi max': hdi_max},
            **q_labels,
            "max_observed": max_observed
        }
        results = pd.DataFrame([stats_dict])
        return results
