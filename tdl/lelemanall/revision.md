
# Le Léman

**Summary and analysis of observations of trash density**: objects related to recreation, personal items, unclassified, infrastructure, food and drink, packaging non food, plastic pieces, waste water, agriculture, tobacco and micro plastics (< 5mm) found in lakes. <i>Report number: Le Léman None lake 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting</i>




## Sample results

The report includes data from 13 cities: La Tour-de-Peilz, Genève, Montreux, Tolochenaz, Bourg-en-Lavaux, Saint-Gingolph, Allaman, Gland, Saint-Sulpice (VD), Préverenges, Vevey, Versoix, and Lausanne. There is one lake, named Lac-Leman, included in the report. The sampling period extended from April 28, 2020, to May 12, 2021, within the survey area of Rhone.

A total of 98 samples were collected, yielding an average of 8.66 pcs/m (objects per meter) with a maximum of 66.17 pcs/m. The standard deviation was 11.61, and a total of 27,447 objects were identified during the survey. The material composition revealed that 90% of the identified objects were plastic, followed by glass at 3%, metal at 2%, and paper at 1%.

### Frequently asked questions

**What were the five most common items found?**  
The five most common items found were:  
1. Fragmented plastics - fail rate 96.94% (15.35% of total)  
2. Expanded polystyrene - fail rate 83.67% (13.07% of total)  
3. Cigarette filters - fail rate 94.90% (11.35% of total)  
4. Food wrappers (candy, snacks) - fail rate 95.92% (6.12% of total)  
5. Plastic caps, lid rings - fail rate 88.78% (4.42% of total)  

The fail rate indicates the proportion of samples where at least one of the objects was found.

**Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**  
Yes, many of these objects are commonly found on European beaches. According to OSPAR results from 2022, an average of approximately 600 items of litter were recorded per 100 meters of beach.

**What are possible sources of these specific objects?**  
Possible sources of these specific objects include recreational activities (such as picnicking and smoking), general consumer use (plastic packaging, food wrappers), and waste management issues (single-use plastics not being disposed of properly).

**Which three cities had the highest average pcs/m? Which three had the lowest?**  
The three cities with the highest average pcs/m were:  
1. Saint-Gingolph - 23.64 pcs/m  
2. Saint-Sulpice (VD) - 18.43 pcs/m  
3. Lausanne - 19.41 pcs/m  

The three cities with the lowest average pcs/m were:  
1. Gland - 1.43 pcs/m  
2. Genève - 3.30 pcs/m  
3. Tolochenaz - 3.56 pcs/m

## Sampling stratification

Sampling stratification refers to the process of dividing a population into subgroups or strata to ensure that different segments of the population are adequately represented in the sample. In this survey, sampling stratification was applied to assess the density of trash in relation to various land-use features surrounding the survey locations, which are defined by a buffer zone of 1,500 meters. The land-use categories include buildings, wetlands, forest, public services, recreation, undefined, streets, vineyards, and orchards. Each category occupies a different proportion of the buffer zone, which allows for an analysis of how trash density varies based on the land-use features present.

Land use pertains to the various ways in which land is utilized, as represented in the survey report. The categories listed in the sampling stratification table indicate the different land uses surrounding the survey locations, which are crucial for understanding the environmental context of the survey results. 

In terms of sample proportions, the survey reveals that buildings occupied more than 60% of the buffer zone in 79.6% of the samples, which is derived from the sum of the proportions for the rows 60-80% and 80-100% in the buildings column (19.4% + 60.2%). Conversely, forest occupied more than 60% of the buffer zone in no samples, as indicated by the absence of values in the relevant rows for the forest column. This suggests that the area surveyed cannot be classified as rural because no significant proportion of the buffer zone was occupied by forests.

The two highest pieces of trash per meter (pcs/m) values in the sampling stratification and trash density table are found in the buildings category (19.42 pcs/m when buildings occupy 20-40% of the buffer) and in the streets category (21.01 pcs/m when streets occupy 60-80% of the buffer). These values reflect the density of trash present in relation to the specific land use and the proportion of the buffer zone they occupy.

### Frequently asked questions

**What does the sampling stratification table tell us?**  
The sampling stratification table provides insights into the relationship between the density of trash and the different land-use features surrounding the survey locations. For example, in areas where buildings occupy 20-40% of the buffer, the average density of trash was 19.42 pcs/m, indicating a significant presence of litter. In contrast, areas where streets occupy 60-80% of the buffer showed a higher density at 21.01 pcs/m. These values highlight the impact of specific land-use features on trash density.

**How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The information in the sampling stratification and trash density table can help identify areas of concern by revealing which land-use features correlate with higher trash density. For instance, high densities of trash in urban areas, particularly where buildings or streets dominate, may indicate inadequate waste management practices or higher recreational use leading to littering. Identifying these areas can facilitate targeted cleanup efforts and inform local policies aimed at reducing litter.

**Under what land-use conditions would a surveyor expect to find the most trash?**  
A surveyor would expect to find the most trash in areas where buildings and streets occupy a significant proportion of the buffer zone. For example, in locations where buildings occupy 20-40% of the buffer, the average density is 19.42 pcs/m. Additionally, in areas where streets occupy 60-80% of the buffer, the density is even higher at 21.01 pcs/m. These conditions suggest that urbanized areas with limited green space may contribute to greater litter accumulation.

**Given the results in the sampling stratification table, were these surveys collected in mostly urban environments or forested?**  
The surveys do not meet the criteria for being classified as predominantly urban or rural. The proportion of samples where buildings occupied greater than 60% of the buffer is 79.6%, while the proportion of samples where forest occupied greater than 60% of the buffer is 0%. The highest proportion of samples is associated with buildings, indicating that the area is predominantly urban with limited forested land.

## Linear and ensemble methods

Cluster analysis (k-means) divides a dataset into distinct groups (clusters) based on feature similarity. K-means clustering aims to minimize the variance within each cluster. Linear regression is a method to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data. Ensemble regression combines multiple models to improve prediction accuracy, including techniques like Random Forest, Gradient Boosting, Bagging, and Voting.

The basic assumptions of linear regression include linearity, independence, homoscedasticity, and normality of residuals. Ensemble regression methods assume that combining multiple models can reduce variance and improve predictive performance, making fewer assumptions about the underlying data distribution.

The model with the highest r² was Bagging: Linear Regression with an r² of 0.26 and an MSE of 1.55. Given this model, conclusions indicate that while some predictive power exists, the relatively low r² suggests only a modest proportion of the variance in the target variable is explained by the model. Predictions would be moderately reliable but not highly accurate.

If the regression analysis is considered reliable, the features with the greatest influence on the target variable, based on feature importance, include forest (coefficient 1.48), buildings (coefficient 1.31), and public services (coefficient 0.35).

### Frequently asked questions

**What were the r² and MSE of each test?**

The r² and MSE values for each model were as follows:

| Model                        |    R² |   MSE |
|------------------------------|-------|-------|
| Linear Regression            |  0.24 |  1.60 |
| Random Forest Regression     |  0.19 |  1.69 |
| Gradient Boosting Regression |  0.09 |  1.90 |
| Theil-Sen Regressor          |  0.13 |  1.82 |
| Bagging: Linear Regression   |  0.26 |  1.55 |
| Voting                       |  0.19 |  1.71 |

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**

The predictions based on these models would be moderately reliable. The highest r² of 0.26 suggests that the model explains only a modest portion of the variance in the target variable. The MSE values indicate a degree of error in predictions, with the best model (Bagging: Linear Regression) having an MSE of 1.55.

**Can any conclusions be drawn from these results?**

Conclusions that can be drawn are that the Bagging: Linear Regression model provides the best fit among the tested models, explaining approximately 25.9% of the variance in the target variable. However, the model's predictive power is modest, indicating that other unobserved factors might be influencing the target variable.

**According to the cluster analysis, what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**

Cluster 3 has the greatest average pcs/m, with a value of 20.22 objects per meter of the beach. The distribution of land use values within Cluster 3 is:
- Buildings: 26.8%
- Wetlands: 0%
- Forest: 50.4%
- Public Services: 1.2%
- Recreation: 3.1%
- Undefined: 22.8%
- Streets: 1.06%
- Vineyards: 0%
- Orchards: 0%

## Forecasts and methods

Grid approximation is a numerical technique used to estimate the distribution of a parameter, such as litter density, based on previously observed data under similar conditions. The method in this report employs conditional probability to evaluate what can be expected given prior observations, utilizing land use features and buffer zone proportions. The grid approximation involves discretizing the parameter space, evaluating the statistical function at grid points, and normalizing the results to create a valid probability distribution. In Bayesian statistics, a prior distribution represents the initial beliefs about a parameter before observing data, while the posterior distribution reflects updated beliefs after incorporating the likelihood of the observed data.

In this report, three priors were used:

1. **Combined prior grid approximation**: Similarity threshold 0.77
2. **In-boundary grid approximation**: Similarity threshold not explicitly stated, but limited to samples within the boundary.
3. **Out-boundary grid approximation**: Similarity threshold 0.74

The differences between the priors lie in the geographic boundaries from which the samples are drawn. The combined prior considers samples from both inside and outside the boundary, while the in-boundary prior only considers samples within the specified geographic area, and the out-boundary prior includes only samples from outside the geographic area.

Comparing the different posterior distributions to the observed results:

- Observed average pcs/m: 8.66
- Combined prior average pcs/m: 3.06
- In-boundary prior average pcs/m: 2.93
- Out-boundary prior average pcs/m: 2.23

All posterior averages are lower than the observed average, indicating a decrease is expected. Given the standard deviation of the observed data (11.61 pcs/m), a person taking one sample would likely notice a difference since the observed average is significantly higher than any of the posterior averages.

### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**  
The observed data, with a mean of 8.66 pcs/m and a median of 4.51 pcs/m, suggests a right-skewed distribution, as the mean is greater than the median. This indicates that the data may not be normally distributed. If the data were normally distributed, predictions would be more reliable and centered around the mean, but the skew suggests that the presence of outliers may influence the predictions. 

**2. Do you have an example of other fields or domains that use a grid approximation or Bayesian methods?**  
Grid approximation and Bayesian methods are commonly used in fields such as ecology for species distribution modeling, finance for risk assessment, and machine learning for probabilistic modeling.

**3. If the data is normally distributed would the predictions from the grid approximation and the predictions from the normal distribution be different? If so in what way?**  
Yes, if the data is normally distributed, predictions from a grid approximation may yield different estimates compared to predictions based on normal distribution assumptions, particularly in terms of confidence intervals and the behavior of the tails of the distribution.

**4. What is the difference between grid approximation and linear or ensemble regression?**  
Grid approximation is a Bayesian method focused on estimating probability distributions, while linear and ensemble regression are primarily focused on predicting outcomes based on independent variables. Grid approximation considers prior beliefs and evidence, while regression typically assumes a linear relationship between variables.

**5. With which posterior do we expect to find most? The least?**  
The most expected posterior is the combined prior grid approximation with an average of 3.06 pcs/m. The least expected is the out-boundary grid approximation, which has an average of 2.23 pcs/m.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**  
If the in-boundary prior predicts an increase, it suggests that elevated values were likely observed in other locations within the boundary compared to the likelihood samples.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**  
If the out-boundary prior predicts an increase, it indicates that locations outside the region likely had elevated values compared to the likelihood samples.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**  
The expected average results from the posterior distributions are all lower than the observed average of 8.66 pcs/m. The differences are:

- Combined prior: -5.60 pcs/m
- In-boundary prior: -5.73 pcs/m
- Out-boundary prior: -6.44 pcs/m

Given the standard deviation of 11.61 pcs/m, a person taking one sample is likely to notice the decrease as the differences are substantial compared to the variability in the observed data.

