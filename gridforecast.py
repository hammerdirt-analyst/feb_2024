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


# def make_report_objects(df):
#     # make a survey report and a landuse report
#     # from filtered data
#     this_report = reports.SurveyReport(dfc=df)
#
#     # generate the parameters for the landuse report
#     target_df = this_report.sample_results
#     features = geospatial.collect_topo_data(locations=target_df.location.unique())
#
#     # make a landuse report
#     this_land_use = geospatial.LandUseReport(target_df, features)
#
#     return this_report, this_land_use

def weighted_prior(land_use_profile, catalog_data, bin_labels, columns, ncols=1):
    sampled_data = []

    for feature in columns[:ncols]:

        for i in bin_labels:
            v = land_use_profile.loc[i, feature]

            if v > 0:
                sampler = catalog_data[catalog_data[feature] == i]
                if len(sampler) > 0:

                    samples = sampler.sample(v, replace=True)
                    sampled_data.append(samples)
    sampled_data_df = pd.concat(sampled_data).drop_duplicates().reset_index(drop=True)
    return sampled_data_df






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
        max_predicted = max(self.posterior_samples)
        stats_dict = {
            "average": average,
            **{'hdi min': hdi_min, 'hdi max': hdi_max},
            **q_labels,
            "max predicted": max_predicted
        }
        # results = pd.DataFrame([stats_dict])
        result = pd.DataFrame(stats_dict.values(), index=list(stats_dict.keys()), columns=['expected'])
        return result
