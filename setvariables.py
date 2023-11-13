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
table_caption = {'selector': 'caption', 'props': 'caption-side: bottom; font-size:1em; text-align: left;'}
table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data, table_caption]

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

code_data =  "data/end_process/codes.csv"
beach_data = "data/end_process/beaches.csv"
land_cover_data = "data/end_process/land_cover.csv"
land_use_data = "data/end_process/land_use.csv"
street_data = "data/end_process/streets.csv"
intersection_attributes = "data/end_process/river_intersect_lakes.csv"

# order of aggregation corresponds to place labels and types
geo_h = ['parent_boundary', 'feature_type',  'feature_name', 'canton', 'city']

# the unit total columns. aggregating by these columns will give
# total value for each unique code identified with loc_date
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

work_columns = ['slug', 'loc_date', 'feature_name', 'parent_boundary', 'city','canton', 'pcs_m', 'quantity','code', 'feature_type']
#
# group_by_columns = [
#     'loc_date',
#     'date',
#     'parent_boundary',
#     'feature_name',
#     'city',
#     'slug',
#     'length',
#     'groupname',
#     'code',
# ]

agg_groups = {
    "quantity":"sum",
    "pcs_m": "median"
}




unit_agg = {
    "quantity":"sum",
    "pcs_m": "sum"
}


# land_cover_fr = {
#     'undefined': 'Non défini',
#     'Siedl': 'Siedl',
#     'Wald': 'Forêt',
#     'Reben': 'Vignes',
#     'Obstanlage': 'Verger'
# }

land_cover_en = {
    'undefined': 'Undefined',
    'Siedl': 'Settlement',
    'Wald': 'Forest',
    'Reben': 'Vines',
    'Obstanlage': 'Orchard'
}

# land_use_fr = {
#     'Baumschule': 'Pépinière',
#     'Friedhof': 'Cimetière',
#     'Schul- und Hochschulareal': 'Zone scolaire et universitaire',
#     'Wald nicht bestockt': 'Forêt non peuplée',
#     'Abwasserreinigungsareal': 'Zone de traitement des eaux usées',
#     'Historisches Areal': 'Zone historique',
#     'Kraftwerkareal': 'Zone de centrale électrique',
#     'Schrebergartenareal': 'Zone de jardins familiaux',
#     'Truppenuebungsplatz': 'Terrain d\'entraînement militaire',
#     'Unterwerkareal': 'Zone de sous-station',
#     'Kehrichtverbrennungsareal': 'Zone d\'incinération des déchets',
#     'Spitalareal': 'Zone d\'hôpital',
#     'Oeffentliches Parkareal': 'Zone de parc public',
#     'Messeareal': 'Zone d\'exposition',
#     'Massnahmenvollzugsanstaltsareal': 'Zone d\'établissement de traitement',
#     'Kiesabbauareal': 'Zone d\'extraction de gravier',
#     'Steinbruchareal': 'Zone de carrière',
#     'Klosterareal': 'Zone de monastère',
#     'Deponieareal': 'Zone de décharge',
#     'Antennenareal': 'Zone d\'antennes',
#     'Lehmabbauareal': 'Zone d\'extraction d\'argile'
# }

# land_use_en = {
#     'Baumschule': 'Nursery',
#     'Friedhof': 'Cemetery',
#     'Schul- und Hochschulareal': 'School and University Area',
#     'Wald nicht bestockt': 'Non-stocked Forest',
#     'Abwasserreinigungsareal': 'Wastewater Treatment Area',
#     'Historisches Areal': 'Historical Area',
#     'Kraftwerkareal': 'Power Plant Area',
#     'Schrebergartenareal': 'Allotment Garden Area',
#     'Truppenuebungsplatz': 'Military Training Ground',
#     'Unterwerkareal': 'Substation Area',
#     'Kehrichtverbrennungsareal': 'Waste Incineration Area',
#     'Spitalareal': 'Hospital Area',
#     'Oeffentliches Parkareal': 'Public Park Area',
#     'Messeareal': 'Exhibition Area',
#     'Massnahmenvollzugsanstaltsareal': 'Correctional Facility Area',
#     'Kiesabbauareal': 'Gravel Extraction Area',
#     'Steinbruchareal': 'Quarry Area',
#     'Klosterareal': 'Monastery Area',
#     'Deponieareal': 'Landfill Area',
#     'Antennenareal': 'Antenna Area',
#     'Lehmabbauareal': 'Clay Extraction Area'
# }

# land_uses_grouped:
# outdoor non technical use:
lu_non_tech = {'places': ['Friedhof', 'Hitorisches Areal', 'Schrebergartenareal', 'Oeffentliches Parkareal', 'Messeareal', 'Klosterareal',  'Wald nicht bestockt', 'Baumschule']}

# technical-extraction-incineration
# lu_extraction = {'mining': ['Kiesabbauareal', 'Steinbruchareal',  'Lehmabbauareal']}

# waste-water-treatment-powere
lu_technical = {'technical':['Kehrichtverbrennungsareal', 'Deponieareal', 'Deponieareal', 'Abwasserreinigungsareal','Unterwerkareal', 'Antennenareal', 'Kraftwerkareal', 'Kiesabbauareal', 'Steinbruchareal',  'Lehmabbauareal']}

# services:
lu_services = {'services': ['Massnahmenvollzugsanstaltsareal', 'Schul- und Hochschulareal', 'Spitalareal', 'Historisches Areal', 'Truppenuebungsplatz']}

#combined:
lu_combined = {'land_use':[*list(lu_non_tech.keys()), *list(lu_technical.keys()), *list(lu_services.keys())]}

lu_groups = [lu_non_tech,lu_technical, lu_services, lu_combined]

# streets_fr = {
#     'Autostr': 'autoroute',
#     'NebenStr3': 'route secondaire 3',
#     'NebenStr6': 'route secondaire 6',
#     'HauptStrAB6': 'route principale 6',
#     'HauptStrAB4': 'route principale 4',
#     'Fahrstraes': 'chemin carrossable',
#     'Fussweg': 'chemin pédestre',
#     'Autobahn': 'autoroute',
#     'Autob_Ri': 'autoroute',
#     'VerbindStr4': 'route de liason 4',
#     'VerbindStr6': 'route de liason 6',
# }
#
# streets_en = {
#     'Autostr': 'freeway',
#     'NebenStr3': 'surface streets 3',
#     'NebenStr6': 'surface streets 3 6',
#     'HauptStrAB6': 'inter regional 6',
#     'HauptStrAB4': 'inter regional 4',
#     'Fahrstraes': 'bridle path',
#     'Fussweg': 'pedestrian trail',
#     'Autobahn': 'freeway',
#     'Autob_Ri': 'freeway',
#     'VerbindStr4': 'intra regional 4',
#     'VerbindStr6': 'intra regional 6',
# }

str_surface = {'surface streets':['NebenStr3', 'NebenStr6']}
str_ped_br = {'pedestrian': ['Fahrstraes', 'Fussweg']}
str_main = {'principal': [ 'HauptStrAB6', 'VerbindStr4','VerbindStr6', 'HauptStrAB4', 'NebenStr6']}

str_auto = {'highways': ['Autobahn', 'Autostr', 'Autob_Ri']}

str_combined = {'streets':['surface streets', 'pedestrian', 'principal', 'highways']}

street_groups = [str_surface, str_ped_br, str_main, str_auto, str_combined]


