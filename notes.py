import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Construct the inference table using the beta-binomial conjugate model
def inference_table_beta_binomial(grid, prior, likelihood, n_prior, n_likelihood):
    inference_table = []

    for grid_point in grid:
        # Step 2: Get prior and likelihood successes for the grid point
        prior_successes = (prior >= grid_point).sum()  # successes in prior (exceeding grid point)
        likelihood_successes = (likelihood >= grid_point).sum()  # successes in likelihood
        
        # Step 3: Compute prior and likelihood failures
        prior_failures = n_prior - prior_successes
        likelihood_failures = n_likelihood - likelihood_successes
        
        # Step 4: Update the beta posterior parameters
        alpha_posterior = prior_successes + likelihood_successes  # Posterior alpha (successes)
        beta_posterior = prior_failures + likelihood_failures  # Posterior beta (failures)
        
        # Step 5: Compute the posterior mean (expected value of the beta distribution)
        posterior_mean = alpha_posterior / (alpha_posterior + beta_posterior)
        
        # Store results in the inference table
        inference_table.append({
            'grid': grid_point,
            'prior': prior_successes,
            'likelihood': likelihood_successes,
            'posterior': posterior_mean
        })
    
    return pd.DataFrame(inference_table)

# Step 2: Generate the inference table
def generate_inference_table_and_normalize(prior, likelihood):
    # Define the grid based on the new test data
    grid_max = max(np.percentile(likelihood, 99), np.percentile(prior, 99))
    grid_limit = round(grid_max, 2) + 0.03
    grid = np.arange(0, grid_limit, 0.01)
    
    # Number of prior and likelihood samples
    n_prior = len(prior)
    n_likelihood = len(likelihood)
    
    # Generate the inference table using the beta-binomial conjugate model
    inference_table = inference_table_beta_binomial(grid, prior, likelihood, n_prior, n_likelihood)
    
    return inference_table, grid

# Step 3: Function to sample from the posterior based on the normalized posterior column
def sample_posterior_mle(inference_table, n_samples=100):
    # Use the posterior mean as weights to sample from the grid
    grid_values = inference_table['grid'].values
    posterior_probs = inference_table['posterior'].values
    posterior_probs = posterior_probs / posterior_probs.sum()  # Normalize the posterior probabilities
    sampled_values = np.random.choice(grid_values, size=n_samples, p=posterior_probs)
    return sampled_values

# Step 4: Generate PDFs and CDFs
def generate_cdf_from_inference_table(inference_table, column_name):
    return np.cumsum(inference_table[column_name]) / np.sum(inference_table[column_name])

# Step 5: Test prior and likelihood data
test_prior_new = np.array([0.25, 0.36, 0.37, 0.43, 0.47, 0.56, 1.13, 1.41, 1.55, 1.63, 1.76, 2.0, 2.23, 2.4, 2.82, 2.96, 3.0, 3.02, 3.06, 3.11, 3.3, 3.34, 3.62, 4.0, 4.35, 4.76, 5.9, 9.41, 35.34])
test_likelihood_new = np.array([0.4, 0.43, 0.64, 0.84, 0.91, 1.15, 1.22, 1.4, 1.41, 1.42, 1.45, 1.45, 1.83, 2.36, 2.52, 2.69, 2.88, 3.14, 3.4, 3.4, 3.48, 4.57, 4.82, 4.97, 5.06, 5.42, 5.46, 5.9, 6.0, 6.34, 6.71, 6.75, 7.5, 8.02, 8.21, 9.33, 9.68, 10.47, 14.8])

# Generate the inference table
inference_table_new, grid_new = generate_inference_table_and_normalize(test_prior_new, test_likelihood_new)

# Generate posterior samples
posterior_samples_new = sample_posterior_mle(inference_table_new, n_samples=1000)

# Plot CDFs
plt.figure(figsize=(10, 6))
sns.ecdfplot(test_prior_new, label='prior CDF', color='green')
sns.ecdfplot(test_likelihood_new, label='likelihood CDF', color='red')
posterior_cdf = generate_cdf_from_inference_table(inference_table_new, 'posterior')
plt.plot(inference_table_new['grid'], posterior_cdf, label='posterior CDF', color='blue')
plt.title('CDF Comparison: Prior, Likelihood, and Posterior')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()

# Plot PDFs
plt.figure(figsize=(10, 6))
plt.plot(inference_table_new['grid'], inference_table_new['prior'] / len(test_prior_new), label='prior PDF', color='green')
plt.plot(inference_table_new['grid'], inference_table_new['likelihood'] / len(test_likelihood_new), label='likelihood PDF', color='red')
plt.plot(inference_table_new['grid'], inference_table_new['posterior'], label='posterior PDF', color='blue')
plt.title('PDF Comparison: Prior, Likelihood, and Posterior')
plt.xlabel('Grid Values')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# Show the first 10 rows of the inference table
inference_table_new.head(10)

