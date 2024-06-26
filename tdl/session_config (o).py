import datetime as dt
import numpy as np
from pathlib import Path
import pandas as pd
import xyzservices.providers as xyz

# data specific session variables
columns = ['sample_id', 'location', 'date', 'feature_name', 'parent_boundary', 'city', 'canton', 'feature_type',
           'orchards', 'vineyards', 'buildings', 'forest', 'undefined', 'public services', 'streets', 'code']

administrative = ['location', 'city', 'canton', 'parent_boundary']
geographic = ['feature_name',  'feature_type']
feature_types = ['r', 'l', 'p']
feature_variables = ['orchards', 'vineyards', 'buildings', 'forest', 'undefined', 'public services', 'streets']
the_report_themes = ['Canton', 'Municipality', 'River basin', 'River', 'Lake', 'Park']

def report_themes_selection(session_language: str):
    report_themes = {
        'de': ['Kanton', 'Gemeinde', 'Flusseinzugsgebiet', 'Fluss', 'See', 'Park'],
        'en': ['Canton', 'Municipality', 'River basin', 'River', 'Lake', 'Park'],
        'fr': ['Canton', 'Municipalité', 'Bassin versant', 'Rivière', 'Lac', 'Parc']
    }
    return report_themes[session_language]


def report_theme_selection_to_label(theme, session_language: str):

    selection_to_label = {
        'de': {
            'Kanton': 'canton',
            'Gemeinde': 'city',
            'Flusseinzugsgebiet': 'parent_boundary',
            'Fluss': 'r',
            'See': 'l',
            'Park': 'p'
        },
        'en': {
            'Canton': 'canton',
            'Municipality': 'city',
            'River basin': 'parent_boundary',
            'River': 'r',
            'Lake': 'l',
            'Park': 'p'
        },
        'fr': {
            'Canton': 'canton',
            'Municipalité': 'city',
            'Bassin versant': 'parent_boundary',
            'Rivière': 'r',
            'Lac': 'l',
            'Parc': 'p'
        }
    }
    return selection_to_label[session_language][theme]


# languages
languages = ['de', 'en', 'fr']

session_language = 'en'

# quantiles
report_quantiles = [.05, .25, .5, .75, .95]

# bins and labels for land use categorization
bins = [-1, 0.2, 0.4, 0.6, 0.8, 1]
bin_labels = [1, 2, 3, 4, 5]

# area of a buffer pi*1500²
buffer_radius = 1500
buffer_area = 7068583

# column of interest
object_of_interest = 'code'

# indentify target variable and type
Y = 'pcs/m'
y_type = 'float'

Q = 'quantity'

# distribution point estimate
tendencies = 'mean'

# this column is used to key feature variables to 'Y'
location_label = "location"

# the sample id
index_label = "sample_id"

# location of data
data_directory = 'data'

# file
survey_data = "results_2015_2021.csv"

date_format = "%Y-%m-%d"

# default combination of feature labels
buildings_services = ['buildings', 'public services']
new_label = 'buildings_services'
new_display_label = 'Urbanization'
combination_method = 'sum'
default_args = [(buildings_services, new_label, combination_method)]


# period dates
period_dates = {
    "mcbp": ["2015-11-15", "2017-03-31"],
    "slr": ["2017-04-01", "2020-02-28"],
    "iqaasl": ["2020-03-01", "2021-12-31"],
    "plastock": ["2022-01-01", "2022-12-31"],
}
# column of interest
object_of_interest = 'code'

# indentify target variable and type
Y = 'pcs/m'
y_type = 'float'

Q = 'quantity'

# distribution point estimate
tendencies = 'mean'

# this column is used to key feature variables to 'Y'
location_label = "location"

# the sample id
index_label = "sample_id"

# location of data
data_directory = 'data'

# file
survey_data = "results_2015_2021.csv"

date_format = "%Y-%m-%d"

# most common objects
sort_columns = ['quantity', 'rate']

# land use profiles

mostly_forest = ['forest', 'undefined']
mostly_agg = ['orchards', 'vineyards']
mostly_urban = ['buildings']
interaction = ['public services', 'streets']

land_use_profiles = {
    'mostly_forest': mostly_forest,
    'mostly_agg': mostly_agg,
    'mostly_urban': mostly_urban,
    'interaction': interaction
}

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

code_definitions_c = "codes.csv"
location_description = "locations.csv"
geo_data = "beaches.csv"

code_selections = ["all", "G70", "G27", "G112", "G30"]

def available_dates():
    start = "2015-11-15"
    end = dt.date.today().strftime("%Y-%m-%d")
    return [start, end]


# def make_feature_mask(df, column, labels):
#     return df[column].isin(labels)

def make_date_mask(df, start, end):
    # Convert the 'date' column to pandas datetime format (datetime64[ns])
    df['date'] = pd.to_datetime(df['date'])

    # print("Type of 'date' column after conversion:", type(df['date'].values[0]))

    # convert 'start' and 'end' to the same datetime format
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # print("Start date type:", type(start))
    # print("End date type:", type(end))

    # Create the mask: True if the date is within the start and end range (inclusive)
    mask = (df['date'] >= start) & (df['date'] <= end)

    return mask


def unpack_with_numpy(path_variables: tuple) -> np.ndarray:
    """Utility to function to put text data files to ndarray"""
    try:
        d = np.loadtxt(Path(*path_variables))
        return d
    except Exception as e:
        statement = "Either the path variables did not work or the file is not readable, see below."
        print(f'{statement}\n{e}')
        return np.ndarray([])


def unpack_with_pandas(path_variables: tuple) -> pd.DataFrame:
    """Utility function to put csv to pd.DataFrame"""
    try:
        d = pd.read_csv(Path(*path_variables))
        return d
    except Exception as e:
        statement = "Either the path variables did not work or the file is not readable, see below."
        print(f'{statement}\n{e}')
        

def remove_outliers_by_percentile(df, group_col, sum_col, percentile, remove_zeros=True):
    group_sums = df.groupby(group_col)[sum_col].sum()

    # the limit as the specified percentile
    limit = np.quantile(group_sums, percentile)

    # groups to remove based on the conditions
    if remove_zeros:
        to_remove = group_sums[(group_sums == 0) | (group_sums > limit)].index
    else:
        to_remove = group_sums[group_sums > limit].index

    # excluding the identified groups
    return df[~df[group_col].isin(to_remove)].copy()

theme_labels = {
    'en': 'Theme',
    'fr': 'Thème',
    'de': 'Thema'
}

feature_labels = {
    'en': 'Feature',
    'fr': 'Fonctionnalité',
    'de': 'Feature'
}

start_date_labels = {
    'en': 'Start date',
    'fr': 'Date de début',
    'de': 'Startdatum'
}

end_date_labels = {
    'en': 'End date',
    'fr': 'Date de fin',
    'de': 'Enddatum'
}

theme_selection_to_column_values = {
    "Municipality": "city",
    "Canton": "canton",
    "Feature": "feature_name",
    "River basin": "parent_boundary",
    "Lake": "l",
    "Park": "p",
    "River": "r",

}

survey_area_labels = {
        'en': {
            "linth": "Linth",
            "rhone": "Rhone",
            "aare": "Aare",
            "ticino": "Ticino",
            "rhine": "Rhine",
        },
        'de': {
            "linth": "Linth",
            "rhone": "Rhone",
            "aare": "Aare",
            "ticino": "Tessin",
            "rhine": "Rhein",
        },
        'fr': {
            "linth": "Linth",
            "rhone": "Rhône",
            "aare": "Aar",
            "ticino": "Tessin",
            "rhine": "Rhin",
        }
}

survey_area_labels_inverse = {
    'en': {
        "Linth": "linth",
        "Rhone": "rhone",
        "Aare": "aare",
        "Ticino": "ticino",
        "Rhine": "rhine",
    },
    'de': {
        "Linth": "linth",
        "Rhone": "rhone",
        "Aare": "aare",
        "Tessin": "ticino",
        "Rhein": "rhine",
    },
    'fr': {
        "Linth": "linth",
        "Rhône": "rhone",
        "Aar": "aare",
        "Tessin": "ticino",
        "Rhin": "rhine",
    }
}


swiss_topo = xyz.SwissFederalGeoportal

map_tiles = swiss_topo['NationalMapColor']

folium_map_kwargs = dict(
    tiles=map_tiles['url'],
    attr=map_tiles['html_attribution'],
    zoom_start=8,
    min_zoom=7,
    location=[0, 0],
    max_bounds=True,
    max_lat=0,
    max_lon=0,
    min_lat=0,
    min_lon=0,
    width=700,
    height=500)

# links
iqaasl = "https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/land_use_correlation.html"
near_or_far = "https://hammerdirt-analyst.github.io/landuse/titlepage.html"
manu_script = "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4561991"
hammerdirt = "https://hammerdirt.ch/"
litter_assistant = "https://hammerdirt-analyst.github.io/feb_2024/titlepage.html"
litter_thresholds = "https://mcc.jrc.ec.europa.eu/main/dev.py?N=41&O=453"
guidelines_2023 = "https://mcc.jrc.ec.europa.eu/main/dev.py?N=41&O=466"
solide_waste_team = "https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html"


def apply_requested_parameters(df, parameters: dict):

    if parameters['code'] not in ['all', 'tout', 'alle']:
        df = df[df['code'] == parameters['code']]
    theme = parameters['theme']
    print(theme)
    if theme in feature_types:
        df = df[df.feature_type == theme]
        df = df[df.feature_name == parameters['feature']]
    else:
       df = df[df[theme] == parameters['feature']]

    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.date

    mask = make_date_mask(df, parameters['start_date'], parameters['end_date'])
    return df[mask]





