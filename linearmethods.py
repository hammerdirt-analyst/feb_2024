"""
linearmethods.py
hammerdirt 2024
Author: Roger Erismann

This module provides classes and functions for performing linear and ensemble regression analyses, cluster analyses, and
feature importance evaluations.

Dependencies
------------
- pandas
- numpy
- sklearn.preprocessing.StandardScaler
- sklearn.preprocessing.MinMaxScaler
- sklearn.linear_model.LinearRegression
- sklearn.linear_model.TheilSenRegressor
- sklearn.ensemble.RandomForestRegressor
- sklearn.ensemble.GradientBoostingRegressor
- sklearn.ensemble.BaggingRegressor
- sklearn.ensemble.VotingRegressor
- sklearn.model_selection.train_test_split
- sklearn.cluster.KMeans
- sklearn.metrics.r2_score
- sklearn.metrics.mean_squared_error
- sklearn.exceptions.ConvergenceWarning
- sklearn.inspection.permutation_importance
- session_config

Classes
-------
LinearMethods
    A class to perform various linear and ensemble regression analyses, cluster analyses, and feature importance
    evaluations.

Functions
---------
a_model_feature_importance_prompt(table: str) -> str
    Generate a prompt to summarize the model feature importance.
a_permutation_feature_importance_prompt(table: str) -> str
    Generate a prompt to summarize the permutation feature importance.
cluster_composition_prompt(table: str) -> str
    Generate a prompt to summarize the cluster composition.
cluster_rates_prompt(table: str) -> str
    Generate a prompt to summarize the cluster rates.
regression_results_prompt(table: str) -> str
    Generate a prompt to summarize the regression results.
filter_features(data: pd.DataFrame, threshold: float = 0.2, terms: list[str] = None) -> list[str]
    Filter features based on a threshold.
find_elbow_point(sse: list[float]) -> int
    Find the elbow point in a list of sum of squared errors (SSE).
determine_optimal_clusters(d: pd.DataFrame) -> tuple[int, list[float]]
    Determine the optimal number of clusters using the elbow method.
perform_regression_analysis(d: pd.DataFrame, features: list[str] = None, target_var: str = 'pcs/m') -> tuple
    Perform regression analysis using various models.
evaluate_feature_importance(best_model: object, X_test: pd.DataFrame, y_test: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]
    Evaluate the feature importance using the provided model.
"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor, VotingRegressor
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.exceptions import ConvergenceWarning
import warnings
from sklearn.inspection import permutation_importance

from session_config import permutation_feature_importance, cluster_analysis_description, construct_report_label
from session_config import linear_regression_description, feature_importance_description
from session_config import Y
prd = "".join(permutation_feature_importance)
cdud = "".join(cluster_analysis_description)
lrd = "".join(linear_regression_description)
frd = "".join(feature_importance_description)

def a_model_feature_importance_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the model feature importance.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the model feature importance for each feature.

    Parameters
    ----------
    table : str
        The table containing the model feature importance data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the model feature importance.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    feature_importance_prompt = (
        "The following table details the model feature importance.\n\n"
        "Table has the following format:\n\n"
        "1. Feature: the name of the land-use feature\n"
        "2. importance: The model feature importance\n\n"
        "Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:\n\n"
        "{table}\n"
    ).format(table=table)
    return feature_importance_prompt

def a_permutation_feature_importance_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the permutation feature importance.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the permutation feature importance for each feature.

    Parameters
    ----------
    table : str
        The table containing the permutation feature importance data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the permutation feature importance.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    feature_importance_prompt = (
        "The following table details the permutation feature importance.\n\n"
        "Table has the following format:\n\n"
        "1. Feature: the name of the land-use feature\n"
        "2. importance: The model feature importance\n\n"
        "Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:\n\n"
        "{table}\n"
    ).format(table=table)
    return feature_importance_prompt

def cluster_composition_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the cluster composition.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the cluster composition for each feature.

    Parameters
    ----------
    table : str
        The table containing the cluster composition data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the cluster composition.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    cluster_prompt = (
        "The following are the summary results of a cluster analysis. The columns are the features that were used to make the clusters. The optimal number of clusters was\n"
        "determined using the elbow method (you can check the docs for this: https://hammerdirt-analyst.github.io/feb_2024/titlepage.html). The table displays the average magnitude\n"
        "of each feature in the cluster. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location that was\n"
        "45% dedicated to forest.\n\n"
        "Table has the following format:\n\n"
        "1. the columns are the measured land use features\n"
        "2. the index is the cluster number\n"
        "3. the value is the proportion of the cluster that is attributed to that column. For example if buildings in cluster 1 = .17 it means that the average magnitude of\n"
        "the buildings variable was 0.17 in cluster 1.\n\n"
        "Convert the following table into a paragraph, reporting the values for each column along with their cluster number values without any comments or analysis:\n\n"
        "{table}\n"
    ).format(table=table)
    return cluster_prompt

def cluster_rates_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the cluster rates.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the observed sample average per cluster.

    Parameters
    ----------
    table : str
        The table containing the cluster rates data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the cluster rates.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    cluster_rates = (
        "The following are the observed sample average per cluster. The units is objects per meter of beach. The columns are the use case of the objects: personal or professional. The index is\n"
        "the cluster number.\n\n"
        "Table has the following format:\n\n"
        "1. the columns are the object use case\n"
        "2. the index is the cluster number\n"
        "3. the value is the objects found per meter of beach\n\n"
        "Convert the following table into a paragraph, reporting the values for each column along with their respective cluster values without any comments or analysis:\n"
        "The narrative needs to be in paragraph format.\n\n"
        "{table}\n"
    ).format(table=table)
    return cluster_rates

def regression_results_prompt(table: str) -> str:
    """
    Generate a prompt to summarize the regression results.

    This function creates a prompt to generate a narrative summary of the provided table,
    detailing the results from different regression analyses.

    Parameters
    ----------
    table : str
        The table containing the regression results data in markdown format.

    Returns
    -------
    str
        The formatted prompt for generating a summary of the regression results.

    Raises
    ------
    ValueError
        If the table is None.
    """
    if table is None:
        raise ValueError("Table cannot be None")

    prompt = (
        "\n\n"
        "The following table details the results from different regression analysis of our data.\n\n"
        "The table has the following format:\n\n"
        "1. Model: the type of regression model used\n"
        "2. R²: The coefficient of determination\n"
        "3. MSE: the mean squared error\n\n"
        "Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.\n"
        "The narrative needs to be in paragraph format.\n\n"
        "{table}\n"
    ).format(table=table)
    return prompt

def filter_features(data: pd.DataFrame, threshold: float = 0.2, terms: list[str] = None) -> list[str]:
    """
    Filter features based on a threshold.

    This function filters the columns of the provided DataFrame based on the given threshold.
    Only columns where the proportion of non-zero values is greater than or equal to the threshold are retained.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the data to be filtered.
    threshold : float, optional
        The threshold for filtering columns (default is 0.2).
    terms : list of str, optional
        The list of column names to be filtered (default is None).

    Returns
    -------
    list of str
        The list of filtered column names.

    Raises
    ------
    ValueError
        If the terms parameter is None.
    """
    if terms is None:
        raise ValueError("Terms cannot be None")

    filtered_columns = [col for col in terms if (data[col] > 0).mean() >= threshold]
    return filtered_columns

def find_elbow_point(sse: list[float]) -> int:
    """
    Find the elbow point in a list of sum of squared errors (SSE).

    This function determines the optimal number of clusters by finding the point
    where the SSE starts to decrease more slowly, known as the elbow point.

    Parameters
    ----------
    sse : list of float
        The list of sum of squared errors for different numbers of clusters.

    Returns
    -------
    int
        The index of the elbow point in the SSE list.
    """
    n_points = len(sse)
    all_coords = np.vstack((range(n_points), sse)).T
    first_point = all_coords[0]
    last_point = all_coords[-1]

    line_vec = last_point - first_point
    line_vec_norm = line_vec / np.sqrt(np.sum(line_vec ** 2))

    vec_from_first = all_coords - first_point
    scalar_product = np.sum(vec_from_first * line_vec_norm, axis=1)
    vec_from_first_parallel = np.outer(scalar_product, line_vec_norm)
    vec_to_line = vec_from_first - vec_from_first_parallel

    dist_to_line = np.sqrt(np.sum(vec_to_line ** 2, axis=1))
    elbow_point = np.argmax(dist_to_line)

    return elbow_point

def determine_optimal_clusters(d: pd.DataFrame) -> tuple[int, list[float]]:
    """
    Determine the optimal number of clusters using the elbow method.

    This function calculates the sum of squared errors (SSE) for different numbers of clusters
    and identifies the optimal number of clusters by finding the elbow point.

    Parameters
    ----------
    d : pd.DataFrame
        The DataFrame containing the data to be clustered.

    Returns
    -------
    tuple
        A tuple containing the optimal number of clusters and the list of SSE values.
    """
    sse = []
    k_range = range(1, 10)
    for k in k_range:
        if k > len(d):
            break
        kmeans = KMeans(n_clusters=k, random_state=42)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            kmeans.fit(d)
            sse.append(kmeans.inertia_)

    optimal_k = find_elbow_point(sse)
    return optimal_k, sse

def perform_regression_analysis(d: pd.DataFrame, features: list[str] = None, target_var: str = Y) -> tuple:
    """
    Perform regression analysis using various models.

    This function performs regression analysis using different models and returns the results,
    the best model, and predictions.

    Parameters
    ----------
    d : pd.DataFrame
        The DataFrame containing the data to be analyzed.
    features : list of str, optional
        The list of feature column names to be used in the regression (default is None).
    target_var : str, optional
        The name of the target variable column (default is 'pcs/m').

    Returns
    -------
    tuple
        A tuple containing the regression results, the best model, the name of the best model,
        the predictions, the test and train data for features and target variable.
    """
    params = {
        "n_estimators": 100,
        "max_depth": 4,
        "min_samples_split": 5,
        "learning_rate": 0.01,
        "loss": "huber",
        "alpha": .9
    }
    these_models = {
        'Linear Regression': LinearRegression(),
        'Random Forest Regression': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting Regression': GradientBoostingRegressor(**params),
        'Theil-Sen Regressor': TheilSenRegressor(random_state=42)
    }
    target_scaler = StandardScaler()
    feature_scaler = StandardScaler()
    street_scaler = StandardScaler()

    cluster_d = d.copy()

    # the streets and target variable are scaled separately
    cluster_d[Y] = target_scaler.fit_transform(cluster_d[[Y]])
    cluster_d['streets'] = street_scaler.fit_transform(cluster_d[['streets']])

    # scale the rest of the features
    polygons_not_lines = [x for x in features if x != 'streets']
    cluster_d[polygons_not_lines] = feature_scaler.fit_transform(cluster_d[polygons_not_lines])
    cluster_d.reset_index(drop=True, inplace=True)

    X = cluster_d[features]
    y = cluster_d[target_var]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    regression_results = []
    best_model = None
    best_r2 = -np.inf
    the_name = None

    # sklearn - linear models
    for model_name, model in these_models.items():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            regression_results.append({'Model': model_name, 'R²': r2, 'MSE': mse})

            if r2 > best_r2:
                best_r2 = r2
                best_model = model
                the_name = model_name

    # bagging
    bag_estimator = these_models[the_name]
    bag = BaggingRegressor(estimator=bag_estimator)
    bag.fit(X_train, y_train)
    y_pred = bag.predict(X_test)
    predictions = {
        the_name: best_model.predict(X_test),
        'Bagging': y_pred
    }

    regression_results.append(
        {'Model': f'Bagging:{the_name}', 'R²': bag.score(X_test, y_test), 'MSE': mean_squared_error(y_test, y_pred)}
    )

    # voting
    lnr = these_models['Linear Regression']
    rf = these_models['Random Forest Regression']
    gbr = these_models['Gradient Boosting Regression']
    voting = VotingRegressor([('lnr', lnr), ('rf', rf), ('gbr', gbr)])
    voting.fit(X_train, y_train)
    y_pred = voting.predict(X_test)
    predictions.update({'voting': y_pred})

    regression_results.append(
        {'Model': 'Voting', 'R²': voting.score(X_test, y_test), 'MSE': mean_squared_error(y_test, y_pred)}
    )

    return regression_results, best_model, the_name, predictions, X_test, y_test, X_train, y_train

def evaluate_feature_importance(best_model: object, X_test: pd.DataFrame, y_test: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Evaluate the feature importance using the provided model.

    This function calculates both the model feature importance and the permutation importance
    of features using the provided model and test data, and returns the results in DataFrames.

    Parameters
    ----------
    best_model : object
        The trained model used for evaluating feature importance.
    X_test : pd.DataFrame
        The test data containing the features.
    y_test : pd.Series
        The test data containing the target variable.

    Returns
    -------
    tuple
        A tuple containing two DataFrames: one for the model feature importance and one for the permutation importance.
    """
    # Calculate permutation importance
    perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=30, random_state=42)
    perm_importance_df = pd.DataFrame({
        'Feature': X_test.columns,
        'Importance': perm_importance.importances_mean
    }).sort_values(by='Importance', ascending=False)

    # Try to calculate model feature importance or coefficients
    try:
        feature_importances_rf = best_model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'Feature': X_test.columns,
            'Importance': feature_importances_rf
        }).sort_values(by='Importance', ascending=False)
    except AttributeError:
        try:
            params = best_model.coef_
            feature_importance_df = pd.DataFrame({
                'Feature': X_test.columns,
                'Coefficient': params
            }).sort_values(by='Coefficient', ascending=False)
        except AttributeError:
            feature_importance_df = pd.DataFrame()

    return feature_importance_df, perm_importance_df

class LinearMethods:
    """
    A class to perform various linear and ensemble regression analyses, cluster analyses, and feature importance
    evaluations.

    This class provides methods to:
    - Perform cluster analysis on the provided data.
    - Perform linear and ensemble regression analysis using various models.
    - Evaluate the feature importance using the best model.
    - Generate a string representation of the cluster and regression analysis.

    Attributes
    ----------
    report_meta : dict
        Metadata for the report.
    survey_report : pd.DataFrame
        DataFrame containing the survey report data.
    landuse_report : pd.DataFrame
        DataFrame containing the land use report data.
    prior_report : pd.DataFrame, optional
        DataFrame containing the prior report data (default is None).
    columns_of_interest : list of str
        List of columns of interest for the analysis.
    nsamples : int
        Number of samples in the survey report.
    nlocations : int
        Number of locations in the survey report.
    filtered_columns : list of str
        List of filtered columns based on a threshold.
    chat : bool
        Flag indicating whether chat is enabled (default is False).
    cluster_d : pd.DataFrame, optional
        DataFrame containing the cluster analysis results (default is None).
    best_model_name : str, optional
        Name of the best model selected during regression analysis (default is None).
    best_model : object, optional
        The best model selected during regression analysis (default is None).
    predictions : dict, optional
        Dictionary containing the predictions from the best model and other models (default is None).
    x_train : pd.DataFrame, optional
        Training data for features (default is None).
    x_test : pd.DataFrame, optional
        Test data for features (default is None).
    y_train : pd.Series, optional
        Training data for the target variable (default is None).
    y_test : pd.Series, optional
        Test data for the target variable (default is None).

    Methods
    -------
    cluster_analysis(scaled_cols: list[str] = None) -> dict:
        Perform cluster analysis on the provided data.
    linear_and_ensemble_regression() -> dict:
        Perform linear and ensemble regression analysis.
    feature_importance() -> dict:
        Evaluate the feature importance using the best model.
    string_rep() -> str:
        Generate a string representation of the cluster and regression analysis.
    """
    def __init__(self, report_meta: {}, survey_report: pd.DataFrame = None, landuse_report: pd.DataFrame = None,
                 prior_report: pd.DataFrame = None):




        self.report_meta = report_meta
        self.report_label = construct_report_label(self.report_meta)
        self.columns_of_interest = report_meta['columns_of_interest']
        self.survey_report = survey_report
        self.landuse_report = landuse_report
        self.nsamples = self.survey_report.number_of_samples
        self.nlocations = self.survey_report.number_of_locations
        self.filtered_columns = filter_features(self.landuse_report.df_cont, threshold=0.2, terms=self.columns_of_interest)
        self.prior_report = prior_report
        self.chat = False
        self.cluster_d = None
        self.best_model = None
        self.best_model_name = None
        self.predcitions = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.target_scaler = None
        self.feature_scaler = None
        self.street_scaler = None

    def cluster_analysis(self, scaled_cols: list[str] = None) -> dict:
        """
        Perform cluster analysis on the provided data.

        This function performs cluster analysis on the provided data, scales the features,
        determines the optimal number of clusters using the elbow method, and returns the
        cluster composition and average density per cluster.

        Parameters
        ----------
        scaled_cols : list of str, optional
            The list of columns to be scaled and used in the cluster analysis (default is None).

        Returns
        -------
        dict
            A dictionary containing the cluster analysis DataFrame and the prompt for the report.
        """
        report_label_cluster_features = f"\n{self.report_meta['name']}: Cluster composition"
        report_label_cluster_averages = f"\n{self.report_meta['name']}: Average density per cluster"

        # if there is less than 5 locations and 20 samples
        # the cluster analysis will not be performed
        if self.nsamples <= 20 and self.nlocations <= 5:
            user_prompt_text = "There was insufficient data for a cluster analysis. Consider the sampling stratification"
            end_cluster_prompt = (
                f"\n## Cluster analysis {self.report_label}\n\n{report_label_cluster_features}"
                f"\n{user_prompt_text}\n\n{report_label_cluster_averages}\n{user_prompt_text}")
            return {'dataframe': None, 'prompt': end_cluster_prompt}

        # there are enough samples to perform the cluster analysis
        # scale the feature variables and the target variable
        self.target_scaler = StandardScaler()
        self.feature_scaler = StandardScaler()
        self.street_scaler = StandardScaler()

        cluster_d = self.landuse_report.df_cont.copy()

        # the streets and target variable are scaled separately
        cluster_d[Y] = self.target_scaler.fit_transform(cluster_d[[Y]])
        cluster_d['streets'] = self.street_scaler.fit_transform(cluster_d[['streets']])

        # scale the rest of the features
        polygons_not_lines = [x for x in scaled_cols if x != 'streets']

        cluster_d[polygons_not_lines] = self.feature_scaler.fit_transform(cluster_d[polygons_not_lines])
        cluster_d.reset_index(drop=True, inplace=True)

        # determine the optimal number of clusters
        no_duplicates = cluster_d.drop_duplicates(scaled_cols).copy()
        nclusters = determine_optimal_clusters(no_duplicates[scaled_cols])

        # perform the clustering
        kmeans = KMeans(n_clusters=nclusters[0], random_state=42).fit(no_duplicates[scaled_cols])

        # merge the results in with the observed data
        # unscale the values
        no_duplicates['cluster'] = kmeans.labels_
        no_duplicates.set_index('location', inplace=True, drop=True)
        cluster_d['cluster'] = cluster_d.location.apply(lambda x: no_duplicates.loc[x, 'cluster'])

        cluster_d[polygons_not_lines] = self.feature_scaler.inverse_transform(cluster_d[polygons_not_lines])
        cluster_d[Y] = self.target_scaler.inverse_transform(cluster_d[Y].values.reshape(-1, 1))
        cluster_d['streets'] = self.street_scaler.inverse_transform(cluster_d['streets'].values.reshape(-1, 1))
        scaler = MinMaxScaler().fit(cluster_d['streets'].values.reshape(-1, 1))
        cluster_d['streets'] = scaler.transform(cluster_d['streets'].values.reshape(-1, 1))
        self.cluster_d = cluster_d.copy()

        # make the cluster analysis dataframe
        df = cluster_d.drop_duplicates('cluster').sort_values('cluster').set_index('cluster', drop=True)
        pcs_m = cluster_d.groupby(['cluster'], as_index=False).agg({Y: 'mean'}).set_index('cluster', drop=True)
        samps = cluster_d.groupby(['cluster'], as_index=False).agg({Y: 'count'}).rename(
            columns={Y: 'nsamples'}).set_index('cluster', drop=True)
        pcs_m['nsamps'] = samps.nsamples.values
        df = pcs_m.merge(df[scaled_cols], left_index=True, right_index=True)

        df.drop(['nsamps'], inplace=True, axis=1)
        cols = [x for x in df.columns if x not in [Y]]
        cluster_features = df[cols].drop_duplicates()
        cluster_results = df[[Y]].copy()
        user_prompt_f = cluster_composition_prompt(cluster_features.to_markdown())
        user_prompt_r = cluster_rates_prompt(cluster_results.to_markdown())

        end_cluster_prompt = (
            f"\n### Cluster analysis {self.report_label}\n\n{report_label_cluster_features}"
            f"{cdud}\n\n{user_prompt_f}\n\n"
            f"\n\n{report_label_cluster_averages}\n{user_prompt_r}")

        return {'dataframe': (self.cluster_d, cluster_features, cluster_results), 'prompt': end_cluster_prompt}

    def linear_and_ensemble_regression(self) -> dict:
        """
        Perform linear and ensemble regression analysis.

        This function performs regression analysis using various models, including linear and ensemble methods,
        and returns the results along with the best model and predictions.

        Returns
        -------
        dict
            A dictionary containing the regression results DataFrame and the prompt for the report.
        """
        regression_label = f"\n### Summary of regression methods {self.report_label}: \n\n"
        section_description = lrd + "\n\n"
        section_label = regression_label + section_description

        if self.nsamples < 10:
            user_prompt = "There was insufficient data for a regression analysis. Consider the sampling stratification"
            return {'dataframe': None, 'prompt': f'{section_label}\n\n{user_prompt}'}

        d, best_model, the_name, predictions, X_test, y_test, X_train, y_train = perform_regression_analysis(
            self.landuse_report.df_cont, features=self.filtered_columns)
        d = pd.DataFrame(d)

        self.best_model = best_model
        self.best_model_name = the_name
        self.predictions = predictions
        self.x_train = X_train
        self.x_test = X_test
        self.y_train = y_train
        self.y_test = y_test

        user_prompt = regression_results_prompt(d.to_markdown())
        return {'dataframe': d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def feature_importance(self) -> dict:
        """
        Evaluate the feature importance using the best model.

        This function calculates both the model feature importance and the permutation importance
        of features using the best model and test data, and returns the results in DataFrames and a prompt.

        Returns
        -------
        dict
            A dictionary containing the feature importance DataFrames and the prompt for the report.
        """
        if self.best_model_name is None:
            if self.nsamples < 10:
                user_prompt = "There was insufficient data for a regression analysis. Therefore we cannot calculate feature importance."
                return {'dataframe': None, 'prompt': user_prompt}
            else:
                user_prompt = "There was no model selected. Please run the regression analysis first."
                return {'dataframe': None, 'prompt': user_prompt}

        d1, d2 = evaluate_feature_importance(self.best_model, self.x_test, self.y_test)
        report_label_model_f = f"\n__Model feature importance__\n\n{frd}"
        report_label_model_p = f"\n__Permutation feature importance__\n\n{prd}"
        section_label = f'### Feature and permutation importance {self.report_label}\n\n'

        user_prompt_f = a_model_feature_importance_prompt(d1.to_markdown())
        user_prompt_p = a_permutation_feature_importance_prompt(d2.to_markdown())

        return {'dataframe': (d1, d2), 'prompt': f"\n{section_label}\n{report_label_model_f}\n{user_prompt_f}\n\n{report_label_model_p}\n{user_prompt_p}"}

    def string_rep(self) -> str:
        """
        Generate a string representation of the cluster and regression analysis.

        This function generates a string representation of the cluster analysis, linear and ensemble regression analysis,
        and feature importance analysis, and returns the combined results as a formatted string.

        Returns
        -------
        str
            The formatted string containing the analysis results.
        """
        title = f"\n## Cluster and regression analysis {self.report_label}\n\n"

        cluster_analysis_result = self.cluster_analysis(self.columns_of_interest)
        linear_ensemble_result = self.linear_and_ensemble_regression()
        feature_importance_result = self.feature_importance()

        analysis_string = (
            f"{title}"
            f"{cluster_analysis_result['prompt']}\n\n"
            f"{linear_ensemble_result['prompt']}\n\n"
            f"{feature_importance_result['prompt']}\n"
        )

        return analysis_string

    def __repr__(self):
        return str(self.report_meta)