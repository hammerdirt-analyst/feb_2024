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
from pathlib import Path

# labels and groups for selection
administrative = ['location', 'city', 'canton', 'parent_boundary']
geographic = ['feature_name',  'feature_type']
feature_types = ['r', 'l', 'p']
feature_variables = ['buildings', 'wetlands', 'forest', 'public-services', 'recreation', 'undefined', 'streets', 'vineyards', 'orchards']
the_report_themes = ['Canton', 'Municipality', 'River basin', 'River', 'Lake', 'Park']

# the consolidated codes
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

feature_data = dict(
    code_data = "data/end_process/codes.csv",
    beach_data = "data/end_process/beaches.csv",
    land_cover_data = "data/end_process/land_cover.csv",
    land_use_data = "data/end_process/land_use.csv",
    street_data = "data/end_process/streets.csv",
    intersection_attributes = "data/end_process/river_intersect_lakes.csv"

)

# languages
languages = ['de', 'en', 'fr']

session_language = 'en'

# the 90th percentile range
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

default_survey_type = 'length'

# column of interest
object_of_interest = 'code'

# indentify target variable and type
Y = 'pcs/m'
y_type = 'float'

Q = 'quantity'

# distribution point estimate
tendencies = 'mean'

# correlation threshold
corr_threshold = 0.3

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
# session config to get the data for codes and the lat
# lon data for the beaches
codes = pd.read_csv(feature_data['code_data'])
code_definitions_map = codes[['code', 'en', 'fr', 'de']].set_index('code')
code_material = codes[['code', 'material']].set_index('code')

# default location of data
data_directory = 'data/end_process/'
date_format = "%Y-%m-%d"
default_data = ['data/end_process/before_2019.csv', 'data/end_process/after_2019.csv']
buildings_services = ['buildings', 'public services']
new_label = 'buildings_services'
new_display_label = 'Urbanization'
combination_method = 'sum'
default_args = [(buildings_services, new_label, combination_method)]

color_style = {'prior':'#daa520', 'likelihood':'#1e90ff'}
palette = {'prior':'goldenrod', 'likelihood':'dodgerblue'}


def assign_target_variable(target: str = None) -> str:
    if target is None:
        return Y
    if target not in [Y, 'pcs/m²']:
        raise ValueError('target must be either pcs/m or pcs/m²')
    return target


def define_data_fields(survey_type: str = None, reporting_units: str = None) -> []:

    if survey_type is None:
        survey_type = default_survey_type
    if reporting_units is None:
        reporting_units = Y

    if survey_type not in [default_survey_type, 'area']:
        raise ValueError('survey_type must be either length or area')
    if reporting_units not in [Y, 'pcs/m2']:
        raise ValueError('reporting_units must be either pcs/m or pcs/m2')

    columns = [
        'sample_id',
        'date',
        'location',
        survey_type,
        'code',
        'quantity',
        reporting_units,
        'feature_name',
        'feature_type',
        'parent_boundary',
        'city',
        'canton',
        'en',
        'fr',
        'de',
        'date']
    return columns

def collect_survey_data(connection: str = None, afunc: callable = None, columns: [] = None) -> pd.DataFrame:
    if connection is None:
        datas = [pd.read_csv(data) for data in default_data]
        return pd.concat(datas)
    if connection == 'external':
        # this function should return a dataframe
        datas = afunc()
        if columns is None:
            if all(col in define_data_fields() for col in datas.columns):
                return datas
            else:
                raise ValueError(f'The columns in the dataframe : {datas.columns} do not match the default columns : {define_data_fields()}')
        else:
            if all(col in columns for col in datas.columns):
                return datas
            else:
                raise ValueError(f'The columns in the dataframe : {datas.columns} do not match the supplied columns {columns}')


def unpack_with_pandas(path_variables: tuple) -> pd.DataFrame:
    """Utility function to put csv to pd.DataFrame"""
    try:
        d = pd.read_csv(Path(*path_variables))
        return d
    except Exception as e:
        statement = "Either the path variables did not work or the file is not readable, see below."
        print(f'{statement}\n{e}')