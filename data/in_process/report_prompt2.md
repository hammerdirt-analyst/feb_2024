## Cluster Analysis and regression


## Correlation Spearmans $ho$

method : [pandas df.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)

The following are the correlation of pcs/m and feature variables done on the two object groups. Spearmans Rho is the correlation method
Note that the values for the number of samples and the feature values are the same in both tables. we are interested in the differences
between the pcs/m column and the cluster number in the two tables. 

### Results
#### Profesional

|                 |   pcs/m |   public-services |   buildings |   forest |   undefined |   vineyards |   streets |   recreation |
|:----------------|--------:|------------------:|------------:|---------:|------------:|------------:|----------:|-------------:|
| pcs/m           |    1    |              0.66 |        0.31 |    -0.08 |        0.05 |        0.47 |      0.6  |         0.45 |
| public-services |    0.66 |              1    |        0.48 |    -0.32 |       -0.11 |        0.82 |      0.68 |         0.29 |
| buildings       |    0.31 |              0.48 |        1    |    -0.28 |       -0.48 |        0.1  |      0.75 |         0.11 |
| forest          |   -0.08 |             -0.32 |       -0.28 |     1    |       -0.5  |       -0.52 |      0.03 |         0.14 |
| undefined       |    0.05 |             -0.11 |       -0.48 |    -0.5  |        1    |        0.33 |     -0.55 |         0.12 |
| vineyards       |    0.47 |              0.82 |        0.1  |    -0.52 |        0.33 |        1    |      0.24 |         0.1  |
| streets         |    0.6  |              0.68 |        0.75 |     0.03 |       -0.55 |        0.24 |      1    |         0.21 |
| recreation      |    0.45 |              0.29 |        0.11 |     0.14 |        0.12 |        0.1  |      0.21 |         1    |


#### Recreation

|                 |   pcs/m |   public-services |   buildings |   forest |   undefined |   vineyards |   streets |   recreation |
|:----------------|--------:|------------------:|------------:|---------:|------------:|------------:|----------:|-------------:|
| pcs/m           |    1    |              0.43 |        0.31 |     0.22 |       -0.19 |        0.19 |      0.56 |         0.47 |
| public-services |    0.43 |              1    |        0.48 |    -0.32 |       -0.11 |        0.82 |      0.68 |         0.29 |
| buildings       |    0.31 |              0.48 |        1    |    -0.28 |       -0.48 |        0.1  |      0.75 |         0.11 |
| forest          |    0.22 |             -0.32 |       -0.28 |     1    |       -0.5  |       -0.52 |      0.03 |         0.14 |
| undefined       |   -0.19 |             -0.11 |       -0.48 |    -0.5  |        1    |        0.33 |     -0.55 |         0.12 |
| vineyards       |    0.19 |              0.82 |        0.1  |    -0.52 |        0.33 |        1    |      0.24 |         0.1  |
| streets         |    0.56 |              0.68 |        0.75 |     0.03 |       -0.55 |        0.24 |      1    |         0.21 |
| recreation      |    0.47 |              0.29 |        0.11 |     0.14 |        0.12 |        0.1  |      0.21 |         1    |

\* Summarize Spearmans Rho use this : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
\* Summarize the differences and similarities between the two tables. be specific
\* describe under what conditions we will find more or less for each use case
\* How is this related to land use and land cover?




## Regression results


### Recreation

The following table has the regression ressults for the different methods tested, the data is limited to the recreation group. The one with the highest r² is selected as best model.
Then we use a bagging regressor with the best model. Predictions are collected for the bagging regressor and the best model

|    | Model                            |       R² |      MSE |
|---:|:---------------------------------|---------:|---------:|
|  0 | Linear Regression                | 0.324434 | 1.01758  |
|  1 | Random Forest Regression         | 0.424015 | 0.867584 |
|  2 | Gradient Boosting Regression     | 0.373533 | 0.943623 |
|  3 | Theil-Sen Regressor              | 0.366329 | 0.954474 |
|  4 | Bagging:Random Forest Regression | 0.406718 | 0.893637 |
|  5 | Voting                           | 0.425927 | 0.864704 |

\* Summarize the tests used and the results, identify the best model
\* do this in paragraph format
\* reproduce the table





### Feature importance

The following table has the feature importances from the best model. Both the model feature importance and the permuation feature importance.
#### Model feature importance
|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  5 | streets         |    0.501551  |
|  0 | public-services |    0.137597  |
|  4 | vineyards       |    0.108158  |
|  6 | recreation      |    0.0894848 |
|  3 | undefined       |    0.0797985 |
|  2 | forest          |    0.0719538 |
|  1 | buildings       |    0.0114576 |


#### Permutation feature importance|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  5 | streets         |   0.531794   |
|  6 | recreation      |   0.097208   |
|  3 | undefined       |   0.039398   |
|  2 | forest          |   0.0130664  |
|  1 | buildings       |  -0.00114786 |
|  0 | public-services |  -0.0558385  |
|  4 | vineyards       |  -0.0615335  |

\* Explain the difference between permutation feature importance and model feature importance
\* Identify the differences between the two tables
\* reproduce the table





### Professional

The following table has the regression ressults for the different methods tested, the data is limited to the recreation group. The one with the highest r² is selected as best model.
Then we use a bagging regressor with the best model. Predictions are collected for the bagging regressor and the best model

|    | Model                            |       R² |      MSE |
|---:|:---------------------------------|---------:|---------:|
|  0 | Linear Regression                | 0.29823  | 0.558896 |
|  1 | Random Forest Regression         | 0.338826 | 0.526565 |
|  2 | Gradient Boosting Regression     | 0.267577 | 0.583308 |
|  3 | Theil-Sen Regressor              | 0.278534 | 0.574582 |
|  4 | Bagging:Random Forest Regression | 0.366359 | 0.504637 |
|  5 | Voting                           | 0.332161 | 0.531873 |

\* Summarize the tests used and the results, identify the best model
\* do this in paragraph format
\* reproduce the table





### Feature importance

The following table has the feature importances from the best model. Both the model feature importance and the permuation feature importance.
#### Model feature importance
|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  5 | streets         |    0.377831  |
|  0 | public-services |    0.331515  |
|  6 | recreation      |    0.0843752 |
|  3 | undefined       |    0.0676314 |
|  1 | buildings       |    0.0528272 |
|  4 | vineyards       |    0.0432322 |
|  2 | forest          |    0.0425881 |


#### Permutation feature importance|    | Feature         |   Importance |
|---:|:----------------|-------------:|
|  0 | public-services |   0.260735   |
|  5 | streets         |   0.228619   |
|  6 | recreation      |   0.0109182  |
|  2 | forest          |   0.00106447 |
|  1 | buildings       |  -0.0121382  |
|  4 | vineyards       |  -0.0173567  |
|  3 | undefined       |  -0.0193293  |

\* Explain the difference between permutation feature importance and model feature importance
\* Identify the differences between the two tables
\* reproduce the table




