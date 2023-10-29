# aconfig file for summarizing the data from surveys
import matplotlib as mpl
import numpy as np
from matplotlib.colors import ListedColormap

# the formatting for pd.styler
format_kwargs = dict(precision=2, thousands="'", decimal=",")

# this defines the css rules for the note-book table displays
header_row = {'selector': 'th:nth-child(1)', 'props': f'background-color: #FFF; font-size:12px; text-align:left;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': f'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 10px;'}
table_data = {'selector': 'td', 'props': 'padding:4px; font-size:12px;'}
table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data]

# a color gradient for heat maps
# this uses a mix and resamples between 0 and 1
# change the colors  or substitute a  valid matplotlib colormap
top = mpl.colormaps['Oranges'].resampled(2000)
bottom = mpl.colormaps['Greys'].resampled(2000)

newcolors = np.vstack((bottom(np.linspace(0, 1, 2000)),
                   top(np.linspace(0, 1, 2000))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')

a_cmap = newcmp(np.arange(newcmp.N))
a_cmap[:, -1] = np.linspace(0, 1, newcmp.N)
newcmp = ListedColormap(a_cmap)

# period dates
period_dates = {
    "mcbp":["2015-11-15", "2017-03-31"],
    "slr": ["2017-04-01", "2020-02-28"],
    "iqaasl": ["2020-03-01", "2021-05-31"],
    "2022": ["2021-06-01", "2022-12-01"]
}

survey_files = [
    "data/end_process/after_may_2021.csv",
    "data/end_process/iqaasl.csv",
    "data/end_process/mcbp.csv",
    "data/end_process/slr.csv",
]

language_maps = {
    'fr':'data/end_process/fr_labels.csv',
    'de': 'data/end_process/de_labels.csv'
}

geo_h = ['parent_boundary', 'feature_type',  'feature_name','canton', 'city']

code_data =  "data/end_process/codes.csv"
beach_data = "data/end_process/beaches.csv"
land_cover_data = "data/end_process/land_cover.csv"
land_use_data = "data/end_process/land_use.csv"
street_data = "data/end_process/streets.csv"
intersection_attributes = "data/end_process/river_intersect_lakes.csv"

code_result_columns = [
    'loc_date', 
    'date',
    'parent_boundary',
    'feature_name',
    'city',
    'slug',
    'length',
    'code'
]

group_by_columns = [
    'loc_date',
    'date',
    'parent_boundary',
    'feature_name',
    'city',
    'slug',
    'length',
    'groupname',
    'code',
]

agg_groups = {
    "quantity":"sum",
    "pcs_m": "median"
}




unit_agg = {
    "quantity":"sum",
    "pcs_m": "sum"
}



