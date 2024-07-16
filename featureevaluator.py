import pandas as pd
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import session_config
import statsmodels.api as sm

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.inspection import permutation_importance
from sklearn.decomposition import PCA
from scipy.spatial import ConvexHull
from sklearn.exceptions import ConvergenceWarning
import warnings

features_to_scale = session_config.feature_variables[:-1]

def negative_binomial_regression(y_train_corr, y_test_corr, X_test_corr, X_train_corr):
    # negative binomial regression
    poisson_model = sm.GLM(y_train_corr, X_train_corr, family=sm.families.Poisson())
    poisson_results = poisson_model.fit()
    
    # Calculate the Pearson Chi-Square dispersion
    dispersion = poisson_results.pearson_chi2 / poisson_results.df_resid
    
    # Fit a negative binomial model
    model = sm.GLM(y_train_corr, X_train_corr, family=sm.families.NegativeBinomial(alpha=dispersion))
    nb_results = model.fit()
    
    # Predict on the test set
    y_pred_nb = nb_results.predict(X_test_corr)
    
    # Evaluate the model
    mse_nb = mean_squared_error(y_test_corr, y_pred_nb)
    r2_nb = r2_score(y_test_corr, y_pred_nb)
    return mse_nb, r2_nb, nb_results

def filter_features(data, threshold: float = 0.4, interaction_terms: [] = None ):
    filtered_columns = [col for col in features_to_scale if (data[col] > 0).mean() >= threshold or col == 'streets']
    if interaction_terms is None:
        return data[['pcs/m', 'streets', *filtered_columns]]
    else:
        return data[['pcs/m',*interaction_terms, *filtered_columns]]
 
def create_interaction_terms(data, interaction_terms=None, target='pcs/m'):
    if interaction_terms is None:
        interaction_terms = ['streets']
    
    
    interaction_columns = [x for x in data.columns if x != target]
    interaction_data = {}
    for col in interaction_columns:
        if col not in interaction_terms:
            feature_value = data[col].values
            interaction_name = f'{col}'
            for term in interaction_terms:
                feature_value += data[col].values * data[term].values
                interaction_name += f'_inter_{term}'
            interaction_data[interaction_name] = feature_value
    
    interaction_data = pd.DataFrame(interaction_data)
    interaction_data[target] = data[target]  # Add the target variable to the interaction data
    return interaction_data

class FeatureEvaluation:
    def __init__(self, data, feature_vars=None, target_var='pcs/m', regression_models=None):
        self.data = data
        self.feature_vars = feature_vars or ['orchards', 'vineyards', 'buildings', 'forest', 'undefined', 'public services', 'streets']
        self.target_var = target_var
        self.target_scaler = MinMaxScaler()
        self.feature_scaler = MinMaxScaler()
        self.feature_int_scaler = MinMaxScaler()
        self.regression_models = regression_models or {
            'Linear Regression': LinearRegression(),
            'Random Forest Regression': RandomForestRegressor(n_estimators=100, random_state=42)
        }
        self.interactions = self.preprocess_data()

    def unscale_values(self, scaled_values, columns=None):
        """
        Unscale the given values.
        
        :param scaled_values: Array-like, scaled values to unscale
        :param columns: List of column names or indices to unscale. If None, unscale all columns.
        :return: Unscaled values
        """
        if isinstance(scaled_values, pd.DataFrame):
            if columns is None:
                columns = scaled_values.columns
            scaled_array = scaled_values[columns].values
        else:
            scaled_array = np.array(scaled_values)
            if columns is None:
                columns = range(scaled_array.shape[1])
            elif isinstance(columns[0], str):
                raise ValueError("Column names provided but input is not a DataFrame")
            scaled_array = scaled_array[:, columns]

        original_shape = scaled_array.shape

        # Reshape to 2D if necessary
        if scaled_array.ndim == 1:
            scaled_array = scaled_array.reshape(1, -1)

        unscaled_array = self.feature_scaler.inverse_transform(scaled_array)

        # Reshape back to original shape if it was 1D
        if len(original_shape) == 1:
            unscaled_array = unscaled_array.flatten()

        if isinstance(scaled_values, pd.DataFrame):
            unscaled_df = scaled_values.copy()
            unscaled_df[columns] = unscaled_array
            return unscaled_df
        else:
            return unscaled_array
    
    def unscale_target(self, means):
        means = means.values
        means_shape = means.shape
        if means.ndim == 1:
            means = means.reshape(1, -1)
    
        means_unscaled = self.target_scaler.inverse_transform(means)
            
        means_unscaled.reshape(means_shape)
        return means_unscaled[0]

    def preprocess_data(self, remove_features_by_threshold=0.5, scale_these: [] = None):

        
        if scale_these is None:
            dfi = filter_features(self.data.copy(), threshold=remove_features_by_threshold)
            dfi.reset_index(drop=True, inplace=True)
            df = dfi.copy()
            Y = df[['pcs/m']].copy()
            these_features = [x for x in df.columns if x not in ['streets', 'pcs/m']]
            self.feature_vars = these_features
            df[these_features] = self.feature_scaler.fit_transform(df[these_features])
            df['pcs/m'] = self.target_scaler.fit_transform(Y)
            df['streets'] = dfi.streets
                        
            self.data = df # a_df.merge(Y, left_index=True, right_index=True)
            
            new_df = create_interaction_terms(dfi)
            these_features = [x for x in new_df.columns if x not in ['streets', 'pcs/m']]
            

            new_df[these_features] = self.feature_int_scaler.fit_transform(new_df[these_features])
            new_df['pcs/m'] = self.target_scaler.fit_transform(Y)
            new_df['streets'] = dfi.streets
            self.interactions = new_df
            self.interaction_terms = these_features
            return new_df
            
        else:
            return scaler.fit_transform(df[scale_these])
            
            
    
    def find_elbow_point(self, sse):
        n_points = len(sse)
        all_coords = np.vstack((range(n_points), sse)).T
        first_point = all_coords[0]
        last_point = all_coords[-1]

        line_vec = last_point - first_point
        line_vec_norm = line_vec / np.sqrt(np.sum(line_vec**2))

        vec_from_first = all_coords - first_point
        scalar_product = np.sum(vec_from_first * line_vec_norm, axis=1)
        vec_from_first_parallel = np.outer(scalar_product, line_vec_norm)
        vec_to_line = vec_from_first - vec_from_first_parallel

        dist_to_line = np.sqrt(np.sum(vec_to_line**2, axis=1))
        elbow_point = np.argmax(dist_to_line)
        
        return elbow_point + 1

    def determine_optimal_clusters(self, w_interactions: bool = False):

        if w_interactions is True:
            d = self.interactions
        else:
            d = self.data
        
        sse = []
        k_range = range(1, 11)
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(d)
            sse.append(kmeans.inertia_)
        
        optimal_k = self.find_elbow_point(sse)
        return optimal_k
    
    def kmeans_clustering(self, n_clusters, w_interactions: bool = False):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)

        if w_interactions is True:
            d = self.interactions
        else:
            d = self.data
        d['clusters'] = kmeans.fit_predict(d)
        some_features = [x for x in d.columns if x not in ['pcs/m','clusters', 'streets']]

        means = d.groupby(['clusters'])['pcs/m'].mean()
        means_unscaled = self.unscale_target(means)

        counts = d.groupby(['clusters'])['pcs/m'].count()
        
        cluster_summary = d.groupby('clusters').agg({x:'mean' for x in some_features}).reset_index()
        cluster_summary = self.unscale_values(cluster_summary, columns=some_features)
        cluster_summary['pcs/m'] = means_unscaled
        cluster_summary['samples'] = counts.values
        cluster_summary = cluster_summary[['samples', 'pcs/m', *cluster_summary.columns[:-2]]]
               
        return cluster_summary, kmeans, d

    def create_interaction_terms(self, some_data: pd.DataFrame = None):
        if some_data is None:
            d = self.data.copy()
            these_features = self.feature_vars
            
        else:
            d = some_data.copy()
            these_features = [x for x in d.columns if x != 'pcs/m']
        
        
        correlation_matrix = d[these_features].corr()
        self.corr_matrix = correlation_matrix
        interaction_terms = []
        
        for (feature1, feature2) in correlation_matrix[abs(correlation_matrix) > 0.5].stack().index.tolist():
            if feature1 != feature2 and (feature2, feature1) not in interaction_terms:
                interaction_term = feature1 + "_" + feature2
                d[interaction_term] = d[feature1] * d[feature2]
                interaction_terms.append(interaction_term)
        
        return interaction_terms, d
        
    def perform_regression_analysis(self, w_interactions: bool = False):

        if w_interactions is True:
            d = self.interactions
            features = [x for x in self.interaction_terms if x not in ['pcs/m', 'clusters', 'streets']]
        else:
            d = self.data
            features = [x for x in d.columns if x not in ['pcs/m', 'clusters']]       
        
        X = d[features]
        y = d[self.target_var]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        regression_results = []
        best_model = None
        best_r2 = -np.inf
        the_name = None

        # sklearn - linear models        
        for model_name, model in self.regression_models.items():
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
        
        # mse_nb, r2_nb, nb_results = negative_binomial_regression(y_train, y_test, X_test, X_train)
        # regression_results.append({'Model': 'Negative Binomial' , 'R²': r2_nb, 'MSE': mse_nb})
        # if r2_nb > best_r2:
        #             best_r2 = r2_nb
        #             best_model = nb_results
        return regression_results, best_model, the_name, X_test, y_test, X_train, y_train

    

    

    def evaluate_feature_importance(self, best_model, model_name, X_test, y_test, X_train, y_train):

        # the_model = self.regression_models[model]
        

        if model_name != 'Negative Binomial':
            perm_importance = permutation_importance(best_model, X_test, y_test, n_repeats=30, random_state=42)
            perm_importance_df = pd.DataFrame({
                'Feature': X_test.columns,
                'Importance': perm_importance.importances_mean
                }).sort_values(by='Importance', ascending=False)

        try:
        # Attempt to get feature importances
            feature_importances_rf = best_model.feature_importances_
            feature_importance_df = pd.DataFrame({
                'Feature': X_test.columns,
                'Importance': feature_importances_rf
            }).sort_values(by='Importance', ascending=False)
            return feature_importance_df, perm_importance_df
        except AttributeError:
        # If feature importances are not available, try to get parameters
            try:
                params = best_model.coef_
                feature_importances_rf = params
                feature_importance_df = pd.DataFrame({'feature':X_test.columns, 'Coeficient':feature_importances_rf})
                return feature_importance_df, perm_importance_df
            except AttributeError:
                # If neither are available, return an empty DataFrame
                return pd.DataFrame(), perm_importance_df

    def plot_cluster_barchart(self, cluster_summary, title, w_interactions: bool = False):

        if w_interactions is True:
            d = self.interactions.copy()
            features = self.interaction_terms
        else:
            d = self.data.copy()
            features = self.feature_vars
      
        if 'clusters' in d:
            
            cluster_means =d[['clusters' ,*features]].groupby('clusters', as_index=False).mean()
            cluster_means = pd.melt(cluster_means, id_vars=['clusters'], value_vars=[x for x in cluster_means.columns if x != 'clusters'])
        else:
            n = self.determine_optimal_clusters()
            cluster_summary, kmeans, d = self.kmeans_clustering(n, w_interactions=w_interactions)
            cluster_means = d[['clusters' , *features]].copy()
            
            cluster_means =cluster_means.groupby('clusters', as_index=False).mean()
            cluster_means = pd.melt(cluster_means, id_vars=['clusters'], value_vars=cluster_means.columns[0:])
            

        # Custom color palette
        custom_palette = sns.color_palette("gist_rainbow", n_colors=len(cluster_means['variable'].unique()))
        fig, ax = plt.subplots()

        ax = sns.barplot(data=cluster_means, x=cluster_means.clusters, y=cluster_means.value, hue=cluster_means.variable, palette=custom_palette)

        
        ax2 = ax.twinx()  # instantiate a second Axes that shares the same x-axis
        
        ax2.set_ylabel('pcs/m', color='black')  # we already handled the x-label with ax1
        sns.scatterplot(data=cluster_summary, x=cluster_summary.index, y='pcs/m' , color='black', ax=ax2)
        ax2.tick_params(axis='y', labelcolor='black')
        ax.legend(title='Feature', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        ax.set_xlabel('Cluster')
        ax.set_ylabel('Average Proportion')
        ax.set_title('Average Feature Values and pcs/m by Cluster')
        # 
        plt.tight_layout()
        plt.show()

    def plot_feature_importances(self, feature_importance_df, title):
        custom_palette = sns.color_palette("gist_rainbow", n_colors=len(feature_importance_df))
        # feature_importance_df.plot(kind='bar', x='Feature', y='Importance', figsize=(10, 6))
        sns.barplot(data=feature_importance_df, x='Feature', y='Importance', hue='Feature', palette=custom_palette)
        plt.xlabel('Cluster')
        plt.ylabel('Importance')
        plt.title('Feature importance')
        plt.legend(title='Feature', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.show()

