# CHAPTER 1

## INTRODUCTION

### 1.1 Research Background

Systematic precipitation data collection in Malaysia has been conducted over several decades, providing an extensive observational record for hydrological and climatological investigations. The Hydrology and Water Resources Division of the Department of Irrigation and Drainage (DID), Malaysia, maintains an extensive hydrometric network across the country to monitor and record rainfall regimes (DID, 2009). This historical dataset forms the empirical foundation for regional flood frequency modeling, water resource planning, and hydraulic infrastructure design.

Accurate precipitation frequency analysis is essential for sizing hydraulic infrastructure, assessing flood hazards, and managing surface water resources. Conventional flood frequency analysis relies primarily on the Annual Maximum Series (AMS) framework paired with standard probability distributions formulated for temperate climate regimes (Hosking & Wallis, 1997; Rao & Hamed, 2000). While this approach provides satisfactory estimates in temperate regions where severe weather events are sporadic and temporally dispersed, its application in tropical monsoon climates introduces structural limitations. In tropical environments, conventional AMS sampling discards secondary severe rainfall occurrences within each year, leading to information loss and inaccurate recurrence frequency estimation.

Terengganu, located on the eastern coast of Peninsular Malaysia, is characterized by an equatorial tropical climate governed by the Northeast Monsoon from November to March. The seasonal monsoon delivers recurring high-intensity precipitation events that differ fundamentally from the rainfall regimes of temperate regions. Consequently, the conventional AMS approach, which reduces an entire year of daily observations to a single maximum value, causes extensive information loss by discarding secondary extreme events that occur within the same annual cycle (Volpi et al., 2019).

The L-moments method offers established mathematical advantages over conventional product-moment and maximum likelihood estimators, primarily due to its robustness against outliers and reduced estimation bias in small sample sizes (Hosking, 1990). Formulated as linear combinations of probability-weighted moments (Greenwood et al., 1979), L-moments provide stable parameter estimates for heavy-tailed probability distributions. While the L-moments framework has been extensively applied to temperate Annual Maximum Series, its implementation on complete daily precipitation series within tropical monsoon climates remains limited. The primary motivation for this study is that daily rainfall series preserve all high-magnitude events throughout the annual cycle, avoiding the severe information loss caused by reducing observations to a single annual maximum (Volpi et al., 2019).

Accurate determination of extreme rainfall recurrence intervals is critical for flood hazard mitigation and hydraulic sizing. The frequent occurrence of torrential downpours during the monsoon season in Terengganu requires re-evaluating standard frequency analysis paradigms. This research adapts the L-moments framework to both Annual Maximum Series and daily precipitation records across 20 hydrological stations in Terengganu, evaluating an adapted Complete Time-Series Analysis (CTA) framework against the conventional AMS approach.

The implications of this research extend beyond local catchment planning. While geographically focused on Terengganu, the empirical findings provide methodological insights applicable to tropical monsoon regions globally. By clarifying how data sampling frameworks impact quantile estimation, this study supports more dependable flood risk assessment and drainage infrastructure design in equatorial regions.

This study conducts a comparative analysis of both Annual Maximum Series (AMS) and daily rainfall records compiled across 20 gauging stations in Terengganu. The research adapts the L-moments method to tropical conditions, evaluating candidate probability distributions and quantifying the systematic recurrence discrepancies between AMS and daily time series.

By evaluating both Annual Maximum Series and daily rainfall records using the L-moments method, this research establishes an empirical foundation for improved flood frequency analysis in tropical environments. The outcomes deliver a refined representation of precipitation recurrence in Terengganu, providing practical criteria for hydraulic design and regional flood hazard mitigation.

---

### 1.2 Problem Statement

Rainfall frequency modeling forms the basis for hydraulic infrastructure design, drainage network planning, and disaster mitigation. Conventional frequency analysis relies primarily on the Annual Maximum Series (AMS) framework, which extracts the single largest event in each year. While theoretically grounded in classical Extreme Value Theory for temperate climates (Gumbel, 1958; Coles, 2001), where extreme storms are rare and temporally dispersed, applying this approach to tropical monsoon climates introduces severe structural limitations.

Terengganu experiences an intense tropical monsoon regime characterized by prolonged and recurring precipitation surges during the Northeast Monsoon. Under these climatological conditions, multiple severe storms occur within a single annual cycle. The conventional AMS framework discards all secondary extreme storms within each year, retaining only one value per year. In a 30-year daily record, this data reduction eliminates more than 99.7% of available observations, discarding severe events that may exceed annual maxima from other years (Volpi et al., 2019).

This data reduction leads to a systematic misrepresentation of extreme event frequencies. In tropical regions, extreme storms recur with higher frequency than annual maximum models suggest. Discarding secondary extreme storms within the AMS framework leads to an overestimation of return periods, resulting in hydraulic infrastructure that is under-designed for actual recurrence frequencies.

Furthermore, conventional probability distributions formulated for temperate regimes, such as the two-parameter Gumbel or standard three-parameter distributions, lack the mathematical flexibility to model the pronounced positive skewness and heavy upper tails characteristic of tropical monsoon rainfall (Papalexiou & Koutsoyiannis, 2013). There is an essential requirement to evaluate more flexible distribution families, such as the 4-Parameter Kappa distribution, using robust parameter estimation methods.

This discrepancy demonstrates a fundamental limitation in current hydrological practices in Malaysia, which often follow temperate-based guidelines (DID, 2009). Addressing this research gap requires evaluating alternative analytical frameworks using L-moments on both annual and daily scales.

This thesis investigates the limitations of conventional Annual Maximum Series analysis in tropical climates, focusing on 20 hydrological gauging stations in Terengganu, Malaysia. It establishes an adapted analytical framework using L-moments and the 4-Parameter Kappa distribution to capture tropical rainfall characteristics, quantifying the overestimation factor inherent in conventional methods to support improved flood risk management.

---

### 1.3 Research Objectives

The primary objectives of this research are:

i. To estimate the distribution parameters of the rainfall datasets using the L-moments parameter estimation method.

ii. To identify the most accurate distribution model for the rainfall datasets using suitable performance evaluation metrics, specifically the Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI).

iii. To conduct return period analysis using the most accurate distribution model to estimate extreme rainfall quantiles for various return periods ranging from 2 to 100 years.

iv. To evaluate and quantify the degree of overestimation in return period analysis when using the conventional Annual Maximum Series (AMS) framework relative to the adapted Complete Time-Series Analysis (CTA) framework.

---

### 1.4 Research Questions

This research addresses the following specific research questions:

i. What are the estimated parameter values for candidate probability distributions across the 20 rainfall stations in Terengganu, Malaysia, using the L-moments method?

ii. Which probability distribution model provides the optimal fit for the rainfall datasets at each station based on MADI and MSDI goodness-of-fit criteria?

iii. What are the estimated return periods and design rainfall quantiles for extreme events across recurrence intervals from 2 to 100 years?

iv. What is the quantitative degree of overestimation in recurrence interval estimates when using the conventional Annual Maximum Series (AMS) framework relative to the adapted Complete Time-Series Analysis (CTA) framework?

---

### 1.5 Significance of Study

This research addresses an established limitation in hydrological frequency analysis, which relies primarily on Annual Maximum Series data. Formulated originally for temperate climatic regions where severe storms occur infrequently (Hosking & Wallis, 1997), standard methodologies can mischaracterize precipitation dynamics in tropical regimes. The significance of this study is detailed across four domains:

#### 1.5.1 Methodological Adaptation for Tropical Climates
There is a direct need for methodological frameworks that account for the unique characteristics of tropical monsoon climates. By incorporating both Annual Maximum Series and complete daily rainfall records, this research provides a comprehensive assessment of precipitation patterns. Applying the L-moments methodology to tropical daily rainfall series represents an advance in regional statistical hydrology, offering robust parameter estimation that is less sensitive to sample size limitations and extreme outliers.

#### 1.5.2 Enhanced Understanding of Extreme Precipitation Recurrence
Evaluating daily precipitation data alongside Annual Maximum Series using L-moments clarifies the true recurrence frequency of extreme storms in Terengganu. This empirical understanding is vital for flood mitigation planning, hydraulic structure sizing, and regional water resource management. Quantifying the recurrence discrepancy provides hydrologists with objective evidence regarding the limitations of traditional AMS assumptions.

#### 1.5.3 Regional and Global Relevance
While geographically focused on Terengganu, the empirical findings have broader significance for tropical hydrology. Adapting analytical techniques for tropical monsoon regimes provides a methodological reference for other equatorial countries facing similar flood frequency modeling challenges.

#### 1.5.4 Engineering and Hydraulic Design Applications
The quantile estimates generated from this research provide practical design parameters for flood mitigation infrastructure, drainage channels, culverts, and retention basins. By quantifying the overestimation factor inherent in annual maximum models, this research assists drainage engineers and water resource planners in avoiding structural under-design.

---

### 1.6 Scope and Limitations of Study

This research is defined within specific geographical, temporal, methodological, and analytical boundaries:

#### 1.6.1 Geographical Scope
The study encompasses 20 continuous rainfall gauging stations located across Terengganu, Malaysia, managed by the Department of Irrigation and Drainage (DID), Malaysia. These stations represent diverse topographic and coastal conditions across the state.

#### 1.6.2 Temporal Scope
The investigation utilizes multi-decadal historical daily rainfall records collected by the DID. Both Annual Maximum Series (AMS) and complete daily precipitation records are evaluated to compare recurrence behaviors across timescales.

#### 1.6.3 Methodological Scope
The study employs the L-moments method for sample moment computation (mean $\lambda_1$, scale $\lambda_2$, L-skewness $\tau_3$, and L-kurtosis $\tau_4$) and distribution parameter estimation. Nine candidate probability distributions are evaluated: Gumbel (GUM), Normal (NOR), Exponential (EXP), Generalized Extreme Value (GEV), Generalized Logistic (GLO), Generalized Normal (GNO), Generalized Pareto (GPA), Pearson Type III (PE3), and 4-Parameter Kappa (K4D). Goodness of fit is evaluated using the Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI) plotted against Gringorten empirical plotting positions.

#### 1.6.4 Analytical Scope
The analysis calculates design rainfall quantiles across standard return periods of 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100 years. Furthermore, the Overestimation Factor (OE) is formulated and evaluated at the 99th percentile of complete daily precipitation to quantify the discrepancy between AMS and daily series.

#### 1.6.5 Study Limitations
The findings of this study are subject to the following limitations:
i. The empirical data are drawn from gauging stations in Terengganu, Malaysia; regional extrapolation to non-monsoonal tropical climates requires separate verification.
ii. Parameter estimation is conducted exclusively through the L-moments method; product moments and maximum likelihood methods are not applied.
iii. Distribution fitting is restricted to the nine specified candidate distributions.
iv. The analysis assumes climate stationarity across the historical record; non-stationary climate change projections are not modeled.

---

### 1.7 Organization of Thesis

This thesis is structured into six chapters:

* **Chapter 1: Introduction** presents the research background, problem statement, research objectives, research questions, significance, and scope of the study.
* **Chapter 2: Literature Review** provides an overview of flood frequency analysis, tracing the historical development from conventional product moments to probability-weighted moments and L-moments, evaluating candidate distribution families, and reviewing hydrological studies in tropical Malaysia.
* **Chapter 3: Methodology** details the mathematical formulations of L-moments, parameter estimation algorithms for the nine candidate distributions, goodness-of-fit metrics (MADI and MSDI), quantile estimation procedures, and the formulation of the overestimation factor.
* **Chapter 4: Research Gap** establishes the theoretical and empirical limitations of current flood frequency practices in tropical regions, focusing on data decimation, zero-inflation adaptations, and the lack of daily-based L-moment modeling.
* **Chapter 5: Results and Discussion** presents the empirical findings across the 20 gauging stations, detailing L-moment statistics, distribution selection results, quantile curves, sensitivity analyses, and overestimation factor quantifications.
* **Chapter 6: Conclusion** synthesizes the core findings in relation to each research objective, outlines the academic and practical contributions, acknowledges limitations, and provides recommendations for engineering practice and future research.
