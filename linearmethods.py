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

from reports import construct_report_label

permutation_feature_importance = [
    "Permutation importance is a model-agnostic method for assessing the importance of individual ",
    "features in a predictive model. It is particularly useful because it can be applied to any ",
    "type of model, whether it's a linear model, a decision tree, or a complex ensemble model. ",
    "This method involves randomly shuffling the values of a feature in the dataset and observing ",
    "the impact on the model's performance. A significant drop in performance indicates that the feature is important."

]

prd = "".join(permutation_feature_importance)


def a_model_feature_importance_prompt(table):
    feature_importance_prompt = (
        "The following table details the model feature importance.\n\n"
        "Table has the following format:\n\n"
        "1. Feature: the name of the land-use feature\n"
        "2. importance: The model feature importance\n\n"
        "Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:\n\n"
        "{table}\n"
    ).format(table=table)
    return feature_importance_prompt

def a_permutation_feature_importance_prompt(table):
    feature_importance_prompt = (
        "The following table details the permutation feature importance.\n\n"
        "Table has the following format:\n\n"
        "1. Feature: the name of the land-use feature\n"
        "2. importance: The model feature importance\n\n"
        "Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:\n\n"
        "{table}\n"
    ).format(table=table)
    return feature_importance_prompt

def cluster_composition_prompt(table):
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


def cluster_rates_prompt(table):
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


def regression_results_prompt(table):
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

cluster_analysis_description = [
    "The survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone around"
    "around each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of "
    "clusters was determined using the elbow method. Each cluster represents a group of locations that have similar "
    "land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use."
    "We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. ",
    "For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken ",
    "from a location whose buffer zone was 45% dedicated to forest. "
]

cdud = "".join(cluster_analysis_description)

linear_regression_description = [
    "In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. ",
    "The feature variables are the land-use features identified in the land-use profile. ",
    "From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model ",
    "with the highest r² is then used in the BaggingRegressor and the VotingRegressor."
]

lrd = "".join(linear_regression_description)

feature_importance_description = [
    "Feature importance is a technique used in machine learning to identify and quantify ",
    "the significance of different input variables (features) in predicting the target variable. ",
    "In models like decision trees, random forests, and gradient boosting machines, feature importance "
    "is often calculated by measuring how much the model's accuracy or error changes when a ",
    "particular feature is included versus when it is excluded. "
]

frd = "".join(feature_importance_description)


def filter_features(data, threshold: float = 0.2, terms: [] = None):
    print(terms)
    filtered_columns = [col for col in terms if (data[col] > 0).mean() >= threshold]
    return filtered_columns

def append_to_markdown(filename, content):
    with open(filename, 'a') as f:
        f.write(content)



def find_elbow_point(sse):
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

def determine_optimal_clusters(d):
    sse = []
    k_range = range(1, 11)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(d)

        sse.append(kmeans.inertia_)

    optimal_k = find_elbow_point(sse)
    return optimal_k, sse


def perform_regression_analysis(d, features: [] = None, target_var: str = 'pcs/m'):
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
    cluster_d['pcs/m'] = target_scaler.fit_transform(cluster_d[['pcs/m']])
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
        {'Model': f'Bagging:{the_name}', 'R²': bag.score(X_test, y_test), 'MSE': mean_squared_error(y_test, y_pred)})
    # voting

    lnr = these_models['Linear Regression']
    rf = these_models['Random Forest Regression']
    gbr = these_models['Gradient Boosting Regression']
    voting = VotingRegressor([('lnr', lnr), ('rf', rf), ('gbr', gbr)])
    voting.fit(X_train, y_train)
    y_pred = voting.predict(X_test)
    predictions.update({'voting': y_pred})

    regression_results.append(
        {'Model': 'Voting', 'R²': voting.score(X_test, y_test), 'MSE': mean_squared_error(y_test, y_pred)})

    return regression_results, best_model, the_name, predictions, X_test, y_test, X_train, y_train

def evaluate_permutation_importance(best_model, X_test, y_test):
    perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=30, random_state=42)
    perm_importance_df = pd.DataFrame({
        'Feature': X_test.columns,
        'Importance': perm_importance.importances_mean
    }).sort_values(by='Importance', ascending=False)
    return perm_importance_df

def evaluate_feature_importance(best_model, model_name, X_test, y_test):

    # the permutation importance of the variables
    if model_name in ['Random Forest Regression', 'Linear Regression', 'Gradient Boosting Regression',  'Theil-Sen Regressor']:
        perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=30, random_state=42)
        perm_importance_df = pd.DataFrame({
            'Feature': X_test.columns,
            'Importance': perm_importance.importances_mean
            }).sort_values(by='Importance', ascending=False)

    try:
    # we try for either the feature importance or the coefficients
    # model feature importance
        feature_importances_rf = best_model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'Feature': X_test.columns,
            'Importance': feature_importances_rf
        }).sort_values(by='Importance', ascending=False)
        return feature_importance_df, perm_importance_df
    except AttributeError:
    # if feature importance not available try the coefficients
        try:
            params = best_model.coef_
            feature_importances_rf = params
            feature_importance_df = pd.DataFrame({'feature':X_test.columns, 'Coeficient':feature_importances_rf})
            return feature_importance_df, perm_importance_df
        except AttributeError:
            #return an empty DataFrame
            return pd.DataFrame(), perm_importance_df



class LinearMethods:
    def __init__(self, name: str, start: str, end: str, report_meta: {}, survey_report: pd.DataFrame = None,
                 landuse_report: pd.DataFrame = None, prior_report: pd.DataFrame = None, columns_of_interest: [] = None):
        self.name = name
        self.start = start
        self.end = end
        self.report_meta = report_meta
        self.report_label = construct_report_label(self.report_meta)
        self.columns_of_interest = columns_of_interest
        self.survey_report = survey_report
        self.landuse_report = landuse_report
        self.nsamples = self.survey_report.number_of_samples
        self.nlocations = self.survey_report.number_of_locations
        self.filtered_columns = filter_features(self.landuse_report.df_cont, threshold=0.2, terms=self.columns_of_interest)
        self.prior_report = prior_report
        self.chat = False
        self.cluster_d = None
        self.best_model_name = None




    def cluster_analysis(self, scaled_cols: [] = None,):

        report_label_cluster_features = f"\n{self.report_meta['name']}: Cluster composition"
        report_label_cluster_averages = f"\n{self.report_meta['name']}: Average density per cluster"


        # if there is less than 5 locations and 20 samples
        # the cluster analysis will not be performed
        # nsamples = self.survey_report.number_of_samples
        # nlocations = self.landuse_report.df_cont.location.nunique()

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
        cluster_d['pcs/m'] = self.target_scaler.fit_transform(cluster_d[['pcs/m']])
        cluster_d['streets'] = self.street_scaler.fit_transform(cluster_d[['streets']])

        # scale the rest of the features
        polygons_not_lines = [x for x in scaled_cols if x != 'streets']
        cluster_d[polygons_not_lines] = self.feature_scaler.fit_transform(cluster_d[polygons_not_lines])
        cluster_d.reset_index(drop=True, inplace=True)

        # determine the optimal number of clusters
        nclusters = determine_optimal_clusters(cluster_d[scaled_cols])

        # perform the clustering
        kmeans = KMeans(n_clusters=nclusters[0], random_state=42).fit(cluster_d[scaled_cols])

        # merge the results in with the observed data
        # unscale the values
        cluster_d['cluster'] = kmeans.labels_

        cluster_d[polygons_not_lines] = self.feature_scaler.inverse_transform(cluster_d[polygons_not_lines])
        cluster_d['pcs/m'] = self.target_scaler.inverse_transform(cluster_d['pcs/m'].values.reshape(-1, 1))
        cluster_d['streets'] = self.street_scaler.inverse_transform(cluster_d['streets'].values.reshape(-1, 1))
        scaler = MinMaxScaler().fit(cluster_d['streets'].values.reshape(-1, 1))
        cluster_d['streets'] = scaler.transform(cluster_d['streets'].values.reshape(-1, 1))
        self.cluster_d = cluster_d.copy()

        # make the cluster analysis dataframe
        df = cluster_d.drop_duplicates('cluster').sort_values('cluster').set_index('cluster', drop=True)
        pcs_m = cluster_d.groupby(['cluster'], as_index=False).agg({'pcs/m': 'mean'}).set_index('cluster', drop=True)
        samps = cluster_d.groupby(['cluster'], as_index=False).agg({'pcs/m': 'count'}).rename(
            columns={'pcs/m': 'nsamples'}).set_index('cluster', drop=True)
        pcs_m['nsamps'] = samps.nsamples.values
        df = pcs_m.merge(df[scaled_cols], left_index=True, right_index=True)

        df.drop(['nsamps'], inplace=True, axis=1)
        cols = [x for x in df.columns if x not in ['pcs/m']]
        cluster_features = df[cols].drop_duplicates()
        cluster_results = df[['pcs/m']].copy()
        user_prompt_f = cluster_composition_prompt(cluster_features.to_markdown())
        user_prompt_r = cluster_rates_prompt(cluster_results.to_markdown())

        end_cluster_prompt = (
            f"\n### Cluster analysis {self.report_label}\n\n{report_label_cluster_features}"
            f"{cdud}\n\n{user_prompt_f}\n\n"
            f"\n\n{report_label_cluster_averages}\n{user_prompt_r}")

        return {'dataframe': self.cluster_d, 'prompt' : end_cluster_prompt}

    def linear_and_ensemble_regression(self):
        # print(self.filtered_columns)

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
        return {'dataframe':d, 'prompt': f'{section_label}\n\n{user_prompt}'}

    def feature_importance(self):

        if self.best_model_name is None:
            if self.nsamples < 10:
                user_prompt = "There was insufficient data for a regression analysis. Therefore we can not calculate feature importance"
                return {'dataframe': None, 'prompt': user_prompt}
            else:
                user_prompt = "There was no model selected. Please run the regression analysis first."
                return {'dataframe': None, 'prompt': user_prompt}

        d1, d2 = evaluate_feature_importance(self.best_model, self.best_model_name, self.x_test, self.y_test)
        report_label_model_f = f"\n__Model feature importance__\n\n{frd}"
        report_label_model_p = f"\n__Permutation feature importance__\n\n{prd}"
        section_label = f'### Feature and permutation importance {self.report_label}\n\n'

        user_prompt_f = a_model_feature_importance_prompt(d1.to_markdown())
        user_prompt_p = a_permutation_feature_importance_prompt(d2.to_markdown())

        return {'dataframe':(d1, d2), 'prompt':f"\n{section_label}\n{report_label_model_f}\n{user_prompt_f}\n\n{report_label_model_p}\n{user_prompt_p}"}



    def string_rep(self):
        title = f"\n## Cluster and regression analysis {self.report_label}\n\n"

        clusteranalysis = self.cluster_analysis(self.columns_of_interest)
        linear_ensemble = self.linear_and_ensemble_regression()
        feat_imp = self.feature_importance()
        astring = f"""
        {title}
        {clusteranalysis['prompt']}
        {linear_ensemble['prompt']}
        {feat_imp['prompt']}
        """
        return astring

    def __repr__(self):
        return self.string_rep(scaled_cols=[])