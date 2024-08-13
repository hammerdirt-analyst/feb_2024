import openai
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor, VotingRegressor
from featureevaluator import FeatureEvaluation
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.exceptions import ConvergenceWarning
import warnings
from sklearn.inspection import permutation_importance

from session_config import code_definitions_map as codes


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()
def filter_features(data, threshold: float = 0.2, terms: [] = None):
    filtered_columns = [col for col in terms if (data[col] > 0).mean() >= threshold]
    return data[['pcs/m', *filtered_columns]], filtered_columns
def append_to_markdown(filename, content):
    with open(filename, 'a') as f:
        f.write(content)


def use_chat_completion(client, model: str = 'gpt-3.5-turbo-0125', messages: [{}] = None):
    completed_chat = client.chat.completions.create(model=model, messages=messages)
    return completed_chat


def messages_for_chat_completion(system_prompt: str = None, user_prompt: str = None):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}]

    return messages


def clusters_by_use_case(cluster_data, scaled_cols: [] = None, columns_to_cluster: [] = None, scalers: {} = None):
    cluster_p = cluster_data.copy()

    nclusters = determine_optimal_clusters(cluster_p[columns_to_cluster])
    kmeans = KMeans(n_clusters=nclusters[0], random_state=42).fit(cluster_p[columns_to_cluster])
    cluster_p['cluster'] = kmeans.labels_
    cluster_p[scaled_cols] = scalers['feature_scaler'].inverse_transform(cluster_p[scaled_cols])
    cluster_p['pcs/m'] = scalers['target_scaler'].inverse_transform(cluster_p['pcs/m'].values.reshape(-1, 1))
    cluster_p['streets'] = scalers['street_scaler'].inverse_transform(cluster_p['streets'].values.reshape(-1, 1))
    scaler = MinMaxScaler().fit(cluster_p['streets'].values.reshape(-1, 1))
    cluster_p['streets'] = scaler.transform(cluster_p['streets'].values.reshape(-1, 1))
    df = cluster_p.drop_duplicates('cluster').sort_values('cluster').set_index('cluster', drop=True)
    pcs_m = cluster_p.groupby(['cluster'], as_index=False).agg({'pcs/m': 'mean'}).set_index('cluster', drop=True)
    samps = cluster_p.groupby(['cluster'], as_index=False).agg({'pcs/m': 'count'}).rename(
        columns={'pcs/m': 'nsamples'}).set_index('cluster', drop=True)
    pcs_m['nsamps'] = samps.nsamples.values
    df = pcs_m.merge(df[columns_to_cluster], left_index=True, right_index=True)

    return cluster_p, df


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

    X = d[features]
    y = d[target_var].values

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

def evaluate_feature_importance(best_model, model_name, X_test, y_test, X_train, y_train):

    # the permuation importance of the variables
    if model_name in ['Random Forest Regression', 'Linear Regression', 'Gradient Boosting Regression',  'Theil-Sen Regressor']:
        perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=30, random_state=42)
        perm_importance_df = pd.DataFrame({
            'Feature': X_test.columns,
            'Importance': perm_importance.importances_mean
            }).sort_values(by='Importance', ascending=False)

    try:
    # model feature importance
        feature_importances_rf = best_model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'Feature': X_test.columns,
            'Importance': feature_importances_rf
        }).sort_values(by='Importance', ascending=False)
        return feature_importance_df, perm_importance_df
    except AttributeError:
    # if feature importance not avaialable try the coefficients
        try:
            params = best_model.coef_
            feature_importances_rf = params
            feature_importance_df = pd.DataFrame({'feature':X_test.columns, 'Coeficient':feature_importances_rf})
            return feature_importance_df, perm_importance_df
        except AttributeError:
            #return an empty DataFrame
            return pd.DataFrame(), perm_importance_df
def create_system_prompt(prompt, context="") -> str:
    return f"{prompt}{context}"

def a_model_feature_importance_prompt(table):
    feature_importance_prompt = f"""
The following table details the model feature importance. 

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

{table}


"""
    return feature_importance_prompt


def a_permutation_feature_importance_prompt(table):
    feature_importance_prompt = f"""
The following table details the permutation feature importance. 

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

{table}


"""
    return feature_importance_prompt


def a_forecast_prompt(table):
    forecast_prompt = f"""
The following contains the expected distribution of survey results.

The table has the following format:

1. average: the expected average sample total
2. hdi min: the minimum of the 90% Highest Density Interval
3. hdi max: the maximum of the 90% of the Highest Density Interval
4. 5th, 25th, 50th, 75th, 95th : the percentile rankings based on the expected distribution
5. max predicted: the maximum value predicted by the model

Generate a narrative summary based on the following table. Include all values. Reply in paragraph format, do not comment do not embelish. Use the following style guide:

{table}


"""
    return forecast_prompt


def admin_prompt(table, place_names):
    prompt = f"""
The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis. 

Please provide a concise narrative of the contents of the following table. In your narrative be sure to include the list of cities, 
and the names of the canton and survey areas.

 {table}

The following is the names of the cities, cantons, and survey areas.

{place_names}    
"""
    return prompt


def feature_count_prompt(table, place_names):
    prompt = f"""
The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. 

Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river
that is mentioned.

{table}


The following is the names of the lakes, rivers and parks included in the data.

{place_names}


"""
    return prompt


def survey_result_summary_prompt(table):
    combined_summary_prompt = f"""
These are the survey totals for the data we are studying. We are analyzing count data from beach-litter surveys. The table has the following format:

1. total (quantity) = the total number of objects identified
2. nsamples = the numner of samples collected
3. average = average objects per meter\n
4. 5th, 25th, 50th,	75th, 95th = the objects per meter percentile ranking
5. std = standard deviation in objects per meter
6. max = the maximum recorded objects per meter
7. start = the date of the first sample
8. end = the date of the las sample

Generate a narrative summary based on the following table.

{table}


"""
    return combined_summary_prompt


def inventory_prompt(table):
    inventory_prompt = f"""
This is the list of all objects found at the beach. The table has the following format:   

1. code: object identifier
1. quantity: the total number found
2. pcs/m = average objects per meter
3. % of total = the proportion of the total for for this object
4. sample_id = the number of samples
5. fails = the number of times at least one of the object was found at a survey
6. rate =  fails/the number of samples
7. object: the plain english name of the object type

Generate a narrative summary based on the following table. You need to list all the codes starting from the top and working down that make up at least 50% of the total.
Provide the code quantity and % of total.

{table}


"""
    return inventory_prompt


def sampling_stratification_prompt(table):
    profile_prompt = f"""

The sampling stratification quantifies what proportion of the samples were conducted according to the proportion of the buffer zone that is dedicated to a particular land use feature.
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. 
What changes is how the land use features are distributed within the buffer zone, That is we can group locations by the similarity of the measured topographical present in the buffer zone. 

__Example of how to interpret sampling-stratification table:__\n\n


__Sample table:__\n\n

|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |   ('Proportion of samples collected', 'wetlands') |   ('Proportion of samples collected', 'forest') |   ('Proportion of samples collected', 'public-services') |   ('Proportion of samples collected', 'recreation') |   ('Proportion of samples collected', 'undefined') |   ('Proportion of samples collected', 'streets') |   ('Proportion of samples collected', 'vineyards') |   ('Proportion of samples collected', 'orchards') |
|----------------------------:|---------------------------------------------------:|--------------------------------------------------:|------------------------------------------------:|---------------------------------------------------------:|----------------------------------------------------:|---------------------------------------------------:|-------------------------------------------------:|---------------------------------------------------:|--------------------------------------------------:|
|                           1 |                                          0.0588235 |                                                 1 |                                       0.976471  |                                                0.776471  |                                                   1 |                                          0.870588  |                                                0 |                                          0.976471  |                                                 1 |
|                           2 |                                          0.0588235 |                                                 0 |                                       0.0235294 |                                                0.2       |                                                   0 |                                          0.0470588 |                                                0 |                                          0         |                                                 0 |
|                           3 |                                          0.0117647 |                                                 0 |                                       0         |                                                0.0235294 |                                                   0 |                                          0.0823529 |                                                0 |                                          0.0235294 |                                                 0 |
|                           4 |                                          0.376471  |                                                 0 |                                       0         |                                                0         |                                                   0 |                                          0         |                                                0 |                                          0         |                                                 0 |
|                           5 |                                          0.494118  |                                                 0 |                                       0         |                                                0         |                                                   0 |                                          0         |                                                0 |                                          0         |                                                 0 |


__exmple paragraph__

The sampling-stratification of the surveys was as follows: 49% of the surveys were conducted at locations where 80-100% of the buffer was dedicated to buidlings. 37% of the surveys were taken where 60 -80% of the buffer
was dedicated to buidlings. 1% of the surveys were taken where 40-60% of the buffer was dedicated to buidlings. 6% of the samples were taken from locations where 20 - 40% of the buffer was dedicated to buidlings. 
6% of samples was taken from locations where 0-20% of the buffer was dedicated to buidlings. All of the samples were taken in locations where 0-20% of the buffer was dedicated to wetlands. 98% of the samples were 
taken from locations where 0-20% of the buffer was dedicated to forest. 2% of surveys were taken where 20-40% of the buffer was dedicated to forest. 77% of the samples were taken from locations that had
0-20% of the buffer dedicated to public-services. 20% of the surveys were taken from locations that had 20-40% of the buffer dedicated to public services. 2% of surveys were taked from locations that had
20-40% of the buffer dedicated to public services.


Convert the following table into a paragraph use the example given above to report the values for each column and index pair.

{table}\n\n

"""
    return profile_prompt


def landuse_rates_prompt(table):
    rates_prompt = f"""


The table has the following format:

1. Index = proportion of buffer occupied by feature: (1 - 5) or (0-20%, 20-40%, 40-60%, 60-80%, 80-100%)
2. Columns = The named topographical feature that maybe in the buffer
3. Values = the average pieces of trash per meter that was observed at the magnitude and feature

Convert the following table into a paragraph, reporting the values for each column along with their respective index values without any comments or analysis:

{table}


"""
    return rates_prompt


def cluster_composition_prompt(table):
    cluster_prompt = f"""    
The following are the summary results of a cluster analysis. The columns are the features that were used to make the clusters. The optimal number of clusters was
determined using the elbow method (you can check the docs for this: https://hammerdirt-analyst.github.io/feb_2024/titlepage.html). The table displays the average magnitude
of each feature in the cluster. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location that was
45% dedicated to forest.

Table has the following format:

1. the columns are the measured land use features
2. the index is the cluster number
3. the value is the proportion of the cluster that is attributed to that column. For example if buildings in cluster 1 = .17 it means that the average magnitude of
the buildings variable was 0.17 in cluster 1.

Convert the following table into a paragraph, reporting the values for each column along with their cluster number values without any comments or analysis:

{table}


"""
    return cluster_prompt


def cluster_rates_prompt(table):
    cluster_rates = f"""    
The following are the observed sample average per cluster. The units is objects per meter of beach. The columns are the use case of the objects: personal or professional. The index is
the cluster number.

Table has the following format:

1. the columns are the object use case
2. the index is the cluster number
3. the value is the objects found per meter of beach

Convert the following table into a paragraph, reporting the values for each column along with their respective cluster values without any comments or analysis:
The narrative needs to be in paragraph format.

{table}   


"""
    return cluster_rates


def regression_results_prompt(table):
    prompt = f"""

The following table details the results from different regression analysis of our data. 

Table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.


{table}


"""
    return prompt


def material_results_prompt(table):
    prompt = f"""

The following table details the proportion that each material type represents to the total

Generate a narrative summary based on the following table. You need to include all the material types and their float values


{table}


"""
    return prompt


def municipal_results_prompt(table):
    prompt = f"""

The following table details the quantity (total number of objects) and the average pieces per meter or number of objects per meter for each municipality.

Generate a narrative summary based on the following table. You need to include all the cities and their results


{table}


"""
    return prompt


system_prompt = (
    "Transcribe the values from tables and put them in paragraph form."
    "Being carefull that each value in the table is accounted for in the"
    "paragraph. You are to do this in a narrative form. Answers must be concise."
    "\n\n"
    "{context}"
)

land_use_description = [
    "Each survey location is surounded by a buffer zone of radius = 1 500 meters. ",
    "The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). ",
    "The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. ",
    "Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, ",
    "That is we can group locations by the similarity of the measured topographical features present in the buffer",
]
ldu = "".join(land_use_description)
land_use_litter_density = [
    "The land use profile allows us to group locations according to the topography. ",
    "Here we consdider how the observed litter density changes based on the land use "
    "feature and the proportion of the buffer-zone that the feature occupies"
]

ldud = "".join(land_use_litter_density)

cluster_analysis_description = [
    "The survey locations were grouped using K-Means clustering, the optimal amoount of clusters was determined using the the elbow method. ",
    "We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. ",
    "For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken ",
    "from a location whose buffer zone was 45% dedicated to forest. "
]

cdud = "".join(cluster_analysis_description)

linear_regression_description = [
    "In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. ",
    "The feature variables are the land-use features identified in the land-use profile. ",
    "From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model ",
    "with the lowest r² is then used in the BaggingRegressor and the VotingRegressor."
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

permutation_feature_importance = [
    "Permutation importance is a model-agnostic method for assessing the importance of individual ",
    "features in a predictive model. It is particularly useful because it can be applied to any ",
    "type of model, whether it's a linear model, a decision tree, or a complex ensemble model. ",
    "This method involves randomly shuffling the values of a feature in the dataset and observing ",
    "the impact on the model's performance. A significant drop in performance indicates that the feature is important."

]

prd = "".join(permutation_feature_importance)

grid_approximation_def = [
    "Grid approximation of the posterior is a technique used in Bayesian inference to estimate the posterior distribution ",
    "of parameters by discretizing the parameter space and evaluating the posterior probability at each point on a grid. ",
    "This method is especially useful when the posterior distribution does not have a closed-form solution and when the ",
    "parameter space is of low dimensionality, allowing for a feasible grid search. We use two priors, one is a weigheted ",
    "combination of survey results from locations similar to the likelihood. The other prior uses the samples taken from the ",
    "same location, but prior to the specified date range"
]
grd = "".join(grid_approximation_def)
model = 'gpt-4o-mini'
from session_config import agg_groups


class ReportTexts:
    def __init__(self, name: str, start: str, end: str, groups: {}, standard_report: {}, report: {}, landuse_report: {},
                 client: callable = None, report_scope: str = None, region_type: str = None):
        self.name = name
        self.start = start
        self.end = end
        self.region = region_type
        self.groups = groups
        self.report = report
        self.landuse_report = landuse_report
        self.client = client
        self.standard_report = standard_report
        self.chat = False
        self.cluster_d = None

    def the_admin_boundaries(self, system_prompt: str = None, user_prompt: str = None):
        d = self.report.administrative_boundaries()[0]
        d.loc['survey areas', 'count'] = d.loc['parent_boundary', 'count']
        d.drop('parent_boundary', inplace=True)

        d_names = self.report.administrative_boundaries()[1]
        d_names['survey_area'] = d_names['parent_boundary']
        d_names.pop('parent_boundary')
        report_label = f"\n## Administrative boundaries {self.name} {self.start} {self.end} : Cities, cantons, survey areas and survey locations\n\n"
        section_description = "The number and and names of the cities, cantons and surveys included in this report\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = admin_prompt(d.to_markdown(), d_names)

            messages = messages_for_chat_completion(system_prompt=system_prompt, user_prompt=user_prompt)

            completed_chat = use_chat_completion(self.client, model=model, messages=messages)
            return d, completed_chat, section_label
        else:
            user_prompt = admin_prompt(d.to_markdown(), d_names)
            return f'{report_label}\n\n{user_prompt}'

    def the_named_features(self, system_prompt: str = None, user_prompt: str = None):
        d = self.report.feature_inventory()[0]
        d_names = self.report.feature_inventory()[1]
        report_label = f"\n## Named features {self.name} {self.start} {self.end} : The lakes, rivers and parks\n\n"
        section_description = "The number and names of the lakes, rivers or parks included in this report\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = feature_count_prompt(d.to_markdown(), d_names)
            messages = messages_for_chat_completion(system_prompt=system_prompt, user_prompt=user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = feature_count_prompt(d.to_markdown(), d_names)
            return f'{report_label}\n\n{user_prompt}'

    def summary_statistics(self, system_prompt: str = None, user_prompt: str = None):
        d = self.report.sampling_results_summary.T
        report_label = f"\n## Summary statistics {self.name} {self.start} {self.end}: The descriptive statistics of the survey results\n\n"
        section_description = f"{self.name}: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = survey_result_summary_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = survey_result_summary_prompt(d.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def material_composition(self, system_prompt: str = None, user_prompt: str = None):
        d = self.report.material_report
        report_label = f"\n## Material composition of objects {self.name} {self.start} {self.end}: estimated material composition\n\n"
        section_description = f"{self.name}: The proportion of each material type according to material category\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = material_results_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = material_results_prompt(d.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def inventory(self, system_prompt: str = None, user_prompt: str = None):
        d = self.report.object_summary()
        d['object'] = d.index.map(lambda x: codes.loc[x, 'en'])
        report_label = f"\n## Inventory items {self.name} {self.start} {self.end} : The complete list of the objects found and indentified included in this report.\n\n"
        section_description = "The quantity, average density, % of total and fail rate per object category\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = inventory_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = inventory_prompt(d.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def landuse_profile(self, system_prompt: str = None, user_prompt: str = None):
        # print("!! Methoding !!")
        # print(self.landuse_report.n_samples_per_feature())
        d = self.landuse_report.n_samples_per_feature() / self.report.number_of_samples
        # print(d.head())
        # print(self.landuse_report.df_cont.streets.head())
        # print(d.index)
        d.sort_index(inplace=True)
        new_columns = pd.MultiIndex.from_product([["Proportion of samples collected"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        # d.index.name = 'Proportion of buffer zone'
        report_label = f"\n## Sampling stratification {self.name} {self.start} {self.end}: The environmental features surrounding the survey location.\n\n"
        section_description = ldu + "\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = sampling_stratification_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = sampling_stratification_prompt(d.to_markdown())
            return f'{section_label}\n\n{user_prompt}'

    def landuse_rates(self, system_prompt: str = None, user_prompt: str = None):
        d = self.landuse_report.rate_per_feature()
        report_label = f"\n## Topography and trash density {self.name} {self.start} {self.end}: The changes in the observed litter density and the changes in land use\n\n"
        section_description = ldud + "\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = landuse_rates_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(self.client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = landuse_rates_prompt(d.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def cluster_analysis(self, scaled_cols: [] = None, system_prompt: str = None, user_prompt: str = None):

        report_label_cluster_features = f"\n{self.name}: Cluster composition"
        report_label_cluster_averages = f"\n{self.name}: Average density per cluster"

        cluster_d, filtered_columns = filter_features(self.landuse_report.df_cont.copy(), terms=scaled_cols)

        self.target_scaler = StandardScaler()
        self.feature_scaler = StandardScaler()
        self.street_scaler = StandardScaler()

        cluster_d['pcs/m'] = self.target_scaler.fit_transform(cluster_d[['pcs/m']])
        cluster_d['streets'] = self.street_scaler.fit_transform(cluster_d[['streets']])
        cluster_d[filtered_columns] = self.feature_scaler.fit_transform(cluster_d[filtered_columns])
        self.cluster_d = cluster_d
        self.filtered_columns = filtered_columns

        args = {
            'cluster_data': cluster_d,
            'columns_to_cluster': self.filtered_columns,
            'scaled_cols': self.filtered_columns,
            'scalers': {'street_scaler': self.street_scaler, 'target_scaler': self.target_scaler,
                        'feature_scaler': self.feature_scaler}
        }

        cluster_pro, summary_pro = clusters_by_use_case(**args)

        # if use is None:
        summary_pro.drop(['nsamps'], inplace=True, axis=1)
        cols = [x for x in summary_pro.columns if x not in ['pcs/m']]
        cluster_features = summary_pro[cols].drop_duplicates()
        cluster_results = summary_pro[['pcs/m']].copy()

        if self.chat:
            # cluster composition
            user_prompt = cluster_composition_prompt(cluster_features.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_comp = use_chat_completion(client, model, messages)

            # average rate per cluster
            user_prompt = cluster_rates_prompt(cluster_results.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_rate = use_chat_completion(client, model, messages)
            self.cluster_comp = completed_chat_comp
            self.cluster_results = completed_chat_rate
            return report_label_cluster_features, completed_chat_comp, cluster_features, report_label_cluster_averages, completed_chat_rate
        else:
            user_prompt_f = cluster_composition_prompt(cluster_features.to_markdown())
            user_prompt_r = cluster_rates_prompt(cluster_results.to_markdown())

            return f"\n## Cluster analysis {self.name} {self.start} {self.end}\n\n{report_label_cluster_features}\n{user_prompt_f}\n\n{report_label_cluster_averages}\n{user_prompt_r}"

    def linear_and_ensemble_regression(self, system_prompt: str = None, user_prompt: str = None):

        d, best_model, the_name, predictions, X_test, y_test, X_train, y_train = perform_regression_analysis(
            self.cluster_d, features=self.filtered_columns)
        d = pd.DataFrame(d)
        report_label = f"\n## Summary of regression methods {self.name} {self.start} {self.end}: The different linear models the data were tested on\n\n"

        section_description = lrd + "\n\n"
        section_label = report_label + section_description

        self.best_model = best_model
        self.best_model_name = the_name
        self.predictions = predictions
        self.x_train = X_train
        self.x_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        if self.chat:
            user_prompt = regression_results_prompt(d.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return d, completed_chat, section_label
        else:
            user_prompt = regression_results_prompt(d.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def feature_importance(self, system_prompt: str = None, user_prompt: str = None):

        d1, d2 = evaluate_feature_importance(self.best_model, self.best_model_name, self.x_test, self.y_test,
                                             self.x_train, self.y_train)
        report_label_model_f = f"\n__Model feature importance__\n\n{frd}"
        report_label_model_p = f"\n__Permutation feature importance__\n\n{prd}"

        if self.chat:
            user_prompt = a_model_feature_importance_prompt(d1.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_model_features = use_chat_completion(client, model, messages)

            user_prompt = a_model_feature_importance_prompt(d2.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_model_permutation = use_chat_completion(client, model, messages)
            return report_label_model_f, completed_chat_model_features, d1, report_label_model_p, completed_chat_model_permutation, d2
        else:
            user_prompt_f = a_model_feature_importance_prompt(d1.to_markdown())
            user_prompt_p = a_model_feature_importance_prompt(d2.to_markdown())

            return f"{report_label_model_f}\n{user_prompt_f}\n\n{report_label_model_p}\n{user_prompt_p}"

    def grid_approximation(self, system_prompt: str = None, user_prompt: str = None):

        d1 = self.standard_report['weighted-forecast'].copy()
        d2 = self.standard_report['observed-99-forecast'].copy()
        report_label_model_f = f"\n__{self.name}: Weighted prior forecast__"
        report_label_model_p = f"\n__{self.name}: Observed 99th percentile forecast__"

        if self.chat:
            user_prompt = a_forecast_prompt(d1)
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_weighted = use_chat_completion(client, model, messages)

            user_prompt = a_forecast_prompt(d2.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat_99 = use_chat_completion(client, model, messages)
            return report_label_model_f, completed_chat_weighted, d1, report_label_model_p, completed_chat_99, d2
        else:
            user_prompt_f = a_forecast_prompt(d1.to_markdown())
            user_prompt_p = a_forecast_prompt(d2.to_markdown())
            return f"\n## Forecasts\n\n{grd}\n\n{report_label_model_f}__\n{user_prompt_f}\n\n{report_label_model_p}\n{user_prompt_p}"

    def survey_totals_boundary(self, info_columns: [], system_prompt: str = None, user_prompt: str = None):
        d = self.report.sample_results(info_columns=info_columns)
        dt = d.groupby(info_columns).agg(agg_groups)
        # print(dt)
        report_label = f"\n## Municipal results {self.name} {self.start} {self.end} : The average pcs/m by municipality.\n\n"
        section_description = "The average sample total for each municipality in the report\n\n"
        section_label = report_label + section_description

        if self.chat is True:
            user_prompt = municipal_results_prompt(dt.to_markdown())
            messages = messages_for_chat_completion(system_prompt, user_prompt)
            completed_chat = use_chat_completion(client, model, messages)
            return dt, completed_chat, section_label
        else:
            user_prompt = municipal_results_prompt(dt.to_markdown())
            return f'{report_label}\n\n{user_prompt}'

    def chat_rep(self, scaled_cols, file_name, system_prompt: str = None, user_prompt: str = None):

        report_label = f'{self.region} {self.name} {self.start} {self.end}'
        title = f"\n# Survey report {report_label}\n\n"
        objects = f"\n__Objects in data__\n\n{', '.join([x for x in self.groups.values()])}\n\n"
        with open(file_name, 'w') as file:
            file.write(title)

        append_to_markdown(file_name, objects)

        a, b, c = self.the_admin_boundaries(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.the_named_features(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.summary_statistics(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.material_composition(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.inventory(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.landuse_profile(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.landuse_rates(system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c, d, e = self.cluster_analysis(scaled_cols=scaled_cols, system_prompt=system_prompt)
        section = f"\n## Cluster analysis {self.name} {self.start} {self.end}\n\n{cdud}\n\n"
        entry = f'{section}{a}\n\n{b.choices[0].message.content}\n\n{c.to_markdown()}\n\n{d}\n\n{e.choices[0].message.content}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.linear_and_ensemble_regression(system_prompt=system_prompt)
        entry = f'{c}\n\n{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c, d, e, f = self.feature_importance(system_prompt=system_prompt)
        section = f"\n## Feature and permutation importance {self.name} {self.start} {self.end}\n\n"
        entry = f'{section}{a}\n\n{b.choices[0].message.content}\n\n{c.to_markdown()}\n\n{d}\n\n{e.choices[0].message.content}\n\n{f.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c, d, e, f = self.grid_approximation(system_prompt=system_prompt)
        section = f"\n## Forecasts grid approximation {self.name} {self.start} {self.end}\n\n{grd}\n\n"
        entry = f'{section}{a}\n\n{b.choices[0].message.content}\n\n{c.to_markdown()}\n\n{d}\n\n{e.choices[0].message.content}\n\n{f.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        a, b, c = self.survey_totals_boundary(info_columns=['city'], system_prompt=system_prompt)
        entry = f'{c}{b.choices[0].message.content}\n\n{a.to_markdown()}'
        append_to_markdown(file_name, entry + '\n\n')

        return print(f"file saved as {file_name}")

    def string_rep(self, scaled_cols: [] = None):
        title = f"\n# Survey report {self.name} {self.start} {self.end}\n\n"
        objects = f"\n__Objects in data__\n\n{', '.join([x for x in self.groups.values()])}\n\n"
        admin_boundaries = self.the_admin_boundaries()
        feature_names = self.the_named_features()
        summary_statistics = self.summary_statistics()
        inventory = self.inventory()
        clusteranalysis = self.cluster_analysis(scaled_cols=scaled_cols)
        linear_ensemble = self.linear_and_ensemble_regression()
        forecasts = self.grid_approximation()
        astring = f"""
        {title}
        {objects}
        {admin_boundaries}
        {feature_names}
        {summary_statistics}
        {inventory}
        {clusteranalysis}
        {linear_ensemble}
        {forecasts}
        """
        return astring

    def __repr__(self):
        return self.string_rep(scaled_cols=[])