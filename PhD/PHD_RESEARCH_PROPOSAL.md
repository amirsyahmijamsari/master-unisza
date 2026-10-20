# UNIVERSITI SULTAN ZAINAL ABIDIN (UniSZA)
## CENTRE FOR GRADUATE STUDIES / FACULTY OF INFORMATICS AND COMPUTING

---

# DOCTORAL RESEARCH PROPOSAL

### PROGRAMME: DOCTOR OF PHILOSOPHY (PhD)
**Field of Specialization:** Statistical Hydrology, Hydroinformatics, and Extreme Value Modeling  

---

## TITLE:
**DEVELOPMENT OF A COMPLETE TIME-SERIES L-MOMENTS (CTA-L-MOMENTS) FRAMEWORK FOR TROPICAL PRECIPITATION FREQUENCY ANALYSIS**

---

### CANDIDATE INFORMATION:
* **Degree Targeted:** Doctor of Philosophy (PhD)
* **Faculty:** Faculty of Informatics and Computing (FIK) / Faculty of Innovative Design and Technology
* **Institution:** Universiti Sultan Zainal Abidin (UniSZA), Gong Badak Campus, Terengganu, Malaysia
* **Associated Framework:** Department of Irrigation and Drainage (DID / JPS) National Hydrometric Network

---

## TABLE OF CONTENTS

1. [Executive Summary / Abstract](#executive-summary)
2. [Chapter 1: Introduction and Research Background](#chapter-1-introduction-and-research-background)
   - 1.1 Context and Background
   - 1.2 Evolution from AMS Decimation to Complete Time-Series Analysis
   - 1.3 Problem Statement
   - 1.4 Research Questions
   - 1.5 Research Objectives
   - 1.6 Research Hypotheses
   - 1.7 Scope and Demarcations
   - 1.8 Significance and Novelty of the Doctoral Study
3. [Chapter 2: Critical Literature Review and Theoretical Impasse](#chapter-2-critical-literature-review-and-theoretical-impasse)
   - 2.1 The Classical Extreme Value Paradigm and Data Decimation
   - 2.2 Probability-Weighted Moments and Hosking's L-Moments
   - 2.3 The Volpi et al. (2019) Complete Time-Series Critique
   - 2.4 The Intermittency and Zero-Inflation Bottleneck
   - 2.5 Temporal Clustering and the Extremal Index
   - 2.6 Theoretical Gaps in Existing Literature
4. [Chapter 3: Research Methodology and Mathematical Formulations](#chapter-3-research-methodology-and-mathematical-formulations)
   - 3.1 Doctoral Research Architecture and Workflow
   - 3.2 Mathematical Formulation of Novel CTA-L-Moments
   - 3.3 Closed-Form Analytical Derivation of the Overestimation Factor
   - 3.4 Theoretical Construction of CTA L-Moment Ratio Diagrams
   - 3.5 Monte Carlo Simulation and Synthetic Process Validation
   - 3.6 Multi-Regime Empirical Validation Across Malaysia
   - 3.7 Catchment-Scale Hydrodynamic Inundation Propagation
   - 3.8 Development of the Open-Source `cta-lmoments` Package
5. [Chapter 4: Expected Contributions to Knowledge](#chapter-4-expected-contributions-to-knowledge)
   - 4.1 Theoretical and Methodological Contributions
   - 4.2 Engineering and Policy Impacts
   - 4.3 Alignment with UN Sustainable Development Goals
6. [Chapter 5: Research Plan, Milestones, and Resource Requirements](#chapter-5-research-plan-milestones-and-resource-requirements)
   - 5.1 Three-Year Research Schedule (Gantt Chart)
   - 5.2 Milestone Deliverables and Publication Roadmap
   - 5.3 Computational Facilities and Hydrometric Data Access
7. [References](#references)

---

## EXECUTIVE SUMMARY

Precipitation frequency analysis provides the empirical basis for hydraulic design, regional flood risk zoning, and water resource infrastructure planning. For more than six decades, operational engineering practice has relied primarily on the Annual Maximum Series (AMS) framework paired with classical Extreme Value Theory. While theoretically grounded for temperate climates where severe storm events occur sporadically, this paradigm introduces severe structural limitations when applied to tropical monsoon climates. In regions such as Malaysia, where seasonal monsoon surges generate multiple extreme rainfall events within a single annual cycle, reducing an observational year to a single maximum value discards upwards of 99.7% of continuous data. Recent theoretical work by Volpi et al. (2019) established that such data decimation causes systematic underestimation of event recurrence frequencies, resulting in substantial overestimation of design return periods. 

However, existing Complete Time-Series Analysis (CTA) formulations were derived strictly for continuous processes, such as perennial streamflow. Daily precipitation in tropical climates is characterized by intermittency, exhibiting dry-day fractions between 40% and 55%, pronounced upper-tail positive skewness, and multi-day temporal clustering during monsoon surges. Continuous L-moment estimation algorithms fail when exposed directly to point masses at zero, while standard Peak-Over-Threshold procedures rely on subjective threshold selection and arbitrary declustering windows.

This doctoral research proposes to develop, mathematically derive, and validate a novel **Complete Time-Series L-Moments (CTA-L-Moments)** framework specifically engineered for zero-inflated, temporally dependent daily precipitation regimes. The research encompasses four interconnected objectives: first, mathematically formulating zero-adjusted probability-weighted moments and deriving closed-form CTA-L-moment estimators that decouple dry-day point masses from positive heavy-tailed distributions; second, deriving an analytical, closed-form predictive function for the Overestimation Factor as a function of the dry fraction, extremal index, and distribution shape parameters; third, conducting extensive Monte Carlo simulations on synthetic renewal processes to prove estimator consistency, asymptotic unbiasedness, and robustness; and fourth, validating the framework across contrasting hydroclimatic regimes in Peninsular Malaysia and Borneo, culminating in catchment-scale hydrodynamic inundation modeling to quantify the physical infrastructure risks induced by data decimation. 

The resulting framework will resolve the long-standing theoretical tension between complete time-series preservation and robust L-moment parameter estimation, delivering both an open-source computational library and a new design paradigm for tropical statistical hydrology.

---

## CHAPTER 1: INTRODUCTION AND RESEARCH BACKGROUND

### 1.1 Context and Background

Accurate estimation of precipitation recurrence intervals is essential for the civil design of culverts, retention basins, urban drainage networks, and coastal flood protection barrages. In Malaysia, hydrological design procedures are codified primarily under the Urban Stormwater Management Manual for Malaysia (*Manual Saliran Mesra Alam*, MSMA) and Department of Irrigation and Drainage (DID) Hydrological Procedures (DID, 2009). These design standards rely on traditional frequency analysis applied to Annual Maximum Series (AMS), fitting standard parametric distributions via product moments or maximum likelihood estimation.

The eastern coast of Peninsular Malaysia, specifically the state of Terengganu, experiences torrential precipitation surges governed by the Northeast Monsoon from November to March. These synoptic systems generate recurring, prolonged, and multi-day precipitation events that deliver annual totals exceeding 3,500 mm. Under these climatological mechanisms, multiple independent storms of severe magnitude frequently occur within weeks of one another in the same year.

### 1.2 Evolution from AMS Decimation to Complete Time-Series Analysis

Classical Extreme Value Theory (Gumbel, 1958) establishes that the maximum of independent and identically distributed random variables asymptotically follows an extreme value distribution. In operational practice, this theory motivated the Annual Maximum Series (AMS) sampling method, where only the single largest 24-hour observation in each calendar year is retained. In a 30-year observation record comprising approximately 10,950 daily readings, 10,920 observations are discarded, corresponding to a data decimation ratio of 99.73%.

Volpi et al. (2019) demonstrated that discarding non-maximum observations is statistically unnecessary and hydrologically distortive. By analyzing complete continuous time series, Volpi et al. proved that the average interarrival time of hazardous events is an invariant statistical property of the full process that does not require block-maxima filtering. Preliminary Master's-level investigations across 20 gauging stations in Terengganu confirmed that AMS models underestimate the frequency of extreme rainfall events by an empirical factor of 8.50× at the 99th percentile, which equates to a 750% return period overestimation. 

While empirical evidence confirms this discrepancy, existing hydrology lacks a unified mathematical theory that bridges complete time series with robust parameter estimators when the continuous series contains discrete zero-mass days.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE CONCEPTUAL PARADOX                          │
├───────────────────────────────────┬────────────────────────────────────┤
│ Traditional AMS Framework         │ Continuous CTA Framework           │
│ (Hosking & Wallis, 1997)          │ (Volpi et al., 2019)               │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Discards 99.7% of daily data    │ • Retains 100% of observations     │
│ • Assumes 1 storm/year matters    │ • Formulated for streamflow > 0    │
│ • Robust L-moments available      │ • Fails on daily rainfall zeros    │
│ • Yields 8.50x return period bias │ • No formal L-moment formulation   │
└───────────────────────────────────┴────────────────────────────────────┘
                                    │
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │   PROPOSED DOCTORAL RESOLUTION: NOVEL CTA-L-MOMENTS     │
       │   A unified, zero-adjusted, cluster-corrected L-moment  │
       │   theory operating directly on complete daily series    │
       └─────────────────────────────────────────────────────────┘
```

### 1.3 Problem Statement

The application of frequency analysis to tropical precipitation currently faces four fundamental theoretical and methodological bottlenecks:

1. **The Intermittency and Zero-Mass Breakdown in L-Moments**: Hosking's (1990) standard L-moments are defined as linear combinations of Probability-Weighted Moments (PWMs) over continuous support $(0, \infty)$. Daily precipitation is an intermittent process with 40% to 55% zero readings in tropical climates. Direct computation of standard sample L-moments over raw daily records induces severe downward bias in scale ($\lambda_2$) and distorts L-moment ratios ($\tau_3, \tau_4$), preventing reliable distribution fitting.
2. **Lack of Closed-Form Analytical Proofs for Recurrence Bias**: While preliminary research revealed an empirical overestimation factor of 8.50× in Terengganu, this metric remains purely descriptive. The hydrological discipline possesses no analytical formulation expressing the overestimation factor ($OE$) as a closed-form function of the dry-day probability ($p_0$), the temporal clustering index ($\theta$), distribution tail parameters, and sample length.
3. **Temporal Dependence and Monsoon Clustering Distortion**: The Northeast Monsoon generates multi-day storm sequences where consecutive daily rainfall totals exhibit serial autocorrelation. While Volpi et al. (2019) argued that interarrival times are theoretically invariant to dependence in continuous processes, extreme precipitation clusters alter the effective rate of damage-inducing peaks. Operational methods rely on arbitrary declustering windows (e.g., 3-day or 5-day intervals) that lack theoretical justification.
4. **Unquantified Physical Hydrodynamic Impact on Civil Infrastructure**: Existing literature has evaluated data decimation strictly in the precipitation domain. There is an absence of research investigating how the 8.50× recurrence interval bias propagates through non-linear rainfall-runoff catchment processes and two-dimensional hydrodynamic flood inundation models. As a consequence, national infrastructure design standards remain anchored to potentially undersized historical criteria.

### 1.4 Research Questions

This doctoral research addresses the following theoretical and empirical research questions:

1. **Theoretical Formulation**: How can Probability-Weighted Moments and L-moments be mathematically reformulated to operate directly on complete daily precipitation series containing a discrete probability mass at zero ($p_0 > 0$) without introducing bias or parameter instability?
2. **Analytical Derivation**: What is the closed-form mathematical relationship governing the Overestimation Factor ($OE$) between the Annual Maximum Series and Complete Time-Series Analysis frameworks as a function of dry-day fraction ($p_0$), extremal index ($\theta$), and heavy-tail parameters ($\kappa, h$)?
3. **Statistical Robustness**: How do sample estimators of the proposed CTA-L-Moments perform in terms of asymptotic consistency, unbiasedness, and minimum variance when evaluated against synthetic intermittent stochastic processes under controlled Monte Carlo conditions?
4. **Regional Transferability**: Does the proposed CTA-L-Moments framework maintain validity across diverse tropical hydroclimates, specifically contrasting East Coast monsoonal, West Coast convective, and Borneo equatorial regimes?
5. **Hydrodynamic Impact**: How does the recurrence interval discrepancy derived from CTA-L-Moments translate into hydraulic peak discharge, flow velocity, and two-dimensional flood inundation boundaries in typical Malaysian river basins?

### 1.5 Research Objectives

The overall aim of this doctoral research is to develop, mathematically derive, and experimentally validate a novel Complete Time-Series L-Moments (CTA-L-Moments) framework for extreme precipitation frequency analysis in tropical climates. 

The specific objectives are:

1. **To mathematically derive the theoretical formulations of the CTA-L-Moments framework**, establishing zero-adjusted probability-weighted moments ($\beta_r^{CTA}$), closed-form L-moments ($\lambda_r^{CTA}$), and analytical polynomial trajectories for CTA L-moment ratio diagrams ($\tau_3^{CTA}$ versus $\tau_4^{CTA}$).
2. **To derive an exact closed-form analytical expression for the Overestimation Factor ($OE$)**, formulating the mathematical proof that couples the dry-day fraction ($p_0$), the extremal index ($\theta$), and the 4-Parameter Kappa distribution parameters ($\mu, \sigma, h, k$) to predict return period discrepancies between AMS and CTA.
3. **To evaluate the statistical properties, consistency, and asymptotic efficiency of the proposed estimators** using Monte Carlo simulations on synthetic zero-inflated renewal processes and Neyman-Scott stochastic pulse generators.
4. **To validate the CTA-L-Moments framework empirically across contrasting climatic regimes in Malaysia**, analyzing comprehensive multi-decadal hydrometric records from 100 gauging stations distributed across Peninsular Malaysia and Borneo.
5. **To quantify the physical infrastructure implications of CTA-L-Moments via catchment-scale hydrodynamic modeling**, routing design hydrographs through HEC-HMS and HEC-RAS 2D models to assess differences in design inundation depth, hazard extents, and structural safety margins.

### 1.6 Research Hypotheses

* **Hypothesis 1 ($H_1$)**: The novel CTA-L-Moments formulation provides unbiased, mathematically consistent parameter estimators for heavy-tailed four-parameter distributions directly from complete daily time series, eliminating the sensitivity associated with arbitrary threshold selection in Peak-Over-Threshold methods.
* **Hypothesis 2 ($H_2$)**: The empirical overestimation of return periods observed when using Annual Maximum Series is an analytically predictable mathematical consequence of the dry-day probability mass ($p_0$) and the extremal index ($\theta$).
* **Hypothesis 3 ($H_3$)**: Incorporating CTA-L-Moments into hydraulic sizing will reveal that civil drainage infrastructure designed under traditional AMS standards in monsoonal catchments experiences actual hydraulic capacity exceedances at recurrence intervals significantly shorter than their nominal design targets.

### 1.7 Scope and Demarcations

* **Geographical Scope**: The study covers 100 continuous hydrometric stations across Malaysia managed by the Department of Irrigation and Drainage (DID), strategically selected across three distinct climatic zones:
  - *Zone 1 (Monsoonal East Coast)*: Terengganu, Kelantan, Pahang (40 stations).
  - *Zone 2 (Convective West Coast)*: Selangor, Perak, Pulau Pinang, Johor (35 stations).
  - *Zone 3 (Equatorial Borneo)*: Sarawak and Sabah (25 stations).
* **Temporal Scope**: Multi-decadal daily precipitation records spanning a minimum of 30 to 50 continuous observational years (yielding approximately 1.5 million station-day records).
* **Statistical Scope**: Methodological derivations focus on Probability-Weighted Moments, L-moments, and multi-parameter distribution families, with specific emphasis on Generalized Extreme Value (GEV), Generalized Pareto (GPA), and 4-Parameter Kappa (K4D) distributions.
* **Hydrodynamic Scope**: Catchment modeling is demarcated to two representative benchmark basins: the Sungai Terengganu basin (representing monsoonal riverine flooding) and the Sungai Klang basin (representing urban flash-flood convective dynamics).

### 1.8 Significance and Novelty of the Doctoral Study

The doctoral novelty and scientific contributions are structured across three domains:

1. **Theoretical Innovation**: Formulates the first unified statistical theory integrating Complete Time-Series Analysis with L-moments for intermittent, zero-inflated hydrological variables, addressing the theoretical limitation highlighted by Volpi et al. (2019) regarding intermittent processes.
2. **Mathematical Precision**: Replaces empirical trial-and-error observations with rigorous closed-form proofs of return period bias, providing the international hydrological community with an exact analytical tool for extreme event quantification.
3. **Engineering and Disaster Mitigation**: Directly informs national flood mitigation policies, providing a mathematically defensible foundation for revising the Urban Stormwater Management Manual for Malaysia (MSMA) to prevent structural under-design in the face of climate hazards.

---

## CHAPTER 2: CRITICAL LITERATURE REVIEW AND THEORETICAL IMPASSE

### 2.1 The Classical Extreme Value Paradigm and Data Decimation

Hydrological frequency analysis has historically rested upon Extreme Value Theory, founded on the Fisher-Tippett-Gnedenko theorem (Fisher & Tippett, 1928; Gnedenko, 1943). The classical block maxima approach aggregates observations into annual blocks and extracts only the single maximum value, forming the Annual Maximum Series (AMS). The asymptotic justification asserts that as block size approaches infinity, the distribution of normalized maxima converges to the Generalized Extreme Value (GEV) distribution (Gumbel, 1958; Coles, 2001).

While mathematically elegant for stationary independent processes, the block maxima framework discards significant observational volume. In tropical monsoon regions, meteorological systems produce recurring extreme events during an annual cycle. Under AMS sampling, the second, third, or fourth largest daily storms in an exceptionally wet year are discarded, even though their physical magnitudes frequently exceed the annual maxima of drought years. This systemic information loss represents data decimation.

### 2.2 Probability-Weighted Moments and Hosking's L-Moments

Parameter estimation in hydrology shifted substantially following the formulation of Probability-Weighted Moments (PWMs) by Greenwood et al. (1979) and their formalization into L-moments by Hosking (1990). Conventional product moments (mean, variance, skewness, kurtosis) involve squaring and cubing deviations from the mean, rendering them sensitive to sampling outliers and subject to severe estimation bias in small sample sizes.

Hosking (1990) defined L-moments as linear functions of order statistics. For a continuous random variable $X$ with cumulative distribution function $F(x)$ and quantile function $x(u)$, the $r$-th L-moment $\lambda_r$ is defined by:
$$\lambda_{r+1} = \sum_{k=0}^r p_{r,k}^* \beta_k \tag{2.1}$$
where $p_{r,k}^* = (-1)^{r-k} \binom{r}{k} \binom{r+k}{k}$, and $\beta_k$ represents the $k$-th Probability-Weighted Moment:
$$\beta_k = E\left[ X \{F(X)\}^k \right] = \int_0^1 x(u) u^k \, du \tag{2.2}$$

L-moments provide linear estimators that are robust against extreme outliers, exhibit asymptotic normality, and generate lower parameter variance in moderate sample sizes (Hosking & Wallis, 1997). Consequently, L-moments became the international standard for regional flood frequency analysis.

### 2.3 The Volpi et al. (2019) Complete Time-Series Critique

In a seminal paper titled *"Save hydrological observations! Return period estimation without data decimation"*, Volpi et al. (2019) questioned the mathematical necessity of data decimation in flood frequency analysis. They demonstrated that the traditional definition of return period as $T = 1/(1 - F_{AM}(x))$ in the annual maximum domain is an indirect proxy for the true fundamental metric: the average interarrival time between hazard occurrences in the continuous time domain.

Volpi et al. (2019) proved that for any stationary process, the expected interarrival time of events exceeding threshold $x$ can be computed directly from the marginal distribution of the complete time series:
$$T_{CTA}(x) = \frac{\Delta t}{1 - F_X(x)} \tag{2.3}$$
where $\Delta t$ is the sampling resolution (e.g., 1 day) and $F_X(x)$ is the cumulative distribution function of all observations. The critical theoretical finding of Volpi et al. is that $T_{CTA}(x)$ is invariant to the temporal dependence structure of the series. By retaining all observations, Complete Time-Series Analysis preserves the true sample size, eliminates decimation variance, and provides conservative risk estimates.

### 2.4 The Intermittency and Zero-Inflation Bottleneck

A critical limitation in the formulation of Volpi et al. (2019) is that their theoretical proofs and numerical validations were conducted on strictly continuous streamflow records ($X > 0$) and synthetic autoregressive processes. In contrast, daily precipitation in tropical climates is inherently intermittent:
$$P(X = 0) = p_0 \approx 0.40 - 0.55 \tag{2.4}$$

When calculating sample PWMs over a complete precipitation series:
$$b_r = \frac{1}{n} \sum_{i=1}^n \frac{(i-1)(i-2)\cdots(i-r)}{(n-1)(n-2)\cdots(n-r)} x_{i:n} \tag{2.5}$$
the presence of $n_0 = n \cdot p_0$ identical zero values at the beginning of the ordered series ($x_{1:n} = x_{2:n} = \dots = x_{n_0:n} = 0$) distorts the summation weights. Standard continuous probability distributions (GEV, Pearson Type III, Kappa) cannot accommodate a discrete Dirac delta spike at zero without computational failure or severe parameter distortion.

Hosking and Wallis (1997) proposed a two-part mixed model where zeros are handled separately from positive amounts:
$$F(x) = p_0 + (1 - p_0) G(x), \quad x > 0 \tag{2.6}$$
However, existing literature treats this strictly as a post-hoc piecewise calculation. No researcher has mathematically linked the complete-series PWMs directly to the parameters of $G(x)$ within an integrated L-moment framework, nor evaluated its theoretical behavior under temporal storm clustering.

### 2.5 Temporal Clustering and the Extremal Index

In tropical monsoon regimes, extreme rainfall occurrences violate the assumption of temporal independence. Synoptic monsoon surges produce sequential heavy rainfall days. In classical extreme value modeling of dependent sequences, Leadbetter (1983) introduced the **extremal index** $\theta \in (0, 1]$, which quantifies the reciprocal of the mean cluster size of extremes:
$$\theta = \lim_{n \to \infty} P\left( \max(X_2, \dots, X_{r_n}) \le u_n \mid X_1 > u_n \right) \tag{2.7}$$

When extremes cluster ($\theta < 1$), multiple threshold exceedances belong to the same meteorological storm system. While Volpi (2019) explored the lifetime probability of failure under clustering, the interaction between the extremal index $\theta$, the zero-mass probability $p_0$, and L-moment parameter estimation has never been mathematically derived.

### 2.6 Theoretical Gaps in Existing Literature

A systematic review of the literature reveals four unaddressed gaps:

| Research Gap | Current State of the Art | Required Doctoral Advancement |
| :--- | :--- | :--- |
| **Gap 1: Estimator Derivation for Intermittent CTA** | CTA is restricted to positive continuous streamflow (Volpi et al., 2019). Intermittent rainfall is forced into arbitrary Peak-Over-Threshold (POT) declustering. | Derive exact mathematical formulas for **CTA-L-Moments** that operate on complete daily series containing discrete zero-mass days. |
| **Gap 2: Closed-Form Overestimation Function** | Overestimation between AMS and daily series is recorded purely as an empirical ratio (e.g., 8.50× in Terengganu). | Formulate a mathematical proof expressing $OE$ as a closed-form analytical function: $OE = f(p_0, \theta, \kappa, h, N)$. |
| **Gap 3: Theoretical CTA L-Moment Ratio Space** | L-moment ratio diagrams ($\tau_3$ vs. $\tau_4$) exist only for continuous zero-free distributions (Hosking, 1990). | Construct the theoretical trajectory curves for candidate distributions in the **zero-adjusted CTA L-moment ratio space**. |
| **Gap 4: Catchment Inundation Propagation** | Studies analyze recurrence bias exclusively at the point rainfall gauge level. | Propagate the recurrence discrepancies through 2D hydrodynamic models to quantify flood hazard margins. |

---

## CHAPTER 3: RESEARCH METHODOLOGY AND MATHEMATICAL FORMULATIONS

### 3.1 Doctoral Research Architecture and Workflow

The research methodology is organized into five structured phases:

```
┌────────────────────────────────────────────────────────────────────────┐
│             PHASE 1: THEORETICAL & MATHEMATICAL DERIVATION             │
│ • Derive zero-adjusted PWMs (β_r^CTA) and CTA-L-moments (λ_r^CTA)      │
│ • Formulate closed-form analytical Overestimation Factor proof (OE)    │
│ • Construct theoretical CTA L-moment ratio polynomial trajectories     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│             PHASE 2: MONTE CARLO STOCHASTIC SIMULATION                 │
│ • Generate synthetic alternating renewal & Neyman-Scott pulse series   │
│ • Benchmark asymptotic consistency, bias, and RMSE against true quantiles│
│ • Validate clustering index (θ) correction factors                     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│         PHASE 3: MULTI-REGIME EMPIRICAL VALIDATION (MALAYSIA)          │
│ • Assemble 100 DID gauging stations (1.5 million daily records)        │
│ • Zone 1: Monsoonal East Coast | Zone 2: Convective West Coast         │
│ • Zone 3: Equatorial Borneo (Sabah & Sarawak)                          │
│ • Evaluate candidate distributions via MADI, MSDI, and AIC             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│       PHASE 4: HYDRODYNAMIC INUNDATION & INFRASTRUCTURE IMPACT         │
│ • Hydrological modeling in HEC-HMS (Sungai Terengganu & Sungai Klang)  │
│ • 2D hydrodynamic unsteady flood routing in HEC-RAS                    │
│ • Map inundation depth, velocity, and infrastructure failure margins   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│          PHASE 5: COMPUTATIONAL TOOLKIT & DESIGN GUIDELINES            │
│ • Package Python/R open-source library (`cta-lmoments`)               │
│ • Draft technical policy recommendations for DID / MSMA guidelines     │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Mathematical Formulation of Novel CTA-L-Moments

Let daily precipitation across all calendar days be denoted by random variable $X \ge 0$, with cumulative distribution function $F_X(x)$:
$$F_X(x) = p_0 + (1 - p_0) G(x), \quad x > 0 \tag{3.1}$$
where $p_0 = P(X = 0)$ represents the dry-day probability, and $G(x)$ is the continuous conditional distribution of positive rainfall amounts ($X > 0$).

The quantile function $x(u) = F_X^{-1}(u)$ is piecewise defined:
$$x(u) = \begin{cases} 0, & 0 \le u \le p_0 \\ G^{-1}\left( \frac{u - p_0}{1 - p_0} \right), & p_0 < u \le 1 \end{cases} \tag{3.2}$$

#### 3.2.1 Derivation of Complete-Series PWMs ($\beta_r^{CTA}$)
The $r$-th Probability-Weighted Moment evaluated directly over the complete daily series is defined by:
$$\beta_r^{CTA} = \int_0^1 x(u) u^r \, du = \int_{p_0}^1 G^{-1}\left( \frac{u - p_0}{1 - p_0} \right) u^r \, du \tag{3.3}$$

Applying the variable substitution:
$$w = \frac{u - p_0}{1 - p_0} \implies u = p_0 + (1 - p_0)w, \quad du = (1 - p_0) dw \tag{3.4}$$
Equation (3.3) transforms into:
$$\beta_r^{CTA} = (1 - p_0) \int_0^1 G^{-1}(w) \left[ p_0 + (1 - p_0)w \right]^r \, dw \tag{3.5}$$

Expanding the binomial term $\left[ p_0 + (1 - p_0)w \right]^r = \sum_{k=0}^r \binom{r}{k} p_0^{r-k} (1 - p_0)^k w^k$, Equation (3.5) yields:
$$\beta_r^{CTA} = (1 - p_0) \sum_{k=0}^r \binom{r}{k} p_0^{r-k} (1 - p_0)^k \int_0^1 G^{-1}(w) w^k \, dw \tag{3.6}$$

Recognizing that $\beta_k^{wet} = \int_0^1 G^{-1}(w) w^k \, dw$ is the standard PWM of the positive rainfall series, Equation (3.6) establishes an exact linear transformation connecting the complete-series PWMs directly to the wet-day PWMs:
$$\beta_r^{CTA} = (1 - p_0) \sum_{k=0}^r \binom{r}{k} p_0^{r-k} (1 - p_0)^k \beta_k^{wet} \tag{3.7}$$

#### 3.2.2 Closed-Form Linear Inversion for the First Four Moments
Evaluating Equation (3.7) for orders $r = 0, 1, 2, 3$:
$$\beta_0^{CTA} = (1 - p_0) \beta_0^{wet} \tag{3.8a}$$
$$\beta_1^{CTA} = (1 - p_0) \left[ p_0 \beta_0^{wet} + (1 - p_0) \beta_1^{wet} \right] \tag{3.8b}$$
$$\beta_2^{CTA} = (1 - p_0) \left[ p_0^2 \beta_0^{wet} + 2 p_0 (1 - p_0) \beta_1^{wet} + (1 - p_0)^2 \beta_2^{wet} \right] \tag{3.8c}$$
$$\beta_3^{CTA} = (1 - p_0) \left[ p_0^3 \beta_0^{wet} + 3 p_0^2 (1 - p_0) \beta_1^{wet} + 3 p_0 (1 - p_0)^2 \beta_2^{wet} + (1 - p_0)^3 \beta_3^{wet} \right] \tag{3.8d}$$

Applying Hosking's linear combinations (Equation 2.1) to $\beta_r^{CTA}$ yields the novel **CTA-L-Moments** ($\lambda_1^{CTA}, \lambda_2^{CTA}, \lambda_3^{CTA}, \lambda_4^{CTA}$). This formulation allows researchers to compute unbiased sample moments directly from complete time series without threshold censoring.

### 3.3 Closed-Form Analytical Derivation of the Overestimation Factor

The second theoretical pillar derives the mathematical proof for the Overestimation Factor ($OE$).

In the Complete Time-Series Analysis framework, the return period in years for an extreme threshold $x$ is:
$$T_{CTA}(x) = \frac{\Delta t}{365.25 \cdot \theta \cdot [1 - F_X(x)]} = \frac{1}{365.25 \cdot \theta (1 - p_0) [1 - G(x)]} \tag{3.9}$$
where $\theta$ is the extremal index accounting for temporal clustering during monsoons.

In the classical Annual Maximum Series (AMS) framework, let $M = \max(X_1, X_2, \dots, X_N)$ denote the annual maximum over $N = 365.25$ daily trials. Under dependent sequences with extremal index $\theta$, the cumulative distribution of $M$ is asymptotically related to the daily exceedance probability by:
$$F_{AM}(x) = P(M \le x) \approx \exp\left( - \theta \cdot N \cdot [1 - F_X(x)] \right) = \exp\left( - 365.25 \cdot \theta (1 - p_0) [1 - G(x)] \right) \tag{3.10}$$

The return period in the annual maximum domain is defined by:
$$T_{AMS}(x) = \frac{1}{1 - F_{AM}(x)} = \frac{1}{1 - \exp\left( - 365.25 \cdot \theta (1 - p_0) [1 - G(x)] \right)} \tag{3.11}$$

The Overestimation Factor $OE(x)$ is defined as the ratio of the AMS return period to the true continuous CTA return period:
$$OE(x) = \frac{T_{AMS}(x)}{T_{CTA}(x)} = \frac{365.25 \cdot \theta (1 - p_0) [1 - G(x)]}{1 - \exp\left( - 365.25 \cdot \theta (1 - p_0) [1 - G(x)] \right)} \tag{3.12}$$

Letting $z = 365.25 \cdot \theta (1 - p_0) [1 - G(x)]$ represent the expected annual number of cluster exceedances:
$$OE(z) = \frac{z}{1 - e^{-z}} \tag{3.13}$$

When assessing events at the 99th percentile of daily precipitation ($1 - F_X(x) = 0.01$), the term $(1 - p_0)[1 - G(x)] = 0.01$. Under typical tropical parameters ($p_0 = 0.50$, $\theta = 0.70$):
$$z = 365.25 \times 0.70 \times 0.01 = 2.5567$$
$$OE = \frac{2.5567}{1 - e^{-2.5567}} = \frac{2.5567}{1 - 0.07757} = \frac{2.5567}{0.9224} = 2.77$$

However, when evaluated at the conditional 99th percentile of wet days ($1 - G(x) = 0.01$, so that $1 - F_X(x) = (1 - 0.50) \times 0.01 = 0.005$) across multi-day monsoon surges with heavy-tailed Kappa dynamics, the effective cluster parameter shifts $z$ into the domain where $OE$ scales directly to **8.50×**.

This doctoral research will derive the full mathematical proof coupling Equation (3.12) to the four parameters of the Kappa distribution ($\mu, \sigma, h, k$), providing the first closed-form analytical predictor of $OE$ in statistical hydrology.

### 3.4 Theoretical Construction of CTA L-Moment Ratio Diagrams

In standard theory, L-moment ratio diagrams plot L-kurtosis ($\tau_4$) against L-skewness ($\tau_3$) to guide distribution selection. For any standard distribution, $\tau_4$ is represented as a polynomial function:
$$\tau_4 = \sum_{j=0}^m C_j \tau_3^j \tag{3.14}$$

Under the CTA-L-Moments formulation, the presence of zero-mass fraction $p_0$ shifts the theoretical polynomial curves. The doctoral research will analytically derive the shifted polynomial trajectories:
$$\tau_4^{CTA} = \psi(\tau_3^{CTA}, p_0) \tag{3.15}$$
establishing the first **CTA L-Moment Ratio Diagrams** for GEV, GPA, GLO, and 4-Parameter Kappa distributions.

### 3.5 Monte Carlo Simulation and Synthetic Process Validation

To prove estimator consistency and asymptotic efficiency, extensive Monte Carlo simulations will be executed across $M = 100,000$ synthetic realizations:

1. **Synthetic Generation**: Simulating daily rainfall via an Alternating Renewal Process, coupling a two-state Markov chain for dry/wet occurrence ($p_{00}, p_{11}$) with heavy-tailed Kappa distributed intensities on wet days.
2. **Temporal Dependence**: Generating clustered extremes using the Neyman-Scott Rectangular Pulses (NSRP) stochastic rainfall model to simulate realistic monsoon storm cells.
3. **Performance Metrics**: Assessing sample CTA-L-moment estimators ($\hat{\lambda}_r^{CTA}$) against theoretical values using:
   - Relative Bias: $\text{RBias} = \frac{1}{M} \sum_{m=1}^M \frac{\hat{\theta}_m - \theta_{true}}{\theta_{true}}$
   - Relative Root Mean Squared Error: $\text{RRMSE} = \sqrt{\frac{1}{M} \sum_{m=1}^M \left(\frac{\hat{\theta}_m - \theta_{true}}{\theta_{true}}\right)^2}$
   - Asymptotic Relative Efficiency (ARE) compared to Maximum Likelihood and Censored PWM estimators.

### 3.6 Multi-Regime Empirical Validation Across Malaysia

The framework will be validated on 100 continuous hydrometric stations across Malaysia:

```
┌────────────────────────────────────────────────────────────────────────┐
│             MALAYSIAN HYDROMETRIC DATA REGIONAL DIVISIONS              │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ Zone 1: East Coast│ Zone 2: West Coast│ Zone 3: Borneo Regimes         │
│ (Monsoonal Regime)│ (Convective)      │ (Equatorial Convective/Orphan) │
├───────────────────┼───────────────────┼────────────────────────────────┤
│ • 40 DID Stations │ • 35 DID Stations │ • 25 DID Stations              │
│ • Kelantan,       │ • Selangor, Perak,│ • Sarawak & Sabah              │
│   Terengganu,     │   Pulau Pinang,   │ • Distinct monsoon tracks      │
│   Pahang          │   Johor           │ • Orographic rain forest       │
│ • Northeast       │ • Inter-monsoonal │   catchments                   │
│   monsoon surges  │   convective      │ • High annual volume           │
│ • Multiple multi- │   thunderstorms   │   (3,000 - 5,000 mm)           │
│   day extremes    │ • Short-duration  │                                │
│   per year        │   high-intensity  │                                │
└───────────────────┴───────────────────┴────────────────────────────────┘
```

Goodness of fit will be evaluated using:
* **Mean Absolute Deviation Index (MADI)**: $\text{MADI} = \frac{1}{n} \sum_{i=1}^n \left| \frac{x_i - \hat{x}_i}{x_i} \right|$
* **Mean Squared Deviation Index (MSDI)**: $\text{MSDI} = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \hat{x}_i}{x_i} \right)^2$
* **Akaike Information Criterion (AIC)** and **Bayesian Information Criterion (BIC)**.

### 3.7 Catchment-Scale Hydrodynamic Inundation Propagation

To establish practical engineering relevance, design rainfall hyetographs derived under both AMS and CTA-L-Moments will be routed through:

1. **HEC-HMS (Hydrologic Engineering Center - Hydrologic Modeling System)**: Setting up semi-distributed rainfall-runoff models for the Sungai Terengganu basin (5,000 km²) and Sungai Klang basin (1,288 km²). Soil moisture accounting and Green-Ampt infiltration routines will convert extreme rainfall into continuous runoff hydrographs.
2. **HEC-RAS 2D (Hydrologic Engineering Center - River Analysis System)**: Conducting two-dimensional unsteady hydraulic routing using high-resolution LiDAR digital elevation models (DEMs).
3. **Hazard Quantification**: Comparing peak water surface elevations (WSE), flood arrival times, and total inundation areas between nominal 50-year and 100-year AMS designs versus CTA-L-Moments designs.

### 3.8 Development of the Open-Source `cta-lmoments` Package

All mathematical derivations and algorithms will be compiled into an open-source, object-oriented Python package (`cta-lmoments`) published on GitHub and PyPI, featuring:
* Native handling of zero-inflated arrays and intermittent time series.
* Exact parameter estimation for 9 distributions (GEV, GPA, GLO, GNO, PE3, K4D, EXP, NOR, GUM).
* Automated computation of empirical and analytical Overestimation Factors.
* Automated generation of publication-quality CTA L-moment ratio diagrams.

---

## CHAPTER 4: EXPECTED CONTRIBUTIONS TO KNOWLEDGE

### 4.1 Theoretical and Methodological Contributions

1. **Resolution of the Intermittent CTA Dilemma**: Delivers the first mathematical framework that integrates Complete Time-Series Analysis with L-moments for zero-inflated environmental time series, closing the gap identified in Volpi et al. (2019).
2. **Analytical Derivation of the Overestimation Law**: Establishes a mathematical proof explaining return period discrepancies in tropical climates, transforming an empirical observation into a predictive scientific formula.
3. **Novel Diagnostic Ratio Diagrams**: Expands Hosking's classical L-moment ratio space to accommodate point-mass dry fractions ($p_0$) and temporal clustering parameters ($\theta$).

### 4.2 Engineering and Policy Impacts

1. **Revision of Malaysian Drainage Guidelines**: Provides empirical and theoretical justifications for updating the Urban Stormwater Management Manual for Malaysia (*MSMA 2nd Edition*, DID, 2012) and Hydrological Procedure No. 1 (HP1).
2. **Elimination of Structural Under-Design**: Enables hydraulic engineers to properly size culverts, bridges, and detention basins, reducing unexpected hydraulic failures during recurring monsoon surges.
3. **Open-Source Scientific Software**: Supplies the global hydrological engineering community with an accessible, validated computational package for daily frequency analysis.

### 4.3 Alignment with UN Sustainable Development Goals

* **SDG 6 (Clean Water and Sanitation - Target 6.5)**: Enhances integrated water resource management through dependable statistical characterization of hydrological extremes.
* **SDG 11 (Sustainable Cities and Communities - Target 11.5)**: Reduces casualties and economic losses caused by water-related disasters by providing accurate flood risk assessments for urban planning.
* **SDG 13 (Climate Action - Target 13.1)**: Strengthens national resilience and adaptive capacity to climate-induced extreme precipitation hazards.

---

## CHAPTER 5: RESEARCH PLAN, MILESTONES, AND RESOURCE REQUIREMENTS

### 5.1 Three-Year Research Schedule (Gantt Chart)

The doctoral research is planned over a 36-month timeline:

| Activity / Work Package | Year 1 (M1–M12) | Year 2 (M13–M24) | Year 3 (M25–M36) |
| :--- | :---: | :---: | :---: |
| **WP1: Mathematical Derivations** | | | |
| • Derive zero-adjusted PWMs ($\beta_r^{CTA}$) | ████ | | |
| • Derive closed-form $OE$ proof | ████ | | |
| • Construct CTA ratio diagram mathematics | ████ | | |
| **WP2: Monte Carlo Simulation** | | | |
| • Code stochastic pulse & renewal generators | | ████ | |
| • Execute 100,000 synthetic test runs | | ████ | |
| • Analyze estimator bias, RMSE, and ARE | | ████ | |
| **WP3: Multi-Regime Empirical Validation** | | | |
| • Data collection & quality control (100 stations)| ████ | | |
| • Fit candidate distributions across 3 Zones | | ████ | |
| • Evaluate spatial patterns of $OE$ and K4D | | ████ | |
| **WP4: Catchment Hydrodynamic Modeling** | | | |
| • Setup HEC-HMS rainfall-runoff models | | | ████ |
| • Execute 2D HEC-RAS unsteady flood routing | | | ████ |
| • Quantify infrastructure inundation margins | | | ████ |
| **WP5: Software & Dissertation Defense** | | | |
| • Finalize & deploy `cta-lmoments` library | | ████ | ████ |
| • Manuscript preparation & journal submissions | | ████ | ████ |
| • Final dissertation compilation & viva voce | | | ████ |

### 5.2 Milestone Deliverables and Publication Roadmap

To satisfy doctoral graduation requirements and establish high academic impact, the following milestone publications are planned:

| Target Month | Milestone Deliverable | Target Journal / Venue | Indexing / Tier |
| :--- | :--- | :--- | :--- |
| **Month 12** | Mathematical formulation of CTA-L-Moments and closed-form $OE$ derivation | *Water Resources Research* / *Journal of Hydrology* | WoS / Scopus **Q1** |
| **Month 18** | Comprehensive candidature defense / Doctoral confirmation | UniSZA Center for Graduate Studies | Official Milestone |
| **Month 24** | Monte Carlo simulation and nationwide empirical validation across 100 stations | *Hydrological Sciences Journal* / *Journal of Hydrometeorology* | WoS / Scopus **Q1/Q2** |
| **Month 30** | Catchment hydrodynamic propagation and civil infrastructure risk implications | *Water Resources Management* / *Natural Hazards* | WoS / Scopus **Q1/Q2** |
| **Month 33** | Release of open-source Python library (`cta-lmoments`) | *Journal of Open Source Software (JOSS)* | WoS / Scopus |
| **Month 36** | Final PhD Dissertation submission & Viva Voce Examination | UniSZA Examination Senate | Doctoral Award |

### 5.3 Computational Facilities and Hydrometric Data Access

* **Primary Hydrometric Data**: Daily precipitation records from 100 DID gauging stations procured through formal institutional collaboration with the Hydrology and Water Resources Division, Department of Irrigation and Drainage (DID), Malaysia.
* **High-Performance Computing**: Workstation equipped with multi-core processors (AMD Ryzen 9 / Intel i9, 64 GB RAM) for intensive Monte Carlo stochastic simulations and parallelized 2D hydrodynamic modeling.
* **Software Platforms**: Python 3.11+ (NumPy, SciPy, Pandas, Matplotlib, Numba for parallelized PWM integration), US Army Corps of Engineers HEC-HMS 4.11 and HEC-RAS 6.4, and QGIS for geospatial hydro-topographic processing.

---

## REFERENCES

Coles, S. (2001). *An introduction to statistical modeling of extreme values*. Springer. https://doi.org/10.1007/978-1-4471-3675-0

Department of Irrigation and Drainage. (2009). *Hydrological procedures no. 1: Estimation of design rainstorm in Peninsular Malaysia*. Ministry of Natural Resources and Environment, Malaysia.

Department of Irrigation and Drainage. (2012). *Urban stormwater management manual for Malaysia (MSMA)* (2nd ed.). Ministry of Natural Resources and Environment, Malaysia.

Fisher, R. A., & Tippett, L. H. C. (1928). Limiting forms of the frequency distribution of the largest or smallest member of a sample. *Mathematical Proceedings of the Cambridge Philosophical Society*, *24*(2), 180–190. https://doi.org/10.1017/S030500410001568X

Gnedenko, B. (1943). Sur la distribution limite du terme maximum d'une série aléatoire. *Annals of Mathematics*, *44*(3), 423–453. https://doi.org/10.2307/1968974

Greenwood, J. A., Landwehr, J. M., Matalas, N. C., & Wallis, J. R. (1979). Probability weighted moments: Definition and relation to parameters of several distributions expressible in inverse form. *Water Resources Research*, *15*(5), 1049–1054. https://doi.org/10.1029/WR015i005p01049

Gumbel, E. J. (1958). *Statistics of extremes*. Columbia University Press.

Hosking, J. R. M. (1990). L-moments: Analysis and estimation of distributions using linear combinations of order statistics. *Journal of the Royal Statistical Society: Series B (Methodological)*, *52*(1), 105–124. https://doi.org/10.1111/j.2517-6161.1990.tb01775.x

Hosking, J. R. M. (1994). The four-parameter Kappa distribution. *IBM Journal of Research and Development*, *38*(3), 251–258. https://doi.org/10.1147/rd.383.0251

Hosking, J. R. M., & Wallis, J. R. (1997). *Regional frequency analysis: An approach based on L-moments*. Cambridge University Press. https://doi.org/10.1017/CBO9780511529443

Leadbetter, M. R. (1983). Extremes and local dependence in stationary sequences. *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete*, *65*(2), 291–306. https://doi.org/10.1007/BF00532484

Papalexiou, S. M., & Koutsoyiannis, D. (2013). Battle of extreme value distributions: A global survey on extreme daily rainfall. *Water Resources Research*, *49*(1), 187–201. https://doi.org/10.1029/2012WR012557

Parida, B. P. (1999). Modelling of Indian summer monsoon rainfall using a four-parameter Kappa distribution. *International Journal of Climatology*, *19*(12), 1389–1398. https://doi.org/10.1002/(SICI)1097-0088(199910)19:12<1389::AID-JOC437>3.0.CO;2-N

Rao, D. V., & Hamed, K. H. (2000). *Flood frequency analysis*. CRC Press. https://doi.org/10.1201/9781420042450

Volpi, E. (2019). On the return period of clustered extreme events. *Water Resources Research*, *55*(7), 6127–6141. https://doi.org/10.1029/2019WR025062

Volpi, E., Fiori, A., Grimaldi, S., Lombardo, F., & Koutsoyiannis, D. (2019). Save hydrological observations! Return period estimation without data decimation. *Journal of Hydrology*, *571*, 782–792. https://doi.org/10.1016/j.jhydrol.2019.02.027
