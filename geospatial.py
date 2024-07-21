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

1. merge_land_use_to_survey_data: merges the land use data to the survey data
2. categorize_columns: categorizes the feature columns in the DataFrame
3. n_samples_per_feature: returns the number of samples per feature
4. n_pieces_per_feature: returns the number of pieces per feature
5. locations_per_feature: returns the number of locations per feature
6. rate_per_feature: returns the rate per feature
7. combine_features: combines the features in the DataFrame
8. correlation_matrix: returns the correlation matrix of the features
9. assign_combination_method: assigns the combination method to correlated pairs
10. correlated_pairs: returns the correlated pairs
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import session_config
from session_config import feature_variables
from session_config import location_label, Y, Q

pd.set_option('future.no_silent_downcasting', True)

feature_data = session_config.feature_data
landuse = pd.read_csv(feature_data['land_use_data'])
landcover = pd.read_csv(feature_data['land_cover_data'])
streets = pd.read_csv(feature_data['street_data'])
river_intersects = pd.read_csv(feature_data['intersection_attributes'])

words_land_use_profile = {
    'en': 'Percent of land attributed v/s % of samples',
    'fr': 'Pourcentage d\'occupation du sol v/s % d\'échantillons',
    'de': 'Prozent des Landes zugeschrieben v/s % der Proben'
}

words_land_use_litter_rates = {
    'en': 'Percent of land attributed v/s trash per meter of shoreline',
    'fr': 'Pourcentage d\'occupation du sol v/s déchets par mètre de rivage',
    'de': 'Prozent des Landes zugeschrieben v/s Stück Müll pro Meter Ufer'
}

column_labels_land_use = {
    1: '0 - 20%',
    2: '20 - 40%',
    3: '40 - 60%',
    4: '60 - 80%',
    5: '80 - 100%'
}

def select_x_and_y(df_target, features, x_value: str = 'scale'):
    """Selects the feature columns and the target column from the DataFrame"""

    for label in ['public services', 'streets']:
        df_target[label] = df_target.location.apply(lambda x: features[label].loc[x, x_value])

    for label in ['landcover']:
        df = df_target.merge(features[label], left_on=location_label, right_on=location_label, how='left')
    for label in ['river_intersects']:
        if len(features[label]) == 0:
            df.fillna(0, inplace=True)
            return df.infer_objects(copy=False)
        else:
            df_rivers = df_target.merge(features[label], left_on=location_label, right_on=location_label, how='left')
            df_rivers.fillna(0, inplace=True)
            df.fillna(0, inplace=True)
            return df.infer_objects(copy=False), df_rivers.infer_objects(copy=False)
#
def categorize_features(df, feature_columns=feature_variables):
    """Categorizes the feature columns in the DataFrame"""
    bins = session_config.bins
    labels = session_config.bin_labels
    for column in feature_columns:
        df[column] = pd.cut(df[column], bins=bins, labels=labels)
    return df
#
#
# def category_quantiles(df, feature, category):
#     return df[df[feature] == category].groupby([feature]).agg(agg_groups)


def scale_combined(df, column_to_scale, new_column_name):
    """Scales the combined columns"""
    scaler = MinMaxScaler()
    df[new_column_name] = scaler.fit_transform(df[[column_to_scale]])
    return df


def collect_topo_data(locations: [] = None, labels: {} = None):
    """Collects the topographical data"""

    d_t_c = {
        'public services': landuse.rename(columns={'slug': location_label}),
        'landcover': landcover.rename(columns={'slug': location_label}),
        'streets': streets.rename(columns={'slug': location_label}),
        'river_intersects': river_intersects.rename(columns={'slug': location_label})
    }

    if labels is None:
        if locations is None:
            return d_t_c
        else:
            strts = d_t_c['streets'].copy()
            strts = strts.groupby(location_label)[['length']].sum().reset_index()
            strts = scale_combined(strts, 'length', 'scale')
            strts.set_index(location_label, inplace=True, drop=True)

            ps = d_t_c['public services'].copy()
            ps = ps.groupby(location_label).agg({'scale': 'sum', 'area': 'sum'})

            lc = d_t_c['landcover'].copy()
            lc = lc.pivot(index=location_label, columns='attribute', values='scale').reset_index()
            new_columns = {'Siedl': 'buildings', 'Wald': 'forest', 'Reben': 'vineyards', 'Obstanlage': 'orchards'}
            lc.rename(columns=new_columns, inplace=True)

            d_t_c.update({'streets': strts, 'public services': ps, 'landcover': lc})

            return d_t_c
    else:
        return labels
    
# def combine_landuse_features(data, columns_to_combine: list = None, new_column_name: str = None, method: str = 'sum'):
#     """Combines the columns in the DataFrame
#
#     The columns are put back into m² before combining. Then scaled back.
#     """
#     if method == 'sum':
#         data[new_column_name] = data[columns_to_combine[0]] + data[columns_to_combine[1]]
#         return data
#     if method == 'rate':
#         not_public_services = [x for x in columns_to_combine if 'public services' not in x]
#         data[new_column_name] = (data['public services']*data[not_public_services[0]]).round(3)
#         return data
#
#     else:
#         return "Method not recognized. Please use 'sum' or 'rate' as the method."
#

# def find_correlated_values(df, threshold: float = session_config.corr_threshold):
#     """Finds the correlated values in the DataFrame"""
#
#     labels = df.columns.to_list()
#     correlated_features = []
#     for i in range(len(labels)):
#         for j in range(i+1, len(labels)):
#             if df.at[labels[i], labels[j]] >= .99999:
#                 pass
#             elif df.at[labels[i], labels[j]] <= 0:
#                 pass
#             elif df.at[labels[j], labels[i]] <= 0:
#                 pass
#             elif df.at[labels[i], labels[j]] >= threshold:
#                 correlated_features.append((labels[i], labels[j]))
#
#     return correlated_features


# def make_multi_index(column_labels: dict, group_label: dict, nlabels: int, session_language: str = 'en'):
#     """Creates a multi index for the DataFrame"""
#     ""
#     indexes = [(group_label[session_language], column_labels[x]) for x in range(1, nlabels+1)]
#
#     return pd.MultiIndex.from_tuples(indexes)


class LandUseReport:

    def __init__(self, df_target, features):
        self.target = df_target
        self.features = features
        self.feature_variables = list(self.features.keys())
        self.intersects = None
        self.df_cont = None
        self.merge_land_use_to_survey_data()
        self.df_cat = self.categorize_columns(self.df_cont.copy())

    def merge_land_use_to_survey_data(self):
        lu = select_x_and_y(self.target, self.features)
        if len(lu) == 2:
            self.df_cont, self.intersects = lu
        else:
            self.df_cont = lu
        
    def categorize_columns(self, df, feature_columns=feature_variables):
        return categorize_features(df, feature_columns=feature_columns)

    def n_samples_per_feature(self, df: pd.DataFrame = None, features: [] = None):

        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()
        if features is None:
            features = feature_variables
        df_feature = {feature: df[feature].value_counts() for feature in
                      features}
        df_concat = pd.concat(df_feature, axis=1)
        return df_concat.fillna(0).astype('int')

    def n_pieces_per_feature(self):
        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[Q].sum() for feature in
                      self.feature_variables}
        df_concat = pd.concat(df_feature, axis=1)
        return df_concat.fillna(0).astype('int')

    def locations_per_feature(self):
        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[location_label].nunique() for feature in
                      feature_variables}
        df_concat = pd.concat(df_feature, axis=1)
        return df_concat.fillna(0).astype('int')

    def rate_per_feature(self, df: pd.DataFrame = None):

        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()

        avg_matrix = pd.DataFrame(index=feature_variables, columns=session_config.bin_labels)

        # Calculate the mean for each category in each identified column
        for column in feature_variables:
            for category in session_config.bin_labels:
                # Filter df by category and calculate mean for the target variable, only if it's relevant
                filtered = df[df[column] == category]
                avg_matrix.at[column, category] = filtered[Y].mean() if not filtered.empty else 0

        return avg_matrix.round(2).T
    

    def correlation_matrix(self):

        return self.df_cont[feature_variables].corr()
    



