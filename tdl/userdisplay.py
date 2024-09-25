"""
userdisplay.py
hammerdirt 2024
Author: Roger Erismann

NOTE: This module is a work in progress.

The userdisplay.py module is a collection of functions that are used to display the results of the survey report in a
jupyter notebook. For tables, we rely on the pandas styling API. The charts are generated with the bokeh plotting library
or matplotlib.

The intention is to fold the userdisplay.py module into a module that takes advantage of the sphinx documentation system.
While the user interface for the app would be handled by NEXT.js.
"""
import folium
from folium import Marker
from folium.plugins import MarkerCluster
import pandas as pd

from session_config import session_language
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np

from session_config import code_definitions_map,  feature_data





beaches = pd.read_csv(feature_data['beach_data'])
lat_lon = beaches[['slug', 'latitude', 'longitude']].set_index('slug')
f_names = beaches[['feature_name', 'display_feature_name']].drop_duplicates().set_index('feature_name')

# definitions for charts and tables
land_use_map = {
    'en': {
        'orchards': 'Orchards',
        'vineyards': 'Vineyards',
        'buildings': 'Buildings',
        'forest': 'Forest',
        'undefined': 'Undefined',
        'public services': 'Public Services',
        'streets': 'Streets'
    },
    'fr': {
        'orchards': 'Vergers',
        'vineyards': 'Vignobles',
        'buildings': 'Bâtiments',
        'forest': 'Forêt',
        'undefined': 'Non défini',
        'public services': 'Services publics',
        'streets': 'Rues'
    },
    'de': {
        'orchards': 'Obstgärten',
        'vineyards': 'Weinberge',
        'buildings': 'Gebäude',
        'forest': 'Wald',
        'undefined': 'undefiniert',
        'public services': 'öffentliche Dienste',
        'streets': 'Strassen'
    }
}

theme_map = {
    'en': {
        'canton': 'Canton',
        'city': 'Municipality',
        'parent_boundary': 'River basin',
        'r': 'River',
        'l': 'Lake',
        'p': 'Park'
    },
    'fr': {
        'canton': 'Canton',
        'city': 'Municipalité',
        'parent_boundary': 'Bassin versant',
        'r': 'Rivière',
        'l': 'Lac',
        'p': 'Parc'
    },
    'de': {
        'canton': 'Kanton',
        'city': 'Gemeinde',
        'parent_boundary': 'Flusseinzugsgebiet',
        'r': 'Fluss',
        'l': 'See',
        'p': 'Park'
    }}

display_units = {
    'en': 'pcs/m',
    'fr': 'pcs/m',
    'de': 'Stk/m'
}

w_sampling_results = {
    "en": {
        'title': 'Summary of selected data',
        'total': 'Total objects',
        'nsamples': 'Number of samples',
        'average': 'Average pcs/m',
        'std': 'Standard deviation',
        'max': 'Maximum pcs/m',
        'quantiles': f'Distribution of {display_units[session_language]}',
        'start': 'Date of first sample',
        'end': 'Date of last sample'
    },
    "fr": {
        'title': 'Résumé des données sélectionnées',
        'total': 'Nombre total d\'objets',
        'nsamples': 'Nombre d\'échantillons',
        'average': 'Moyenne par mètre',
        'quantiles': f'Distribution observée des {display_units[session_language]}',
        'start': 'premier échantillon',
        'end': 'dernier échantillon'
    },
    "de": {
        'title': 'Zusammenfassung der ausgewählten Daten',
        'total': 'Abfallobjekte',
        'nsamples': 'Erhebungen',
        'average': 'Durchschnitt pro Meter',
        'quantiles': f'Beobachtete Verteilung der {display_units[session_language]}',
        'start': 'erste Probe',
        'end': 'letzte Probe'}
}

w_admin_boundaries = {
    'en': {
        'title': 'Administrative boundaries',
        'count': 'Count',
        'city' : 'Cities',
        'canton': 'Cantons',
        'parent_boundary': 'River basins or Parks',
        'location': 'Survey locations'
    },
    'fr': {
        'title': 'Limites administratives',
        'count': 'Compter',
        'city': 'Villes',
        'canton': 'Cantons',
        'parent_boundary': 'Bassins versants ou parcs',
        'location': 'Sites d\'enquête'
    },
    'de': {
        'title': 'Verwaltungsgrenzen',
        'count': 'Zählen',
        'city': 'Städte',
        'canton': 'Kantone',
        'parent_boundary': 'Flussgebiete oder Parks',
        'location': 'Untersuchungsstandorte',
    }}

w_feature_inventory = {
    'en': {
        'title': 'Features surveyed',
        'count': 'Count',
        'l': 'Lakes',
        'p': 'Parks',
        'r': 'Rivers',
    },
    'fr': {
        'title': 'Fonctionnalités étudiées',
        'count': 'Compte',
        'l': 'Lacs',
        'p': 'Parcs',
        'r': 'Rivières',
    },
    'de': {
        'title': 'Untersuchte Funktionen',
        'count': 'Zählen',
        'l': 'Seen',
        'p': 'Parks',
        'r': 'Flüsse',
    }
}

material_languages = {
    'en': {
        'plastic': 'Plastic',
        'metal': 'Metal',
        'glass': 'Glass',
        'paper': 'Paper',
        'wood': 'Wood',
        'unidentified': 'Unidentified',
        'chemicals': 'Chemicals',
        'rubber': 'Rubber',
        'cloth': 'Cloth',
    },
    'fr': {
        'plastic': 'Plastique',
        'metal': 'Métal',
        'glass': 'Verre',
        'paper': 'Papier',
        'wood': 'Bois',
        'unidentified': 'Non identifié',
        'chemicals': 'Produits chimiques',
        'rubber': 'Caoutchouc',
        'cloth': 'Tissu',
    },
    'de': {
        'plastic': 'Plastik',
        'metal': 'Metall',
        'glass': 'Glas',
        'paper': 'Papier',
        'wood': 'Holz',
        'unidentified': 'Ubekannt',
        'chemicals': 'Chemikalien',
        'rubber': 'Gummi',
        'cloth': 'Stoff',
    }
}

# the formatting for pd.styler
format_kwargs = dict(precision=2, thousands="'", decimal=",")

# this defines the css rules for the table displays
header_row = {'selector':'th', 'props': 'background-color: #FFF; font-size:12px; text-align:left; width: auto; word-break: keep-all;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': 'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 12px;'}
table_data = {'selector': 'td', 'props': 'padding:4px; font-size:12px;text-align: center;'}
table_caption = {'selector': 'caption', 'props': 'caption-side: bottom; font-size:1em; text-align: left;'}
table_caption_top = {'selector': 'caption', 'props': 'caption-side: top; font-size:1em; text-align: left; margin-bottom: 10px;'}
caption_css = {'selector': 'caption', 'props': 'caption-side: top; font-size:.9em; text-align: left; font-style: italic; color: #000;'}
table_first_column_left = {'selector': 'td:nth-child(1)', 'props': 'text-align: left;'}
table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data, table_caption_top]
highlight_props = 'background-color:#FAE8E8'

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

# hour color map should be type matplotlib.colors.ListedColormap
newcmp = ListedColormap(a_cmap)


# def sampling_result_summary(data: dict, session_language: str, texts: dict = w_sampling_results):
#     """Display the sampling results summary"""
#
#     data_labels = texts[session_language]
#
#     to_display = ""
#
#     for akey in ['nsamples', 'total', 'average', 'std', 'max']:
#         to_display += f"* {data_labels[akey]}: {round(data[akey], 2)}\n"
#     if 'start' in data.keys():
#
#         for akey in ['start', 'end']:
#             if isinstance(data[akey], str):
#                 to_display += f"* {data_labels[akey]}: {data[akey]}\n"
#             else:
#                 the_date = dt.datetime.strftime(data[akey], session_config.date_format)
#                 to_display += f"* {data_labels[akey]}: {the_date}\n"
#
#
#     display_observed_quantiles = ""
#     for akey in ['quantiles']:
#         pcts_as_string = ['{:.0%}'.format(x) for x in session_config.report_quantiles]
#         data_to_string = [str(round(x, 2)) for i, x in enumerate(data[akey])]
#         combined = [f'{pcts_as_string[i]}: {data_to_string[i]}' for i in range(len(pcts_as_string))]
#         for value in combined:
#             display_observed_quantiles += f"* {value}\n"
#
#     return f"__{data_labels['title']}__", to_display, f"__{data_labels['quantiles']}__", display_observed_quantiles
#
#
# def boundaries(data: dict, session_language: str):
#     """Display the administrative boundaries"""
#     to_display_boundaries = ""
#     for key in data.keys():
#         to_display_boundaries += f"* {w_admin_boundaries[session_language][key]}: {data[key]['count']}\n"
#
#     return f'__{w_admin_boundaries[session_language]["title"]}__\n{to_display_boundaries}\n'
#
#
# def feature_inventory(data: dict, session_language: str = 'de'):
#     """Display the feature inventory"""
#     to_display_features = ""
#     for key in data.keys():
#         to_display_features += f"* {w_feature_inventory[session_language][key]}: {data[key]['count']}\n"
#
#     return f'__{w_feature_inventory[session_language]["title"]}__\n{to_display_features}\n'


default_chart_args = dict(
        title='Sample totals',
        x_axis_type="datetime",
        x_axis_label='date',
        y_axis_label='pcs/m',
        sizing_mode="fixed", width=400, height=400
    )

chart_args_languages = {
    'en': dict(
        title='Sample totals',
        x_axis_type="datetime",
        x_axis_label='date',
        y_axis_label='pcs/m',
        sizing_mode="fixed", width=400, height=400
    ),
    'fr': dict(
        title='Total par échantillon',
        x_axis_type="datetime",
        x_axis_label='date',
        y_axis_label='pcs/m',
        sizing_mode="fixed", width=400, height=400
    ),
    'de': dict(
        title='Stichproben',
        x_axis_type="datetime",
        x_axis_label='Datum',
        y_axis_label='Stk/m',
        sizing_mode="fixed", width=400, height=400
    )
}

most_common_columns = {
    'en': {
        'code': 'Object',
        'quantity': 'Quantity',
        'pcs/m': 'pcs/m',
        '% of total': '% of total',
        'rate': 'Fail rate'
    },
    'fr': {
        'code': 'Objet',
        'quantity': 'Quantité',
        'pcs/m': 'pcs/m',
        '% of total': '% du total',
        'rate': 'Taux d\'échec'
    },
    'de': {
        'code': 'Objekt',
        'quantity': 'Objekt (St.)',
        'pcs/m': 'Stk/m',
        '% of total': 'Anteil',
        'rate': 'Häufigkeitsrate'
        
    }
    
}

w_no_columns_to_combine = {
    'en': '__No columns to combine:__ Note that a correlation coefficient of 1 or -1 is not considered.',
    'fr': '__Aucune colonne à combiner:__ Notez qu\'un coefficient de corrélation de 1 ou -1 n\'est pas considéré.',
    'de': '__Keine Spalten zum Kombinieren:__ Beachten Sie, dass ein Korrelationskoeffizient von 1 oder -1 nicht '
          'berücksichtigt wird.'
}

w_columns_to_combine = {
    "en": {
        'method': 'Method',
        'new_name': 'New name'
    },
    "fr": {
        'method': 'Méthode',
        'new_name': 'Nouveau nom'
    },
    "de": {
        'method': 'Methode',
        'new_name': 'Neuer Name'
        
    }
}


def code_definitions(codes: pd.Series, session_language: str = 'en'):
    
    language_map = code_definitions_map[session_language]
    defined = codes.apply(lambda x: language_map.loc[x])
    return defined

def code_selector(selections: [] = None, session_language: str = 'en'):
    language_map = code_definitions_map[session_language]
    descriptions = [language_map.loc[x] for x in selections[1:]]
    all = {
        'en': 'all',
        'fr': 'tout',
        'de': 'alle'
    }

    return [all[session_language], *descriptions]

def style_negative(v, props=''):
    """from panaas docs: pandas-docs/version/0.24.2/reference/api/pandas.io.formats.style.Styler.applymap.html"""
    return props if v < 0 else None



def highlight_max(s, props: str = highlight_props):
    return np.where((s == np.max(s.values)) & (s != 1), props, '')
def style_negative(v, props=''):
    return props if v < 0 else None


def map_markers(df, lat_lon: pd.DataFrame = lat_lon):
    """Map the markers"""
    nsamples = df.groupby('location', observed=True)['sample_id'].nunique()
    qty_location = df.groupby('location', observed=True)['quantity'].sum()
    rate_location = df.groupby('location', observed=True)['pcs/m'].mean().round(2)
    last_sample = df.groupby('location', observed=True)['date'].max()
    df = pd.concat([nsamples, qty_location, rate_location, last_sample], axis=1)
    df = df.merge(lat_lon, left_index=True, right_index=True)
    df['location'] = df.index
    max_lat, min_lat = df['latitude'].max(), df['latitude'].min()
    max_lon, min_lon = df['longitude'].max(), df['longitude'].min()
    
    return df.to_dict(orient='records'), {'max_lat': max_lat, 'min_lat': min_lat, 'max_lon': max_lon, 'min_lon': min_lon}


def map_pop_up_markers(a_marker, session_language: str = 'en'):
    """Map the pop up markers"""
    language_labels = {
        'en':{
            'location': 'Location',
            'sample_id': 'Samples',
            'quantity': 'Total objects',
            'pcs/m': 'pcs/m',
        },
        'fr': {
            'location': 'Emplacement',
            'sample_id': 'Échantillons',
            'quantity': 'Objets totaux',
            'pcs/m': 'pcs/m',
        },
        'de': {
            'location': 'Ort',
            'sample_id': 'Proben',
            'quantity': 'Gesamtobjekte',
            'pcs/m': 'Stk/m',
        }
        
    }
    loc_list = f'<li>{language_labels[session_language]["location"]} : {a_marker["location"]}</li>'
    n_samples = f'<li>{language_labels[session_language]["sample_id"]} : {a_marker["sample_id"]}</li>'
    quantity = f'<li>{language_labels[session_language]["quantity"]} : {"{:,}".format(a_marker["quantity"])}</li>'
    pcs_meter = f'<li>{language_labels[session_language]["pcs/m"]} : {a_marker["pcs/m"]}</li>'
    
    return f"<div style='min-width:300px; word-break: keep-all;'><ul>{loc_list}{n_samples}{quantity}{pcs_meter}</ul></div>"


def define_folium_markers(m: folium.Map, marker_data: [] = None,  session_language: str = 'en'):
    """Define the folium markers"""

    marker_cluster = MarkerCluster().add_to(m)
    
    for a_marker in marker_data:
        popup = map_pop_up_markers(a_marker, session_language=session_language)
        marker = Marker(location=[a_marker['latitude'], a_marker['longitude']], popup=popup)
        marker.add_to(marker_cluster)
    return m

# def object_summary(df, session_language: str = 'en'):
#     """Display the object summary"""
#     explain = {
#         'en': "The inventory details the total quantity, average pcs/m, % of total and fail rate for each object identified "
#               "in the report.",
#         'fr': "L'inventaire détaille la quantité totale, la moyenne des pcs/m, le % du total et le taux d'échec pour chaque "
#                 "objet identifié dans le rapport.",
#         'de': "Das Inventar enthält die Gesamtmenge, den durchschnittlichen Stückpreis, den Prozentsatz des Gesamtwerts "
#                 "und die Ausfallrate für jedes im Bericht identifizierte Objekt."
#     }
#
#     caption = {
#         'en': f"<b>The inventory.</b> {explain['en']}",
#         'fr': f"<b>L'inventaire</b> {explain['fr']}",
#         'de': f"<b>Das Inventar</b> {explain['de']}"
#     }
#
#     a_new_index = [code_definitions_map[session_language].loc[x] for x in df.code]
#     table_style = [*table_css_styles[:-1], table_caption_top, caption_css, table_first_column_left]
#     df[['rate', '% of total']] = df[['rate', '% of total']].apply(lambda x: (x * 100).round(0).astype(str) + '%')
#     df['code'] = a_new_index
#     df = df[['code', 'quantity', 'pcs/m', '% of total', 'rate']]
#     df = df.sort_values('quantity', ascending=False)
#     df.rename(columns=most_common_columns[session_language], inplace=True)
#     f = df.style.set_table_styles(table_style).format(**format_kwargs)
#     f = f.set_caption(caption[session_language])
#
#
#     return f.hide(axis=0)

# def landuse_catalog(df, session_language: str = 'en'):
#     """Display the land use catalog"""
#     explain = {
#         'en': "The land use catalog details the magnitude of land each land use category for each location, was well as "
#               "the average pcs/m for the location",
#         'fr': "Le catalogue d'utilisation des terres détaille la quantité de terre de chaque catégorie d'utilisation des "
#               "terres pour chaque emplacement, ainsi que la moyenne des pcs/m pour l'emplacement.",
#         'de': "Der Landnutzungskatalog gibt die Grösse des Landes für jede Landnutzungskategorie für jeden Standort an, "
#               "sowie den durchschnittlichen Stückpreis für den Standort."
#     }
#
#     caption = {
#         'en': f"<b>The land use catalog.</b> {explain['en']}",
#         'fr': f"<b>Le catalogue d'utilisation des terres.</b> {explain['fr']}",
#         'de': f"<b>Der Landnutzungskatalog.</b> {explain['de']}"
#     }
#
#     df = df.sort_values('pcs/m', ascending=False)
#     df['pcs/m'] = df['pcs/m'].apply(lambda x: f'{round(x, 2)}'  if x > 0 else '0')
#     df.rename(columns=land_use_map[session_language], inplace=True)
#     f = df.style.set_table_styles([table_caption_top, caption_css, table_font, header_row, table_data, table_first_column_left])
#     # f.map(lambda x: 'color: #E5E5E5' if pd.isnull(x) else '')
#     # f.map(lambda x: 'background: #E5E5E5' if pd.isnull(x) else '')
#     # f.format({**format_kwargs})
#
#     f = f.set_caption(caption[session_language])
#
#     return f.hide(axis=0)


def buffer_pcs_m(m: folium.Map, marker_data: [] = None, df: pd.DataFrame = None, session_language: str = 'en'):
    # """Buffer the pcs/m"""
    # for a_marker in marker_data:
    #
    #     radius = a_marker['pcs/m']
    #     folium.Circle(
    #         location=[a_marker['latitude'], a_marker['longitude']],
    #         radius=radius,
    #         color="black",
    #         weight=1,
    #         fill_opacity=0.6,
    #         opacity=1,
    #         fill_color="green",
    #         fill=False,
    #         popup="{} meters".format(radius),
    #         tooltip="I am in meters",
    #     ).add_to(m)
    # return m
    pass
