

<!-- INSTRUCTION_START

1. Analysis of Sampling Stratification and Sampling stratification and trash density tables
   * Objective: Ensure conclusions about the presence or absence of objects are based on a combined interpretation of sampling stratification and litter density data.
   * Data Validation: Confirm that any conclusions about trash density and land use are supported by the presence of samples in the sampling stratification table"
   * Interpretation Guidelines: Analyze how the distribution of land-use features influences the observed trash density. 
   * Draw conclusions only when both stratification and density data are aligned. Make sure to check all the values for a given land-use feature and proportion of buffer zone. Before making any conlusions"
   * A zero in the trash density table indicates that no objects were found for that land-use feature and proportion of buffer zone.

2. Reporting Geographic Information

   * Always provide the names of all the cities, cantons, and survey areas included in the report.
   * Always provide the names of all the lakes, rivers, and parks included in the report.

3. Definitions of Urban, Rural Areas, fail-rate

   * Urban Areas: The proportion of samples where building occupy 60% or more of the buffer is greater than 50%.

   * Rural Areas: The proportion of samples where forest occupy 60% or more of the buffer is greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   * Fail Rate: The proportion of samples where at least one of the object categories was found.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column, if the table
reads 'no samples' that is equivalent to 0. 

2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column, if the table
reads 'no samples' that is equivalent to 0. 

3. Make the conclusion: If test one is greater than 50% then the classification is urban. If test two is greater than 50% then 
the classification is rural. If neither test one or test two is greater than 50% the the classification is mixed.

  

INSTRUCTION_END -->

# Biel/Bienne - example city

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Biel/Bienne - example city 2020-01-01 2021-05-31</i>



## Administrative boundaries Biel/Bienne - example city 2020-01-01 2021-05-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

|              |   count |
|:-------------|--------:|
| location     |       3 |
| city         |       1 |
| canton       |       1 |
| survey areas |       1 |

The following is the names of the cities, cantons, and survey areas.

city: Biel/Bienne
canton: Bern
survey_area: aare


## Named features Biel/Bienne - example city 2020-01-01 2021-05-31 : The lakes, rivers and parks

The number and names of the lakes, rivers or parks included in this report



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. 

|       |   river |   lake |
|:------|--------:|-------:|
| count |       1 |      1 |

The following is the names of the lakes, rivers and parks included in the data.

river: schuss
lake: bielersee
park: 


## Summary statistics Biel/Bienne - example city 2020-01-01 2021-05-31: The descriptive statistics of the survey results

Biel/Bienne - example: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |    1034 |         17 |   1.61824 | 0.266 |   0.42 |   1.71 |   2.36 |  3.752 | 1.25534 |  3.88 | 2020-01-26 | 2021-03-31 |

## Material composition of objects Biel/Bienne - example city 2020-01-01 2021-05-31: estimated material composition

Biel/Bienne - example: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 

| material   | % of total   |
|:-----------|:-------------|
| plastic    | 100%         |
## Survey Totals for canton


## Biel/Bienne - example city 2020-01-01 2021-05-31 canton: The average pcs/m by canton.

The average sample total for each canton in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 

|    | canton   |   quantity |   pcs/m |
|---:|:---------|-----------:|--------:|
|  0 | Bern     |       1034 | 1.61824 |


## Survey Totals for parent_boundary


## Biel/Bienne - example city 2020-01-01 2021-05-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 

|    | parent_boundary   |   quantity |   pcs/m |
|---:|:------------------|-----------:|--------:|
|  0 | aare              |       1034 | 1.61824 |



## Inventory items Biel/Bienne - example city 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |    pcs/m |   % of total |   sample_id |   fail rate | object                       |
|:-------|-----------:|---------:|-------------:|------------:|------------:|:-----------------------------|
| G27    |        781 | 1.23294  |     0.755319 |          17 |    1        | Cigarette filters            |
| G30    |        253 | 0.385294 |     0.244681 |          17 |    0.941176 | Food wrappers; candy, snacks |

## Sampling stratification Biel/Bienne - example city 2020-01-01 2021-05-31: The environmental features surrounding the survey location.

Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.



The sampling stratification table quantifies what proportion of the samples were collected according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.


<!--- INSTRUCTION_START

__How to interpret sampling stratification table:__

The sampling stratification table quantifies what proportion of the samples were conducted according to the proportion of the buffer
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone.


Therefore when you answer questions about sampling stratification you must qualify that with the corresponding value
in the sampling stratification and trash density table, in parentheses. For example, using the example tables
below, we would say 16% (0.53 pcs/m) of all samples were taken at locations where buildings occupied 80 - 100% of the buffer zone. 

__Example sampling stratification and trash density table:__


|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |

__Example sampling stratification table:__


|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                     0.13 |                       1|                 0.85  |                    0.95      |   
|                    20 - 40% |                     0.21 |              no samples|                   0.1 |                    0.05      |
|                    40 - 60% |                     0.22 |             no samples |             .05       |                    no samples|
|                    60 - 80% |                    0.18  |             no samples |            no samples |                 no samples   |
|                    80 - 100%|                    0.16  |              no samples|       no samples      |                   no samples  | 


__Example interpretation of the sampling stratification and trash density table__

The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer 13% of all samples, (0.37 pcs/m)

where buildings occupied 20 - 40% of the buffer 21% of all samples, (0.03 pcs/m)

where buildings occupied 40 - 60% of the buffer 22% of all samples, (0.01 pcs/m)

where buildings occupied 60 - 80% of the buffer 18% of all samples, (0.37 pcs/m)

where buildings occupied 80 - 100% of the buffer 16% of all samples, (0.49, pcs/m)



1. no samples indicates that no samples were collected at a location that fits this description.

2. Definitions of Urban, Rural or mixed

   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.

   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**

1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.


2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.


3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.


 

INSTRUCTION_END -->
| proportion of buffer   | ('Proportion of samples collected', 'buildings')   | ('Proportion of samples collected', 'wetlands')   | ('Proportion of samples collected', 'forest')   | ('Proportion of samples collected', 'public-services')   | ('Proportion of samples collected', 'recreation')   | ('Proportion of samples collected', 'undefined')   | ('Proportion of samples collected', 'streets')   | ('Proportion of samples collected', 'vineyards')   | ('Proportion of samples collected', 'orchards')   |
|:-----------------------|:---------------------------------------------------|:--------------------------------------------------|:------------------------------------------------|:---------------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------|
| 0-20%                  | none                                               | 100.0%                                            | 11.8%                                           | 100.0%                                                   | 100.0%                                              | 100.0%                                             | 76.5%                                            | 100.0%                                             | 100.0%                                            |
| 20-40%                 | none                                               | none                                              | 88.2%                                           | none                                                     | none                                                | none                                               | 11.8%                                            | none                                               | none                                              |
| 40-60%                 | 76.5%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | none                                             | none                                               | none                                              |
| 60-80%                 | 23.5%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | none                                             | none                                               | none                                              |
| 80-100%                | none                                               | none                                              | none                                            | none                                                     | none                                                | none                                               | 11.8%                                            | none                                               | none                                              |

## Sampling stratification and trash density Biel/Bienne - example city 2020-01-01 2021-05-31: The changes in the observed litter density and the changes in land use



The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.


<!--- INSTRUCTION_START

__How to interpret sampling stratification and trash density table:__

The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer 
zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. 
The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). 
The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the 
buffer zone that is dedicated to a particular land use feature.

Therefore when you answer questions about sampling stratification and trash density you must qualify that with the corresponding value
in the sampling stratification table. For example, if you say that the trash density is 0.05 pcs/m in an area where buildings occupy 0-20% of the buffer zone,
you must also say that 6% of the samples were taken in an area where buildings occupy 0-20% of the buffer zone.


__Example sampling stratification and trash density table:__


|   Proportion of buffer zone |   ('pcs/m', 'buildings') |  ('pcs/m', 'wetlands') |  ('pcs/m', 'forest')  |  ('pcs/m', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.37 |                    .46 |             .52  |                    0.31  |   
|                    20 - 40% |                0.45 |              no samples|             .33 |                    0.49       |
|                    40 - 60% |                0.57 |              no samples|       no samples       |                    no samples |
|                    60 - 80% |                0.5  |              no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.53  |              no samples|       no samples     |                   no samples    |


__Example sampling stratification table:__


|   Proportion of buffer zone |   ('Proportion of samples collected', 'buildings') |  ('Proportion of samples collected', 'wetlands') |  ('Proportion of samples collected', 'forest')  |  ('Proportion of samples collected', 'public-services')|   
|----------------------------:|-------------------------:|-----------------------:|----------------------:|-----------------------------:|
|                     0 - 20% |                0.13 |                   1|             0.85  |                    0.95  |   
|                    20 - 40% |                0.21 |          no samples|             0.1 |                    0.05       |
|                    40 - 60% |                0.22 |         no samples |       .05       |                    no samples |
|                    60 - 80% |                0.18  |        no samples |       no samples     |                 no samples    |
|                    80 - 100%|                0.16  |        no samples|       no samples     |                   no samples    | 



__Example interpretation of the sampling stratification and trash density table__


The average objects per meter based on the sampling-stratification was as follows: 
where buildings occupied 0 - 20% of the buffer (13% of all samples) the average objects per meter was 0.05

where buildings occupied 20 - 40% of the buffer (21% of all samples) the average objects per meter was 0.03

where buildings occupied 40 - 60% of the buffer (22% of all samples) the average objects per meter was 0.01

where buildings occupied 60 - 80% of the buffer (18% of all samples) the average objects per meter was 0.37

where buildings occupied 80 - 100% of the buffer (16% of all samples) the average objects per meter was 0.49


1. no samples indicates that no samples were takes at a location that fits this description.

2. Definitions of Urban, Rural or mixed

   * Urban Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column are greater than 50%.

   * Rural Areas: the sum of the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column are greater than 50%.

   * Mixed Areas: Does not meet the criteria of urban or rural.

   
**Example How to calculate urban, rural or mixed sampling stratification: consider the example sampling stratification table**


1. test one: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the buildings column. In the example 
table above, the proportion of samples where buildings occupy 60-80% of the buffer is .18  and the proportion of samples 
where buildings occupy 80 - 100% of the buffer is .16 therefore the proportion of samples where buildings occupy more than 
50% of the buffer is .16 + .18 or 34%.

2. test two: Sum the rows '60 - 80%' and '80 - 100%' in the sampling stratification table under the forest column. In the example 
table above, the proportion of samples where forest occupy 60-80% of the buffer is 0 (no samples)  and the proportion of 
samples where forest occupy 80 - 100% of the buffer is 0 (no samples) therefore the proportion of samples where forest occupy
more than 50% of the buffer is 0.

3. Make the conclusion: If the value of test one is greater than 50% then the area is urban. If the value of test two
is greater than 50% then the area is considered rural. If neither test one or test two is greater than 50% the classification is mixed.


 INSTRUCTION_END -->



| proportion of buffer   | ('Pieces of trash per meter', 'buildings')   | ('Pieces of trash per meter', 'wetlands')   | ('Pieces of trash per meter', 'forest')   | ('Pieces of trash per meter', 'public-services')   | ('Pieces of trash per meter', 'recreation')   | ('Pieces of trash per meter', 'undefined')   | ('Pieces of trash per meter', 'streets')   | ('Pieces of trash per meter', 'vineyards')   | ('Pieces of trash per meter', 'orchards')   |
|:-----------------------|:---------------------------------------------|:--------------------------------------------|:------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:---------------------------------------------|:-------------------------------------------|:---------------------------------------------|:--------------------------------------------|
| 0-20%                  | none                                         | 1.6182352941176472                          | 0.355                                     | 1.6182352941176472                                 | 1.6182352941176472                            | 1.6182352941176472                           | 1.9969230769230768                         | 1.6182352941176472                           | 1.6182352941176472                          |
| 20-40%                 | none                                         | none                                        | 1.7866666666666664                        | none                                               | none                                          | none                                         | 0.42000000000000004                        | none                                         | none                                        |
| 40-60%                 | 1.9969230769230768                           | none                                        | none                                      | none                                               | none                                          | none                                         | none                                       | none                                         | none                                        |
| 60-80%                 | 0.3875                                       | none                                        | none                                      | none                                               | none                                          | none                                         | none                                       | none                                         | none                                        |
| 80-100%                | none                                         | none                                        | none                                      | none                                               | none                                          | none                                         | 0.355                                      | none                                         | none                                        |

## Grid forecast Biel/Bienne - example city 2020-01-01 2021-05-31


### Grid Approximation method:

We employed a grid-based Bayesian inference approach to estimate the conditional probability that a survey result will exceed or be equal to a given value, using prior observations from similar locations and new data from the location of interest. The prior represents survey data from locations either inside or outside a designated boundary, segmented by geographic or administrative criteria, while the likelihood reflects observations from the specific location being analyzed. The grid spans the range of possible values, from 0 to the maximum value observed in either the prior or likelihood data, with a fixed interval of 0.01.

For each point x on this grid, we calculated the conditional probability that a survey result, y, would exceed or be equal to x. This was modeled using a binomial distribution, where the successes represent the number of times y was greater than or equal to x, and failures represent the number of times y was less than x, for both the prior and the likelihood. By applying Bayes' Theorem, we combined the prior and likelihood distributions to compute the posterior distribution at each grid point, providing a detailed estimate of the probability that a survey outcome exceeds any value across the range of interest.

In our method, the grid points act as thresholds, and the posterior probability at each grid point corresponds to the likelihood that a survey result exceeds or equals that value. This setup is analogous to a multinomial distribution, where each grid point is treated as a category and the probability of an event occurring in each category is computed. Extending this approach to a multinomial framework would simplify the computational process, as the Dirichlet distribution—being the conjugate prior to the multinomial—would allow for efficient posterior updates. This relationship ensures that Bayesian updating remains computationally straightforward, even in more complex settings where probabilities are distributed across multiple categories.

### Combined grid approximation
The expected posterior distribution is a grid approximation from 0 to 3.86 every 0.01.

average cosine similarity score of prior samples 0.97 

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   1.1512   |
| std   |   0.884963 |
| min   |   0        |
| 25%   |   0.415    |
| 50%   |   0.98     |
| 75%   |   1.6625   |
| max   |   3.61     |

### Out boundary grid approximation
The expected posterior distribution is a grid approximation from 0 to 3.86 every 0.01.

average cosine similarity score of prior samples 0.97 

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   1.0836   |
| std   |   0.969237 |
| min   |   0.01     |
| 25%   |   0.31     |
| 50%   |   0.73     |
| 75%   |   1.89     |
| max   |   3.8      |




## Cluster analysis Biel/Bienne - example city 2020-01-01 2021-05-31


Biel/Bienne - example: Cluster composition
There was insufficient data for a cluster analysis. Consider the sampling stratification


Biel/Bienne - example: Average density per cluster
There was insufficient data for a cluster analysis. Consider the sampling stratification


### Summary of regression methods Biel/Bienne - example city 2020-01-01 2021-05-31: 

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
|  0 | Linear Regression            | -0.10461  | 0.97959  |
|  1 | Random Forest Regression     | -0.189586 | 1.05495  |
|  2 | Gradient Boosting Regression | -0.590501 | 1.41049  |
|  3 | Theil-Sen Regressor          | -0.111311 | 0.985532 |
|  4 | Bagging:Linear Regression    | -0.409816 | 1.25025  |
|  5 | Voting                       | -0.280263 | 1.13536  |



### Feature and permutation importance Biel/Bienne - example city 2020-01-01 2021-05-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Coefficient |
|---:|:----------------|--------------:|
|  4 | undefined       |     0.303537  |
|  3 | recreation      |     0.258105  |
|  1 | forest          |     0.224486  |
|  2 | public-services |     0.111299  |
|  5 | streets         |    -0.0548976 |
|  0 | buildings       |    -0.167061  |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  4 | undefined       |   0.276145   |
|  1 | forest          |   0.144776   |
|  0 | buildings       |   0.0823226  |
|  3 | recreation      |   0.0418223  |
|  5 | streets         |   0.014914   |
|  2 | public-services |  -0.00534375 |


## Inventory items Biel/Bienne - example city 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |    pcs/m |   % of total |   sample_id |   fail rate | object                       |
|:-------|-----------:|---------:|-------------:|------------:|------------:|:-----------------------------|
| G27    |        781 | 1.23294  |     0.755319 |          17 |    1        | Cigarette filters            |
| G30    |        253 | 0.385294 |     0.244681 |          17 |    0.941176 | Food wrappers; candy, snacks |
