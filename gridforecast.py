"""
gridforecast.py
hammerdirt 2024
Author: Roger Erismann

NOTE: This module is a work in progress.

Implementation of a grid forecast using a Dirichlet-Multinomial conjugate. The module provides functions to
make reports and forecasts based on the likelihood and prior data. The module provides functions to
compute the posterior distribution, sample from the posterior, compute percentiles, compute the highest density
interval, compute the expected average, and compute the probability of x. The module also provides functions to
compute the descriptive statistics of the forecasted samples.

A Bayesian method is used because of how the data is collected. Each sample is an observation made by an individual that
can make mistakes, has an unknown amount of experience or physical limitations that we may not be aware of. Furthermore,
objects are difficult to identify due to erosion and decomposition. All of these factors contribute to the uncertainty
present in the data.

The land-use is an essential factor in the forecast. The land-use is used to weight the prior data. Comparing strictly on
a temporal scale assumes that the same types of locations was sampled from one epoch to another. This is not the case.
We note that comparing results on land use values is more appropriate than limiting the comparison to temporal or spatial
values. In simple terms, we are comparing apples to apples and not apples to oranges.
"""
import pandas as pd
import numpy as np
import session_config
from reports import construct_report_label, make_report_objects

def append_to_markdown(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

def calculate_proportions(data, columns):
    return data.groupby(columns, observed=True).size().reset_index(name='count')

def manhattan_distance(row, target):
    return sum(abs(row[col] - target[col]) for col in ['buildings', 'forest', 'undefined'])

def calculate_similarity(row, proportions_A):
    # Calculate similarity of a row to all combinations in proportions_A
    similarities = []
    for _, target in proportions_A.iterrows():
        distance = manhattan_distance(row, target)
        # Invert distance to get similarity; avoid division by zero
        similarity = 1 / (1 + distance)
        weighted_similarity = similarity * target['proportion']
        similarities.append(weighted_similarity)
    return sum(similarities)


in_boundary_description = (
    "This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) "
    "not including samples from the likelihood and limited to the end date. "
    "The samples are selected based on the similarity of the land use features: buildings, forest and undefined. "
    "At least two of these variables are present at all sample locations. The similarity is calculated using the Manhatten distance between the "
    "likelihood and the proposed prior samples. In summary this prior assumes that litter density in the selected region is more a question of "
    "geographic location than land-use and that the best predictor of future results is the previous results within the same area."

)

out_boundary_description = (
    "This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) "
    "not including samples from the likelihood and limited to the end date. "
    "The samples are selected based on the similarity of the land use features: buildings, forest and undefined. "
    "At least two of these variables are present at all sample locations. The similarity is calculated using the Manhattan distance between the "
    "likelihood samples and the proposed prior samples. In summary this prior assumes that litter density in the selected region is comparable to locations "
    "outside of the boundary and that trends or correlations of litter density are mostly a matter of land-use and less a question of geographic location."
)


prior_description = (
    "These are random samples from all of the data, not including the likelihood and limited to the requested end date. "
    "The samples are selected based on the similarity of the land use features: buildings, forest and undefined. "
    "At least two of these variables are present at all sample locations. The similarity is calculated using the Manhattan distance between the "
    "likelihood samples and the proposed prior samples. In summary this prior assumes that land-use is the best predictor indifferent of "
    "the geographic location (in or out of the boundary). "
)


def sample_like_subset_general(data, subset_A, label, similarity_columns: [] = ['buildings', 'forest', 'undefined']):
    # Step 1: Calculate proportions in A
    proportions_A = calculate_proportions(subset_A, similarity_columns)
    proportions_A['proportion'] = proportions_A['count'] / proportions_A['count'].sum()

    # Step 2: Calculate similarity of each row in data to combinations in A
    data['similarity'] = data.apply(lambda row: calculate_similarity(row, proportions_A), axis=1)

    n_samples = len(subset_A)  # Number of samples can be adjusted

    prompt_description = {
        'in_boundary': in_boundary_description,
        'out_boundary': out_boundary_description,
        'prior': prior_description}

    similarity_prompt = "They have been selected based on the similarity of the buildings, forest and undefined feature variables."

    # check the number of available samples
    # based on the similarity score
    # work backward from a similarity of .99 to
    for i in np.arange(.3, 1, .01)[::-1]:
        if len(data[data.similarity >= i]) > n_samples:
            data = data[data.similarity >= i]
            sampled_data = data.sample(n=n_samples, weights=data['similarity'], replace=False)
            sampled_data.reset_index(inplace=True, drop=True)
            prompt = f"{prompt_description[label]}\n{similarity_prompt} The similarity threshold is {i}"
            return {'dataframe': sampled_data, 'prompt': prompt}

    if len(data) >= n_samples:
        prompt = f"{prompt_description[label]} The similarity scores were less than .3,. The selection was random similarity was not considered."
        sampled_data = data.sample(n=n_samples, weights=data['similarity'], replace=False)
        return {'dataframe': sampled_data, 'prompt': prompt}

    if len(data) < n_samples:
        prompt = f"{prompt_description[label]} There are fewer samples in the prior than the likelihood. All prior samples were used"
        return {'dataframe': data, 'prompt': prompt}

def collect_prior_data(data, meta_data, likelihood_locations):
    prior_filters = list(meta_data.keys())

    if 'feature_type' in prior_filters:
        feature_type_mask = data.feature_type == meta_data['feature_type']
        data = data[feature_type_mask]

    if 'codes' in prior_filters:
        code_mask = data.code.isin(meta_data['codes'])
        data = data[code_mask]

    return data[~data.location.isin(likelihood_locations)]



grid_approximation_def = (
    "### Grid Approximation method:\n\n"
    "1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.\n\n"
    "2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.\n\n"
    "3. **Normalization**:\n"
    "   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.\n"
    "   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.\n\n"
    "4. **Summation or Integration**: Use the normalized values to compute estimates, such as expectations, by summing over the grid points, potentially weighted by the grid interval size.\n\n"
    "#### Why normalize::\n\n"
    "- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.\n"
    "- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.\n\n"
    "The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.\n"
)



class GridForecast:

    def __init__(self, likelihood, report_meta, data):
        self.likelihood = likelihood
        self.likelihood_locations = likelihood.location.unique()
        self.report_meta = report_meta
        self.info_columns = ['canton', 'city', 'feature_name']
        self.priors = self.evaluate_prior_data(data)
        self.features = ['buildings', 'forest', 'undefined']
        self.valid_priors = []

    def collect_prior_data(self, data):
        prior_filters = list(self.report_meta.keys())

        if 'feature_type' in prior_filters:
            feature_type_mask = data.feature_type == self.report_meta['feature_type']
            data = data[feature_type_mask]

        if 'codes' in prior_filters:
            code_mask = data.code.isin(self.report_meta['codes'])
            data = data[code_mask]

        return data[~data.location.isin(self.likelihood_locations)]


    def evaluate_prior_data(self,data):
        # eliminate the likelihood samples
        prior_data = self.collect_prior_data(data)

        # if there is no data left return empty dataframes
        if len(prior_data) == 0:
            print('prior is len o')
            return {'prior': pd.DataFrame(), 'in_boundary': pd.DataFrame(), 'out_boundary': pd.DataFrame()}
        try:
            # make report objects from the prior data
            _, prior_landuse = make_report_objects(prior_data, info_columns=self.info_columns)
            prior_landuse = prior_landuse.df_cont.reset_index(drop=True)
        except Exception as e:
            # if there is an error return empty dataframes
            print('prior caused exception')
            return {'prior': pd.DataFrame(), 'in_boundary': pd.DataFrame(), 'out_boundary': pd.DataFrame()}

        # check the boundaries and make a set of prior data from within the boundaries
        # if possible and create a prior from data outside the boundaries
        if 'boundary' in self.report_meta.keys():
            if self.report_meta['boundary'] is not None:
                in_boundary_mask = (prior_landuse[self.report_meta['boundary']] == self.report_meta['boundary_name'])
                in_boundary = prior_landuse[in_boundary_mask].copy()
                out_boundary_mask = (prior_landuse[self.report_meta['boundary']] != self.report_meta['boundary_name'])
                out_boundary = prior_landuse[out_boundary_mask].copy()

                if 'feature_name' in self.report_meta.keys():
                    if self.report_meta['feature_name'] is not None:
                        name_mask = (in_boundary['feature_name'] == self.report_meta['feature_name'])
                        feature_in_bounds = in_boundary[name_mask].copy()

                        return {'prior': prior_landuse, 'in_boundary': feature_in_bounds, 'out_boundary': out_boundary}

                    else:
                        return {'prior': prior_landuse, 'in_boundary': in_boundary, 'out_boundary': out_boundary}
                else:
                    return {'prior': prior_landuse, 'in_boundary': in_boundary, 'out_boundary': out_boundary}
            else:
                pass

        if 'feature_name' in self.report_meta.keys():

            if self.report_meta['feature_name'] is not None:
                in_boundary_mask = (prior_landuse['feature_name'] == self.report_meta['feature_name'])
                in_boundary = prior_landuse[in_boundary_mask].copy()
                out_boundary_mask = (prior_landuse['feature_name'] != self.report_meta['feature_name'])
                out_boundary = prior_landuse[out_boundary_mask].copy()
                return {'prior': prior_landuse, 'in_boundary': in_boundary, 'out_boundary': out_boundary}
            else:
                pass

        return {'prior': prior_landuse, 'in_boundary': pd.DataFrame(), 'out_boundary': pd.DataFrame()}

    def inference_tables(self, data):
        valid_priors = {}
        nvalid_priors = 0
        nsamples = len(self.likelihood)
        self.priors = self.evaluate_prior_data(data)


        for label in self.priors.keys():

            if len(self.priors[label]) > 0:

                nvalid_priors += 1
                self.valid_priors.append(label)
                setattr(self, label, self.priors[label])
                valid_priors.update({label: self.priors[label]})

        if nvalid_priors == 0:
            section_head = f"### Prior grid approximation"
            poster_limits = f"{section_head}\nNo valid priors were found."

            return {'prior': {'dataframe': pd.DataFrame(), 'prompt': poster_limits}}

        predictions = {}

        for label, aprior in valid_priors.items():
            a_prior = sample_like_subset_general(aprior, self.likelihood, label)

            grid_max = max(np.percentile(self.likelihood['pcs/m'].values, 99, axis=0),
                           np.percentile(a_prior['dataframe']['pcs/m'].values, 99, axis=0))
            grid_limit = round(grid_max, 2) + .03

            grid = np.arange(0, grid_limit, 0.01)
            lh_rates = np.array([(self.likelihood['pcs/m'] > x).sum() for x in grid])
            lh_rates = lh_rates / nsamples

            pr_rates = np.array([(a_prior['dataframe']['pcs/m'] > x).sum() for x in grid])
            pr_rates = pr_rates / len(a_prior)

            posterior = lh_rates * pr_rates
            normalized = posterior / sum(posterior)

            rng = np.random.default_rng()
            posterior_multinomial = rng.multinomial(100, normalized, size=1)
            posterior_samples = np.repeat(grid, posterior_multinomial[0])
            posterior_samples = pd.DataFrame(posterior_samples, columns=['pcs/m'])
            section_head = f"### {' '.join(label.split('_')).capitalize()} grid approximation\n{a_prior['prompt']}"
            poster_limits = f"{section_head}\nThe expected posterior distribution is a grid approximation from 0 to {grid_limit} every 0.01."
            prompt = f"{poster_limits}\n\n{posterior_samples[['pcs/m']].describe().to_markdown()}"

            predictions.update({label: {'dataframe': posterior_samples, 'prompt': prompt}})

        return predictions

    def sampling_stratiifcation(self, label):
        if hasattr(self, label):
            df = getattr(self, label).copy()  # Dynamically access the attribute using the label string

            df_feature = {feature: df[feature].value_counts() for feature in self.features}

            df = pd.concat(df_feature, axis=1)

            df = df.fillna(0).astype('int')
            df = df/len(df)
            return df
        else:
            return pd.DataFrame()



    def rate_per_feature(self, label):
        if hasattr(self, label):
            df = getattr(self, label).copy()  # Dynamically access the attribute using the label string
            avg_matrix = pd.DataFrame(index=self.features, columns=session_config.bin_labels)

            # Calculate the mean for each category in each identified column
            for column in self.features:
                for category in session_config.bin_labels:
                    # Filter df by category and calculate mean for the target variable, only if it's relevant
                    filtered = df[df[column] == category]
                    avg_matrix.at[column, category] = filtered['pcs/m'].mean() if not filtered.empty else 0

            return avg_matrix.round(2).T
        else:
            return pd.DataFrame()

    def report_draft(self, data, file_name: str = None):
        report_label = construct_report_label(self.report_meta)
        current_forecast = self.inference_tables(data)

        if file_name is not None:
            # here we want to append to a specific document or create a new one
            try:
                with open(file_name, 'a') as file:
                    title = f"\n## Grid forecast {report_label}\n\n"
                    title_and_def = f"{title}{grid_approximation_def}\n\n"
                    append_to_markdown(file_name, title_and_def)
                    for forecast_type, forecast in current_forecast.items():
                        append_to_markdown(file_name, forecast['prompt'])
            except FileNotFoundError:
                title = f"\n# Grid forecast {report_label}\n\n"
                title_and_def = f"{title}{grid_approximation_def}\n\n"
                with open(file_name, 'w') as file:
                    file.write(file_name, title_and_def)

                for forecast_type, forecast in current_forecast.items():
                    append_to_markdown(file_name, forecast['prompt'])

        else:
            # this method is called from another report class and
            # it appends the block of text to the report
            report_string = f"\n## Grid forecast {report_label}\n\n{grid_approximation_def}\n\n"
            for forecast_type, forecast in current_forecast.items():
                report_string += forecast['prompt'] + "\n\n"
            return report_string



