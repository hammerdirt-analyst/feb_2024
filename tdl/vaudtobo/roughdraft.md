

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

# Vaud canton

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Vaud canton 2020-01-01 2021-05-31</i>



## Administrative boundaries Vaud canton 2020-01-01 2021-05-31 : Cities, cantons, survey areas

The number and and names of the cities, cantons and survey areas included in this report



The following table details the number of survey locations, cities, cantons and survey areas present in the data under analysis.

Please provide a narrative of the contents of the following table. In your narrative be sure to include the list of cities and the names of the canton and survey areas.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

 |              |   count |
|:-------------|--------:|
| location     |      26 |
| city         |      14 |
| canton       |       1 |
| survey areas |       2 |

The following is the names of the cities, cantons, and survey areas.

city: Yverdon-les-Bains, Vevey, Lavey-Morcles, Montreux, Cudrefin, Tolochenaz, La Tour-de-Peilz, Préverenges, Lausanne, Bourg-en-Lavaux, Allaman, Saint-Sulpice (VD), Grandson, Gland
canton: Vaud
survey_area: aare, rhone


## Named features Vaud canton 2020-01-01 2021-05-31 : The lakes, rivers and parks

The number and names of the lakes, rivers or parks included in this report



The following table details the number and the name of the lakes, rivers and parks in the survey data under analysis. Please provide a concise narrative of the contents of the following table. In your narrative be sure to the name of each park, lake or river

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
 INSTRUCTION_END ---> 

|       |   river |   lake |
|:------|--------:|-------:|
| count |       2 |      2 |

The following is the names of the lakes, rivers and parks included in the data.

river: rhone, la-thiele
lake: neuenburgersee, lac-leman
park: 


## Summary statistics Vaud canton 2020-01-01 2021-05-31: The descriptive statistics of the survey results

Vaud: The average pcs/m (objects per meter or trash per meter), standard deviation, number of samples, date range, the percentile distribution included in this report.





This table summarizes the sample total in pcs/m for each survey. Each survey is defined by a sample_id. A survey total is the sum of all rows that have the same sample_id.

<!--- INSTRUCTION_START
Generate a narrative summary based on the following table.
INSTRUCTION_END ---> 

|        |   total |   nsamples |   average |   5th |   25th |   50th |   75th |   95th |     std |   max | start      | end        |
|:-------|--------:|-----------:|----------:|------:|-------:|-------:|-------:|-------:|--------:|------:|:-----------|:-----------|
| result |    3416 |         87 |   1.12586 |  0.05 |  0.225 |   0.67 |   1.37 |  4.028 | 1.38471 |     8 | 2020-04-28 | 2021-05-12 |

## Material composition of objects Vaud canton 2020-01-01 2021-05-31: estimated material composition

Vaud: The proportion of each material type according to material category





The following table details the proportion that each material type represents to the total. 
Generate a narrative summary based on the following table. You need to include all the material types and their float values.
If there is more than one material entry in the table.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. Consider the example above

 INSTRUCTION_END ---> 

| material   | % of total   |
|:-----------|:-------------|
| plastic    | 100%         |
## Survey Totals for city


## Vaud canton 2020-01-01 2021-05-31 city: The average pcs/m by city.

The average sample total for each city in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | city               |   quantity |     pcs/m |
|---:|:-------------------|-----------:|----------:|
|  0 | Allaman            |         96 | 0.9       |
|  1 | Bourg-en-Lavaux    |         10 | 0.415     |
|  2 | Cudrefin           |          1 | 0.08      |
|  3 | Gland              |         24 | 0.25      |
|  4 | Grandson           |         23 | 0.33      |
|  5 | La Tour-de-Peilz   |        504 | 0.706667  |
|  6 | Lausanne           |        154 | 2.72857   |
|  7 | Lavey-Morcles      |         17 | 0.0666667 |
|  8 | Montreux           |        184 | 1.16714   |
|  9 | Préverenges        |        781 | 1.41923   |
| 10 | Saint-Sulpice (VD) |        225 | 1.318     |
| 11 | Tolochenaz         |         78 | 1.08      |
| 12 | Vevey              |       1005 | 2.02667   |
| 13 | Yverdon-les-Bains  |        314 | 0.28      |


## Survey Totals for parent_boundary


## Vaud canton 2020-01-01 2021-05-31 survey area: The average pcs/m by survey area.

The average sample total for each survey area in the report





The following table details the results of the survey for each unique occurrence of the selected variable. 
<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. You need to include all the cities and their results

INSTRUCTION_END -->

|    | parent_boundary   |   quantity |    pcs/m |
|---:|:------------------|-----------:|---------:|
|  0 | aare              |        338 | 0.270625 |
|  1 | rhone             |       3078 | 1.31859  |



## Inventory items Vaud canton 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |    pcs/m |   % of total |   sample_id |   fail rate | object                       |
|:-------|-----------:|---------:|-------------:|------------:|------------:|:-----------------------------|
| G27    |       2366 | 0.805172 |     0.692623 |          87 |    0.91954  | Cigarette filters            |
| G30    |       1050 | 0.32069  |     0.307377 |          87 |    0.954023 | Food wrappers; candy, snacks |

## Sampling stratification Vaud canton 2020-01-01 2021-05-31: The environmental features surrounding the survey location.

Each survey location is surounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.



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
Generate a narrative summary based on the following table. Consider the example above

| proportion of buffer   | ('Proportion of samples collected', 'buildings')   | ('Proportion of samples collected', 'wetlands')   | ('Proportion of samples collected', 'forest')   | ('Proportion of samples collected', 'public-services')   | ('Proportion of samples collected', 'recreation')   | ('Proportion of samples collected', 'undefined')   | ('Proportion of samples collected', 'streets')   | ('Proportion of samples collected', 'vineyards')   | ('Proportion of samples collected', 'orchards')   |
|:-----------------------|:---------------------------------------------------|:--------------------------------------------------|:------------------------------------------------|:---------------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------|
| 0-20%                  | 6.9%                                               | 100.0%                                            | 94.3%                                           | 80.5%                                                    | 100.0%                                              | 82.8%                                              | 8.0%                                             | 97.7%                                              | 100.0%                                            |
| 20-40%                 | 8.0%                                               | none                                              | 4.6%                                            | 17.2%                                                    | none                                                | 8.0%                                               | 19.5%                                            | none                                               | none                                              |
| 40-60%                 | 2.3%                                               | none                                              | 1.1%                                            | 2.3%                                                     | none                                                | 9.2%                                               | 56.3%                                            | 2.3%                                               | none                                              |
| 60-80%                 | 36.8%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 3.4%                                             | none                                               | none                                              |
| 80-100%                | 46.0%                                              | none                                              | none                                            | none                                                     | none                                                | none                                               | 12.6%                                            | none                                               | none                                              |

## Sampling stratification and trash density Vaud canton 2020-01-01 2021-05-31: The changes in the observed litter density and the changes in land use



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


Generate a narrative summary based on the following table. Consider the example above 

| proportion of buffer   |   ('Pieces of trash per meter', 'buildings') | ('Pieces of trash per meter', 'wetlands')   | ('Pieces of trash per meter', 'forest')   | ('Pieces of trash per meter', 'public-services')   | ('Pieces of trash per meter', 'recreation')   | ('Pieces of trash per meter', 'undefined')   |   ('Pieces of trash per meter', 'streets') | ('Pieces of trash per meter', 'vineyards')   | ('Pieces of trash per meter', 'orchards')   |
|:-----------------------|---------------------------------------------:|:--------------------------------------------|:------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:---------------------------------------------|-------------------------------------------:|:---------------------------------------------|:--------------------------------------------|
| 0-20%                  |                                     0.533333 | 1.1258620689655172                          | 1.1859756097560976                        | 0.9818571428571431                                 | 1.1258620689655172                            | 1.2645833333333334                           |                                   0.86     | 1.1425882352941177                           | 1.1258620689655172                          |
| 20-40%                 |                                     0.228571 | none                                        | 0.175                                     | 1.8926666666666665                                 | none                                          | 0.4557142857142858                           |                                   0.507647 | none                                         | none                                        |
| 40-60%                 |                                     1.05     | none                                        | none                                      | 0.415                                              | none                                          | 0.46375000000000005                          |                                   1.23122  | 0.415                                        | none                                        |
| 60-80%                 |                                     0.949062 | none                                        | none                                      | none                                               | none                                          | none                                         |                                   1.19     | none                                         | none                                        |
| 80-100%                |                                     1.517    | none                                        | none                                      | none                                               | none                                          | none                                         |                                   1.76364  | none                                         | none                                        |

## Grid forecast Vaud canton 2020-01-01 2021-05-31


### Grid Approximation method:

Grid approximation is a numerical technique used to approximate the distribution of a parameter. The technique employed here uses conditional probability to answer the question _What am I likely to observe given what was observed previously, under similar conditions ?_ The conditions are the land use features (reference sampling stratification table) and the proportion of the buffer zone dedicated to each land use feature. An inference table is constructed using observations from other locations that are similar to the survey location and the observed results. An inference table is a simple way to apply Bayes' theorem to estimate the posterior distribution of the parameter of interest. The data for the prior is randomly selected from the existing data with similar land use features, similarity is measured with cosine similarity or manhattan distance. The data for the prior does not include the data from the likelihood (ie the data defined by the report parameters).

In this report their maybe three priors that represent different possible interpretation of the survey results, each report is different.

 <!--- INSTRUCTION_START
The current report may not have all three priors, the priors are selected based on the similarity of the data. You must consult the users report and identify the priors that were used.  
You must locate the section that corresponds to the prior that was used and provide the results for that prior. 
INSTRUCTION_END -->

The grid approximation method is used to estimate the posterior distribution of the parameter of interest (e.g., the litter density) given the land use profile of the survey location. Therefore this method is an indicator of what the next survey will yield given the land use profile of the survey locations of interest. The steps of the grid approximation are the same for all three priors. The only difference is the data used for the prior (in-boundary, out-boundary, prior).

1. **Parameter Space Discretization**: Divide the continuous parameter space into a discrete grid of points. We use the 0 as the start of the grid and the 99th percentile of the observed values as the grid limit and we evaluate the function every 0.01.

2. **Evaluation of Function**: Evaluate the statistical function of interest (e.g., likelihood, posterior) at each grid point. This step gives a set of unnormalized values across the grid.

3. **Normalization**:
   - **Sum the Values**: Compute the sum of the evaluated function values over all grid points. This sum is used as the normalizing constant.
   - **Normalize**: Divide each evaluated function value by the normalizing constant to ensure that the sum (or integral, in the continuous case) over the grid points is 1. This is crucial when dealing with probability distributions, as it ensures the result is a valid probability distribution.

- **Probability Distributions**: In Bayesian inference, the posterior distribution needs to be properly normalized so that it integrates (or sums) to 1 over the parameter space.
- **Accuracy of Estimates**: Normalization ensures that derived quantities, like expectations or credible intervals, are accurate representations of the true statistical measures.

The normalization step is particularly crucial in Bayesian grid approximations because it transforms the unnormalized posterior into a proper probability distribution, enabling meaningful statistical inference.


### Combined prior grid approximation
These are random samples from all of the data (in different of geographic boundary) not including the likelihood and limited to the requested end date.  The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples This prior makes no difference between the locations inside or outside the boundary of interest. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations (indifferent of the geographic boundary) ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 6.96 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.8033   |
| std   |   0.851319 |
| min   |   0        |
| 25%   |   0.2      |
| 50%   |   0.475    |
| 75%   |   1.095    |
| max   |   4.24     |

### In boundary grid approximation
This prior distribution is selected from random samples from within the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood feature variables  and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations in the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.4300000000000001
The expected posterior distribution is a grid approximation from 0 to 11.28 every 0.01.

|       |     pcs/m |
|:------|----------:|
| count | 100       |
| mean  |   0.7033  |
| std   |   0.87548 |
| min   |   0       |
| 25%   |   0.2275  |
| 50%   |   0.44    |
| 75%   |   0.7975  |
| max   |   5.49    |

### Out boundary grid approximation
This prior distribution is selected from random samples from outside the requested administrative boundary (if a boundary was selected) not including samples from the likelihood and limited to the end date. The samples are selected based on the similarity of the land use features: buildings, forest and undefined. The similarity is calculated using the Manhattan distance between the likelihood samples and the proposed prior samples. In summary the posterior distribution from this prior answers the question 'What am I likely to find given the results from similar locations outside the geographic boundary ?' 
They have been selected based on the similarity of the buildings, forest and undefined feature variables. The similarity threshold is 0.7600000000000005
The expected posterior distribution is a grid approximation from 0 to 13.389999999999999 every 0.01.

|       |      pcs/m |
|:------|-----------:|
| count | 100        |
| mean  |   0.6144   |
| std   |   0.826705 |
| min   |   0        |
| 25%   |   0.0975   |
| 50%   |   0.275    |
| 75%   |   0.8875   |
| max   |   4.48     |




### Cluster analysis Vaud canton 2020-01-01 2021-05-31


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

|   cluster |   buildings |   wetlands |   forest |   public-services |   recreation |   undefined |   streets |   vineyards |   orchards |
|----------:|------------:|-----------:|---------:|------------------:|-------------:|------------:|----------:|------------:|-----------:|
|         0 |       0.055 |      0     |    0.357 |             0.011 |        0.125 |       0.588 |  0.139474 | 6.93889e-18 |       0    |
|         1 |       1     |      0     |    0     |             0.079 |        0.02  |       0     |  0        | 6.93889e-18 |       0    |
|         2 |       0.203 |      0     |    0.07  |             0.467 |        0.003 |       0.236 |  0.533138 | 0.481       |       0.01 |
|         3 |       0.182 |      0     |    0.492 |             0.142 |        0.006 |       0.222 |  1        | 6.93889e-18 |       0    |
|         4 |       0.945 |      0     |    0.041 |             0.38  |        0.044 |       0.014 |  0.571441 | 6.93889e-18 |       0    |
|         5 |       0.245 |      0.089 |    0.118 |             0.007 |        0.027 |       0.548 |  0.227685 | 6.93889e-18 |       0    |





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
|         0 | 0.25      |
|         1 | 1.06545   |
|         2 | 0.415     |
|         3 | 0.0666667 |
|         4 | 2.14083   |
|         5 | 0.205     |



### Summary of regression methods Vaud canton 2020-01-01 2021-05-31: 

In addition to grid approximation using Bayesian techniques the following linear and ensemble regression models were used. The feature variables are the land-use features identified in the land-use profile. From the scikit-learn standard package: LinearRegression, RandomForestRegressor, GradientBoostingRegressor, TheilSennRegressor. The model with the highest r² is then used in the BaggingRegressor and the VotingRegressor.





The following table details the results from different regression analysis of our data.

The table has the following format:

1. Model: the type of regression model used
2. R²: The coefficient of determination
3. MSE: the mean squared error

Generate a narrative summary based on the following table. You need to include all the models and the R² and MSE result.
The narrative needs to be in paragraph format.

|    | Model                                |         R² |      MSE |
|---:|:-------------------------------------|-----------:|---------:|
|  0 | Linear Regression                    | -0.090185  | 0.692157 |
|  1 | Random Forest Regression             | -0.563984  | 0.992972 |
|  2 | Gradient Boosting Regression         |  0.0482949 | 0.604237 |
|  3 | Theil-Sen Regressor                  | -0.0112404 | 0.642035 |
|  4 | Bagging:Gradient Boosting Regression | -0.0291856 | 0.653429 |
|  5 | Voting                               | -0.0499981 | 0.666643 |



### Feature and permutation importance Vaud canton 2020-01-01 2021-05-31



__Model feature importance__

Feature importance is a technique used in machine learning to identify and quantify the significance of different input variables (features) in predicting the target variable. In models like decision trees, random forests, and gradient boosting machines, feature importance is often calculated by measuring how much the model's accuracy or error changes when a particular feature is included versus when it is excluded. 
The following table details the model feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  0 | buildings       |  0.794326    |
|  5 | streets         |  0.0798342   |
|  6 | vineyards       |  0.069294    |
|  2 | public-services |  0.0224765   |
|  4 | undefined       |  0.016637    |
|  3 | recreation      |  0.014353    |
|  1 | forest          |  0.00236152  |
|  7 | orchards        |  0.000717586 |



__Permutation feature importance__

Permutation importance is a model-agnostic method for assessing the importance of individual features in a predictive model. It is particularly useful because it can be applied to any type of model, whether it's a linear model, a decision tree, or a complex ensemble model. This method involves randomly shuffling the values of a feature in the dataset and observing the impact on the model's performance. A significant drop in performance indicates that the feature is important.
The following table details the permutation feature importance.

Table has the following format:

1. Feature: the name of the land-use feature
2. importance: The model feature importance

Convert the following table into a paragraph, reporting the values for each row without any comments or analysis:

|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  0 | buildings       |  0.34195     |
|  5 | streets         |  0.0393282   |
|  6 | vineyards       |  0.022435    |
|  7 | orchards        | -0.000120279 |
|  1 | forest          | -0.000335946 |
|  2 | public-services | -0.00633129  |
|  4 | undefined       | -0.00981132  |
|  3 | recreation      | -0.0164275   |


## Inventory items Vaud canton 2020-01-01 2021-05-31 : The complete list of the objects found and identified included in this report.

The quantity, average density, % of total and fail rate per object category




This is the list of all objects found at the beach. Generate a narrative summary based on the following table.You need to mention all the objects that have a rate >= 0.5. Include % of total for each of the objects that have a rate >= 0.5, label these objects fail rate.

<!--- INSTRUCTION_START

Generate a narrative summary based on the following table. The Fail Rate is The proportion of samples where at least one of the objects were found.

INSTRUCTION_END ---> 
| code   |   quantity |    pcs/m |   % of total |   sample_id |   fail rate | object                       |
|:-------|-----------:|---------:|-------------:|------------:|------------:|:-----------------------------|
| G27    |       2366 | 0.805172 |     0.692623 |          87 |    0.91954  | Cigarette filters            |
| G30    |       1050 | 0.32069  |     0.307377 |          87 |    0.954023 | Food wrappers; candy, snacks |
