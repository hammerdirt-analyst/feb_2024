"""
geospatial.py
hammerdirt 2024
Author: Roger Erismann

NOTE: This module is a work in progress.

The geospatial module is a collection of functions that are used to match survey data with land use data. The land use
for each survey location is calculated by summing the area of each land use type within a buffer of the survey location.

Each location has a unique land use profile. The land use profile is a summary of the land use types within the buffer.
However, when categorized, the land use profile is used to group locations with similar land use attributes.

A LandUseReport is a container for the data and methods that are used to generate a report from a survey data set. The
report is a summary of the data in the survey with respect to the landuse features of the survey locations. The LandUseReport
contains the following information:

Dependencies
------------
- pandas
- sklearn.preprocessing.MinMaxScaler
- session_config

Functions
---------
- select_x_and_y(df_target: pd.DataFrame, features: pd.DataFrame) -> pd.DataFrame
- categorize_features(df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame

Classes
-------
- LandUseReport
    - __init__(self, df_target, features)
    - merge_land_use_to_survey_data(self) -> None
    - categorize_columns(self, df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame
    - n_samples_per_feature(self, df: pd.DataFrame = None, features: list[str] = None) -> pd.DataFrame
    - n_pieces_per_feature(self) -> pd.DataFrame
    - locations_per_feature(self) -> pd.DataFrame
    - rate_per_feature(self, df: pd.DataFrame = None) -> pd.DataFrame
    - correlation_matrix(self) -> pd.DataFrame
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import geopandas as gpd
import folium
from shapely.geometry import Point

import session_config
from session_config import feature_variables, lat_lon, dbckey, canton_layer, rgba_to_css
from session_config import location_label, Y, Q, municipal_layer, rivers_layer, lakes_layer

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from matplotlib import colormaps as mpl_color_maps
from matplotlib.lines import Line2D

gpd.options.io_engine = "pyogrio"
pd.set_option('future.no_silent_downcasting', True)

def make_folium_map(markers, bounds):
    m = folium.Map(
        max_bounds=True,
        zoom_start=15,
        min_zoom= 10,
        min_lat=bounds[0][1] - .1,
        max_lat=bounds[1][1] + .1,
        min_lon=bounds[0][0] - .1,
        max_lon=bounds[1][0] + .1,
        tiles='https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg',
        attr='Swiss Topo'
    )

    for _, row in markers.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['location'],  # Set the location as the popup text
            icon=folium.Icon(icon='info-sign', color='red')  # You can customize the icon as needed
        ).add_to(m)
    m.fit_bounds(bounds)

    return m

def make_map_caption(report_meta):
    prefix = 'Surveys '
    start = report_meta['start'][:4]
    end = report_meta['end'][:4]
    return f'{prefix} {report_meta["name"]} {start} {end}'

def get_color_from_value(value, vmin, vmax, cmap_name='YlOrBr'):
    """
    Returns a color from a specified colormap based on a float value.

    :param value: The float value to map to a color.
    :param vmin: The minimum value of the data range for normalization.
    :param vmax: The maximum value of the data range for normalization.
    :param cmap_name: The name of the colormap to use (default is 'YlOrBr').
    :return: A color in RGBA format.
    """
    # Normalize the value to the range [0, 1] based on vmin and vmax
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

    # Get the colormap
    cmap = mpl_color_maps[cmap_name]

    # Map the normalized value to a color
    color = cmap(norm(value))

    return color

def get_cluster_color(cluster_number, cmap_name='tab20'):
    """
    Assigns a color to a cluster number using the specified colormap and returns it in RGBA format.

    :param cluster_number: The cluster number (integer).
    :param cmap_name: The name of the colormap to use (default is 'tab20').
    :return: A color in RGBA format corresponding to the cluster number.
    """
    # Get the colormap from Seaborn
    cmap = sns.color_palette(cmap_name, 20)  # 'tab20' has 20 colors

    # Map the cluster number to a color, cycling through the colormap if needed
    color = cmap[cluster_number % len(cmap)]

    # Convert the color to RGBA format with alpha set to 1
    rgba_color = mcolors.to_rgba(color)

    return rgba_color

def situation_map_plot(map_legend_markers, report_meta, file_name='situation_map.jpg', location_markers: str = 'o', show: bool = True):

    fig, ax = plt.subplots()
    bounds = map_legend_markers['bounds']

    canton_layer.plot(ax=ax, zorder=1, edgecolor='black', facecolor='white', alpha=.5, linewidth=.4)

    # if map_legend_markers['cluster_results'] is not None:
    #     map_legend_markers['city_layer'].plot(ax=ax, zorder=1, edgecolor='black',
    #                                           facecolor=map_legend_markers['city_layer'].color, alpha=1, linewidth=.6)

    rivers_layer.plot(ax=ax, zorder=2, edgecolor='dodgerblue', linewidth=1)
    municipal_layer.plot(ax=ax, zorder=3, edgecolor='black', facecolor='white', alpha=.6, linewidth=.4)

    lakes_layer.plot(ax=ax, zorder=4, edgecolor='dodgerblue', facecolor='dodgerblue')

    boundary_pad = .02

    ax.set_xlim(bounds[0] - boundary_pad, bounds[2] + boundary_pad)
    ax.set_ylim(bounds[1] - boundary_pad, bounds[3]+ boundary_pad)

    map_legend_markers['markers'].plot(ax=ax, zorder=5, markersize=120, edgecolor='black', linewidth=1,
                                       facecolor=map_legend_markers['markers'].cluster_color.values,
                                       marker=location_markers, alpha=.8)

    ax.axis('off')
    ax.legend(handles=map_legend_markers['legend_handles'], labels=map_legend_markers['legend_labels'],
              title='Clusters', fontsize=6, title_fontsize=8, loc='best')
    situation_map = f'{report_meta["resources"]}{file_name}'
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.tight_layout()# Remove padding
    plt.rcParams.update({'figure.autolayout': True})

    # Save the figure tightly to minimize white space
    print(f'saving map to {situation_map}')
    plt.savefig(situation_map,  bbox_inches='tight', pad_inches=0, dpi=300, transparent=True)

    if show is True:
        plt.show()
    else:
        plt.close()

def situation_map(markers, report_data, linear_methods, pdf_columns, report_meta, location_marker='o'):
    # legend components
    # if their is a cluster analysis we want to note which cluster each location
    # belongs to on the map

    cr = None
    legend_handles = []
    labels = []
    report_cities = None
    g_city = None
    bounds = markers.total_bounds
    print('defining map components')

    if linear_methods['cluster_analysis'] is not None:
        # clusters_ = True
        print('adding cluster analysis to map legend')
        clustered_data, average_landuse_per_cluster, average_pcsm_cluster = linear_methods['cluster_analysis']

        clustered_results = average_pcsm_cluster.merge(average_landuse_per_cluster, left_index=True, right_index=True)
        point_cluster = clustered_data.drop_duplicates('location')
        point_cluster = point_cluster.set_index('location', drop=True)
        markers['cluster'] = markers.location.map(lambda x: point_cluster.loc[x, 'cluster'])
        markers['cluster_color'] = markers.cluster.map(lambda x: get_cluster_color(x))

        cr = clustered_results[['pcs/m', *pdf_columns]].copy()
        cr['color'] = cr.index.map(lambda x: get_cluster_color(x))

        # map legend entries

        for i, a_color in enumerate(cr.color.unique()):
            a_patch = Line2D([0], [0], marker=location_marker, color='black', markerfacecolor=a_color, markersize=6)
            legend_handles.append(a_patch)

            label = f'Cluster {i}'
            labels.append(label)

        # cluster results table
        cr = cr.style.apply(rgba_to_css, axis=1)
        cr = cr.format(**session_config.format_kwargs).hide(['color'], axis=1)

    if report_meta['boundary'] == 'city':
        # if the report is at the municipal level
        # summarize the results by location
        print('making location report')
        markers = markers.sort_values('location')
        markers.reset_index(inplace=True, drop=True)
        markers['cluster_color'] = markers.index.map(lambda x: get_cluster_color(x))


        legend_handles = []
        labels = []
        for a_color in markers[['location', 'cluster_color']].values:
            a_patch = Line2D([0], [0], marker=location_marker, color='black', markerfacecolor=a_color[1],
                             markersize=6)
            legend_handles.append(a_patch)

            labels.append(a_color[0])

        # legend table
        # attach land use to marker data for map table and legend
        mask = report_data.landuse_report.df_cont.location.isin(markers.location.unique())
        land_use = report_data.landuse_report.df_cont[mask].drop_duplicates('location')

        g_city = markers[['location', 'quantity', 'pcs/m', 'cluster_color']].copy()
        clustercolumns = ['buildings', 'forest', 'undefined', 'recreation', 'public-services']
        g_city = g_city.merge(land_use[['location', *clustercolumns]], on='location', how='left')
        g_city.rename(columns={'cluster_color': 'color'}, inplace=True)
        g_city = g_city.style.apply(rgba_to_css, axis=1)
        cr = g_city.format(**session_config.format_kwargs).hide(['color'], axis=1)

    if linear_methods['cluster_analysis'] is None and report_meta['boundary'] != 'city':


        markers = markers.sort_values('location')
        markers.reset_index(inplace=True, drop=True)
        markers['cluster_color'] = markers.index.map(lambda x: get_cluster_color(x))

        legend_handles = []
        labels = []
        for a_color in markers[['location', 'cluster_color']].values:
            a_patch = Line2D([0], [0], marker=location_marker, color='black', markerfacecolor=a_color[1],
                             markersize=6)
            legend_handles.append(a_patch)

            labels.append(a_color[0])

        # legend table
        mask = report_data.landuse_report.df_cont.location.isin(markers.location.unique())
        land_use = report_data.landuse_report.df_cont[mask].drop_duplicates('location')

        g_city = markers[['location', 'quantity', 'pcs/m', 'cluster_color']].copy()
        clustercolumns = ['buildings', 'forest', 'undefined', 'recreation', 'public-services']
        g_city = g_city.merge(land_use[['location', *clustercolumns]], on='location', how='left')
        # g_city = g_city.merge(land_use, on='location', how='left')
        g_city.rename(columns={'cluster_color': 'color'}, inplace=True)
        g_city = g_city.style.apply(rgba_to_css, axis=1)
        cr = g_city.format(**session_config.format_kwargs).hide(['color'], axis=1)

    return {'legend_handles': legend_handles, 'legend_labels': labels, 'cluster_results': cr, 'city_results': g_city,
            'city_layer': report_cities, 'markers': markers, 'bounds': bounds}

def layer_selection_criteria(report_meta):


    layers = {}

    if 'boundary_name' in report_meta:

        if report_meta['boundary'] == 'canton':

            the_canton_layer = canton_layer[canton_layer.NAME == report_meta['boundary_name']]

            layers.update({'canton': the_canton_layer})

            # get the municipal boundaries of the canton
            # dbckey = canton_layer[['NAME', 'KANTONSNUM']].set_index('NAME')
            # dbckey = dbckey.drop_duplicates()
            thiscanton_cities = dbckey.loc[report_meta['boundary_name'], 'KANTONSNUM']
            # db = gpd.read_file('data/ignorethis/shapes/municipalities.shp').to_crs(epsg=4326)
            cities = municipal_layer[municipal_layer.KANTONSNUM == thiscanton_cities]
            layers.update({'city': cities})

            # get the rivers layer
            # riversd = gpd.read_file('data/ignorethis/shapes/rivers.shp').to_crs(epsg=4326)

            rivers = rivers_layer.clip(canton_layer, keep_geom_type=True)  # cx[minx:maxx, miny:maxy]

            layers.update({'river': rivers})

            # lakesd = gpd.read_file('data/ignorethis/shapes/lakes.shp').to_crs(epsg=4326)
            lakes = lakes_layer.clip(canton_layer, keep_geom_type=True)  # [minx:maxx, miny:maxy]
            layers.update({'lake': lakes})

            return layers

        elif report_meta['boundary'] == 'city':
            # citiesd = gpd.read_file('data/ignorethis/shapes/municipalities.shp').to_crs(epsg=4326)

            cities = municipal_layer[municipal_layer['NAME'] == report_meta['boundary_name']]
            layers.update({'city': cities})

            # get the rivers layer
            # riversd = gpd.read_file('data/ignorethis/shapes/rivers.shp').to_crs(epsg=4326)

            # Filter the background layer to cover the bounding box
            rivers = rivers_layer.clip(cities, keep_geom_type=True)  # cx[minx:maxx, miny:maxy]
            layers.update({'river': rivers})

            # lakesd = gpd.read_file('data/ignorethis/shapes/lakes.shp').to_crs(epsg=4326)
            # lakes = lakes.to_crs(epsg=4326)
            layers.update({'lake': lakes_layer})


            return layers

    elif 'feature_name' in report_meta:

        layers.update({'canton': canton_layer})

        # = gpd.recitiesdad_file('data/ignorethis/shapes/municipalities.shp').to_crs(epsg=4326)
        layers.update({'city': municipal_layer})

        # lakesd = gpd.read_file('data/ignorethis/shapes/lakes.shp').to_crs(epsg=4326)


        # riversd = gpd.read_file('data/ignorethis/shapes/rivers.shp').to_crs(epsg=4326)

        layers.update({'river': rivers_layer})
        layers.update({'lake': lakes_layer})

        return layers

    else:
        # canton_shape_layer = gpd.read_file('data/ignorethis/shapes/kantons.shp').to_crs(epsg=4326)

        layers.update({'canton': canton_layer})

        # citiesd = gpd.read_file('data/ignorethis/shapes/municipalities.shp').to_crs(epsg=4326)
        layers.update({'city': municipal_layer})

        # lakesd = gpd.read_file('data/ignorethis/shapes/lakes.shp').to_crs(epsg=4326)
        # lakes = lakesd.clip(lakes_layer,  keep_geom_type=True)

        # riversd = gpd.read_file('data/ignorethis/shapes/rivers.shp').to_crs(epsg=4326)

       #  rivers = riversd.clip(canton_shape_layer,  keep_geom_type=True) # cx[minx:maxx, miny:maxy]
        layers.update({'river': rivers_layer})
        layers.update({'lake': lakes_layer})

        return layers

def map_markers(df, lat_lon: pd.DataFrame = lat_lon):
    """Map the markers"""

    # collect information for popup display at each location
    nsamples = df.groupby('location', observed=True)['sample_id'].nunique()
    qty_location = df.groupby('location', observed=True)['quantity'].sum()
    rate_location = df.groupby('location', observed=True)['pcs/m'].mean().round(2)
    last_sample = df.groupby('location', observed=True)['date'].max()

    # merge the pop-up information with the gps coordinates
    df = pd.concat([nsamples, qty_location, rate_location, last_sample], axis=1)
    df = df.merge(lat_lon, left_index=True, right_index=True)
    df['location'] = df.index

    # get the bounds of these points in a dict
    max_lat, min_lat = df['latitude'].max(), df['latitude'].min()
    max_lon, min_lon = df['longitude'].max(), df['longitude'].min()
    td = df.to_dict(orient='records')

    # make the points and geo dataframe
    geometry = [Point(loc['longitude'], loc['latitude']) for loc in td]
    geo_frame = gpd.GeoDataFrame(td, geometry=geometry, crs="EPSG:4326")

    return geo_frame, [(min_lon, min_lat), (max_lon, max_lat)]

def select_x_and_y(df_target: pd.DataFrame, features: pd.DataFrame) -> pd.DataFrame:
    """
    Select the feature columns and the target column from the DataFrame.

    This function merges the target DataFrame with the features DataFrame based on the location label.

    Parameters
    ----------
    df_target : pd.DataFrame
        The DataFrame containing the target data.
    features : pd.DataFrame
        The DataFrame containing the feature data.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the merged target and feature data.

    Raises
    ------
    ValueError
        If the input DataFrames are empty or if the merge operation fails.
    """
    if df_target.empty or features.empty:
        raise ValueError("Input DataFrames cannot be empty.")

    df = df_target.merge(features, left_on=location_label, right_on=location_label, how='left')
    if df.empty:
        raise ValueError("Merge operation failed. Please check the input DataFrames.")

    return df

def categorize_features(df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame:
    """
    Categorize the feature columns in the DataFrame.

    This function scales the 'streets' column and categorizes the specified feature columns into bins.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the feature data.
    feature_columns : list of str, optional
        The list of feature columns to categorize. Default is `feature_variables`.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the categorized feature columns.

    Raises
    ------
    ValueError
        If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
    """
    if df.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    bins = session_config.bins
    labels = session_config.bin_labels
    scaler = MinMaxScaler()

    if 'streets' not in df.columns:
        raise ValueError("'streets' column not found in the DataFrame.")

    df['streets'] = scaler.fit_transform(df[['streets']])

    for column in feature_columns:
        if column not in df.columns:
            raise ValueError(f"Feature column '{column}' not found in the DataFrame.")
        df[column] = pd.cut(df[column], bins=bins, labels=labels)

    return df

class LandUseReport:
    """
    A class to generate a report from survey data with respect to land use features.

    The `LandUseReport` class is a container for the data and methods used to generate a report from a survey data set.
    The report summarizes the data in the survey with respect to the land use features of the survey locations.

    Attributes
    ----------
    target : pd.DataFrame
        The DataFrame containing the target data.
    features : pd.DataFrame
        The DataFrame containing the feature data.
    feature_variables : list of str
        A list of feature variables extracted from the features DataFrame.
    intersects : pd.DataFrame or None
        A DataFrame containing the intersects data, if available.
    df_cont : pd.DataFrame
        A DataFrame containing the continuous data after merging the target and features DataFrames.
    df_cat : pd.DataFrame
        A DataFrame containing the categorized feature columns.

    Methods
    -------
    merge_land_use_to_survey_data()
        Merge the land use data with the survey data.
    categorize_columns(df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame
        Categorize the feature columns in the DataFrame.
    n_samples_per_feature(df: pd.DataFrame = None, features: list[str] = None) -> pd.DataFrame
        Calculate the number of samples per feature.
    n_pieces_per_feature() -> pd.DataFrame
        Calculate the number of pieces per feature.
    locations_per_feature() -> pd.DataFrame
        Calculate the number of unique locations per feature.
    rate_per_feature(df: pd.DataFrame = None) -> pd.DataFrame
        Calculate the average rate per feature.
    correlation_matrix() -> pd.DataFrame
        Calculate the correlation matrix for the feature variables.
    """

    def __init__(self, df_target, features):
        self.target = df_target
        self.features = features
        self.feature_variables = list(self.features.keys())
        self.intersects = None
        self.df_cont = None
        self.merge_land_use_to_survey_data()
        self.df_cat = self.categorize_columns(self.df_cont.copy())

    def merge_land_use_to_survey_data(self) -> None:
        """
        Merge the land use data with the survey data.

        This method merges the target DataFrame with the features DataFrame to create a continuous DataFrame and an intersects DataFrame.

        Raises
        ------
        ValueError
            If the merge operation fails or if the resulting DataFrame is empty.
        """
        lu = select_x_and_y(self.target, self.features)
        if len(lu) == 2:
            self.df_cont, self.intersects = lu
        else:
            self.df_cont = lu

        if self.df_cont.empty:
            raise ValueError("Merge operation failed. The resulting DataFrame is empty.")
        
    def categorize_columns(self, df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame:
        """
        Categorize the feature columns in the DataFrame.

        This method scales the 'streets' column and categorizes the specified feature columns into bins.

        Parameters
        ----------
        df : pd.DataFrame
            The DataFrame containing the feature data.
        feature_columns : list of str, optional
            The list of feature columns to categorize. Default is `feature_variables`.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the categorized feature columns.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        return categorize_features(df, feature_columns=feature_columns)

    def n_samples_per_feature(self, df: pd.DataFrame = None, features: list[str] = None) -> pd.DataFrame:
        """
        Calculate the number of samples per feature.

        This method calculates the number of samples for each specified feature in the DataFrame.

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the feature data. If not provided, the method uses `self.df_cat`.
        features : list of str, optional
            The list of features to calculate the number of samples for. If not provided, the method uses `session_config.feature_variables`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of samples per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()

        if features is None:
            features = session_config.feature_variables

        if df.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: df[feature].value_counts() for feature in features}

        df_concat = pd.concat(df_feature, axis=1)

        return df_concat.fillna(0).astype('int')

    def n_pieces_per_feature(self) -> pd.DataFrame:
        """
        Calculate the number of pieces per feature.

        This method calculates the sum of pieces for each specified feature in the DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of pieces per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cat.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[Q].sum() for feature in self.feature_variables}
        df_concat = pd.concat(df_feature, axis=1)

        return df_concat.fillna(0).astype('int')

    def locations_per_feature(self) -> pd.DataFrame:
        """
        Calculate the number of unique locations per feature.

        This method calculates the number of unique locations for each specified feature in the DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of unique locations per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cat.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[location_label].nunique() for feature in feature_variables}
        df_concat = pd.concat(df_feature, axis=1)

        return df_concat.fillna(0).astype('int')

    def rate_per_feature(self, df: pd.DataFrame = None) -> pd.DataFrame:
        """
        Calculate the average rate per feature.

        This method calculates the mean rate of the target variable for each category in the specified features.

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the feature data. If not provided, the method uses `self.df_cat`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the average rates per feature category.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()

        if df.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        avg_matrix = pd.DataFrame(index=feature_variables, columns=session_config.bin_labels)

        for column in feature_variables:
            for category in session_config.bin_labels:
                filtered = df[df[column] == category]
                avg_matrix.at[column, category] = filtered[Y].mean() if not filtered.empty else 0

        return avg_matrix.round(2).T
    

    def correlation_matrix(self) -> pd.DataFrame:
        """
        Calculate the correlation matrix for the feature variables.

        This method calculates the correlation matrix for the feature variables in the continuous DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the correlation matrix of the feature variables.

        Raises
        ------
        ValueError
            If the continuous DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cont.empty:
            raise ValueError("Continuous DataFrame cannot be empty.")

        missing_columns = [col for col in feature_variables if col not in self.df_cont.columns]
        if missing_columns:
            raise ValueError(f"Feature columns {missing_columns} not found in the DataFrame.")

        return self.df_cont[feature_variables].corr()

    



