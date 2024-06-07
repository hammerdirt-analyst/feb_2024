(gridforecaster)=
# Grid forecast

We consider that forecasting or predicting is the process of making statements about events that have yet to occurr. In this case we are using historical results to form our opinion about the probability of an event in the future. The event we considering is rather pedestrian:

> What will I find at the beach today, given what has been found at __other similar__ beaches or what was found at the beach in the past ?

Which means that our estimation of the objects we are likely to find is based on our own experience as well as the experience of others under similar conditions. This reasoning does not tell us about the reason why the object has bypassed the elaborate system put in place to prevent it from ending up on the beach. 

We do, however, identify quantifiable vectors that certainly contain the cause. The vectors come directly from the official topographical map for the territory. As a result locations can be grouped according to the magnitude of the vector that has been derived from the topographical map. By comparing local results to national results with a quantifiable vector we have a very efficient way to combine experiences beyond a geographic limit. Thus we can estimate the comparison from one location using the results from locations that have similar attributes but not geographically related.

Here we show how the `gridforecast` module works. Specifically the different methods of the  `gridforecast.MulitnomialDirichlet` class. It is a grid aproximation in Bayesien framework. We start the process with conditional probability, make the connection with Bayes` theorem and finish with the conjugate relationship Dirichlet-Multinomial. The application to survey data is implemented in scipy and numpy. 

Our first consideration, however, is wether or not our research question is comensurate with our assumptions of the model. Otherwise no amount of mathematical manipulation will persuade a reasonable individual that an outstanding or extreme result is probable when there is no evidence that rises to the same level.

## Assumptions of the model about the sample data

The data is assumed to be subject to the experience of the surveyor and each survey is independent and identically distributed. We add to these basic assumptions the particularities of the domain:

1. Locations that have similar environmental conditions will yield similar survey results
2. There is an exchange of material (trash) between the beach and body of water
3. Following from two, the material recovered at the beach is a result of the assumed exchange
4. The type of activities adjacent to the survey location are an indicator of the trash that will be found there
5. Following from four and three, the local environmental conditions are an indicator of the local contribution to the mix of objects at the beach
6. Surveys are not accurate
   * Some objects will be misidentified
   * Not all objects will be found
   * There will be inaccuracies in object counts or data entry

**Following 1 through 6:** the survey results are a reasonable estimate of the minimum number of objects that were present at the time the survey was completed. 


## Conditional probability

[Conditional probability](https://en.wikipedia.org/wiki/Conditional_probability) is a fundamental concept in probability theory that describes the probability of an event occurring given that another event has already occurred. It is denoted as $P(A∣B)$, which reads as "the probability of A given B". 

The conditional probability of event \(A\) given event \(B\) is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

where:

- $P(A|B)$ is the conditional probability of $A$ given $B$.
- $P(A \cap B)$ is the joint probability of both $A$ and $B$ occurring.
- $P(B)$ is the probability of event $B$ occurring, provided that $P(B) > 0$.


### Bayes' theorem

[Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) is a fundamental principle in probability theory and statistics that describes the probability of an event based on __prior__ knowledge of conditions that might be related to the event. It allows for the updating of probabilities as new evidence or information becomes available. It is derived from the definition of conditional probability.

__Deriving Bayes theorem__

::::{grid} 2 2 2 2
:gutter: 1

:::{grid-item-card} Define conditional probability

For events \(A\) and \(B\):

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

$$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

:::

:::{grid-item-card} The joint probability $P(A \cap B)$

From the first equation:

$$P(A \cap B) = P(A|B) \cdot P(B)$$

From the second equation:

$$P(A \cap B) = P(B|A) \cdot P(A)$$

:::

:::{grid-item-card} Equate the two expressions

$$P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

Solve for $P(A|B)$

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

:::

:::{grid-item-card} This is Bayes' Theorem

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

:::
::::

#### Prior knowledge

In the context of Bayes' theorem, the term "prior" refers to the prior probability, which is the probability of an event or hypothesis before any new evidence or data is taken into account. It represents the initial degree of belief in a particular outcome based on existing knowledge or assumptions.

> In this use case the __prior__ is what we __beleive__ we will find at the beach, before we get to the beach, given everything we know about beaches and litter in Switzerland. Our beliefs are based on the cumulative experience from all previous visits to the beach, or beaches that are similar. Our beliefs come from what we have actually experienced.

Mathematically, if we are trying to determine the probability of a hypothesis A given new evidence B, the prior probability is denoted as P(A). It is the baseline probability of A before considering the new evidence provided by B.

Bayes' Theorem uses the prior probability along with the likelihood of the evidence given the hypothesis and the marginal probability of the evidence to update the probability of the hypothesis. This updated probability is called the posterior probability.

### Empirical Bayes

Empirical Bayes methods are statistical techniques that combine the principles of Bayesian inference with empirical data. These methods use data to estimate the prior distribution, which is then used in the Bayesian framework to update probabilities and make inferences. Using this method means that our prior distribution is testable in the sense of Jaynes

> A piece of information _I_ concerning a parameter $\theta$ will be called __testable__ if, given any proposed prior probability assignment  $f( \theta )$ $d\theta$, there is a procedure which will determine unambiguously whether $f( \theta )$ does or does not agree with the information _I_. ([Jaynes,1968](https://bayes.wustl.edu/etj/articles/prior.pdf))

In traditional Bayesian analysis, the prior distribution is chosen based on subjective beliefs or historical data. In contrast, empirical Bayes methods __estimate the prior distribution directly from the observed data, making the process more objective and often more practical in large-scale problems__. ([Petrone, S. et al, 2014](https://link.springer.com/article/10.1007/s40300-014-0044-1))

#### Conjugate prior

In Bayesian statistics, a [conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior) is a prior distribution that, when combined with a given likelihood through Bayes' theorem, results in a [posterior distribution](https://en.wikipedia.org/wiki/Posterior_probability) of the same family as the prior. This property simplifies the computation of the posterior distribution.

1. Jaynes, E.T.: ["Probability Theory: The Logic of Science"](https://bayes.wustl.edu/etj/prob/book.pdf): Emphasized the logical consistency and practical advantages of conjugate priors.
2. Gelman, A. et al.: ["Bayesian Data Analysis"](http://www.stat.columbia.edu/~gelman/book/) : discusses conjugate priors in the context of hierarchical models and practical Bayesian analysis.

#### Deriving conjugate relationship

The [binomial](https://en.wikipedia.org/wiki/Binomial_distribution), [multinomial](https://en.wikipedia.org/wiki/Multinomial_distribution), and [Dirichlet](https://en.wikipedia.org/wiki/Dirichlet_distribution) distributions are intrinsically linked through the concept of conjugate priors in Bayesian statistics. The binomial distribution describes the probability of a fixed number of successes in a series of independent trials, with a success probability _p_. When modeling this in a Bayesian framework, the Beta distribution is used as a conjugate prior for _p_. This means that the posterior distribution, after observing data, remains a Beta distribution, simplifying the update process.

Extending this to multiple categories, the multinomial distribution generalizes the binomial by modeling the counts of outcomes across multiple categories. The Dirichlet distribution serves as the conjugate prior for the multinomial distribution, just as the Beta distribution does for the binomial. When using a Dirichlet prior, the posterior distribution after observing data also remains a Dirichlet distribution.

::::{grid} 2 2 2 2
:gutter: 1

:::{grid-item-card} Binomial Likelihood:

The binomial distribution models the number of successes in _n_ trials, given a success probability _p_:

$$P(X = k | p) = \binom{n}{k} p^k (1 - p)^{n - k}$$

The Beta distribution is a conjugate prior for the binomial likelihood, parameterized by $\alpha$ and $\beta$:

$$P(p | \alpha, \beta) = \frac{p^{\alpha - 1} (1 - p)^{\beta - 1}}{B(\alpha, \beta)}$$
:::

:::{grid-item-card} Posterior Distribution:

Combining the likelihood and prior using Bayes' theorem gives the posterior distribution:

$$P(p | k, n) \propto p^k (1 - p)^{n - k} \cdot p^{\alpha - 1} (1 - p)^{\beta - 1}$$

$$P(p | k, n) \propto p^{k + \alpha - 1} (1 - p)^{n - k + \beta - 1}$$

Which is a Beta distribution:

$$P(p | k, n) = \text{Beta}(p | k + \alpha, n - k + \beta)$$
:::

:::{grid-item-card} Generalize binomial to multinomial

The multinomial distribution generalizes the binomial to more than two categories. For counts 
$\mathbf{x} = (x_1, x_2, \ldots, x_K) \quad \text{in} \quad K \quad \text{categories, given probabilities} \quad \mathbf{p} = (p_1, p_2, \ldots, p_K)$:

$$P(\mathbf{x} | \mathbf{p}) = \frac{n!}{x_1! x_2! \cdots x_K!} p_1^{x_1} p_2^{x_2} \cdots p_K^{x_K}$$

where: $n = \sum_{i=1}^K x_i$
:::

:::{grid-item-card} The conjugate prior to the multinomial

The Dirichlet distribution is a conjugate prior for the multinomial distribution, parameterized by α=(α1​,α2​,…,αK​):

$P(\mathbf{p} | \boldsymbol{\alpha}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^K p_i^{\alpha_i - 1}$

where B(α) is the multivariate Beta function.
:::

:::{grid-item-card} Posterior Distribution
The posterior distribution is a combination of the likelihood and prior:

$$P(\mathbf{p} | \mathbf{x}) \propto \left( \prod_{i=1}^K p_i^{x_i} \right) \left( \prod_{i=1}^K p_i^{\alpha_i - 1} \right)$$

Which is a Dirichlet distribution:

$P(\mathbf{p} | \mathbf{x}) \propto \prod_{i=1}^K p_i^{x_i + \alpha_i - 1}$

:::
:::{grid-item-card} Posterior with updated parameters

$$P(\mathbf{p}|\mathbf{x}) = \text{D}(\mathbf{p}|x_1 + \alpha_1, \ldots, x_K + \alpha_K)$$

Where D is a _Dirichlet_ distribution
:::
::::

#### Grid Approximation

Grid approximation is a technique used in numerical analysis and statistical inference to approximate the values of a continuous function or parameter by evaluating it at a discrete set of points. This involves creating a grid of possible values within a defined range and calculating the function or parameter at each grid point. We are using $P(\mathbf{p}|\mathbf{x}) = \text{D}(\mathbf{p}|x_1 + \alpha_1, \ldots, x_K + \alpha_K)$ to approximate the grid.

### Empirical Bayes grid approximation using a conjugate prior

Empirical Bayes grid approximations involves estimating the prior and posterior distributions of parameters using a discretized set of values. In the context of the multinomial-Dirichlet conjugate relationship, this method is particularly effective. The Dirichlet distribution serves as the prior for the multinomial likelihood, and empirical Bayes methods estimate this prior directly from the data. By defining a grid of possible parameter values, in this case spaced every 0.1 units from 0 to the maximum observed value or 100, the posterior distribution is approximated by evaluating the likelihood and updating the Dirichlet prior at each grid point.

This approach simplifies the computational complexity of Bayesian inference. Instead of integrating over a continuous parameter space, which can be analytically challenging, grid approximation transforms the problem into a finite summation. The [multinomial-Dirichlet conjugate pair](https://en.wikipedia.org/wiki/Dirichlet-multinomial_distribution) ensures that the posterior remains in the Dirichlet family, making the updates straightforward.

__Adding probability__

We have noticed that using this method is sensitive to the max value of the likelihood. The further out the maximum is the more likely elevated values appear. This may be the case, but there is also the chance that extreme elements are just that.

Here we consider the following question:

1. What are the chances of finding at least one _O_ if I go to the beach at _C_ ?

Where _O_ is some object of interest that is in the list of items identified on the beach (there are 229 options) and C is a lake or municipality on a lake.

This example was first tested in November 2021 at the request of members from an environmental organization that was visiting Lake Geneva, [finding one object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html). This value was initially expected to be approximately 40%. The method of calculation was the Beta-Binomial conjugate pair. Instead of considering all the values on the grid we consider only two results: was the number found greater than zero or not. From the general form in (1) we get:

> What is the chance of finding at least one feminine hygiene product at the beach on Lac Léman ?


````{tab-set}

```{tab-item} Steps to complete the calculation

1. identify the codes for the items of interest: `G96` and `G144`
2. define the region of interest: `lac-leman`
3. define the date range of the likelihood : `{'start':'2020-01-01', 'end':'2021-11-01'}`
4. define the date range of the prior :  `{'start':'2015-11-15', 'end':'2019-12-31'}`

### The likelihood and prior

The likelihood data is defined as all the data collected durring the current sampling campaign, up to one week before the planned event in Geneva. The prior data is all collected in the previous sampling campaigns, not including results from locations in the likelihod. In both cases we are considering only the codes G96 and G144.



```

```{tab-item} Default parameters and methods

__Default parameters__

1. range of the default index $X = \{ x \in \mathbb{R} \mid x = 0.1k, \; k \in \mathbb{Z}, \; 0 \leq x < 100 \}$
   * or `np.arange(0, 100, 0.1)`
2. Max range of forecast grid = $\max_{i} \{ x_i \} \text{ or } P_{99} = \text{percentile}_{99} \{ x_i \}$
3. The magnitude of the land use for each survey location is categorized in the following manner:

$$
\text{binning}(x) = 
\begin{cases} 
1 & \text{if } -1 \leq x < 0.2 \\
2 & \text{if } 0.2 \leq x < 0.4 \\
3 & \text{if } 0.4 \leq x < 0.6 \\
4 & \text{if } 0.6 \leq x < 0.8 \\
5 & \text{if } 0.8 \leq x \leq 1 
\end{cases},
\text{ where x is the \% of land occupied by a land-use feature } 
$$

__Distributions__

The posterior distribution is $P(\text{Likelihood} \mid \text{Prior}) \approx \text{Dirichlet}(\alpha)$ or more commonly: $P(\theta \mid \mathbf{X}) \approx  text{Dirichlet}(\alpha + \mathbf{n})$

1. $\theta$ is the parameters of the Dirichlet distribution
2. $\mathbf{X}$ is the observed data
3. $\alpha$ is the parameters of the prior Dirichlet distribution
4. $\mathbf{n}$ is the count data from the likelihood

__Forecasted samples__

$$
\begin{align*}
\theta &\sim \text{Dirichlet}(\alpha) \\
\mathbf{X} \mid \theta &\sim \text{Multinomial}(N, \theta)
\end{align*}
$$
```
````