"""
session_config.py
hammerdirt 2024
Author: Roger Erismann
NOTE: This module is a work in progress.

This module is a configuration file for the litter assisstant. The configuration file is used to define the feature and
target variables, give the location of the default data, and define the columns of interest. The configuration file also
contains the aggregation methods and names the columns. Defines the 90% range, the bins and labels for land use, the
radius of the land use buffer and keys for sorting the data in the userinterface.
"""
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors
import geopandas as gpd


# labels and groups for selection
administrative = ['location', 'city', 'canton', 'parent_boundary']
feature_types = ['r', 'l', 'p']
feature_type_labels = {'l': 'lake', 'r': 'river', 'p': 'park'}
feature_variables = ['buildings', 'wetlands', 'forest', 'public-services', 'recreation', 'undefined', 'streets', 'vineyards', 'orchards']
the_report_themes = ['Canton', 'Municipality', 'River basin', 'River', 'Lake', 'Park']

# the consolidated report_codes
gfoam_frags_caps = {
    'Gfoams': ['G81', 'G82', 'G83'],
    'Gfrags': ['G78', 'G79', 'G80', 'G75', 'G76', 'G77'],
    'Gcaps': ['G21', 'G22', 'G23', 'G24'],
}

period_dates = {
    "mcbp":["2015-11-15", "2016-12-01"],
    "slr": ["2017-04-01", "2018-05-01"],
    "iqaasl": ["2020-03-01", "2021-05-31"],
    "plastock":["2022-01-01", "2022-12-31"]
}

# the 90% interval
report_quantiles = [.05, .25, .5, .75, .95]
quantile_labels = ['5th', '25th', '50th', '75th', '95th']

# bins and labels for land use categorization
bins = [-1, 0.2, 0.4, 0.6, 0.8, 1]
bin_labels = [1, 2, 3, 4, 5]

# forecasting grid
index_range = np.arange(0.0, 100, 0.1)
max_range = .99

# area of a buffer pi*1500²
buffer_radius = 1500
buffer_area = 7068583

# default_survey_type = 'length'

# column of interest
object_of_interest = 'code'

# indentify target variable and type
Y = 'pcs/m'
Q = 'quantity'

# distribution point estimate
tendencies = 'mean'

# these are the columns and methods used to aggregate the data at the sample level
# the sample level is the lowest level of aggregation. The sample level is the collection of all
# the records that share the same sample_id or loc_date. The loc_date is the unique identifier for each survey.
unit_agg = {
    Q: "sum",
    Y: "sum"
}

# Once the data is aggregated at the sample level, it is aggregated at the feature level. The pcs/m or pcs_m
# column can no longer be summed. We can only talk about the median, average or distribution of the pcs/m for the
# samples contained in each feature. The quantity column can still be summed. The median is used for reporting
# purposes. The median is less sensitive to outliers than the average. The median is also more intuitive than the
# average.

agg_groups = {
    Q: "sum",
    Y: tendencies
}

# this column is used to key feature variables to 'Y'
location_label = "location"

# the sample id
index_label = "sample_id"

# the material and definitions for each code are on
# on a different table. In this instance we call the
# session config to get the data for report_codes and the lat
# lon data for the beaches
codes = pd.read_csv("data/end_process/codes.csv")
code_definitions_map = codes[['code', 'en', 'fr', 'de']].set_index('code')
code_material = codes[['code', 'material']].set_index('code')
code_use = codes[['code', 'groupname']].set_index('code')

beaches = pd.read_csv('data/end_process/beaches.csv')
lat_lon = beaches[['slug', 'latitude', 'longitude']].set_index('slug')

canton_layer = gpd.read_file('data/ignorethis/shapes/kantons.shp').to_crs(epsg=4326)
dbckey = canton_layer[['NAME', 'KANTONSNUM']].set_index('NAME')
dbckey = dbckey.drop_duplicates()


municipal_layer = gpd.read_file('data/ignorethis/shapes/municipalities.shp').to_crs(epsg=4326)
rivers_layer = gpd.read_file('data/ignorethis/shapes/rivers.shp').to_crs(epsg=4326)
lakes_layer = gpd.read_file('data/ignorethis/shapes/lakes.shp').to_crs(epsg=4326)

# code groups
# code groups
# objects of personal consumption food, drink, tobacco
personal_objects = ['G10',  'G30', 'G31', 'G33', 'G34', 'G35', 'G8', 'G7', 'G6', 'G5', 'G4', 'G37', 'G2', 'G27', 'G25', 'G26', 'G11']

# just tobacco and snack wrappers
tobo_snacks = ['G27', 'G30']

# fragmented foams and plastics
fragmented = ['Gfrags', 'Gfoams']

# personal hygiene, medical water treatment
steps = ['G144', 'G96', 'G95', 'G91', 'G97', 'G98', 'G100', 'G91', 'G99']

# industrial and construction
indus = ['G89', 'G67', 'G112', 'G93' , 'G66','G74', 'G72', 'G87', 'G65', 'G69', 'G68', 'G43', 'G41', 'G38', 'G36', 'G19', 'G17', 'Gfrags']

# default location of data
data_directory = 'data/end_process/'
date_format = "%Y-%m-%d"
default_data = ['data/end_process/before_2019.csv', 'data/end_process/after_2019.csv']


color_style = {'prior':'#daa520', 'likelihood':'#1e90ff'}
palette = {'prior':'goldenrod', 'likelihood':'dodgerblue'}

format_kwargs = dict(precision=2, thousands="'", decimal=",")

# this defines the css rules for the table displays
header_row = {'selector':'th', 'props': 'background-color: #FFF; font-size:14px; text-align:left; width: auto; word-break: keep-all;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': 'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 12px;'}
table_data = {'selector': 'td', 'props': 'padding:4px; font-size:12px;text-align: center;'}
table_caption = {'selector': 'caption', 'props': 'caption-side: bottom; font-size:1em; text-align: left;'}
table_caption_top = {'selector': 'caption', 'props': 'caption-side: top; font-size:1em; text-align: left; margin-bottom: 10px;'}
caption_css = {'selector': 'caption', 'props': 'caption-side: top; font-size:.9em; text-align: left; font-style: italic; color: #000;'}
table_first_column_left = {'selector': 'td:nth-child(1)', 'props': 'text-align: left;'}
table_border = {'selector': 'table, th, tr, td', 'props': 'border: 1px solid black; border-collapse: collapse;'}

table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data, table_border, table_caption_top]
highlight_props = 'background-color:#FAE8E8'

def style_negative(v, props=''):
    """from panaas docs: pandas-docs/version/0.24.2/reference/api/pandas.io.formats.style.Styler.applymap.html"""
    return props if v < 0 else None

def highlight_max(s, props: str = highlight_props):
    return np.where((s == np.max(s.values)) & (s != 1), props, '')

# llms and prompts
model_rough_draft = 'gpt-4o-mini'
model_corrections = 'gpt-4o'

report_instructions = """\n
<!-- INSTRUCTION_START\n
1. Analysis of Sampling Stratification and Sampling stratification and trash density tables
   * Objective: Ensure conclusions about the presence or absence of objects are based on a combined interpretation of sampling stratification and litter density data.
   * Data Validation: Confirm that any conclusions about trash density and land use are supported by the presence of samples in the sampling stratification table"
   * Interpretation Guidelines: Analyze how the distribution of land-use features influences the observed trash density. 
   * Draw conclusions only when both stratification and density data are aligned. Make sure to check all the values for a given land-use feature and proportion of buffer zone. Before making any conlusions"
   * A zero in the trash density table indicates that no objects were found for that land-use feature and proportion of buffer zone.

2. Reporting Geographic Information

   * Always provide the names of all the cities, cantons, and survey areas included in the report.
   * Always provide the names of all the lakes, rivers, and parks included in the report.

3. Definitions of Urban, Rural Areas, fail-rate

   * Urban Areas: The proportion of samples where building occupy 60% or more of the buffer is greater than 50%.\n
   * Rural Areas: The proportion of samples where forest occupy 60% or more of the buffer is greater than 50%.\n
   * Mixed Areas: Does not meet the criteria of urban or rural.\n
   * Fail Rate: The proportion of samples where at least one of the object categories was found.\n
   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column, if the table
reads 'no samples' that is equivalent to 0. 

2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column, if the table
reads 'no samples' that is equivalent to 0. 

3. Make the conclusion: If test one is greater than 50% then the classification is urban. If test two is greater than 50% then 
the classification is rural. If neither test one or test two is greater than 50% the the classification is mixed.\n
  

INSTRUCTION_END -->\n
"""

land_use_description = [
    "\n",
    "Each survey location is surrounded by a buffer zone of radius = 1 500 meters. ",
    "The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). ",
    "The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. ",
    "Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, ",
    "Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. ",
    "The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken ",
    "according to the different conditions.\n",
]

sampling_stratification_example = """\n
The sampling stratification table quantifies what proportion of the samples were collected according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.\n\n
<!--- INSTRUCTION_START\n
__How to interpret sampling stratification table:__\n
The sampling stratification table quantifies what proportion of the samples were conducted according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.\n

Therefore when you answer questions about sampling stratification you must qualify that with the corresponding value
in the sampling stratification and trash density table, in parentheses. For example, using the example tables
below, we would say 16% (0.53 pcs/m) of all samples were taken at locations where buildings occupied 80 - 100% of the buffer zone. 

__Example sampling stratification and trash density table:__\n

|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |\n
__Example sampling stratification table:__\n

|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                     0.13 |                       1|                 0.85  |                    0.95      |   
|                    20 - 40% |                     0.21 |              no samples|                   0.1 |                    0.05      |
|                    40 - 60% |                     0.22 |             no samples |             .05       |                    no samples|
|                    60 - 80% |                    0.18  |             no samples |            no samples |                 no samples   |
|                    80 - 100%|                    0.16  |              no samples|       no samples      |                   no samples  | 


__Example interpretation of the sampling stratification and trash density table__

The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer 13% of all samples, (0.37 pcs/m)\n
where buildings occupied 20 - 40% of the buffer 21% of all samples, (0.03 pcs/m)\n
where buildings occupied 40 - 60% of the buffer 22% of all samples, (0.01 pcs/m)\n
where buildings occupied 60 - 80% of the buffer 18% of all samples, (0.37 pcs/m)\n
where buildings occupied 80 - 100% of the buffer 16% of all samples, (0.49, pcs/m)\n


1. no samples indicates that no samples were collected at a location that fits this description.

2. Definitions of Urban, Rural or mixed

   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.\n
   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.\n
   * Mixed Areas: Does not meet the criteria of urban or rural.\n
   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.\n

2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.\n

3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.\n

 
\nINSTRUCTION_END -->
"""

land_use_rates_example = """\n
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.\n\n
<!--- INSTRUCTION_START\n
__How to interpret sampling stratification and trash density table:__\n
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.\n
Therefore when you answer questions about sampling stratification and trash density you must qualify that with the corresponding value
in the sampling stratification table. For example, if you say that the trash density is 0.05 pcs/m in an area where buildings occupy 0-20% of the buffer zone,
you must also say that 6% of the samples were taken in an area where buildings occupy 0-20% of the buffer zone.\n\n
__Example sampling stratification and trash density table:__\n\n
|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |\n\n
__Example sampling stratification table:__\n\n
|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.13 |                   1|             0.85  |                    0.95  |   
|                    20 - 40% |                0.21 |          no samples|             0.1 |                    0.05       |
|                    40 - 60% |                0.22 |         no samples |       .05       |                    no samples |
|                    60 - 80% |                0.18  |        no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.16  |        no samples|       no samples     |                   no samples    | 
\n\n
__Example interpretation of the sampling stratification and trash density table__\n\n
The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer (13% of all samples) the average objects per meter was 0.05\n
where buildings occupied 20 - 40% of the buffer (21% of all samples) the average objects per meter was 0.03\n
where buildings occupied 40 - 60% of the buffer (22% of all samples) the average objects per meter was 0.01\n
where buildings occupied 60 - 80% of the buffer (18% of all samples) the average objects per meter was 0.37\n
where buildings occupied 80 - 100% of the buffer (16% of all samples) the average objects per meter was 0.49\n\n
1. no samples indicates that no samples were takes at a location that fits this description.\n
2. Definitions of Urban, Rural or mixed\n
   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.\n
   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.\n
   * Mixed Areas: Does not meet the criteria of urban or rural.\n\n   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**\n\n
1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.\n
2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.\n
3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.\n
\n INSTRUCTION_END -->\n
"""

landuse_litter_density = [
    "\n",
    "The land use profile allows us to group locations according to the topography. ",
    "Here we consdider how the observed litter density changes based on the land use ",
    "feature and the proportion of the buffer-zone that the feature occupies"
]

permutation_feature_importance = [
    "Permutation importance is a model-agnostic method for assessing the importance of individual ",
    "features in a predictive model. It is particularly useful because it can be applied to any ",
    "type of model, whether it's a linear model, a decision tree, or a complex ensemble model. ",
    "This method involves randomly shuffling the values of a feature in the dataset and observing ",
    "the impact on the model's performance. A significant drop in performance indicates that the feature is important."

]

cluster_analysis_description = [
    "The survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone around"
    "around each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of "
    "clusters was determined using the elbow method. Each cluster represents a group of locations that have similar "
    "land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use."
    "We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. ",
    "For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken ",
    "from a location whose buffer zone was 45% dedicated to forest. "
]

linear_regression_description = [
    "In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. ",
    "The feature variables are the land-use features identified in the land-use profile. ",
    "From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model ",
    "with the highest r² is then used in the BaggingRegressor and the VotingRegressor."
]

feature_importance_description = [
    "Feature importance is a technique used in machine learning to identify and quantify ",
    "the significance of different input variables (features) in predicting the target variable. ",
    "In models like decision trees, random forests, and gradient boosting machines, feature importance "
    "is often calculated by measuring how much the model's accuracy or error changes when a ",
    "particular feature is included versus when it is excluded. "
]


grid_approximation_def = (
     "\n### Grid Approximation method:\n\n"
    "We employed a grid-based Bayesian inference approach to estimate the conditional probability that a "
    "survey result will exceed or be equal to a given value, using prior observations from similar locations "
    "and new data from the location of interest. The prior represents survey data from locations either inside "
    "or outside a designated boundary, segmented by geographic or administrative criteria, while the likelihood "
    "reflects observations from the specific location being analyzed. The grid spans the range of possible values, "
    "from 0 to the maximum value observed in either the prior or likelihood data, with a fixed interval of 0.01.\n\n"

    "For each point x on this grid, we calculated the conditional probability that a survey result, y, would exceed "
    "or be equal to x. This was modeled using a binomial distribution, where the successes represent the number of times "
    "y was greater than or equal to x, and failures represent the number of times y was less than x, for both the prior and "
    "the likelihood. By applying Bayes' Theorem, we combined the prior and likelihood distributions to compute the posterior "
    "distribution at each grid point, providing a detailed estimate of the probability that a survey outcome exceeds any value "
    "across the range of interest.\n\n"

    "In our method, the grid points act as thresholds, and the posterior probability at each grid point corresponds to the "
    "likelihood that a survey result exceeds or equals that value. This setup is analogous to a multinomial distribution, where "
    "each grid point is treated as a category and the probability of an event occurring in each category is computed. Extending "
    "this approach to a multinomial framework would simplify the computational process, as the Dirichlet distribution—being the "
    "conjugate prior to the multinomial—would allow for efficient posterior updates. This relationship ensures that Bayesian updating "
    "remains computationally straightforward, even in more complex settings where probabilities are distributed across multiple categories."
)

in_boundary_description = (
    "This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) "
    "and if their are enough samples with similar land use. The prior does not include samples from the likelihood. "
    "The samples are selected based on the similarity of the land use features: buildings, forest and undefined. "
    "The similarity is calculated using the manhattan distance between the likelihood feature variables  and the proposed prior samples. "
    "In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations "
    "in the geographic boundary ?' "

)

out_boundary_description = (
    "This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) "
    "and if their are enough samples with similar land use. The prior does not include samples from the likelihood. "
    "The samples are selected based on the similarity of the land use features: buildings, forest and undefined. "
    "The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. "
    "In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations "
    "outside the geographic boundary ?' "
)


prior_description = (
    "This prior distribution is selected from random samples from inside and outside the requested administrative boundary (if a boundary was selected) "
    "and if their are enough samples with similar land use. The prior does not include samples from the likelihood. The samples are selected based on the "
    "similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the manhattan distance between the likelihood samples "
    "and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from "
    "similar locations (indifferent of the geographic boundary) ?' "

)

def collect_survey_data(connection: str = None, afunc: callable = None) -> pd.DataFrame:
    if connection is None:
        datas = [pd.read_csv(data) for data in default_data]
        return pd.concat(datas)
    if connection == 'external':
        # this function should return a dataframe
        datas = afunc()
        return datas

def append_to_markdown(filename: str, content: str):
    """
    Append content to a markdown file.

    This function opens a markdown file in append mode and writes the provided content to it.

    Parameters
    ----------
    filename : str
        The name of the markdown file to which the content will be appended.
    content : str
        The content to append to the markdown file.

    Returns
    -------
    None
    """

    # if not os.path.basename(filename) == filename:
    #     raise ValueError("Invalid filename. Path traversal detected.")

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(content)


def construct_report_label(report_meta):
    report_label = report_meta.get('name', '')
    if report_meta['boundary'] is not None:
        report_label += f" {report_meta['boundary']}"

    if report_meta['feature_type'] is not None:
        report_label += f" {feature_type_labels[report_meta['feature_type']]}"

    report_label += f" {report_meta.get('start', '')} {report_meta.get('end', '')}"

    return report_label


def date_labels_for_display(args):
    start = args['date_range']['start'][:4]
    end = args['date_range']['end'][:4]
    labels = f"{start} - {end}"
    return labels


def report_meta_data(data, start: str = None, end: str = None, name: str = None,
                     feature_name: str = None, feature_type: str = None, columns_of_interest: [] = None,
                     boundary: str = None, boundary_name: str = None, report_codes: [] = None):
    date_mask = (data['date'] >= start) & (data['date'] <= end)
    code_mask = (data[object_of_interest].isin(report_codes))
    code_types = codes[codes.code.isin(report_codes)]['groupname'].unique()
    report_meta = dict(
        start=None,
        end=None,
        name=None,
        report_codes=None,
        code_types=None,
        columns_of_interest=None,
        feature_name=None,
        feature_type=None,
        boundary=None,
        boundary_name=None

    )
    print('new report meta data')
    report_meta_update = {
        'start': start,
        'end': end,
        'name': name,
        'report_codes': report_codes,
        'code_types': code_types,
        'columns_of_interest': columns_of_interest}
    report_meta.update(report_meta_update)
    if feature_type in ['l', 'p', 'r'] and feature_name is None:
        feature_mask = (data['feature_type'] == feature_type)
        report_meta.update({'feature_type': feature_type})

        if boundary in ['canton', 'city', 'parent_boundary']:
            boundary_mask = (data[boundary] == boundary_name)
            report_meta.update({'boundary': boundary})
            report_meta.update({'boundary_name': boundary_name})
            d = data[date_mask & code_mask & feature_mask & boundary_mask].copy()
            return d, report_meta
        else:
            d = data[date_mask & code_mask & feature_mask].copy()
            return  d, report_meta

    elif boundary in ['canton', 'city', 'parent_boundary'] and feature_type is None and feature_name is None:
        boundary_mask = (data[boundary] == boundary_name)
        report_meta.update({'boundary': boundary})
        report_meta.update({'boundary_name': boundary_name})
        if feature_type in ['l', 'p', 'r']:
            feature_mask = (data['feature_name'] == feature_name)
            report_meta.update({'feature_type': feature_type})
            if feature_name is not None:
                report_meta.update({'feature_name': feature_name})
                name_mask = (data['feature_name'] == feature_name)
                d = data[date_mask & code_mask & feature_mask & boundary_mask & name_mask].copy()
                return d, report_meta
            else:

                d = data[date_mask & code_mask & boundary_mask & feature_mask].copy()
                return d, report_meta
        else:
            d = data[date_mask & code_mask & boundary_mask].copy()
            return d,  report_meta

    elif feature_name is not None:
        feature_mask = (data['feature_name'] == feature_name)
        report_meta.update({'feature_type': feature_type})
        report_meta.update({'feature_name': feature_name})

        if boundary in ['canton', 'city', 'parent_boundary']:
            if boundary_name is not None:
                boundary_mask = (data[boundary] == boundary_name)
                report_meta.update({'boundary': boundary})
                report_meta.update({'boundary_name': boundary_name})
                d = data[date_mask & code_mask & feature_mask & boundary_mask].copy()
                return d, report_meta
            else:
                report_meta.update({'boundary': boundary})
                d = data[date_mask & code_mask & feature_mask].copy()
                return d, report_meta
        else:
            d = data[date_mask & code_mask & feature_mask].copy()
            return d, report_meta

    else:
        return data[date_mask & code_mask].copy(), report_meta


def report_args(data: pd.DataFrame, start: str = None, end: str = None, name: str = None, boundary: str = None,
                boundary_name: str = None, feature_type: str = None, feature_name: str = None,
                report_codes: [] = None, columns_of_interest: [] = None):
    args = dict(

        data=data,
        start=start,
        end=end,
        name=name,
        feature_name=feature_name,
        feature_type=feature_type,
        boundary=boundary,
        boundary_name=boundary_name,
        report_codes=report_codes,
        columns_of_interest=columns_of_interest
    )
    return args


def rgba_to_css(row):
    """
    Converts color values (either RGBA tuples or named colors) to CSS-compatible strings
    for styling background and font color, with alpha set to 0.6.

    :param row: A row of the DataFrame.
    :return: A list of CSS properties for background and font color.
    """
    color = row['color']

    # Check if the color is a tuple (RGBA)
    if isinstance(color, tuple):
        # Assume it's an RGBA tuple, adjust the alpha to 0.6
        r, g, b, _ = color
        color_css = f'rgba({int(r * 255)}, {int(g * 255)}, {int(b * 255)}, 0.6)'
    else:
        # If it's a named color, convert to RGBA and set alpha to 0.6
        rgba = mcolors.to_rgba(color)
        r, g, b, _ = rgba
        color_css = f'rgba({int(r * 255)}, {int(g * 255)}, {int(b * 255)}, 0.6)'

    # Calculate brightness using the relative luminance formula
    brightness = 0.299 * r + 0.587 * g + 0.114 * b

    # Choose font color: white for dark backgrounds, black for light backgrounds
    font_color = 'white' if brightness < 0.5 else 'black'

    # Return the CSS styles for background and font color
    return [f'background-color: {color_css}; color: {font_color}' for _ in row]