# Vaud canton

**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobacco and micro plastics (< 5mm) found in lakes and rivers. <i>Report number: Vaud canton 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting</i>




## Sample results

The report encompasses observations made across 14 cities within the Vaud canton, specifically focusing on the survey areas of Rhone and Aare. The sampling period ranged from April 28, 2020, to May 12, 2021. A total of 87 samples were collected, resulting in the identification of 17,414 objects, with an average density of 6.42 objects per meter (pcs/m) and a maximum density recorded at 66.17 pcs/m. The standard deviation of the results was approximately 9.31.

In terms of geographical features, the survey identified 2 rivers (La Thiele and Rhone) and 2 lakes (Lac Leman and Neuenburgersee). 

The material composition of the identified objects revealed that plastic constituted 89% of the total, followed by glass at 4%, metal at 2%, and paper at 1%.

### Frequently asked questions

**1. What were the five most common items found?**

The five most common items identified in the report were:
1. Fragmented plastics: Fail rate of 95.4% (0.15% of total)
2. Cigarette filters: Fail rate of 91.9% (0.14% of total)
3. Expanded polystyrene: Fail rate of 82.8% (0.12% of total)
4. Food wrappers (candy, snacks): Fail rate of 95.4% (0.06% of total)
5. Industrial pellets (nurdles): Fail rate of 43.7% (0.05% of total)

The fail rate indicates the proportion of samples in which at least one of the specified objects was found.

**2. Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**

Yes, many of these objects are commonly found on European beaches. For instance, data from the OSPAR (Oslo and Paris Conventions) monitoring program indicates that cigarette butts, plastic packaging, and other similar debris are frequently recorded, with typical counts often exceeding 20 items per 100 meters of beach.

**3. What are possible sources of these specific objects?**

Possible sources of the identified objects include littering by beachgoers, improper waste disposal, and runoff from urban areas. For instance, cigarette filters may result from smoking on beaches, while fragmented plastics and food wrappers often originate from picnics and food consumption in public spaces, as well as from industrial activities.

**4. Which three cities had the highest average pcs/m? Which three had the lowest?**

The three cities with the highest average pcs/m were:
1. Lausanne: 19.41 pcs/m
2. Saint-Sulpice (VD): 18.43 pcs/m
3. Vevey: 6.39 pcs/m

Conversely, the three cities with the lowest average pcs/m were:
1. Cudrefin: 2.23 pcs/m
2. Gland: 1.43 pcs/m
3. Grandson: 1.41 pcs/m

## Sampling stratification

Sampling stratification refers to the process of dividing a population into distinct subgroups, or strata, for the purpose of sampling. In this survey, sampling stratification was applied to assess the distribution of various land-use features within a buffer zone surrounding each survey location, allowing for a more nuanced understanding of how different environments may influence trash density. Land use encompasses the various ways in which land is utilized within a specific area, such as residential, commercial, agricultural, or recreational purposes. 

In this report, to determine if the land-use is urban, the proportions of samples for buildings in the rows corresponding to 60-80% and 80-100% are summed. If this sum exceeds 50%, the area is classified as urban. Conversely, to assess if the area is rural, the proportions of samples for forests in the same rows are summed; if that sum exceeds 50%, the area is classified as rural. If neither condition is met, the area is classified as mixed. The analysis indicates that the sum of the proportions where buildings occupy greater than 60% of the buffer is 36.80% (60-80%) and 46.00% (80-100%), totaling 82.80%, which classifies the area as urban. The highest pieces of trash per meter (pcs/m) values from the relevant columns in the sampling stratification and trash density table are 9.31 pcs/m for buildings (80-100% buffer) and 6.99 pcs/m for undefined land use (0-20% buffer). 

The land use features and their corresponding proportions of the buffer they occupy include buildings, wetlands, forests, public services, recreation, undefined areas, streets, vineyards, and orchards, with varying percentages as detailed in the provided data.

### Frequently asked questions

**What does the sampling stratification table tell us?**  
The sampling stratification table provides insights into the distribution of trash density in relation to different land-use features across various proportions of buffer zones. For example, when examining the buildings column, we find that in areas where buildings occupy 0-20% of the buffer, the average trash density is 4.85 pcs/m. In contrast, in areas where buildings occupy 80-100% of the buffer, the trash density significantly increases to 9.31 pcs/m. Similarly, in the undefined column, the average trash density in the 0-20% buffer zone is 6.99 pcs/m, indicating a moderate presence of trash. These examples illustrate how different land-use distributions correspond with varying levels of trash density, reflecting the impact of urbanization on litter accumulation.

**How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The information in the sampling stratification and trash density table is instrumental in identifying areas of concern regarding litter accumulation. By analyzing the average pieces of trash per meter (pcs/m) in different land-use categories, stakeholders can pinpoint locations where trash density is particularly high. For instance, the data reveals that in areas where buildings occupy 80-100% of the buffer, there is a notably high trash density of 9.31 pcs/m. Such findings can inform local authorities and environmental organizations where to focus cleanup efforts and develop strategies for reducing litter, thereby improving environmental health and community aesthetics.

**Under what land-use conditions would a surveyor expect to find the most trash?**  
A surveyor would expect to find the most trash in areas where buildings occupy a high proportion of the buffer. For instance, the average pieces of trash per meter for buildings in the 80-100% buffer zone is 9.31 pcs/m, which is significantly higher compared to other land-use categories. Additionally, streets also show a high density of trash, particularly in the 60-80% buffer zone where the density reaches 24.73 pcs/m, indicating that areas with considerable infrastructure and human activity are likely to accumulate more litter.

**Given the results in the sampling stratification table, were these surveys collected in mostly urban environment or forested?**  
Based on the definitions provided, the surveys were collected predominantly in an urban environment, as the total proportion where buildings occupy more than 60% of the buffer exceeds 50%, totaling 82.80%. In contrast, the sum for forests in the same rows is 0%, indicating no significant forested areas were assessed in this study. The greatest proportion of samples taken corresponds to buildings (46.00% in the 80-100% column), confirming the urban classification.

## Linear and ensemble methods

**Define cluster analysis (kmeans) what cluster had the highest pcs/m and what was the composition of buildings, forest, undefined?**  
Cluster analysis, specifically K-Means clustering, is a method used to categorize data points into groups based on their features, ensuring that the points in the same group are more similar to each other than to those in other groups. From the cluster analysis conducted, cluster 4 had the highest average density of objects, with 19.00 pcs/m. The composition of land use in cluster 4 was as follows: buildings occupied 0.95 (or 95%), forest occupied 0.04 (or 4%), and undefined land use occupied 0.01 (or 1%).

**Define linear regression and ensemble regression, explain the basic assumptions of each method.**  
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data. The basic assumptions include linearity, independence, homoscedasticity (equal variance of errors), and normality of error terms. Ensemble regression combines multiple models to improve predictive performance, often through methods like bagging and boosting. Similar assumptions apply, with additional considerations for the diversity of the combined models.

**If a regression analysis was conducted, what model had the highest r² (the best model)? What was the mse of the best model?**  
The model with the highest R² value was the Bagging: Theil-Sen Regressor, which had an R² of 0.50 and a Mean Squared Error (MSE) of 0.10.

**If a regression analysis was conducted, what conclusions can be drawn given the best model?**  
Given that the Bagging: Theil-Sen Regressor had the highest R², it indicates that this model explains approximately 50% of the variance in the data. This suggests a moderate level of predictive power, but further analysis would be required to fully understand the model's performance and applicability.

**Given the r² and MSE of the best model how reliable would predictions be?**  
The R² value of 0.50 suggests that the predictions from the model could be moderately reliable, but the relatively high MSE of 0.10 indicates that there may still be considerable error in the predictions. Thus, while the model provides some level of insight, caution should be exercised in relying solely on its predictions.

### Frequently asked questions

**What were the r² and MSE of each test?**  
The following are the results from different regression analyses regarding R² and MSE:

|    | Model                        |    R² |   MSE |
|---:|:-----------------------------|------:|------:|
|  0 | Linear Regression            | -1.05 | 0.42  |
|  1 | Random Forest Regression     | -2.69 | 0.76  |
|  2 | Gradient Boosting Regression |  0.42 | 0.12  |
|  3 | Theil-Sen Regressor          |  0.50 | 0.10  |
|  4 | Bagging: Theil-Sen Regressor |  0.50 | 0.10  |
|  5 | Voting                       | -0.43 | 0.29  |

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**  
The reliability of predictions varies across the different regression models based on their R² and MSE values. The models with negative R² values, such as Linear Regression and Random Forest Regression, indicate poor predictive capabilities. However, the Bagging: Theil-Sen Regressor and Theil-Sen Regressor show some level of reliability, with R² values around 0.50 and relatively low MSE, suggesting moderate predictive reliability for these models.

**Can any conclusions be drawn from these results?**  
Yes, several conclusions can be drawn. The models with negative R² values are ineffective for predicting the target variable, while the Bagging: Theil-Sen Regressor and Theil-Sen Regressor demonstrated better performance. This indicates the potential for using ensemble methods to improve predictive accuracy over simpler models.

**According to the cluster analysis, what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**  
The cluster with the greatest average pcs/m is cluster 4, which has an average density of 19.00 pcs/m. The distribution of land use values within cluster 4 is as follows: buildings occupy 95% of the buffer zone, forest occupies 4%, and undefined land use occupies 1%.

## Forecasts and methods

Grid approximation is a numerical technique used to estimate the distribution of a parameter, such as litter density, by utilizing conditional probability. The method applied in this report leverages land use features to create an inference table that allows for the estimation of posterior distributions based on prior knowledge. An inference table is a systematic way to apply Bayes' theorem, where the prior distribution reflects the initial beliefs about the parameter before observing data, and the posterior distribution represents the updated beliefs after incorporating the observed data.

In this report, three priors were utilized: the **Combined prior**, the **In-boundary prior**, and the **Out-boundary prior**. The similarity thresholds are as follows: 
- **Combined prior**: 0.76
- **In-boundary prior**: 0.43
- **Out-boundary prior**: 0.76

The differences among these priors lie in their geographical considerations. The **Combined prior** considers samples from both inside and outside the boundary, while the **In-boundary prior** is limited to samples only within the specified boundary, and the **Out-boundary prior** includes samples only from outside the boundary.

Comparing the posterior distributions to the observed results, the average pcs/m for the observed data is 6.42. The averages for each prior are:
- **Combined prior**: 2.40
- **In-boundary prior**: 2.38
- **Out-boundary prior**: 2.39

There is a notable decrease in the average pcs/m when comparing the observed results to the posterior averages. The differences are as follows:
- Combined prior: 6.42 - 2.40 = 4.02
- In-boundary prior: 6.42 - 2.38 = 4.04
- Out-boundary prior: 6.42 - 2.39 = 4.03

Given the standard deviations (9.31 for the observed data, 2.65 for the combined prior, 2.12 for the in-boundary prior, and 3.29 for the out-boundary prior), an individual sampling would likely notice the variations in the observed results compared to the average of the posterior distributions due to the substantial differences in averages relative to the standard deviations.

### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**  
Grid approximation is suitable for this data as it allows for the estimation of parameter distributions, particularly in contexts where the observed data may not be normally distributed. The observed data indicates a mean of 6.42 and a median (50th percentile) of 3.62. The difference between the mean and median suggests a right-skewed distribution, indicating that the data is likely not normally distributed. If the data were normally distributed, predictions would assume symmetry around the mean, which is not the case given the observed skewness. This skewness implies that extreme values could disproportionately influence the estimates, thus necessitating a more nuanced approach such as grid approximation.

**2. Do you have an example of other fields or domains that use grid approximation or Bayesian methods?**  
Yes, grid approximation and Bayesian methods are commonly used in various fields, including epidemiology for disease mapping, environmental science for pollution distribution modeling, and finance for risk assessment and stock price predictions.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**  
Yes, if the data were normally distributed, predictions from a grid approximation could differ from those derived from a normal distribution in terms of the shape of the distribution and the expected values. A normal distribution would yield a symmetric bell curve, while the grid approximation would accommodate skewness and kurtosis, reflecting the actual data distribution more accurately.

**4. What is the difference between grid approximation and linear or ensemble regression?**  
Grid approximation focuses on estimating the distribution of a parameter based on prior information and observed data, while linear and ensemble regression techniques are primarily predictive modeling tools that establish relationships between dependent and independent variables. Regression models typically assume a specific form of the relationship, while grid approximation is more flexible and non-parametric in nature.

**5. With which posterior do we expect to find the most? The least?**  
We expect to find the most with the **Combined prior** average (2.40 pcs/m) and the least with the **In-boundary prior** average (2.38 pcs/m).

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**  
If the in-boundary grid approximation predicts an increase, it suggests that elevated values were likely observed at other locations within the boundary, indicating that the conditions influencing litter density are consistent across sampled locations.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**  
If the out-boundary grid approximation predicts an increase, it indicates that locations outside the region likely had elevated litter density values compared to the likelihood, reflecting that similar external conditions may be affecting waste accumulation.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**  
The expected results from the posterior distributions show a decrease compared to the observed average of 6.42. The averages for the combined, in-boundary, and out-boundary priors are all significantly lower (ranging from approximately 2.38 to 2.40). Given the standard deviations, a person sampling from the posterior distributions would likely notice a decrease, as the averages are well below the observed mean. The numerical differences highlight a substantial reduction in expected litter density based on the priors utilized.

