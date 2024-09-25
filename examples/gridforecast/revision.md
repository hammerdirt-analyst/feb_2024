# Bern - roughdraft canton

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Bern - roughdraft canton 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting grid forecasting example</i>




## Sample results

The report on trash density in Bern from January 1, 2020, to May 31, 2021, includes a total of 13 cities: Biel/Bienne, Vinelz, Brienz (BE), Spiez, Lüscherz, Nidau, Gals, Unterseen, Erlach, Thun, Beatenberg, Ligerz, and Bönigen. There are three lakes identified in the report: Bielersee, Brienzersee, and Thunersee. The survey area under analysis is Aare.

A total of 74 samples were collected during the survey. The average density of trash was 0.69 pcs/m, with a median of 0.35 pcs/m. The maximum density recorded was 3.88 pcs/m, and the standard deviation was 0.89. The total number of objects identified was 2,128.

The two most common objects found in the survey were:
1. Cigarette filters: Fail rate of 83.78% (indicating presence in approximately 84% of samples), comprising 73.45% of the total, with a density of 0.48 pcs/m and a total quantity of 1,563.
2. Food wrappers (candy, snacks): Fail rate of 82.43%, accounting for 26.55% of the total, with a density of 0.22 pcs/m and a total quantity of 565.

The material composition of the identified objects was 100% plastic.

### Frequently asked questions

**What were the ten most common items found?**  
The most common items found were:
1. Cigarette filters: Fail rate of 83.78%, comprising 73.45% of the total. 
2. Food wrappers (candy, snacks): Fail rate of 82.43%, accounting for 26.55% of the total. 

The fail rate is defined as the proportion of samples in which at least one of the objects was found.

**Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**  
Yes, many of these objects are commonly found on European beaches. According to the OSPAR results from 2021, which can be accessed at [OSPAR](https://www.ospar.org), cigarette butts were found at a density of approximately 24,000 per 100 meters of beach.

**What are possible sources of these specific objects?**  
Possible sources of these specific objects include urban littering, improper disposal of cigarette butts, and packaging waste from food items. Activities such as picnicking, outdoor events, and general consumer behavior contribute to the presence of these materials in aquatic environments.

**Which three cities had the highest average pcs/m? Which three had the lowest?**  
The three cities with the highest average pcs/m were:
1. Biel/Bienne: 1.79 pcs/m
2. Ligerz: 1.55 pcs/m
3. Bönigen: 1.25 pcs/m

The three cities with the lowest average pcs/m were:
1. Lüscherz: 0.06 pcs/m
2. Spiez: 0.08 pcs/m
3. Gals: 0.21 pcs/m

## Sampling stratification

Sampling stratification refers to the method of dividing a survey area into distinct sections or strata based on specific characteristics, such as land use. In this context, the survey locations are surrounded by a buffer zone of 1,500 meters, which is analyzed based on the proportion of different land use features present. This stratification allows researchers to evaluate how the distribution of these features impacts the observed trash density. Land use is categorized into various types, including buildings, forests, wetlands, and other features.

In the sampling stratification and trash density table, the highest pieces of trash per meter (pcs/m) for the specified categories are as follows: for buildings, a density of 1.79 pcs/m is recorded in the 40-60% buffer zone, where buildings occupy a significant proportion of the area. For forests, the highest density is 0.88 pcs/m in the 20-40% buffer zone. These values indicate the average amount of trash found per meter in areas where buildings and forests are prevalent.

To classify the surveyed locations, we sum the proportions of samples for buildings in the rows of 60-80% and 80-100% of the sampling stratification table, which are 6.8% and 2.7%, respectively, totaling 9.5%. In contrast, for forests, the sums from the same rows are both 0%, resulting in a total of 0%. Since both sums are less than 50%, the classification of the surveyed locations is mixed.

### Frequently asked questions

**1. What does the sampling stratification table tell us?**  
The sampling stratification table provides insight into the distribution of trash density across different land use features. For instance, in the buildings category, 1.79 pcs/m was recorded in the 40-60% buffer zone, where 21.6% of the samples were taken. In contrast, for undefined land use, the highest density is 1.12 pcs/m in the 0-20% buffer zone, where 35.1% of samples were collected. These examples highlight the relationship between land use and trash density, allowing researchers to identify patterns in litter accumulation.

**2. How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The sampling stratification and trash density table aids in pinpointing areas with high litter accumulation, which can indicate environmental concerns. By examining the densities across various land uses, stakeholders can identify specific zones that require targeted cleanup efforts or further investigation. For example, areas with high trash density in urban settings may necessitate greater waste management initiatives, while regions with significant litter in natural environments could indicate potential ecological issues.

**3. Under what land use conditions would a surveyor expect to find the most trash?**  
Surveyors can expect to find the most trash in areas where buildings occupy a larger portion of the buffer zone, particularly in the 40-60% range, which has a density of 1.79 pcs/m. Another notable example is the undefined land use category, which has a density of 1.12 pcs/m in the 0-20% buffer zone. These conditions suggest that urbanized areas or those with ambiguous land use may be more prone to litter accumulation.

**4. Given the results in the sampling stratification table, were these surveys collected in mostly urban environments or forested?**  
The surveys were not primarily collected in urban or forested environments, as the sums of proportions do not meet the criteria for either classification. The proportion of samples for buildings in the 60-80% and 80-100% rows is 9.5%, while for forests, it is 0%. Therefore, the surveyed locations remain classified as mixed, with the highest proportion of samples occupying the 0-20% buffer zone for buildings at 31.1%.

## Linear and ensemble regression

Cluster analysis, specifically K-Means clustering, is a method used to group data points into clusters based on their similarities. The algorithm partitions the data into K distinct clusters by minimizing the variance within each cluster and maximizing the variance between clusters. Each cluster is represented by its centroid, which is the average of all points within that cluster. 

The cluster with the highest average pcs/m is cluster 0, which has a value of 1.55 objects per meter of beach. The composition of this cluster includes buildings at 0.14, wetlands at 0, forest at 0.31, public services at 0.19, recreation at 0.01, undefined land use at 0.30, streets at 0.27, vineyards at 0.19, and orchards at 0.

Linear regression is a statistical method for modeling the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data. Basic assumptions of linear regression include linearity, independence, homoscedasticity (constant variance of errors), and normality of errors. Ensemble regression, on the other hand, combines multiple models to improve predictive performance. It relies on the principle that a group of weak learners can come together to form a strong learner. Ensemble methods, such as Bagging and Boosting, also assume that the individual models are independent.

The regression analysis conducted identified the Gradient Boosting Regression model as having the highest R² value of 0.43 and a mean squared error (MSE) of 0.36. Given the best model's R² and MSE, the reliability of predictions can be considered moderate, as the R² value indicates that approximately 43% of the variance in the dependent variable can be explained by the model, while the MSE reflects the average squared difference between the observed and predicted values.

### Frequently asked questions

**What were the r² and MSE of each test?**  
The R² and MSE results for each regression model are as follows:

|    | Model                                |       R² |      MSE |
|---:|:-------------------------------------|---------:|---------:|
|  0 | Linear Regression                    | 0.27     | 0.46     |
|  1 | Random Forest Regression             | 0.25     | 0.47     |
|  2 | Gradient Boosting Regression         | 0.43     | 0.36     |
|  3 | Theil-Sen Regressor                  | 0.36     | 0.41     |
|  4 | Bagging:Gradient Boosting Regression | 0.42     | 0.37     |
|  5 | Voting                               | 0.37     | 0.40     |

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**  
The reliability of predictions based on these models varies. The R² values suggest that none of the models are fully capturing the variance in the data, with the highest being 0.43 from the Gradient Boosting Regression model. The MSE values indicate the average prediction error, with lower values suggesting better performance. Overall, predictions could be considered moderate in reliability, particularly for the Gradient Boosting model.

**Can any conclusions be drawn from these results?**  
Yes, conclusions can be drawn from the results. The Gradient Boosting model performed the best among the tested models, indicating that more complex relationships in the data may be captured effectively with ensemble methods. However, the relatively low R² values across models suggest that there may be other factors influencing the target variable not accounted for in the analysis, indicating potential areas for further investigation.

**According to the cluster analysis, what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**  
The cluster that has the greatest average pcs/m is cluster 0, with a value of 1.55 objects per meter of beach. The distribution of land use values within this cluster is as follows: buildings occupy 14% of the buffer, wetlands occupy 0%, forest occupies 31%, public services occupy 19%, recreation occupies 1%, undefined land use occupies 30%, streets occupy 27%, vineyards occupy 19%, and orchards occupy 0%.

## Forecasts and methods

A grid approximation is a statistical modeling technique that estimates the distribution of potential outcomes based on prior observations and new data. It involves creating a grid of possible values, where each point on the grid represents a threshold for which the probability of a survey result exceeding that value is calculated. This is constructed using an inference table, which organizes the prior and likelihood data, allowing for the application of Bayesian inference to derive the posterior distribution. 

An inference table is a structured representation of data that includes information about prior and likelihood distributions for a specific analysis. In this context, a "prior" refers to the initial belief or estimate about the distribution of a variable based on previous data before observing new data, while a "posterior" is the updated belief after considering the new evidence. In an inference table, the prior provides a baseline for comparison, and the posterior incorporates both the prior information and the likelihood of the observed data, allowing researchers to refine their estimates.

In the report, the prior distributions are defined as follows:

- **In-Boundary Prior**: Average pcs/m = 0.92, Similarity threshold = 0.98
- **Out-Boundary Prior**: Average pcs/m = 0.82, Similarity threshold = 0.98

When comparing the different posterior distributions to the observed results (in pcs/m), we find:

- **In-Boundary Posterior**: Average pcs/m = 0.92 (prior) vs. observed average pcs/m = 0.69, indicating an expected increase of approximately 0.23 pcs/m.
- **Out-Boundary Posterior**: Average pcs/m = 0.82 (prior) vs. observed average pcs/m = 0.69, indicating an expected increase of approximately 0.13 pcs/m.

Given the observed data, it is reasonable to expect an increase in future samples based on the posterior distributions. However, if a person takes only one sample, the likelihood of noticing a significant increase or decrease is less certain due to the inherent variability in the data (as indicated by the standard deviation: 0.89 for the observed results). If two samples are taken, the reliability of detecting a change becomes higher, as averages from multiple samples tend to provide a more accurate reflection of the underlying distribution.

### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**

Grid approximation is a reasonable modeling technique for this data because the observed distribution appears to be skewed. The mean observed pcs/m is 0.69, while the median (50th percentile) is 0.35, indicating a significant difference (0.35), which suggests that the data is not normally distributed. If the data were normally distributed, we would expect the mean and median to be close together. The implications for predictions are that if the data is not normally distributed, grid approximation may provide a more robust estimation by accounting for the skewness and variability in the observed outcomes.

**2. Do you have an example of other fields or domains that use grid approximation or Bayesian methods?**

Grid approximation and Bayesian methods are widely used across various fields, including environmental science for pollution modeling, epidemiology for disease spread predictions, and finance for risk assessment and decision-making under uncertainty.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**

Yes, if the data is normally distributed, the predictions from the grid approximation and those from the normal distribution could be different. The grid approximation provides a non-parametric approach that does not rely on distributional assumptions, while the normal distribution assumes a specific shape (bell curve) for the data. As such, if the data were normally distributed, the predictions from the normal distribution might be more precise and centered around the mean, potentially leading to narrower confidence intervals compared to the broader estimates from the grid approximation.

**4. What is the difference between grid approximation and linear or ensemble regression?**

The primary difference between grid approximation and linear or ensemble regression lies in the modeling approach. Grid approximation uses a probabilistic framework to estimate the distribution of outcomes based on prior and likelihood data, while linear regression predicts outcomes based on a linear relationship between independent and dependent variables. Ensemble regression combines multiple models to improve prediction accuracy, relying on averaging or voting mechanisms. In contrast, grid approximation does not assume a fixed relationship between variables but instead focuses on estimating probabilities over a range of values.

**5. With which posterior do we expect to find most? The least?**

We expect to find most observations with the **in-boundary posterior**, which has a higher average pcs/m of 0.92, compared to the **out-boundary posterior**, which has a lower average pcs/m of 0.82.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**

If the in-boundary grid approximation predicts an increase, it suggests that elevated values were likely observed in other locations within the boundary. Since the prior is based solely on data collected from within the same geographic boundary, this increase indicates that similar trends may persist across the region, thereby reinforcing the likelihood of higher trash density in future surveys.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**

If the out-boundary grid approximation predicts an increase, it suggests that locations outside of the geographic boundary have experienced elevated values compared to the likelihood derived from the specific area being analyzed. This indicates that external factors may be influencing trash density in the broader region, potentially providing insights into littering patterns or waste management practices in those areas.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**

The expected results differ from the observed results as follows: the in-boundary posterior (average pcs/m = 0.92) exceeds the observed average (0.69) by approximately 0.23 pcs/m, while the out-boundary posterior (average pcs/m = 0.82) exceeds the observed average by approximately 0.13 pcs/m. Based on these differences, an increase in trash density should be expected in future observations, particularly in the in-boundary locations.

