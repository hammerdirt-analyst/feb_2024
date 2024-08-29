
        

<!-- INSTRUCTION_START


1. Analysis of Sampling Stratification and Sampling stratification and trash density tables
   * Objective: Ensure conclusions about the presence or absence of objects are based on a combined interpretation of sampling stratification and litter density data.
   * Data Validation: Confirm that any conclusions about trash density and land use are supported by the presence of samples in the sampling stratification table"
   * Interpretation Guidelines: Analyze how the distribution of land-use features influences the observed trash density. 
   * Draw conclusions only when both stratification and density data are aligned.
   * A zero in the trash density table indicates that no objects were found for that land-use feature and proportion of buffer zone.

2. Reporting Geographic Information

   * Always provide the names of all the cities, cantons, and survey areas included in the report.
   * Always provide the names of all the lakes, rivers, and parks included in the report.

3. Definitions of Urban, Rural Areas, fail-rate

   * Urban Areas: Defined as areas where 60-100% of the buffer zone is dedicated to buildings, and forest occupies 0-20% of the buffer zone. 
   * Rural Areas: Defined as areas where 60-100% of the buffer zone is dedicated to forest, and buildings occupy 0-20% of the buffer zone.
   * Fail Rate: The proportion of samples where at least one of the object categories was found.

INSTRUCTION_END -->

        
# Survey report Vaud canton lake 2020-04-01 2021-05-01


        
## Administrative boundaries Vaud canton lake 2020-04-01 2021-05-01 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a concise narrative of the contents of the following table. In your narrative be sure to include the list of cities,
and the names of the canton and survey areas.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table.

INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      22 |
| city         |      13 |
| canton       |       1 |
| survey areas |       2 |

The following is the names of the cities, cantons, and survey areas.

__City:__ La tour-de-peilz, Préverenges, Yverdon-les-bains, Lausanne, Vevey, Bourg-en-lavaux, Allaman, Saint-sulpice (vd), Montreux, Grandson, Tolochenaz, Gland, Cudrefin

__Canton:__ Vaud

__Survey_area:__ Rhone, Aare



        
## Named features Vaud canton lake 2020-04-01 2021-05-01 : The lakes, rivers and parks



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river<!--- INSTRUCTION_START

Generate a narrative summary based on the following table.



 INSTRUCTION_END ---> 

|       |   lake |
|:------|-------:|
| count |      2 |

The following is the names of the lakes, rivers and parks included in the data.

__L:__ Lac-leman, Neuenburgersee



        
## Summary statistics Vaud canton lake 2020-04-01 2021-05-01: The descriptive statistics of the survey results





<!--- INSTRUCTION_START

Generate a narrative summary based on the following table.



 INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |     950 |         82 |  0.374146 |     0 |   0.06 |  0.175 |  0.525 |    1.4 | 0.46307 |  1.83 | 2020-04-28 | 2021-05-01 |

        
## Municipal results Vaud canton lake 2020-04-01 2021-05-01 : The average pcs/m by municipality.

The average sample total for each municipality in the report





<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

| city               |   quantity |     pcs/m |
|:-------------------|-----------:|----------:|
| Allaman            |         89 | 1.05667   |
| Bourg-en-Lavaux    |         13 | 0.535     |
| Cudrefin           |          1 | 0.08      |
| Gland              |         10 | 0.11      |
| Grandson           |          1 | 0.01      |
| La Tour-de-Peilz   |        218 | 0.348667  |
| Lausanne           |         49 | 0.994286  |
| Montreux           |         29 | 0.161429  |
| Préverenges        |        214 | 0.374167  |
| Saint-Sulpice (VD) |        147 | 0.952     |
| Tolochenaz         |         12 | 0.165     |
| Vevey              |         92 | 0.188333  |
| Yverdon-les-Bains  |         75 | 0.0746154 |

        
## Material composition of objects Vaud canton lake 2020-04-01 2021-05-01: estimated material composition

Vaud: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If their is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| cloth      | 1%           |
| plastic    | 98%          |

        
## Sampling stratification Vaud canton lake 2020-04-01 2021-05-01: The environmental features surrounding the survey location.



Each survey location is surounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were takenaccording to the different conditions.





<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| proportion of buffer   | ('Proportion of samples collected', 'buildings')   | ('Proportion of samples collected', 'wetlands')   | ('Proportion of samples collected', 'forest')   | ('Proportion of samples collected', 'public-services')   | ('Proportion of samples collected', 'recreation')   | ('Proportion of samples collected', 'undefined')   | ('Proportion of samples collected', 'streets')   | ('Proportion of samples collected', 'vineyards')   | ('Proportion of samples collected', 'orchards')   |
|:-----------------------|:---------------------------------------------------|:--------------------------------------------------|:------------------------------------------------|:---------------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------|
| 0-20%                  | 6.10%                                              | 100.00%                                           | 97.56%                                          | 79.27%                                                   | 100.00%                                             | 86.59%                                             | 7.32%                                            | 97.56%                                             | 100.00%                                           |
| 20-40%                 | 6.10%                                              | no samples                                        | 2.44%                                           | 18.29%                                                   | no samples                                          | 4.88%                                              | 20.73%                                           | no samples                                         | no samples                                        |
| 40-60%                 | 1.22%                                              | no samples                                        | no samples                                      | 2.44%                                                    | no samples                                          | 8.54%                                              | 42.68%                                           | 2.44%                                              | no samples                                        |
| 60-80%                 | 37.80%                                             | no samples                                        | no samples                                      | no samples                                               | no samples                                          | no samples                                         | 17.07%                                           | no samples                                         | no samples                                        |
| 80-100%                | 48.78%                                             | no samples                                        | no samples                                      | no samples                                               | no samples                                          | no samples                                         | 12.20%                                           | no samples                                         | no samples                                        |

        
## Sampling stratification and trash density Vaud canton lake 2020-04-01 2021-05-01: The changes in the observed litter density and the changes in land use



The land use profile allows us to group locations according to the topography. Here we consdider how the observed litter density changes based on the land use feature and the proportion of the buffer-zone that the feature occupies





<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| proportion of buffer   |   buildings | wetlands           | forest              | public-services     | recreation         | undefined           |   streets | vineyards          | orchards           |
|:-----------------------|------------:|:-------------------|:--------------------|:--------------------|:-------------------|:--------------------|----------:|:-------------------|:-------------------|
| 0-20%                  |    0.678    | 0.3741463414634147 | 0.38075000000000003 | 0.22646153846153844 | 0.3741463414634147 | 0.36338028169014097 |  0.601667 | 0.370125           | 0.3741463414634147 |
| 20-40%                 |    0.24     | no samples         | 0.11000000000000001 | 0.9926666666666667  | no samples         | 0.35                |  0.291765 | no samples         | no samples         |
| 40-60%                 |    0.29     | no samples         | no samples          | 0.5349999999999999  | no samples         | 0.49714285714285716 |  0.158286 | 0.5349999999999999 | no samples         |
| 60-80%                 |    0.206774 | no samples         | no samples          | no samples          | no samples         | no samples          |  0.446429 | no samples         | no samples         |
| 80-100%                |    0.48475  | no samples         | no samples          | no samples          | no samples         | no samples          |  1.032    | no samples         | no samples         |

        
## Grid forecast Vaud canton lake 2020-04-01 2021-05-01

### Grid Approximation method:

1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.

2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.

3. **Normalization**:
   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.
   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.

4. **Summation or Integration**: Use the normalized values to compute estimates, such as expectations, by summing over the grid points, potentially weighted by the grid interval size.

#### Why normalize::

- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.
- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.

The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.


### Prior grid approximation
These are random samples from all of the data, not including the likelihood and limited to the requested end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. At least two of these variables are present at all sample locations. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary this prior assumes that land-use is the best predictor indifferent of the geographic location (in or out of the boundary). 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7700000000000005
The expected posterior distribution is a grid approximation from 0 to 4.760000000000001 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.2747   |
| std   |   0.319047 |
| min   |   0        |
| 25%   |   0.04     |
| 50%   |   0.15     |
| 75%   |   0.3725   |
| max   |   1.74     |

### In boundary grid approximation
This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. At least two of these variables are present at all sample locations. The similarity is calculated using the Manhatten distance between the likelihood and the proposed prior samples. In summary this prior assumes that litter density in the selected region is more a question of geographic location than land-use and that the best predictor of future results is the previous results within the same area.
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.4200000000000001
The expected posterior distribution is a grid approximation from 0 to 7.19 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.2943   |
| std   |   0.354983 |
| min   |   0        |
| 25%   |   0.0375   |
| 50%   |   0.14     |
| 75%   |   0.44     |
| max   |   1.6      |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. At least two of these variables are present at all sample locations. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary this prior assumes that litter density in the selected region is comparable to locations outside of the boundary and that trends or correlations of litter density are mostly a matter of land-use and less a question of geographic location.
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 1.69 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.1888   |
| std   |   0.242567 |
| min   |   0        |
| 25%   |   0.04     |
| 50%   |   0.08     |
| 75%   |   0.2475   |
| max   |   0.98     |


        
        
## Cluster and regression analysis Vaud canton lake 2020-04-01 2021-05-01


        
### Cluster analysis Vaud canton lake 2020-04-01 2021-05-01


Vaud: Cluster compositionThe survey locations were labeled according to the type and magnitude of land use in a 1 500 m buffer zone aroundaround each survey location. A cluster analysis was performed using K-Means clustering, the optimal amount of clusters was determined using the elbow method. Each cluster represents a group of locations that have similar land use profiles, that is the locations are surrounded by similar quantities of buildings or forest or undefined land use.We consider the cluster composition and the proportion of each cluster dedicated to a particular land use. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location whose buffer zone was 45% dedicated to forest. 

The following are the summary results of a cluster analysis. The columns are the features that were used to make the clusters. The optimal number of clusters was
determined using the elbow method (you can check the docs for this: https://hammerdirt-analyst.github.io/feb_2024/titlepage.html). The table displays the average magnitude
of each feature in the cluster. For example if the value for forest, cluster 1 = .45 then that means that in cluster 1, the average sample was taken from a location that was
45% dedicated to forest.

Table has the following format:

1. the columns are the measured land use features
2. the index is the cluster number
3. the value is the proportion of the cluster that is attributed to that column. For example if buildings in cluster 1 = .17 it means that the average magnitude of
the buildings variable was 0.17 in cluster 1.

Convert the following table into a paragraph, reporting the values for each column along with their cluster number values without any comments or analysis:

|   cluster |   public-services |   buildings |   forest |   undefined |   vineyards |   orchards |   streets |   recreation |
|----------:|------------------:|------------:|---------:|------------:|------------:|-----------:|----------:|-------------:|
|         0 |             0.079 |       1     |    0     |       0     | 6.93889e-18 |      0     |  0        |        0.02  |
|         1 |             0.126 |       0.362 |    0.044 |       0.393 | 0.087       |      0.114 |  0.241613 |        0     |
|         2 |             0.034 |       0.712 |    0.119 |       0.169 | 6.93889e-18 |      0     |  0.57403  |        0.001 |





Vaud: Average density per cluster
The following are the observed sample average per cluster. The units is objects per meter of beach. The columns are the use case of the objects: personal or professional. The index is
the cluster number.

Table has the following format:

1. the columns are the object use case
2. the index is the cluster number
3. the value is the objects found per meter of beach

Convert the following table into a paragraph, reporting the values for each column along with their respective cluster values without any comments or analysis:
The narrative needs to be in paragraph format.

|   cluster |     pcs/m |
|----------:|----------:|
|         0 | 0.295806  |
|         1 | 0.688571  |
|         2 | 0.0969565 |

        
### Summary of regression methods Vaud canton lake 2020-04-01 2021-05-01: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                        |        R² |      MSE |
|---:|:-----------------------------|----------:|---------:|
|  0 | Linear Regression            | -0.746867 | 0.979593 |
|  1 | Random Forest Regression     | -1.05073  | 1.14999  |
|  2 | Gradient Boosting Regression | -0.512818 | 0.848345 |
|  3 | Theil-Sen Regressor          | -0.429354 | 0.801541 |
|  4 | Bagging:Theil-Sen Regressor  | -0.442295 | 0.808798 |
|  5 | Voting                       | -0.672639 | 0.937968 |

        
### Feature and permutation importance Vaud canton lake 2020-04-01 2021-05-01



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | feature         |   Coeficient |
|---:|:----------------|-------------:|
|  0 | public-services |    0.42406   |
|  1 | buildings       |    0.118882  |
|  2 | forest          |   -0.0994492 |
|  3 | undefined       |    0.10797   |
|  4 | vineyards       |   -0.0486905 |
|  5 | orchards        |    0.166934  |
|  6 | streets         |    0.266642  |
|  7 | recreation      |    0.0610825 |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  0 | public-services |   0.318991   |
|  3 | undefined       |   0.0987176  |
|  5 | orchards        |   0.0527936  |
|  1 | buildings       |   0.0138328  |
|  7 | recreation      |   0.00221078 |
|  2 | forest          |   0.00121535 |
|  4 | vineyards       |  -0.00220536 |
|  6 | streets         |  -0.213929   |

        
        
## Inventory items Vaud canton lake 2020-04-01 2021-05-01 : The complete list of the objects found and indentified included in this report.

The quantity, average density, % of total and fail rate per object category





This is the list of all objects found at the beach.Generate a narrative summary based on the following table. You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table.



 INSTRUCTION_END ---> 

| code   |   quantity |       pcs/m |   % of total |   sample_id |   fails |      rate | object                                              |
|:-------|-----------:|------------:|-------------:|------------:|--------:|----------:|:----------------------------------------------------|
| G95    |        620 | 0.230244    |   0.652632   |          82 |      68 | 0.829268  | Cotton bud/swab sticks                              |
| G100   |        120 | 0.0629268   |   0.126316   |          82 |      48 | 0.585366  | Medical; containers/tubes/ packaging                |
| G98    |         99 | 0.037439    |   0.104211   |          82 |      30 | 0.365854  | Diapers - wipes                                     |
| G91    |         47 | 0.0145122   |   0.0494737  |          82 |      24 | 0.292683  | Biomass holder                                      |
| G96    |         39 | 0.0132927   |   0.0410526  |          82 |      22 | 0.268293  | Sanitary pads /panty liners/tampons and applicators |
| G144   |         12 | 0.0097561   |   0.0126316  |          82 |       7 | 0.0853659 | Tampons                                             |
| G99    |         11 | 0.00536585  |   0.0115789  |          82 |      10 | 0.121951  | Syringes - needles                                  |
| G97    |          2 | 0.000609756 |   0.00210526 |          82 |       2 | 0.0243902 | Toilet fresheners                                   |
     
        