"""
Module: grid_methods.py
Description: Contains methods for Bayesian analysis as part of the Bayesian Workflow.

Includes methods for data preparation, prior probability assignment, likelihood calculation,
unnormalized posterior probability calculation, and normalization of posterior probabilities.
"""

import pandas as pd
import numpy as np
from scipy.stats import beta
from typing import List, Dict, Union, Optional

def slice_data_by_feature(*, data: pd.DataFrame, feature_column: str, feature_values: List[str]) -> pd.DataFrame:
    """
    Selects and returns rows from the given DataFrame where the specified feature column matches one of the feature values.

    Args:
        data (pd.DataFrame): The DataFrame to slice.
        feature_column (str): The name of the column to filter on.
        feature_values (List[str]): A list of values to include in the filter.

    Returns:
        pd.DataFrame: A DataFrame containing only the rows where the feature column matches one of the feature values.
    """
    return data[data[feature_column].isin(feature_values)]

def bin_land_use_values(*, data: pd.DataFrame, column: str, num_bins: int = 20) -> pd.DataFrame:
    """
    Bins the specified column's values into a given number of bins and adds a new column to the DataFrame with these bin labels.

    Args:
        data (pd.DataFrame): The DataFrame to modify.
        column (str): The name of the column to bin.
        num_bins (int, optional): The number of bins to use. Defaults to 20.

    Returns:
        pd.DataFrame: The modified DataFrame with an additional column for binned values.
    """
    data[f'{column}_bin'] = pd.qcut(data[column], q=num_bins, labels=False, duplicates='drop')
    return data

def calculate_pcs_per_meter_per_sample(*, data: pd.DataFrame, groupby_columns: List[str] = ['sample_id'], aggregate_funcs: Dict[str, Union[str, List[str]]] = {'pcs/m': 'sum'}) -> pd.DataFrame:
    """
    Aggregates the 'pcs/m' values per sample based on the specified groupby columns.

    Args:
        data (pd.DataFrame): The DataFrame containing the data to aggregate.
        groupby_columns (List[str], optional): Columns to group by. Defaults to ['sample_id'].
        aggregate_funcs (Dict[str, Union[str, List[str]]], optional): Functions to use for aggregating data. Defaults to {'pcs/m': 'sum'}.

    Returns:
        pd.DataFrame: A DataFrame with aggregated 'pcs/m' values per sample.
    """
    return data.groupby(groupby_columns).agg(aggregate_funcs).reset_index()

def calculate_beta_prior(*, grid_range: np.ndarray = np.linspace(0, 9.99, 1000), bin_density_numbers: List[int] = list(range(1, 21))) -> pd.DataFrame:
    """
    Calculates a Beta(1, 1) prior for each value in the specified grid range for each bin density number.

    Args:
        grid_range (np.ndarray, optional): The range of grid values. Defaults to np.linspace(0, 9.99, 1000).
        bin_density_numbers (List[int], optional): List of bin density numbers. Defaults to range(1, 21).

    Returns:
        pd.DataFrame: A DataFrame with Beta(1, 1) prior values for each grid value and bin density number.
    """
    prior_df = pd.DataFrame(index=grid_range)
    prior_values = beta.pdf(0.5, a=1, b=1)  # Constant value since Beta(1, 1) is uniform
    for bin_number in bin_density_numbers:
        prior_df[f'Bin_{bin_number}'] = prior_values
    return prior_df

def calculate_likelihood(*, aggregated_data: pd.DataFrame, bin_density_column: str, pcs_column: str = 'pcs/m', grid_range: np.ndarray = np.linspace(0, 9.99, 1000)) -> pd.DataFrame:
    """
    Calculates the likelihood of observing the aggregated pcs/m data for each grid point and bin density value.

    Args:
        aggregated_data (pd.DataFrame): The aggregated data to be used for likelihood calculation.
        bin_density_column (str): The column representing bin density numbers.
        pcs_column (str, optional): The pcs/m column to use for calculation. Defaults to 'pcs/m'.
        grid_range (np.ndarray, optional): The range of grid values. Defaults to np.linspace(0, 9.99, 1000).

    Returns:
        pd.DataFrame: A DataFrame with likelihood values for each grid value and bin density number.
    """
    likelihood_df = pd.DataFrame(index=grid_range)
    for bin_value in aggregated_data[bin_density_column].unique():
        bin_data = aggregated_data[aggregated_data[bin_density_column] == bin_value]
        likelihoods = [bin_data[pcs_column].gt(grid_point).mean() for grid_point in grid_range]
        likelihood_df[f'Likelihood_{bin_value}'] = likelihoods
    return likelihood_df

def calculate_unnormalized_posterior(*, prior_df: pd.DataFrame, likelihood_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the unnormalized posterior probabilities by multiplying the prior probabilities with the likelihoods for each grid value and bin density value.

    Args:
        prior_df (pd.DataFrame): The DataFrame containing the prior probabilities.
        likelihood_df (pd.DataFrame): The DataFrame containing the likelihood values.

    Returns:
        pd.DataFrame: A DataFrame with unnormalized posterior probabilities.
    """
    return prior_df.multiply(likelihood_df, axis=0)

def normalize_posterior(*, unnormalized_posterior_df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes the posterior probabilities in each column of the given DataFrame.

    Args:
        unnormalized_posterior_df (pd.DataFrame): The DataFrame containing the unnormalized posterior probabilities.

    Returns:
        pd.DataFrame: A DataFrame with normalized posterior probabilities.
    """
    normalized_posterior_df = unnormalized_posterior_df.copy()
    for column in unnormalized_posterior_df.columns:
        total = unnormalized_posterior_df[column].sum()
        normalized_posterior_df[column] = unnormalized_posterior_df[column] / total
    return normalized_posterior_df

# Additional helper functions can be added here.
