
## Grid forecast Vaud l Vaud 2020-04-01 2021-05-01

 
### Grid Approximation in Statistics (with Normalization):

1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.

2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.

3. **Normalization**:
   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.
   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.

4. **Summation or Integration**: Use the normalized values to compute estimates, such as expectations, by summing over the grid points, potentially weighted by the grid interval size.

### Why Normalization is Important:

- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.
- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.

The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.


### Prior grid approximation
These are random samples from all of the data, not including the likelihood and limited to the requested end date.
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7700000000000005
The expected posterior distribution is a grid approximation from 0 to 13.049999999999999 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.7261   |
| std   |   0.581018 |
| min   |   0.02     |
| 25%   |   0.2675   |
| 50%   |   0.57     |
| 75%   |   1.0725   |
| max   |   2.31     |### In boundary grid approximation
These are random samples from within the requested boundary, not including samples from the likelihood and limited to the end date.
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.4200000000000001
The expected posterior distribution is a grid approximation from 0 to 17.07 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.78     |
| std   |   0.965382 |
| min   |   0        |
| 25%   |   0.2275   |
| 50%   |   0.565    |
| 75%   |   1.1      |
| max   |   7.36     |### Out boundary grid approximation
These are random samples from out side of the requested boundary, limited to the requested end date.
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 11.469999999999999 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.8125   |
| std   |   0.852876 |
| min   |   0        |
| 25%   |   0.205    |
| 50%   |   0.575    |
| 75%   |   1.0875   |
| max   |   4.31     |