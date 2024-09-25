# Vaud canton

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Vaud canton 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting</i>




## Sample results

The report includes data from 14 cities within the canton of Vaud, Switzerland. The cities surveyed are Yverdon-les-Bains, Vevey, Lavey-Morcles, Montreux, Cudrefin, Tolochenaz, La Tour-de-Peilz, Préverenges, Lausanne, Bourg-en-Lavaux, Allaman, Saint-Sulpice (VD), Grandson, and Gland. The survey analyzed 2 lakes (Neuenburgersee and Lac-Leman) and 2 rivers (Rhone and La-Thiele).

The sampling period spanned from April 28, 2020, to May 12, 2021. The survey areas covered are Aare and Rhone. A total of 87 samples were collected, resulting in an average of 1.13 pcs/m, a maximum of 8 pcs/m, and a standard deviation of 1.38. The total number of objects identified during the survey was 3,416.

Regarding material composition, it was found that 100% of the identified objects were made of plastic.

### Frequently asked questions

**What were the five most common items found?**  
The five most common items identified in the report, with their fail rates and percentage of total, are as follows:  
1. Cigarette filters - Fail rate: 91.95% - Percentage of total: 69.26%  
2. Food wrappers (candy, snacks) - Fail rate: 95.40% - Percentage of total: 30.74%  

**Are these objects found on European beaches? If so is there any data on how many per 100 m of beach?**  
Yes, these objects are commonly found on European beaches. For example, results from the OSPAR survey indicated that items such as cigarette butts and food wrappers are prevalent, with cigarette butts often reported at rates exceeding 1000 per 100 meters of beach.

**What are the possible sources of these specific objects?**  
Possible sources of these objects include littering by beachgoers, improper disposal of waste, and the prevalence of single-use plastics in consumer goods. Cigarette filters often come from smokers who discard them on the ground or at beaches, while food wrappers typically result from the consumption of snacks and other food items in public spaces.

**Which three cities had the highest average pcs/m? Which three had the lowest?**  
The three cities with the highest average pcs/m are:  
1. Lausanne - 2.73 pcs/m  
2. Vevey - 2.03 pcs/m  
3. Préverenges - 1.42 pcs/m  

The three cities with the lowest average pcs/m are:  
1. Lavey-Morcles - 0.07 pcs/m  
2. Cudrefin - 0.08 pcs/m  
3. Bourg-en-Lavaux - 0.42 pcs/m  

## Sampling stratification

Sampling stratification is a method used to ensure that the samples collected in a survey represent the different conditions present in the study area. It involves dividing the area into distinct segments based on specific characteristics, such as land use, and then collecting samples from each segment in a way that reflects their proportion in the overall area. In this survey, sampling stratification helps to quantify the different types of land use surrounding each survey location, which is critical for analyzing the density of trash found in various environments. Land use refers to how land is utilized and can include features such as residential, commercial, industrial, agricultural, and natural environments. 

To determine whether the land use in this report is considered rural, urban, or mixed, we analyze the proportions of samples collected. For this report, the sum of the proportions of samples for buildings in the 60-80% and 80-100% rows is 36.8% + 46.0% = 82.8%. Since this value exceeds 50%, the area is classified as urban. Additionally, the sum of the proportions of samples for forests in the same rows is 0% (no samples), indicating that the area does not meet rural criteria. 

The two highest pieces of trash per meter (pcs/m) values in the sampling stratification and trash density table for the relevant land uses (buildings, forest, undefined, and streets) are 1.76 pcs/m for streets at 80-100% buffer and 1.52 pcs/m for buildings at 80-100% buffer. The land-use features and the proportion of buffer they occupy are as follows: 

- Buildings occupy 80-100% with 46.0% of the samples taken.
- Streets occupy 80-100% with 12.6% of the samples taken.

### Frequently asked questions

**What does the sampling stratification table tell us?**  
The sampling stratification table provides insights into the distribution of trash density across various land use types and their corresponding buffer zones. For instance, buildings in the 0-20% buffer zone show an average trash density of 0.53 pcs/m, with 6.9% of samples collected from this area. In contrast, the 80-100% buffer zone for buildings has a much higher density of 1.52 pcs/m, with 46.0% of samples taken. The undefined category shows a density of 1.26 pcs/m with 82.8% of samples in the 0-20% buffer zone. These examples illustrate how different land use distributions correlate with varying levels of trash density.

**How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The information in the sampling stratification and trash density table can help identify areas of concern by highlighting which land use types are associated with higher trash densities. For example, areas where buildings occupy a greater proportion of the buffer zone tend to have higher pieces of trash per meter, such as the 1.52 pcs/m found in the 80-100% buffer zone for buildings. By recognizing these correlations, policymakers and environmental organizations can target efforts to reduce litter and improve waste management in specific high-density areas.

**Under what land use conditions would a surveyor expect to find the most trash?**  
A surveyor would expect to find the most trash in areas where buildings occupy a high proportion of the buffer zone. For instance, in the 80-100% range, the average pieces of trash per meter is 1.52 for buildings, and in the 60-80% range, it is 0.95. This indicates that as the proportion of buildings increases, the density of trash also increases, suggesting that urban environments are likely to have higher litter levels.

**Given the results in the sampling stratification table, were these surveys collected in mostly urban environments or forested?**  
These surveys were conducted in mostly urban environments, as the sum of the proportions of samples for buildings in the 60-80% and 80-100% rows exceeds 50%. Specifically, 36.8% of samples come from the 60-80% buffer and 46.0% from the 80-100% buffer for buildings, totaling 82.8%. In contrast, the proportion of samples for forests does not meet the criteria for rural classification, as it is 0% for both rows. Thus, the area has a greater proportion of samples from buildings, indicating an urban classification.

## Linear and ensemble methods

Cluster analysis (K-Means) is a method used to partition a dataset into distinct groups (clusters) based on the similarity of data points. Each cluster is characterized by its centroid, and data points are assigned to the nearest centroid. In the provided report, Cluster 4 had the highest average pcs/m with a value of 2.14. The composition of Cluster 4 included buildings at 0.95, forest at 0.04, and undefined land use at 0.01.

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data. Ensemble regression, on the other hand, combines multiple regression models to improve prediction accuracy and robustness. The basic assumptions of linear regression include linearity, independence, homoscedasticity (constant variance), and normality of errors. For ensemble regression, the assumptions are similar, but it also assumes that combining models will yield a better prediction than any individual model.

In the regression analysis conducted, the model with the highest R² value was the Gradient Boosting Regression, which had an R² of 0.05. The mean squared error (MSE) of this model was 0.60. Given that this was the best model, it suggests that while the model explains some variation in the data, the predictive power is limited, as indicated by the low R² value. Therefore, predictions based on this model may not be highly reliable due to the poor fit to the data.

### Frequently asked questions

**What were the r² and MSE of each test?**  
The R² and MSE results for each regression model are as follows:  
- Linear Regression: R² = -0.09, MSE = 0.69  
- Random Forest Regression: R² = -0.56, MSE = 0.99  
- Gradient Boosting Regression: R² = 0.05, MSE = 0.60  
- Theil-Sen Regressor: R² = -0.01, MSE = 0.64  
- Bagging: Gradient Boosting Regression: R² = -0.03, MSE = 0.65  
- Voting: R² = -0.05, MSE = 0.67  

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**  
The predictions based on these models would likely be unreliable due to the negative R² values observed in several models, indicating that they do not effectively explain the variability in the data. The best model, Gradient Boosting Regression, has a low R² of 0.05, suggesting that it explains only a small fraction of the variance, further indicating limited reliability.

**Can any conclusions be drawn from these results?**  
Conclusions from these results suggest that the regression models employed did not perform well in explaining the data, as evidenced by the low R² values and high MSE values. This indicates a need for further investigation into the factors influencing the observed outcomes or the potential exploration of alternative modeling approaches.

**According to the cluster analysis, what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**  
The cluster with the greatest average pcs/m is Cluster 4, which has an average of 2.14 objects per meter of beach. The distribution of land use values within Cluster 4 is as follows: buildings occupy 94.5% of the buffer zone, forest occupies 4.1%, and undefined land use occupies 1.4%.

## Forecasts and methods

A grid approximation is a numerical technique used to estimate the distribution of a parameter, such as litter density, based on observed data and specific conditions. In this report, the method involves several steps: discretizing the parameter space into a grid, evaluating a statistical function at each point, normalizing the results to create a probability distribution, and ultimately inferring the posterior distribution given the prior data. In Bayesian statistics, a prior distribution represents the initial assumptions about a parameter before observing any data, while the posterior distribution is the updated belief about that parameter after incorporating the observed data.

In this report, three priors are employed: 

1. **Combined prior**: Similarity threshold of 0.76.
2. **In boundary prior**: Similarity threshold of 0.43.
3. **Out boundary prior**: Similarity threshold of 0.76.

The key differences between the priors lie in their geographic focus—combined prior includes data from both inside and outside the boundary, while the in-boundary prior focuses solely on data from within the boundary, and the out-boundary prior includes data exclusively from outside the boundary.

Comparatively, the expected posterior distributions indicate the following average pcs/m values:
- **Combined prior**: Mean = 0.80, Median = 0.47
- **In boundary prior**: Mean = 0.70, Median = 0.44
- **Out boundary prior**: Mean = 0.61, Median = 0.28
- **Observed average pcs/m**: 1.13, Median = 0.67

The observed average (1.13 pcs/m) is higher than the means of all three priors, suggesting that a decrease in litter density is expected when comparing the posterior averages to the observed values. With a standard deviation in the observed data of 1.38 pcs/m, a person would likely notice an increase or decrease based on sampling due to the relatively large standard deviation compared to the differences in mean values.

### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**  
Grid approximation is reasonable in this context because the observed data does not seem to be normally distributed, as indicated by the difference between the mean (1.13) and median (0.67) in the summary statistics. The mean is significantly higher than the median, suggesting a right-skewed distribution. If the data were normally distributed, predictions would follow a bell curve, but due to the skewness in this case, the grid approximation provides a more accurate representation of the parameter distribution.

**2. Do you have an example of other fields or domains that use a grid approximation or Bayesian methods?**  
Yes, grid approximation and Bayesian methods are used in various fields, including environmental science for pollution modeling, epidemiology for disease spread predictions, and finance for risk assessment and portfolio management.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**  
Yes, if the data were normally distributed, predictions from the grid approximation might align more closely with the normal distribution predictions, which would typically center around the mean. However, the grid approximation would still provide estimates across a discrete parameter space, while normal distribution predictions would yield a continuous curve, potentially leading to different estimates in terms of probability density.

**4. What is the difference between grid approximation and linear or ensemble regression?**  
Grid approximation focuses on estimating the distribution of parameters using prior knowledge and observed data, while linear regression predicts a dependent variable based on one or more independent variables using a linear relationship. Ensemble regression combines multiple predictive models to improve accuracy, whereas grid approximation provides a probabilistic framework rather than a single predictive output.

**5. With which posterior do we expect to find most? The least?**  
The **in-boundary prior** is expected to yield the most findings, with an average of 0.70 pcs/m, while the **out-boundary prior** is expected to yield the least, with an average of 0.61 pcs/m.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**  
If the in-boundary prior predicts an increase, it suggests that elevated values were likely observed in other locations within the same geographic boundary compared to the likelihood, indicating a potential issue with litter density in those areas.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**  
If the out-boundary prior predicts an increase, it implies that locations outside the geographic boundary had elevated litter densities compared to the likelihood, indicating that litter management may be less effective or that external factors are contributing to higher litter levels outside the boundary.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**  
The expected results differ from the observed results, with the observed average pcs/m at 1.13 being higher than all three expected averages. A decrease in litter density should be expected based on the comparisons to the posterior means. The numerical differences between the observed average and each posterior mean are as follows:  
- Combined prior: 1.13 - 0.80 = 0.33  
- In-boundary prior: 1.13 - 0.70 = 0.43  
- Out-boundary prior: 1.13 - 0.61 = 0.52  

Given the standard deviation of 1.38 pcs/m, it is likely that individuals would notice these differences upon sampling, as they exceed the variability expected in typical observations.

