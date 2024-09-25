"""
gridforecast.py
hammerdirt 2024
Author: Roger Erismann

Implementation of a grid forecast using inference tables and priors based on sampling stratification and geographic
proximity. The module provides functions to make reports and forecasts based on the likelihood and prior data.
The module provides functions to compute the posterior distribution, sample from the posterior, compute percentiles,
compute the highest density interval, compute the expected average, and compute the probability of x. The module also
provides functions to compute the descriptive statistics of the forecasted samples.

A Bayesian method is used because of how the data is collected. Each sample is an observation made by an individual that
can make mistakes, has an unknown amount of experience or physical limitations that we may not be aware of. Furthermore,
objects are difficult to identify due to erosion and decomposition. All of these factors contribute to the uncertainty
present in the data.

The land-use is an essential factor in the forecast. The land-use is used to weight the prior data. Comparing strictly on
a temporal scale assumes that the same types of locations were sampled from one epoch to another. This is not the case.
We note that comparing results on land use values is more appropriate than limiting the comparison to temporal or spatial
values. In simple terms, we are comparing apples to apples and not apples to oranges.

Dependencies
------------
- pandas
- numpy
- session_config
- reports

Functions
---------
- calculate_proportions(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame
- manhattan_distance(row: pd.Series, target: pd.Series) -> float
- calculate_similarity(row: pd.Series, proportions_A: pd.DataFrame) -> float
- sample_like_subset_general(data: pd.DataFrame, subset_A: pd.DataFrame, label: str, similarity_columns: list[str] = ['buildings', 'forest', 'undefined']) -> dict

Classes
-------
- GridForecast
    - __init__(self, likelihood, report_meta, data)
    - collect_prior_data(self, data: pd.DataFrame) -> pd.DataFrame
    - evaluate_prior_data(self, data: pd.DataFrame) -> dict
    - inference_tables(self) -> dict
    - sampling_stratification(self, label: str) -> pd.DataFrame
    - rate_per_feature(self, label: str) -> pd.DataFrame
    - report_draft(self, file_name: str = None) -> str
"""
import pandas as pd
import numpy as np
from session_config import grid_approximation_def, construct_report_label
import matplotlib.pyplot as plt
import reports
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean, cityblock
from math import ceil
import scipy.stats as stats
from typing import Optional, Dict


def normalize_streets(pool_of_locations, a_single_location):
    """
    Normalize the 'streets' column in both the pool_of_locations and a_single_location DataFrames
    using MinMaxScaler.
    """
    scaler = MinMaxScaler()

    pool_of_locations['streets'] = scaler.fit_transform(pool_of_locations[['streets']])

    a_single_location['streets'] = scaler.transform(a_single_location[['streets']])

    return pool_of_locations, a_single_location

def calculate_cosine_similarity(pool_of_locations, a_single_location, feature_variables):
    """
    Calculate cosine similarity between the rows of a_single_location and each row in
    pool_of_locations based on the feature variables.
    """
    feature_matrix = pool_of_locations[feature_variables].values
    sample_vector = a_single_location[feature_variables].values.flatten()

    similarities = cosine_similarity([sample_vector], feature_matrix)
    return similarities[0]

def calculate_euclidean_distance(pool_of_locations, a_single_location, feature_variables):
    """
    Calculate Euclidean distance between a_single_location and each row in
    pool_of_locations based on the feature variables.
    """
    feature_matrix = pool_of_locations[feature_variables].values
    sample_vector = a_single_location[feature_variables].values.flatten()
    distances = [euclidean(sample_vector, row) for row in feature_matrix]

    return distances

def calculate_manhattan_distance(pool_of_locations, a_single_location, feature_variables):
    """
    Calculate Manhattan distance between a_single_location and each row in
    pool_of_locations based on the feature variables.
    """
    feature_matrix = pool_of_locations[feature_variables].values
    sample_vector = a_single_location[feature_variables].values.flatten()
    distances = [cityblock(sample_vector, row) for row in feature_matrix]

    return distances

def find_similar_locations(pool_of_locations, a_single_location, feature_variables, metric='cosine',
                           similarity_threshold=0.7):
    """
    Find and return locations from pool_of_locations based on the similarity of
    the feature variables to a_single_location using the specified metric.

    the feature variables to a_single_location using the specified metric.
    Locations are selected if their similarity score exceeds the similarity_threshold.
    """
    available_features = list(set(feature_variables) & set(a_single_location.columns) & set(pool_of_locations.columns))

    assert available_features, "No common feature variables available for comparison."

    assert not pool_of_locations[
        available_features].isnull().values.any(), "Missing values in pool_of_locations for selected features."
    assert not a_single_location[
        available_features].isnull().values.any(), "Missing values in a_single_location for selected features."

    # normalize 'streets'
    if 'streets' in available_features:
        pool_of_locations, a_single_location = normalize_streets(pool_of_locations, a_single_location)

    if metric == 'cosine':
        scores = calculate_cosine_similarity(pool_of_locations, a_single_location, available_features)
        score_type = 'similarity'
    elif metric == 'euclidean':
        scores = calculate_euclidean_distance(pool_of_locations, a_single_location, available_features)
        score_type = 'distance'
    elif metric == 'manhattan':
        scores = calculate_manhattan_distance(pool_of_locations, a_single_location, available_features)
        score_type = 'distance'
    else:
        raise ValueError("Invalid metric specified. Choose from 'cosine', 'euclidean', or 'manhattan'.")

    similarity_scores = list(zip(pool_of_locations['location'], scores))

    if score_type == 'similarity':
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    else:
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1])

    if score_type == 'similarity':
        selected_locations = [(loc, score) for loc, score in sorted_scores if score >= similarity_threshold]
    else:
        selected_locations = [(loc, score) for loc, score in sorted_scores if score <= similarity_threshold]

    return selected_locations

def calculate_optimal_weights(similar_locations, survey_data, n, used_sample_ids, max_samples_per_location=None):
    location_weights = {}
    total_available = 0

    if not isinstance(used_sample_ids, set):
        used_sample_ids = set()

    for location, _ in similar_locations:

        available_data = survey_data[
            (survey_data['location'] == location) &
            (~survey_data['sample_id'].astype(str).isin([str(x) for x in used_sample_ids]))
            ]
        available_count = len(available_data)

        if available_count > 0:
            if max_samples_per_location:
                available_count = min(available_count, max_samples_per_location)
            location_weights[location] = available_count
            total_available += available_count

    if total_available > 0:
        for location in location_weights:
            proportional_weight = (location_weights[location] / total_available) * n
            location_weights[location] = max(ceil(proportional_weight), 1)  # Use ceil to avoid rounding down to zero
            # print(f"Location: {location}, Calculated samples: {location_weights[location]}")

    return location_weights

def select_samples(survey_data, location_weights, used_sample_ids, n):
    samples = []
    total_collected = 0  # Counter to keep track of total samples collected

    if not isinstance(used_sample_ids, set):
        used_sample_ids = set()

    while total_collected < n:
        no_samples_drawn = True  # Flag to check if we are still drawing samples

        for location, sample_count in location_weights.items():
            # stop if the desired number of samples has been collected
            if total_collected >= n:
                break

            if sample_count > 0:
                available_data = survey_data[
                    (survey_data['location'] == location) &
                    (~survey_data['sample_id'].astype(str).isin([str(x) for x in used_sample_ids]))
                    ]

                if not available_data.empty:
                    num_samples_to_take = min(sample_count, len(available_data), n - total_collected)
                    selected_samples = available_data.sample(num_samples_to_take, replace=False)
                    samples.append(selected_samples)
                    used_sample_ids.update(selected_samples['sample_id'])

                    total_collected += num_samples_to_take
                    # print(f"Collected {num_samples_to_take} samples from location: {location}. Total collected: {total_collected}")

                    # Flag that we've drawn samples in this loop iteration
                    no_samples_drawn = False

        if no_samples_drawn:
            break

    if samples:
        sampled_data = pd.concat(samples, ignore_index=True)
    else:
        sampled_data = pd.DataFrame(columns=survey_data.columns)

    return sampled_data

class SampleSelector:
    def __init__(self, feature_data, prior_data, feature_variables, a_single_location, metric: str = 'cosine',
                 n: int = 50, threshold: float = .95, max_samples_per_location: int = 10):
        self.feature_data = feature_data
        self.prior_data = prior_data
        self.feature_variables = feature_variables
        self.metric = metric
        self.threshold = threshold
        self.max_samples_per_location = max_samples_per_location
        self.used_sample_ids = set()
        self.n = n
        self.similar_locations = find_similar_locations(feature_data, a_single_location, feature_variables, metric,
                                                        threshold)

    @property
    def optimal_weights(self):
        location_weights = calculate_optimal_weights(self.similar_locations, self.prior_data, self.n,
                                                     self.used_sample_ids, self.max_samples_per_location)
        return location_weights

    def samples(self):
        sampleddata = select_samples(self.prior_data, self.optimal_weights, self.used_sample_ids, self.n)
        return sampleddata

    def sample_data(self, similarity_threshold: float = None, n: int = None):
        if similarity_threshold is not None:
            self.similarity_threshold = similarity_threshold
        if n is not None:
            self.n = n

        sampled_data = self.samples()

        weights_info = []
        total_samples = len(sampled_data)
        if total_samples > 0:
            for location in sampled_data.location.unique():
                actual_count = sampled_data[sampled_data['location'] == location].shape[0]
                weights_info.append({
                    'location': location,
                    'weight': actual_count / total_samples,
                    'similarity_score': dict(self.similar_locations).get(location, 0)
                })
        weights_df = pd.DataFrame(weights_info)

        return sampled_data, weights_df

class ProportionalSampleSelector:

    def __init__(self, survey_data, weight_df, feature_variables, metric='cosine', max_samples_per_location=10,
                 threshold=0.99):
        """
        Initializes the ProportionalSampleSelector with required data.

        Parameters:
        - feature_data: DataFrame containing feature variables for locations.
        - survey_data: DataFrame with survey samples including 'sample_id' and 'location'.
        - weight_df: DataFrame containing locations, weights, and feature variables.
        - feature_variables: List of feature variables used for similarity calculations.
        - metric: Similarity metric to use ('cosine', 'euclidean', etc.).
        - max_samples_per_location: Maximum samples to draw per location.
        - threshold: Similarity threshold for selecting similar locations (default is 0.99).
        """
        self.feature_data = survey_data.drop_duplicates('location')
        self.survey_data = survey_data
        self.weight_df = weight_df
        self.feature_variables = feature_variables
        self.metric = metric
        self.max_samples_per_location = max_samples_per_location
        self.used_sample_ids = set()
        self.threshold = threshold
        self.similarity_scores = {}

    def proportional_sample_data(self, n):
        """
        Samples data proportionally based on the weights specified in the weight_df.

        Parameters:
        - n: Total number of samples to collect across all locations.

        Returns:
        - A DataFrame with the collected samples.
        """
        all_samples = []

        for index, row in self.weight_df.iterrows():
            location = row['location']
            weight = row['weight']
            required_samples = max(int(weight * n), 1)

            similar_locations = find_similar_locations(self.feature_data.copy(), pd.DataFrame(row).T,
                                                       self.feature_variables, self.metric, self.threshold)
            num_similar = len(similar_locations)

            for loc, score in similar_locations:
                self.similarity_scores[loc] = score

            if num_similar > required_samples:
                required_samples = min(num_similar, required_samples)

            # Calculate optimal weights for similar locations
            location_weights = calculate_optimal_weights(similar_locations, self.survey_data, required_samples,
                                                         self.used_sample_ids, self.max_samples_per_location)

            # Select samples based on calculated weights
            sampled_data = select_samples(self.survey_data, location_weights, self.used_sample_ids,
                                          required_samples)

            # Only add non-empty DataFrames
            if not sampled_data.empty:
                all_samples.append(sampled_data)

        # Combine all collected samples into a single DataFrame if there are valid samples
        if all_samples:  # Check if all_samples is not empty
            final_sampled_data = pd.concat(all_samples, ignore_index=True)
            final_sampled_data['similarity'] = final_sampled_data['location'].map(self.similarity_scores)
        else:
            final_sampled_data = pd.DataFrame(
                columns=self.survey_data.columns)  # Return an empty DataFrame with the same columns as survey_data

        return final_sampled_data

    def generate_weights_table(self, sampled_data):
        """
        Generates a weights table for the sampled data, reflecting the distribution of samples across locations,
        including the similarity scores of each location used.

        Parameters:
        - sampled_data: DataFrame of collected samples.

        Returns:
        - A DataFrame showing the weights, counts, and similarity scores of each location in the sampled data.
        """
        weights_info = []
        total_samples = len(sampled_data)

        if total_samples > 0:
            for location in sampled_data['location'].unique():
                actual_count = sampled_data[sampled_data['location'] == location].shape[0]
                similarity_score = self.similarity_scores.get(location,
                                                              None)  # Get the similarity score for the location
                weights_info.append({
                    'location': location,
                    'weight': actual_count / total_samples,
                    'count': actual_count,
                    'similarity_score': similarity_score
                })

        weights_df = pd.DataFrame(weights_info)
        return weights_df

class BetaBinomialModel:
    def __init__(self, prior: np.ndarray, likelihood: np.ndarray, report_meta: Dict,
                 grid_interval: float = 0.01, percentile_grid_max: float = 0.99) -> None:
        if 'name' not in report_meta:
            raise ValueError("The 'report_meta' dictionary must contain at least the key 'name' with a value.")

        # Validate prior and likelihood as arrays of floats
        self.prior = np.array(prior, dtype=float)
        self.likelihood = np.array(likelihood, dtype=float)
        self.grid_interval = grid_interval
        self.percentile_grid_max = percentile_grid_max
        self.name = report_meta['name']
        self.grid: Optional[np.ndarray] = None

        self._posterior_distributions = None
        self._prior_successes = None
        self._likelihood_successes = None

        self.generate_grid()

    def generate_grid(self) -> np.ndarray:
        prior_percentile = np.percentile(self.prior, self.percentile_grid_max * 100)
        likelihood_percentile = np.percentile(self.likelihood, self.percentile_grid_max * 100)
        grid_max = max(prior_percentile, likelihood_percentile)
        self.grid = np.arange(0, grid_max + self.grid_interval, self.grid_interval)
        return self.grid

    @property
    def prior_successes(self) -> np.ndarray:
        if self._prior_successes is None:
            self._prior_successes = np.sum(self.prior[:, np.newaxis] >= self.grid, axis=0)
        return self._prior_successes

    @property
    def likelihood_successes(self) -> np.ndarray:
        if self._likelihood_successes is None:
            self._likelihood_successes = np.sum(self.likelihood[:, np.newaxis] >= self.grid, axis=0)
        return self._likelihood_successes

    @property
    def calculate_posterior(self) -> np.ndarray:
        if self._posterior_distributions is None:
            prior_failures = len(self.prior) - self.prior_successes
            likelihood_failures = len(self.likelihood) - self.likelihood_successes

            alpha_posterior = self.prior_successes + self.likelihood_successes
            beta_posterior = prior_failures + likelihood_failures

            alpha_posterior = np.where(alpha_posterior == 0, 1, alpha_posterior)
            beta_posterior = np.where(beta_posterior == 0, 1, beta_posterior)

            self._posterior_distributions = stats.beta(alpha_posterior, beta_posterior)
        return self._posterior_distributions

    def sample_posterior(self, n_samples: int) -> np.ndarray:
        posterior_samples = self.calculate_posterior.rvs(size=(n_samples, len(self.grid)))
        return posterior_samples

    def sample_grid_based_on_posterior(self, n_samples: int) -> np.ndarray:
        # Generate the posterior probabilities for each grid point
        posterior_probs = self.calculate_posterior.mean()  # Use the posterior mean as the probability for each grid point

        # Normalize posterior probabilities to ensure they sum to 1
        posterior_probs_normalized = posterior_probs / posterior_probs.sum()

        # Sample grid values based on the posterior probabilities
        sampled_grid_points = np.random.choice(self.grid, size=n_samples, p=posterior_probs_normalized)

        return sampled_grid_points

    def plot_cdf_comparison(self, prior: np.ndarray, likelihood: np.ndarray,
                            sampled_posterior: np.ndarray) -> plt.Figure:
        """Returns a CDF comparison plot of prior, likelihood, and posterior samples."""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.ecdfplot(prior, label='Prior', color='green', ax=ax)
        sns.ecdfplot(likelihood, label='Likelihood', color='red', ax=ax)
        sns.ecdfplot(sampled_posterior, label='Posterior Samples', color='blue', ax=ax)
        ax.set_title(f'CDF Comparison: Prior, Likelihood, and Posterior Samples for {self.name}')
        ax.set_xlabel('Grid Points')
        ax.set_ylabel('Cumulative Probability')
        ax.legend()

        plt.close()
        return fig

    def plot_pdf_comparison(self, prior: np.ndarray, likelihood: np.ndarray,
                            sampled_posterior: np.ndarray) -> plt.Figure:
        """Returns a PDF comparison plot of prior, likelihood, and posterior samples using histograms."""
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(prior, bins=30, label='Prior', color='green', alpha=0.6, density=True)
        ax.hist(likelihood, bins=30, label='Likelihood', color='red', alpha=0.6, density=True)
        ax.hist(sampled_posterior, bins=30, label='Posterior Samples', color='blue', alpha=0.6, density=True)
        ax.set_title(f'PDF Comparison: Prior, Likelihood, and Posterior Samples for {self.name}')
        ax.set_xlabel('Grid Points')
        ax.set_ylabel('Density')
        ax.legend()
        plt.close()
        return fig

    def __repr__(self) -> str:
        """Returns a string representation of the BetaBinomialModel object."""
        return (f"BetaBinomialModel(name='{self.name}', "
                f"prior_samples={len(self.prior)}, "
                f"likelihood_samples={len(self.likelihood)}, "
                f"grid_interval={self.grid_interval}, "
                f"percentile_grid_max={self.percentile_grid_max})")

class GridForecast:
    """
    A class to perform grid forecasting using Bayesian inference.

    This class implements a grid forecast using inference tables and priors based on sampling stratification and geographic proximity.
    It provides methods to generate reports and forecasts based on the likelihood and prior data, compute the posterior distribution,
    sample from the posterior, compute percentiles, compute the highest density interval, compute the expected average, and compute
    the probability of x. It also provides methods to compute the descriptive statistics of the forecasted samples.

    Attributes
    ----------
    likelihood : pd.DataFrame
        The DataFrame containing the likelihood data.
    report_meta : dict
        Metadata for the report, including filters and boundaries.
    data : pd.DataFrame
        The input data used for generating priors.
    likelihood_locations : np.ndarray
        Unique locations from the likelihood data.
    info_columns : list[str]
        List of columns containing information about the data.
    priors : dict
        Dictionary containing the prior data, in-boundary data, and out-boundary data.
    features : list[str]
        List of features used for stratification and similarity calculations.
    valid_priors : list[str]
        List of valid priors identified during the inference process.

    Methods
    -------
    collect_prior_data(data: pd.DataFrame) -> pd.DataFrame
        Collect prior data based on the report metadata.
    evaluate_prior_data(data: pd.DataFrame) -> dict
        Evaluate prior data based on the report metadata.
    inference_tables() -> dict
        Generate inference tables based on the likelihood and prior data.
    sampling_stratification(label: str) -> pd.DataFrame
        Calculate the stratification of samples based on specified features.
    rate_per_feature(label: str) -> pd.DataFrame
        Calculate the average rate per feature for the specified label.
    report_draft(file_name: str = None) -> str
        Generate a draft report of the grid forecast.
    """

    def __init__(self, likelihood, report_meta, data):
        self.likelihood = likelihood
        self.likelihood_locations = likelihood.location.unique()
        self.report_meta = report_meta
        self.info_columns = ['canton', 'city', 'feature_name']
        self.features = ['buildings', 'forest', 'undefined']
        self.priors = self.evaluate_prior_data(data, n=30)
        self.valid_priors = []
        self.posteriors = {}

    def collect_prior_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Collect prior data based on the report metadata.

        This function filters the input data based on the report metadata, excluding the likelihood samples.

        Parameters
        ----------
        data : pd.DataFrame
            The input DataFrame containing the data to be filtered.

        Returns
        -------
        pd.DataFrame
            The filtered DataFrame containing the prior data.

        Raises
        ------
        ValueError
            If the input data is not a DataFrame or if required columns are missing.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")

        # prior_filters = list(self.report_meta.keys())

        if self.report_meta['feature_type'] is not None:
            feature_type_mask = data['feature_type'] == self.report_meta['feature_type']
            data = data[feature_type_mask]

        if self.report_meta['report_codes'] is not None:
            code_mask = data['code'].isin(self.report_meta['report_codes'])
            data = data[code_mask]

        return data[~data['location'].isin(self.likelihood_locations)]

    def evaluate_prior_data(self, data: pd.DataFrame, n) -> dict:

        prior_data = self.collect_prior_data(data)

        if len(prior_data) == 0:
            return {'combined_prior': pd.DataFrame(), 'in_boundary': pd.DataFrame(), 'out_boundary': pd.DataFrame()}
        # print(prior_data.columns, len(prior_data))
        _, prior_landusei = reports.make_report_objects(prior_data, info_columns=self.info_columns)
        # print(prior_landusei.df_cont.head())
        try:
            # Make report objects from the prior data
            _, prior_landusei = reports.make_report_objects(prior_data, info_columns=self.info_columns)
            # print(prior_landusei.head())
            prior_landuse = prior_landusei.df_cont.reset_index(drop=True)
        except Exception:
            print('there is an exception')
            return {'combined_prior': pd.DataFrame(), 'in_boundary': pd.DataFrame(), 'out_boundary': pd.DataFrame()}

        sampledpriors = {
            'combined': pd.DataFrame(),
            'in_boundary': pd.DataFrame(),
            'out_boundary': pd.DataFrame()
        }
        lweights = self.likelihood[['location', *self.features]].drop_duplicates('location')
        lweights = lweights.merge(self.likelihood.location.value_counts(), left_on='location', right_index=True)
        lweights['weight'] = lweights['count'] / lweights['count'].sum()
        lweights.reset_index(drop=True, inplace=True)

        available_combined = prior_landuse.drop_duplicates('location').reset_index()

        if len(available_combined) > 0:
            selector_feature_combined = ProportionalSampleSelector(
                prior_landuse.copy(),
                lweights.copy(),
                self.features,
                metric='cosine',
                max_samples_per_location=10,
                threshold=0.95)
            sampledpriors.update({'combined': selector_feature_combined.proportional_sample_data(n=n)})

        if self.report_meta['boundary'] is not None:
            in_boundary_mask = (prior_landuse[self.report_meta['boundary']] == self.report_meta['boundary_name'])
            in_boundary = prior_landuse[in_boundary_mask].copy()
            out_boundary_mask = (prior_landuse[self.report_meta['boundary']] != self.report_meta['boundary_name'])
            out_boundary = prior_landuse[out_boundary_mask].copy()

            if self.report_meta['feature_name'] is not None:
                name_mask = (in_boundary['feature_name'] == self.report_meta['feature_name'])
                feature_in_bounds = in_boundary[name_mask].copy()

                available_in = feature_in_bounds.drop_duplicates('location').reset_index()
                if len(available_in) > 0:
                    selector_feature_in_boundary = ProportionalSampleSelector(
                        feature_in_bounds.copy(),
                        lweights.copy(),
                        self.features,
                        metric='cosine',
                        max_samples_per_location=10,
                        threshold=0.95)
                    sampledpriors.update({'in_boundary': selector_feature_in_boundary.proportional_sample_data(n=n)})

                available_out = out_boundary.drop_duplicates('location').reset_index()
                if len(available_out) > 0:
                    selector_feature_out_boundary = ProportionalSampleSelector(
                        out_boundary.copy(),
                        lweights.copy(),
                        self.features,
                        metric='cosine',
                        max_samples_per_location=10,
                        threshold=0.95
                    )
                    sampledpriors.update({'out_boundary': selector_feature_out_boundary.proportional_sample_data(n=n)})
                self.priors = sampledpriors
                return sampledpriors

            else:
                available_in = in_boundary.drop_duplicates('location').reset_index()
                if len(available_in) > 0:
                    selector_feature_in_boundary = ProportionalSampleSelector(
                        in_boundary.copy(),
                        lweights.copy(),
                        self.features,
                        metric='cosine',
                        max_samples_per_location=10,
                        threshold=0.95
                    )
                    sampledpriors.update({'in_boundary': selector_feature_in_boundary.proportional_sample_data(n=n)})

                available_out = out_boundary.drop_duplicates('location').reset_index()
                if len(available_out) > 0:
                    selector_feature_out_boundary = ProportionalSampleSelector(
                        out_boundary.copy(),
                        lweights.copy(),
                        self.features,
                        metric='cosine',
                        max_samples_per_location=10,
                        threshold=0.95
                    )
                    sampledpriors.update({'out_boundary': selector_feature_out_boundary.proportional_sample_data(n=n)})
                self.priors = sampledpriors
                return sampledpriors

        if self.report_meta['feature_name'] is not None:
            print('in feature name')

            in_boundary_mask = (prior_landuse['feature_name'] == self.report_meta['feature_name'])
            in_boundary = prior_landuse[in_boundary_mask].copy()
            available_in = in_boundary.drop_duplicates('location').reset_index()
            if len(available_in) > 0:
                selector_feature_in_boundary = ProportionalSampleSelector(
                    in_boundary.copy(),
                    lweights.copy(),
                    self.features,
                    metric='cosine',
                    max_samples_per_location=10,
                    threshold=0.95
                )
                sampledpriors.update({'in_boundary': selector_feature_in_boundary.proportional_sample_data(n=n)})

            out_boundary_mask = (prior_landuse['feature_name'] != self.report_meta['feature_name'])
            out_boundary = prior_landuse[out_boundary_mask].copy()
            available_out = out_boundary.drop_duplicates('location').reset_index()
            if len(available_out) > 0:
                selector_feature_out_boundary = ProportionalSampleSelector(
                    out_boundary.copy(),
                    lweights.copy(),
                    self.features,
                    metric='cosine',
                    max_samples_per_location=10, threshold=0.95
                )
                sampledpriors.update({'out_boundary': selector_feature_out_boundary.proportional_sample_data(n=n)})

            self.priors = sampledpriors
            return sampledpriors

        self.priors = sampledpriors
        return sampledpriors

    def inference_tables(self) -> dict:

        valid_priors = {}
        nvalid_priors = 0
        nsamples = len(self.likelihood)

        for label in self.priors.keys():
            if len(self.priors[label]) > 0:
                nvalid_priors += 1
                self.valid_priors.append(label)
                setattr(self, label, self.priors[label])
                valid_priors.update({label: self.priors[label]})

        if nvalid_priors == 0:
            section_head = f"### Prior grid approximation"
            poster_limits = f"{section_head}\nNo valid priors were found."
            return {'prior': {'dataframe': pd.DataFrame(), 'prompt': poster_limits}}

        predictions = {}

        for prior_type, aprior in valid_priors.items():
            print(f"Processing {prior_type}...")

            model = BetaBinomialModel(prior=aprior['pcs/m'].values, likelihood=self.likelihood['pcs/m'].values,
                                      report_meta=self.report_meta)
            posterior_samples = model.sample_grid_based_on_posterior(n_samples=100)

            posterior_samples = pd.DataFrame(posterior_samples, columns=['pcs/m'])
            section_head = f"### {' '.join(prior_type.split('_')).capitalize()} grid approximation"
            poster_limits = f"{section_head}\nThe expected posterior distribution is a grid approximation from 0 to {model.grid.max()} every 0.01."
            similarity_score = f'average cosine similarity score of prior samples {round(aprior["similarity"].mean(), 2)}'
            poster_limits = f"{poster_limits}\n\n{similarity_score} "
            prompt = f"{poster_limits}\n\n{posterior_samples[['pcs/m']].describe().to_markdown()}"

            predictions.update({prior_type: {'dataframe': (posterior_samples, model), 'prompt': prompt}})

        return predictions

    def report_draft(self, file_name: str = None) -> dict:
        """
        Generate a draft report of the grid forecast.

        This function generates a draft report of the grid forecast based on the current forecast and appends it to a specified file.
        If no file is specified, it returns the report as a string.

        Parameters
        ----------
        file_name : str, optional
            The name of the file to which the report will be appended. If not provided, the report is returned as a string.

        Returns
        -------
        str
            The generated report as a string if no file name is provided.

        Raises
        ------
        ValueError
            If the file name is invalid or if there is an error writing to the file.
        """
        report_label = construct_report_label(self.report_meta)
        current_forecast = self.inference_tables()

        if file_name is not None:
            # here we want to append to a specific document or create a new one
            title = f"\n## Grid forecast {report_label}\n\n"
            title_and_def = f"{title}{grid_approximation_def}\n\n"
            try:
                with open(file_name, 'a') as file:
                    file.write(title_and_def)
                    for forecast_type, forecast in current_forecast.items():
                        file.write(forecast['prompt'])
            except FileNotFoundError:
                with open(file_name, 'w') as file:
                    file.write(title_and_def)
                    for forecast_type, forecast in current_forecast.items():
                        file.write(forecast['prompt'])
        else:
            # this method is called from another report class and
            # it appends the block of text to the report
            report_string = f"\n## Grid forecast {report_label}\n\n{grid_approximation_def}\n\n"
            for forecast_type, forecast in current_forecast.items():
                report_string += forecast['prompt'] + "\n\n"
            return {'dataframe': current_forecast, 'prompt': report_string}

