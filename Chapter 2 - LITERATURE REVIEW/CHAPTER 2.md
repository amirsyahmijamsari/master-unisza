# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

Flood frequency analysis forms the quantitative foundation for hydraulic infrastructure design, flood hazard zoning, and water resource management. In tropical regions prone to recurrent monsoon floods, accurate estimation of precipitation recurrence is essential for safeguarding human lives and civil infrastructure. However, conventional frequency analysis methodologies were formulated primarily within temperate climate regimes, where extreme meteorological events occur sporadically. Applying these classical methods to equatorial regions introduces structural limitations that can bias design quantile estimates.

This chapter presents a critical evaluation of the theoretical and empirical literature governing flood frequency analysis, with specific relevance to tropical monsoon climates. The review is structured into nine sections: Section 2.2 examines the climatological divergence between temperate and tropical precipitation regimes. Section 2.3 traces the historical evolution of frequency analysis, detailing the conventional Annual Maximum Series (AMS) framework and the Complete Time-Series Analysis (CTA) paradigm formulated by Volpi et al. (2019). Section 2.4 evaluates candidate probability distributions utilized in hydrological modeling. Section 2.5 provides a mathematical treatment of L-moments theory and parameter estimation. Section 2.6 reviews goodness-of-fit assessment criteria. Section 2.7 outlines return period concepts and quantile extrapolation. Section 2.8 reviews regional empirical investigations in Malaysia and other tropical zones. Section 2.9 outlines the identified research gaps, and Section 2.10 synthesizes the chapter findings.

---

## 2.2 Temperate versus Tropical Climate Systems

### 2.2.1 Climate Classification

Standard climate classification schemes, notably the Köppen-Geiger system, delineate global climate regions based on annual and monthly precipitation and temperature thresholds (Peel et al., 2007). Temperate climates, categorized as Group C and Group D, exhibit pronounced seasonal thermal cycles with moderate precipitation distributed across the year. Tropical climates, designated as Group A, maintain high temperatures throughout the year and experience heavy precipitation governed by intertropical convergence dynamics and seasonal monsoon circulation (Kottek et al., 2006).

Understanding these underlying climatological boundaries is necessary for evaluating hydrological modeling frameworks. Methodologies and probability distributions developed for temperate catchments often fail when applied directly to equatorial regimes without appropriate modification (Koutsoyiannis & Montanari, 2015).

### 2.2.2 Temperate Climate Rainfall Characteristics

Temperate regions, encompassing major portions of Europe, North America, and continental Asia, exhibit precipitation regimes governed primarily by mid-latitude synoptic weather depressions (Brutsaert, 2005). Mean annual precipitation in these zones is moderate, typically ranging between 500 mm and 1,500 mm, with rainfall distributed across seasons without extreme intra-annual concentration. Major flood-producing events in temperate environments are sporadic, occurring once or twice annually, and are commonly driven by large-scale frontal weather depressions that produce prolonged precipitation over several days.

These meteorological conditions formed the physical basis for classical Extreme Value Theory (Gumbel, 1958; Stedinger et al., 1993). Under temperate conditions, annual maximum events are rare, temporally dispersed, and mutually independent, which supported the assumption that extracting a single peak per year captures the dominant flood risk.

### 2.2.3 Tropical Climate Rainfall Characteristics

Tropical monsoon regions, particularly across Southeast Asia, exhibit fundamentally contrasting hydrometeorological dynamics (Nieuwolt, 1977; Suhaila & Jemain, 2007). Annual precipitation totals frequently exceed 2,000 mm to 4,000 mm, with rainfall concentrated during distinct monsoon surges. Convective storm mechanisms predominate, producing intense, localized downpours with short durations and high rainfall rates. Rather than experiencing solitary extreme events, tropical catchments frequently undergo recurrent heavy storms within narrow temporal windows.

In Peninsular Malaysia, the Northeast Monsoon (November to March) drives recurring high-intensity precipitation surges across the eastern coastal states, including Terengganu (Desa & Niemczynowicz, 1996; Wong et al., 2009; Suhaila et al., 2010). During this season, 24-hour rainfall accumulations frequently surpass 100 mm, with multiple consecutive storm systems occurring within several weeks.

### 2.2.4 Implications for Frequency Analysis

The marked divergence between temperate and tropical rainfall dynamics introduces direct statistical implications for frequency analysis (Koutsoyiannis, 2004; Papalexiou & Koutsoyiannis, 2013). 

First, the standard practice of extracting only annual maxima reduces sample sizes severely, discarding valuable information about secondary extreme storms that occur within the same monsoon season. In tropical regions, secondary extreme events often exceed the annual maxima of drier years, meaning that data decimation induces severe information loss.

Second, the assumption of temporal independence between extreme occurrences becomes problematic in monsoon environments where storm clustering produces dependent flood sequences (Serinaldi & Kilsby, 2015). 

Third, climatic variability and global atmospheric shifts influence stationarity assumptions across tropical catchments differently than in temperate zones (Khaliq et al., 2006; Milly et al., 2008). 

Finally, the choice of probability distribution must reflect the physical mechanisms generating tropical rainfall. Standard temperate distributions frequently fail to capture the heavy upper tails and pronounced positive skewness of equatorial precipitation (Papalexiou & Koutsoyiannis, 2013).

---

## 2.3 Historical Development of Flood Frequency Analysis

### 2.3.1 Early Foundations

The scientific study of flood frequency began in the early twentieth century. Hazen (1914) introduced plotting positions for probability analysis, establishing a framework for relating observed data to theoretical distributions. Fuller (1914) developed empirical formulas for flood frequency estimation that remained influential for several decades.

Gumbel (1941, 1958) made foundational contributions by applying extreme value theory to hydrological problems. His work established the Extreme Value Type I (Gumbel) distribution as a standard tool for flood frequency analysis. Gumbel's methods were widely adopted because they provided an objective basis for extrapolating beyond observed data records.

### 2.3.2 The Annual Maximum Series Approach

The Annual Maximum Series (AMS) framework became the standard convention in hydrological frequency analysis following the work of Dalrymple (1960) and the United States Geological Survey. Under this protocol, the single maximum daily observation recorded in each calendar year is extracted to form an annual series. A probability distribution is subsequently fitted to this decimated sample, and design quantiles are extrapolated across specified return periods. The AMS methodology was codified in national design manuals, including Bulletin 17B (Interagency Advisory Committee on Water Data, 1982), establishing a global precedent for water resource planning.

### 2.3.3 Partial Duration Series (PDS / Peaks-Over-Threshold)

Recognizing limitations of the AMS approach, researchers developed the Partial Duration Series (PDS) or Peaks-Over-Threshold (POT) method (Langbein, 1949; Madsen et al., 1997). This approach considers all events exceeding a specified threshold rather than restricting the sample to the single largest event per year. While PDS captures secondary extreme events within the same annual cycle, it introduces substantial subjective challenges: selecting an appropriate threshold magnitude involves a bias-variance trade-off, and declustering techniques must be applied to filter out mutually dependent peaks within the same storm system (Cunnane, 1989; Coles, 2001).

### 2.3.4 Complete Time-Series Analysis (CTA) Paradigm (Volpi et al., 2019)

To eliminate the severe information loss caused by data filtering, Volpi et al. (2019) formulated the Complete Time-Series Analysis (CTA) paradigm in their study titled *"Save hydrological observations! Return period estimation without data decimation"* (*Journal of Hydrology*, 571, 782–792).

#### 2.3.4.1 The Critique of Data Decimation

Traditional flood frequency analysis reduces rich observational datasets into sparse samples of extremes through either Annual Maxima (AM) or Peaks-Over-Threshold (POT) filtering. Volpi et al. (2019) demonstrated that this data decimation discards over 99.7% of available observations in daily records. In tropical climates characterized by recurring monsoon surges, multiple severe events occur within the same annual cycle. Reducing an entire year of daily readings to a single maximum value eliminates secondary extreme storms that frequently exceed annual maxima recorded in other years, resulting in inflated uncertainty and systematic recurrence misrepresentation.

#### 2.3.4.2 Mathematical Formulation of CTA According to Volpi et al. (2019)

The theoretical foundation of CTA rests on redefining the return period directly through the complete observational time series rather than relying on artificial samples of annual maxima. Volpi et al. (2019) established that the return period $T(x)$ corresponding to an extreme threshold $x$ is fundamentally defined as the mean interarrival time between consecutive exceedance events:

$$T(x) = E[T(x)] = \frac{1}{\nu(x)}$$

where $\nu(x)$ represents the mean crossing rate or probability of exceedance per time unit.

A central mathematical contribution of Volpi et al. (2019) is the proof that the average interarrival time of threshold crossings is invariant to the internal autocorrelation, clustering, or cyclo-stationary structure of the continuous process. In a discrete daily time step of one day, if $F(x) = P(X \le x)$ denotes the cumulative distribution function of the daily observations, the probability of exceeding magnitude $x$ on any given day is $P(X > x) = 1 - F(x)$. The expected interarrival time between exceedances is given by:

$$E[T(x)] = \frac{1}{1 - F(x)} \quad \text{(days)}$$

Expressing this recurrence interval on an annual equivalent basis yields:

$$T_{CTA}(x) = \frac{E[T(x)]}{365.25} = \frac{1}{365.25 \cdot [1 - F(x)]} \quad \text{(years)}$$

Under the conventional Annual Maximum Series, the return period is estimated from the distribution of annual maxima $F_{AM}(x)$:

$$T_{AM}(x) = \frac{1}{1 - F_{AM}(x)} \quad \text{(years)}$$

Because the AMS records at most one event per year, secondary severe storms occurring within the same calendar year are omitted from $F_{AM}$. Consequently, for extreme events that occur multiple times in a year, $T_{AM}(x)$ is systematically larger than $T_{CTA}(x)$. In a companion theoretical study, Volpi (2019) demonstrated that temporal clustering of extremes increases the cumulative probability of failure across a hydraulic structure's operational lifespan compared to independent annual maximum assumptions. This mathematical discrepancy establishes the theoretical basis for the overestimation factor:

$$OE(x) = \frac{T_{AM}(x)}{T_{CTA}(x)}$$

#### 2.3.4.3 Process Assumptions and Tropical Precipitation Adaptation

While Volpi et al. (2019) validated CTA on continuous, strictly positive streamflow records ($X(t) > 0$), applying CTA to daily precipitation introduces a structural physical challenge. Rainfall is an intermittent process containing a large proportion of zero-rainfall days, which account for 40% to 55% of calendar days in Terengganu. Continuous probability distributions cannot accommodate discrete point masses at zero without numerical failure during parameter estimation (Hosking & Wallis, 1997; Rao & Hamed, 2000).

To overcome this limitation, this research implements an adapted complete daily time-series analysis framework. Test threshold magnitudes ($M$) at the 99th percentile are derived from the complete daily time series, including zero days, preserving true calendar frequency across the full observational period as established by Volpi et al. (2019). Parameter estimation for continuous probability distributions, including the 4-Parameter Kappa distribution, is conducted on positive rainfall days ($X \ge 1.0\text{ mm}$) following the two-component mixture model of Hosking and Wallis (1997):

$$F(x) = p_0 + (1 - p_0) F_{wet}(x) \quad \text{for } x \ge 1.0\text{ mm}$$

where $p_0$ is the discrete proportion of dry days, and $F_{wet}(x)$ is fitted via L-moments. This dual formulation preserves the non-decimated frequency philosophy of Volpi et al. (2019) while maintaining statistical rigor for intermittent tropical rainfall.

### 2.3.5 Regional Frequency Analysis

Regional frequency analysis extends single-site analysis by pooling data from multiple stations to improve estimation reliability (Dalrymple, 1960; Hosking & Wallis, 1997). The index flood method, introduced by Dalrymple (1960), assumes that sites within a homogeneous region share a common frequency distribution scaled by a site-specific index.

Hosking and Wallis (1997) established a comprehensive framework for regional frequency analysis utilizing L-moments, which has become standard international practice. Their analytical procedure encompasses five systematic stages: initial screening of data to detect measurement errors and gross outliers; identification of hydrologically homogeneous regions; selection of an appropriate regional probability distribution; estimation of the regional growth curve; and scaling the regional dimensionless quantiles by at-site index flood estimates. Burn (1990) introduced the region of influence approach, defining regional boundaries based on physical and statistical similarity rather than geographical proximity. Lettenmaier et al. (1987) demonstrated that regional pooling reduces estimation variance even in the presence of moderate regional heterogeneity.

---

## 2.4 Probability Distributions in Hydrology

### 2.4.1 Extreme Value Theory

Extreme value theory provides the mathematical foundation for analyzing the distribution of sample maxima. Fisher and Tippett (1928) demonstrated that the asymptotic distribution of normalized maxima from independent and identically distributed random variables converges to one of three limiting forms: Type I (Gumbel), characterized by an unbounded exponential tail; Type II (Fréchet), exhibiting a heavy polynomial tail; and Type III (Weibull), featuring a bounded upper tail. Jenkinson (1955) unified these three limiting distributions into the Generalized Extreme Value (GEV) formulation, which provides a flexible framework widely adopted in hydrological practice (Coles, 2001).

### 2.4.2 Two-Parameter Distributions

The Gumbel distribution, also designated as the Extreme Value Type I distribution, was introduced to hydrology by Gumbel (1941, 1958). It has been widely used for flood and rainfall frequency analysis due to its mathematical simplicity and theoretical justification for maxima of exponentially distributed variables. The distribution is defined by two parameters: location ($\xi$) and scale ($\alpha$).

The Normal distribution is occasionally applied to transformed hydrological variables or to variables that display symmetric behavior (Haan, 1977). However, its symmetrical density function severely restricts its direct applicability to right-skewed rainfall amounts.

The Exponential distribution represents a special case of several generalized distributions and is frequently utilized to model exceedances over high thresholds in partial duration series modeling (Cunnane, 1979).

### 2.4.3 Three-Parameter Distributions

The Generalized Extreme Value (GEV) distribution incorporates a shape parameter ($\kappa$) that governs tail behavior (Jenkinson, 1955; Hosking et al., 1985). When $\kappa = 0$, the GEV reduces to the two-parameter Gumbel distribution. Positive values of $\kappa$ produce bounded upper tails corresponding to the Type III Weibull family, whereas negative values generate heavy, polynomial-like upper tails belonging to the Type II Fréchet family. The GEV distribution is recommended by multiple national hydrological guidelines for flood estimation (Cunnane, 1989).

The Generalized Logistic (GLO) distribution represents the distribution of the logit transform of a GEV variable and is recommended for flood frequency estimation in the United Kingdom by the Flood Estimation Handbook (Robson & Reed, 1999). It yields heavier upper tails than the GEV distribution for equivalent skewness levels.

The Generalized Normal (GNO) distribution, commonly referred to as the three-parameter log-normal distribution, has been widely applied in hydrological investigations (Stedinger, 1980). It describes a random variable whose logarithm, adjusted by a lower bound shift parameter, follows a normal distribution.

The Generalized Pareto (GPA) distribution models exceedances over a high threshold in peaks-over-threshold modeling (Hosking & Wallis, 1987). It represents the limiting distribution of excesses over sufficiently high thresholds under extreme value theory.

The Pearson Type III (PE3) distribution, also known as the three-parameter gamma distribution, was recommended by Bulletin 17B for flood frequency modeling in the United States (Interagency Advisory Committee on Water Data, 1982). It remains widely utilized in engineering hydrology, particularly through its logarithmic variant, the Log-Pearson Type III distribution (Bobée & Ashkar, 1991).

### 2.4.4 Four-Parameter Distributions

The 4-Parameter Kappa distribution (K4D) was introduced by Hosking (1994) as a flexible model that encompasses the Generalized Extreme Value, Generalized Logistic, and Generalized Pareto distributions as special cases. Its two shape parameters provide enhanced flexibility in modeling the upper tail and skewness of extreme hydrological data. Empirical investigations have demonstrated that the 4-Parameter Kappa distribution yields superior fitting accuracy for extreme precipitation across varied climatic regimes (Parida, 1999; Murshed et al., 2014).

The Wakeby distribution, formulated by Houghton (1978), incorporates five parameters to achieve high curve-fitting flexibility. However, its parameter estimation requires extensive sample sizes, making it prone to overfitting when applied to limited historical records (Hosking, 1986).

### 2.4.5 Distribution Selection

Selecting an appropriate probability distribution for hydrological frequency modeling requires balancing multiple statistical and physical criteria (Cunnane, 1989; Rao & Hamed, 2000). The candidate distribution must align with the physical mechanisms governing the generation of extreme precipitation in the catchment. Statistical goodness-of-fit tests must verify that the theoretical distribution adequately reproduces observed data patterns without systematic bias. 

Furthermore, the model must exhibit estimation robustness across varying sample sizes while adhering to the principle of parsimony, whereby simpler models with fewer parameters are preferred unless additional parameters yield measurable improvements in fitting accuracy. L-moment ratio diagrams, which plot sample L-skewness against L-kurtosis, serve as an effective diagnostic tool for evaluating distribution suitability (Vogel & Fennessey, 1993; Hosking & Wallis, 1997).

---

## 2.5 L-Moments: Theory and Applications

### 2.5.1 Introduction to L-Moments

L-moments, introduced by Hosking (1990), are linear combinations of probability-weighted moments (PWMs) that provide an alternative to conventional product moments for summarizing probability distributions and estimating parameters. The designation "L" highlights the linear combinations of order statistics utilized in their mathematical definition.

Conventional product moments (mean, variance, skewness, and kurtosis) have known limitations when applied to skewed distributions or small sample sizes (Hosking, 1990). Higher-order product moments involve squaring and cubing sample deviations, which inflates estimation variance and causes extreme sensitivity to outliers. L-moments overcome these limitations by providing robust parameter estimates that remain stable in the presence of outliers, maintain lower sampling variance in small records, enable clear graphical discrimination between candidate distribution families, and produce bounded moment ratios that facilitate objective regional comparisons.

### 2.5.2 Probability Weighted Moments

L-moments are derived directly from probability-weighted moments (PWMs), originally defined by Greenwood et al. (1979). For a continuous random variable $X$ with cumulative distribution function $F(x)$, PWMs are defined by the expectation:

$$M_{p,r,s} = E\left[X^p \{F(X)\}^r \{1-F(X)\}^s\right]$$

The most commonly utilized PWM specifications are:

$$\beta_r = M_{1,r,0} = E\left[X \{F(X)\}^r\right]$$

Greenwood et al. (1979) established that many probability distributions expressible in inverse form have parameters that relate directly to $\beta_r$, establishing the mathematical framework for Hosking's (1990) development of L-moments.

### 2.5.3 Definition of L-Moments

The first four population L-moments are defined as linear combinations of PWMs (Hosking, 1990):

$$\lambda_1 = \beta_0$$

$$\lambda_2 = 2\beta_1 - \beta_0$$

$$\lambda_3 = 6\beta_2 - 6\beta_1 + \beta_0$$

$$\lambda_4 = 20\beta_3 - 30\beta_2 + 12\beta_1 - \beta_0$$

These scalar quantities correspond to fundamental properties of the probability distribution: $\lambda_1$ represents location (identical to the arithmetic mean); $\lambda_2$ measures scale and dispersion (comparable to standard deviation); $\lambda_3$ quantifies distributional asymmetry and skewness; and $\lambda_4$ reflects peakedness and tail weight (kurtosis).

### 2.5.4 L-Moment Ratios

To enable scale-invariant comparisons, Hosking (1990) defined dimensionless L-moment ratios:

$$\tau = \frac{\lambda_2}{\lambda_1} \quad \text{(L-coefficient of variation, L-CV)}$$

$$\tau_3 = \frac{\lambda_3}{\lambda_2} \quad \text{(L-skewness)}$$

$$\tau_4 = \frac{\lambda_4}{\lambda_2} \quad \text{(L-kurtosis)}$$

Unlike conventional moment ratios, L-moment ratios are strictly bounded:

$$-1 < \tau_3 < 1$$

$$\frac{5\tau_3^2 - 1}{4} \le \tau_4 < 1$$

These defined mathematical bounds prevent extreme values from distorting the moment space, facilitating reliable interpretation and comparison across distinct sample datasets and theoretical distribution families (Hosking & Wallis, 1997).

### 2.5.5 Advantages of L-Moments

Hosking (1990) and subsequent researchers established several distinct advantages of L-moments over conventional product moments. L-moments exhibit marked robustness against outliers because their calculation relies on linear combinations of ranked order statistics rather than squared or cubed deviations from the mean (Hosking & Wallis, 1997). 

In small sample sizes, Vogel and Fennessey (1993) demonstrated that L-moment estimators exhibit lower bias and variance than conventional product moment estimators for records smaller than 50 to 100 observations, which represents the typical operational constraint in hydrological monitoring networks. 

Furthermore, L-moment ratio diagrams provide an effective visual tool for distribution selection. Because distinct distribution families occupy well-defined lines or trajectories within the $\tau_3$ versus $\tau_4$ plane, plotting sample L-moment ratios against theoretical distribution curves enables hydrologists to identify optimal models without subjective bias. 

Finally, L-moments are effective for regional frequency pooling because L-moment ratios are scale-invariant under index flood assumptions, allowing data from disparate gauging sites to be normalized and combined reliably (Hosking & Wallis, 1997).

### 2.5.6 Sample L-Moments

For a sample of size $n$ arranged in ascending order $x_{1:n} \le x_{2:n} \le \dots \le x_{n:n}$, sample L-moments are calculated from unbiased sample PWM estimators (Hosking, 1990):

$$b_r = \frac{1}{n} \sum_{i=r+1}^{n} \frac{(i-1)(i-2)\dots(i-r)}{(n-1)(n-2)\dots(n-r)} x_{i:n}$$

Sample L-moments $l_1, l_2, l_3, l_4$ are computed directly by replacing population PWMs $\beta_r$ with sample estimators $b_r$. Because sample L-moments are linear functions of order statistics, they are strictly unbiased estimators of their population counterparts, eliminating the need for empirical sample size correction factors required by conventional product moments (Hosking & Wallis, 1995).

### 2.5.7 L-Moments for Parameter Estimation

The method of L-moments parameter estimation equates sample L-moments to theoretical distribution parameters and solves the resulting system of algebraic equations (Hosking, 1990). This approach provides explicit, closed-form parameter solutions for numerous candidate distributions, delivers estimators with desirable asymptotic efficiency, and avoids iterative convergence failures common to numerical maximum likelihood algorithms in small samples. Hosking and Wallis (1997) documented explicit parameter estimation formulas for standard hydrological distributions, including GEV, GLO, GPA, and Pearson Type III models.

### 2.5.8 Applications of L-Moments in Hydrology

L-moments have gained widespread international adoption across water resource engineering disciplines. In flood frequency analysis, L-moments are recognized as standard procedure in national engineering guidelines (Stedinger et al., 1993; Hosking & Wallis, 1997). In precipitation frequency modeling, researchers have successfully applied L-moments to daily and sub-daily rainfall series across diverse climatic environments (Zalina et al., 2002; Zin et al., 2009; Papalexiou & Koutsoyiannis, 2013). Regional frequency analysis methodologies worldwide rely predominantly on L-moments for screening gauge homogeneity and establishing regional growth curves. In meteorological applications, L-moments are utilized for drought severity characterization (Santos et al., 2011) and extreme wind speed estimation for structural building codes (Holmes & Moriarty, 1999).

---

## 2.6 Goodness-of-Fit Assessment

### 2.6.1 Purpose of Goodness-of-Fit Testing

Goodness-of-fit assessment provides the objective statistical criterion for confirming that a fitted theoretical distribution adequately represents the empirical data. Evaluating goodness of fit is essential for validating model selection, ranking competing distribution families, identifying systematic model departures in distribution tails, and ensuring that design quantiles extrapolated beyond the observation window remain mathematically sound (D'Agostino & Stephens, 1986).

### 2.6.2 Plotting Positions

Plotting positions assign empirical non-exceedance probabilities to ranked sample observations, enabling direct graphical comparison against theoretical distribution curves. Several plotting position formulas have been established in hydrological literature (Cunnane, 1978).

The Weibull formula, defined by $P_i = i / (n+1)$, was introduced by Weibull (1939) and provides an unbiased estimate of the mean exceedance probability. However, it can introduce tail bias when applied to extreme value distributions.

The Hazen formula, expressed as $P_i = (i - 0.5) / n$, was formulated by Hazen (1914) to provide an approximation of median plotting positions.

The Gringorten formula, defined by $P_i = (i - 0.44) / (n + 0.12)$, was derived by Gringorten (1963) specifically for Gumbel and extreme value distributions. Cunnane (1978) demonstrated that the Gringorten formula yields approximately unbiased quantile plotting positions for extreme value distributions, making it the preferred standard for flood frequency analysis.

### 2.6.3 Classical Goodness-of-Fit Tests

Classical statistical hypothesis tests evaluate empirical agreement with theoretical distributions (D'Agostino & Stephens, 1986). The Chi-square test assesses frequency discrepancies across grouped histogram intervals, though its outcomes depend heavily on subjective interval selection. The Kolmogorov-Smirnov test measures the maximum absolute difference between empirical and theoretical cumulative distribution functions. While exact for fully specified distributions, its critical values require adjustment when parameters are estimated directly from sample data (Lilliefors, 1967).

The Anderson-Darling and Cramér-von Mises tests evaluate integrated squared discrepancies across the entire distribution domain:

$$W^2 = n \int_{-\infty}^{\infty} [F_n(x) - F(x)]^2 \, dF(x)$$

$$A^2 = n \int_{-\infty}^{\infty} \frac{[F_n(x) - F(x)]^2}{F(x)[1 - F(x)]} \, dF(x)$$

The Anderson-Darling statistic ($A^2$) incorporates a weighting function that accentuates discrepancies in the distribution tails, making it effective for extreme value applications (Laio, 2004).

### 2.6.4 Deviation Indices: MADI and MSDI

To provide dimensionless, scale-independent criteria for ranking distribution performance across multiple gauging sites, normalized deviation measures are widely employed in hydrological research:

The Mean Absolute Deviation Index (MADI) quantifies the average relative absolute difference between observed and theoretical quantiles:

$$\text{MADI} = \frac{1}{n} \sum_{i=1}^{n} \frac{|x_i - \hat{x}_i|}{x_i}$$

The Mean Squared Deviation Index (MSDI) penalizes larger individual quantile discrepancies through quadratic weighting:

$$\text{MSDI} = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{x_i - \hat{x}_i}{x_i} \right)^2$$

In both formulations, $x_i$ represents the $i$-th observed sample value arranged in ascending order, and $\hat{x}_i$ denotes the theoretical quantile computed at the empirical plotting position $P_i$. Lower index values indicate superior fit, with models minimizing MADI and MSDI selected as optimal representations of the rainfall series.

---

## 2.7 Return Period Analysis

### 2.7.1 Return Period Concept

The return period (recurrence interval) $T$ is defined as the average elapsed time between occurrences of an event exceeding a designated magnitude (Chow et al., 1988). In annual maximum modeling, the return period in years relates inversely to the annual exceedance probability $p$:

$$T = \frac{1}{p} = \frac{1}{1 - F(x)}$$

A 100-year return period denotes an event with a 1% annual exceedance probability ($p = 0.01$). Stedinger and Griffis (2008) highlighted that the return period represents a long-term statistical average across numerous recurrence cycles and does not imply periodic or cyclical occurrence. Koutsoyiannis (2004) provided an exhaustive review of probabilistic return period interpretations in water engineering.

### 2.7.2 Quantile Estimation

Quantile estimation evaluates the precipitation magnitude $x_T$ corresponding to a specified return period $T$. For a candidate distribution with cumulative distribution function $F(x)$, the design quantile is determined using the inverse cumulative distribution function (quantile function):

$$x_T = F^{-1}\left(1 - \frac{1}{T}\right)$$

Analytical quantile formulations exist for the standard hydrological distributions evaluated in this study, including GEV, GLO, GPA, and 4-Parameter Kappa models (Hosking & Wallis, 1997; Rao & Hamed, 2000).

### 2.7.3 Uncertainty and Risk Assessment

Uncertainty in extreme quantile estimation arises from limited historical sample lengths and model misspecification. In engineering risk assessment, the cumulative probability of failure $R$ (the likelihood of experiencing at least one design exceedance over an operational design lifespan of $n$ years) is given by:

$$R = 1 - \left(1 - \frac{1}{T}\right)^n$$

For example, a hydraulic culvert designed for a 100-year recurrence interval ($T = 100$) operating over a 50-year structural lifespan ($n = 50$) maintains a 39.5% probability of being exceeded during its operational service. Consequently, systematic overestimation of return periods causes infrastructure to be under-designed, substantially escalating operational failure risk.

---

## 2.8 Malaysian and Tropical Rainfall Studies

### 2.8.1 Malaysian Climate and Monsoon Regimes

Malaysia is characterized by an equatorial climate governed by two distinct monsoon circulations: the Northeast Monsoon (November to March) and the Southwest Monsoon (May to September) (Wong et al., 2009). The eastern coastal states of Peninsular Malaysia, specifically Terengganu, receive intense precipitation during the Northeast Monsoon as moisture-laden air masses traverse the South China Sea.

Mean annual precipitation across Malaysia ranges from approximately 2,000 mm in coastal lowlands to over 5,000 mm in mountainous catchment areas (Suhaila et al., 2010). Spatial and temporal variability in precipitation patterns across Peninsular Malaysia has been documented by Desa and Niemczynowicz (1996) and Wong et al. (2009), who confirmed that the east coast experiences the country's most intense storm regimes.

### 2.8.2 Rainfall Frequency Modeling in Malaysia

Multiple empirical investigations have evaluated frequency analysis techniques on Malaysian precipitation records. Zalina et al. (2002) conducted comparative evaluations of candidate distributions for extreme rainfall in Malaysia, finding that Generalized Pareto and Pearson Type III models provided superior representations. Suhaila and Jemain (2007, 2008) investigated daily rainfall characteristics across Peninsular Malaysia, recommending normal-transformed and gamma mixture models for daily amounts.

Zin et al. (2009) evaluated L-moments and LQ-moments for annual maximum rainfall modeling in Peninsular Malaysia, demonstrating that three-parameter distribution models (GEV, GLO, and GNO) consistently outperformed traditional two-parameter formulations. In engineering practice, the Department of Irrigation and Drainage (DID) Malaysia published Hydrological Procedure No. 1 (DID, 2009), providing national guidelines for design storm estimation based on annual maximum series.

### 2.8.3 Regional and Global Context

Empirical studies across tropical Asia, Africa, and South America provide broader hydrological context. Teo and Grobe (2015) analyzed extreme precipitation trends in Singapore, identifying intensified extreme storm occurrences. Limsakul and Singhruck (2016) reported regional variability in extreme precipitation trends across Thailand. In tropical Africa, Olofintoye et al. (2009) applied L-moments to Nigerian rainfall records, identifying the Generalized Logistic distribution as the optimal model for annual maxima. Smithers and Schulze (2001) established regional design rainfall methodologies based on L-moments for Southern Africa.

Globally, Papalexiou and Koutsoyiannis (2013) examined daily extreme precipitation across thousands of hydrometric stations worldwide. Their findings established that heavy-tailed distributions characterize extreme rainfall globally, and that tropical regimes exhibit pronounced skewness and tail weights that diverge substantially from temperate climate expectations. This global evidence reinforces the necessity of adopting flexible distributions and evaluating alternatives to data decimation.

---

## 2.9 Research Gap

Although substantial literature addresses flood frequency modeling and L-moments theory, critical gaps remain regarding their application in tropical climates:

First, foundational frequency modeling methodologies were established using temperate catchment data where storm occurrences are rare and temporally dispersed. The direct transferability of these frameworks to tropical monsoon climates requires empirical verification (Koutsoyiannis, 2004; Papalexiou & Koutsoyiannis, 2013).

Second, as demonstrated by Volpi et al. (2019), conventional frequency analysis relies on data decimation through annual maximum filtering, discarding more than 99.7% of available daily observations. The quantitative implications of this data reduction in tropical regions, where multiple extreme events recur within the same annual cycle, remain largely unquantified across regional hydrometric networks.

Third, while studies have investigated rainfall frequency in Malaysia, comprehensive comparative evaluations assessing recurrence discrepancies between Annual Maximum Series and daily rainfall series using robust L-moments and multi-parameter distributions remain lacking.

These identified gaps establish the scientific justification for this research, which evaluates 20 hydrological gauging stations in Terengganu, Malaysia. A comprehensive treatment of the research gaps and their alignment with research objectives is provided in Chapter 4.

---

## 2.10 Summary

This chapter has synthesized the theoretical, mathematical, and empirical literature governing flood frequency analysis, with dedicated focus on the divergence between temperate and tropical rainfall modeling. 

The review demonstrates that classical frequency analysis frameworks, established around the Annual Maximum Series and two-parameter distributions, were formulated for temperate environments where extreme storms occur infrequently. In tropical monsoon environments such as Terengganu, Malaysia, seasonal monsoon circulations produce multiple severe storm systems within each annual cycle. Under these conditions, the conventional AMS approach causes severe information loss by discarding secondary extreme events, inducing systematic overestimation of return periods and underestimating actual hazard recurrence.

The theoretical foundation of the CTA framework, formulated by Volpi et al. (2019), proves that the average interarrival time of extreme events is invariant to process dependence structures, establishing a mathematical justification for utilizing complete observational records without data decimation. Because pure CTA was developed for continuous streamflow, adapting the framework to tropical daily precipitation requires addressing zero-inflation through a two-component model that benchmarks frequency on the complete calendar series while fitting L-moments to positive rainfall amounts.

Finally, the literature confirms that L-moments provide robust parameter estimation with lower sampling variance than conventional moments, and that flexible multi-parameter distributions, particularly the 4-Parameter Kappa distribution, are necessary to capture the pronounced positive skewness of tropical precipitation. The methodology for implementing this comparative framework is detailed in Chapter 3.

---

## References

*(See References chapter for complete reference list)*
