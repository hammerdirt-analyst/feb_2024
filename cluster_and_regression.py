from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.inspection import permutation_importance
import pandas as pd


# import statsmodels.api as sm
# mod = sm.OLS(Y,X)
# fii = mod.fit()
# p_values = fii.summary2().tables[1]['P>|t|']

# def scale_streets(data):
#     scaler = MinMaxScaler()
#     data['streets'] = scaler.fit_transform(data[['streets']])
#     return data

# def filter_features(data, threshold=0.9):
#     filtered_columns = [col for col in data.columns if (data[col] > 0).mean() >= threshold or col == 'streets']
#     return data[filtered_columns]

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

def random_forest_regression_original(data, target='pcs/m'):
    X = data.drop(columns=[target])
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    return model, r2, mse

def permutation_feature_importance(model, X_test, y_test):
    results = permutation_importance(model, X_test, y_test, n_repeats=30, random_state=42)
    importance_df = pd.DataFrame({'feature': X_test.columns, 'importance': results.importances_mean})
    return importance_df.sort_values(by='importance', ascending=False)

def linear_regression_coefficients(data, target='pcs/m', exclude: [] = None):
    data.reset_index(inplace=True, drop=True)
    if exclude is None:
        X = data[[x for x in data.columns if x not in ['pcs/m', 'clusters']]].copy()
    else:
        X = data[[x for x in data.columns if x not in ['pcs/m', 'clusters', *exclude]]].copy()
    y = data[target]
    model = LinearRegression()
    model.fit(X, y)
    
    coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_})
    return coefficients, model

def analyze_streets_impact(data, interaction_data, target='pcs/m'):
    original_model, original_r2, original_mse = random_forest_regression_original(data, target)
    interaction_model, interaction_r2, interaction_mse = random_forest_regression_original(interaction_data, target)
    
    original_importance = permutation_feature_importance(original_model, data.drop(columns=[target]), data[target])
    interaction_importance = permutation_feature_importance(interaction_model, interaction_data.drop(columns=[target]), interaction_data[target])
    
    original_coefficients = linear_regression_coefficients(data, target)
    interaction_coefficients = linear_regression_coefficients(interaction_data, target)
    
    return {
        'original_model': original_model,
        'interaction_model': interaction_model,
        'original_r2': original_r2,
        'interaction_r2': interaction_r2,
        'original_mse': original_mse,
        'interaction_mse': interaction_mse,
        'original_importance': original_importance,
        'interaction_importance': interaction_importance,
        'original_coefficients': original_coefficients,
        'interaction_coefficients': interaction_coefficients
    }

# example code

# Step 1: Scale the 'streets' variable between 0 and 1
# data = scale_streets(data)

# Step 2: Identify features that are greater than 0 in at least 90% of samples
# filtered_data = filter_features(data)

# Step 3: Create interaction terms with 'streets' and include 'pcs/m' in the interaction data
# interaction_data = create_interaction_terms(filtered_data)

# Step 4 & 5: Perform the analysis
#results = analyze_streets_impact(filtered_data, interaction_data)