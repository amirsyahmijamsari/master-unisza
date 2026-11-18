# CHAPTER 3: METHODOLOGY

## 3.1 INTRODUCTION

This chapter presents the comprehensive methodological framework developed for extreme rainfall and flood frequency analysis using the method of L-moments across tropical catchments in Terengganu, Malaysia. The analytical framework encompasses geographic delineation of the study area, systematic hydrological data acquisition and quality auditing, theoretical foundations of probability-weighted moments (PWMs) and L-moments, rigorous parameter estimation across nine candidate probability distributions, goodness-of-fit evaluation via deviation indices, return period quantile calculations, and a mathematical formulation to quantify the overestimation bias inherent in conventional Annual Maximum Series (AMS) relative to complete daily rainfall series.

The L-moments methodology, introduced by Hosking (1990), provides a mathematically robust alternative to conventional product moments for parameter estimation in frequency analysis. This methodology has been widely adopted in regional and extreme hydrological studies (Hosking & Wallis, 1997; Stedinger et al., 1993) and is especially suitable for analyzing extreme hydrological events where observational records are limited or subject to sampling variability (Vogel & Fennessey, 1993). In tropical climates characterized by extreme convective storms, the robustness of L-moments against severe outliers provides essential statistical stability for hydraulic design and regional flood risk governance.

---

## 3.2 STUDY AREA

The study focuses on the state of Terengganu, situated along the eastern coast of Peninsular Malaysia between latitudes 3°53′ N to 5°51′ N and longitudes 102°23′ E to 103°30′ E. Terengganu experiences a distinct equatorial humid tropical monsoon climate governed by the Northeast Monsoon, which typically prevails from November through March. During this seasonal window, strong northeasterly wind surges traversing the South China Sea deposit intense, prolonged precipitation across the coastal plains and mountainous headwaters.

Annual precipitation across Terengganu ranges between 2,500 mm and 4,000 mm, with more than half of the annual total frequently occurring within the four-month Northeast Monsoon period. These meteorological conditions generate recurring high-volume, multi-day storm systems that produce severe pluvial and fluvial flash floods throughout major river basins, including the Terengganu, Dungun, and Kemaman river systems. The distinct geographic exposure, high precipitation variability, and exposure to seasonal monsoonal surges render Terengganu an exemplary testing ground for evaluating rainfall frequency analysis methods within tropical environments (Desa & Niemczynowicz, 1996; Suhaila & Jemain, 2007; Wong et al., 2009; Suhaila et al., 2010).

---

## 3.3 DATA COLLECTION

### 3.3.1 Data Source

Hydrological records were acquired from the Department of Irrigation and Drainage (DID), Malaysia (Jabatan Pengairan dan Saliran). The dataset comprises daily rainfall records collected from twenty automatic and manual rainfall gauge stations strategically distributed across Terengganu. The DID maintains the primary national hydrometric observation network throughout Malaysia, enforcing rigorous quality assurance protocols and archiving standardized hydrological measurements for engineering design and research purposes (Department of Irrigation and Drainage Malaysia, 2009).

### 3.3.2 Rainfall Stations

The twenty rainfall gauge stations selected for this research represent a balanced spatial coverage across both coastal plains and inland undulating catchments in Terengganu. Table 3.1 details the inventory of selected stations, including their official DID station identification codes and geographic locations.

**Table 3.1: Rainfall Stations in Terengganu**

| No. | Station ID | Station Name |
| :---: | :---: | :--- |
| 1 | 0551621RF | Stor JPS Kuala Terengganu |
| 2 | 0580041RF | Klinik Bidan Kg. Baru Ajil |
| 3 | 0600011RF | JPS Bukit Besi |
| 4 | 0600131RF | JPS Dungun |
| 5 | 0600141RF | Rumah Pam Paya Ketam |
| 6 | 0600151RF | JPS Kuala Dungun |
| 7 | 0620081RF | Rumah Pam Nyatoh |
| 8 | 0630011RF | JPS Kemaman |
| 9 | 0630121RF | JPS Kg. Ibok, Kemaman |
| 10 | 0670051RF | Rumah Pam Tok Sabah, Marang |
| 11 | 0670181RF | Kg. Tepuh, Hulu Terengganu |
| 12 | 0670211RF | Rumah Pam Padang Landak |
| 13 | 0670221RF | JPS Kuala Berang |
| 14 | 0670251RF | Rumah Pam Jerangau |
| 15 | 0670281RF | Kg. Menerong, Hulu Terengganu |
| 16 | 0680071RF | Balai Polis Kg. Dura |
| 17 | 0680081RF | Rumah Pam Rantau Petronas |
| 18 | 0690051RF | Rumah Pam Pengkalan Ranggon |
| 19 | 0700011RF | Rumah Pam Besut |
| 20 | 0700131RF | JPS Jertih, Besut |

### 3.3.3 Data Types

Two distinct rainfall data series were extracted and systematically evaluated for each of the twenty monitoring stations. First, the Annual Maximum Series (AMS) was constructed by extracting the single highest 24-hour rainfall record within each calendar year, representing the conventional hydrological protocol for flood frequency estimation (Dalrymple, 1960; Cunnane, 1989). Second, the daily rainfall series was compiled by incorporating the complete observational record of daily rainfall, filtered to include all positive precipitation events ($X \ge 1.0\text{ mm}$). This non-decimated approach preserves the complete operational record throughout each year, capturing multiple severe storm occurrences and aligning with the Complete Time-Series Analysis (CTA) paradigm formulated by Volpi et al. (2019).

### 3.3.4 Data Preprocessing

Data quality assurance and preprocessing involved three sequential procedures. First, missing observational records were identified, audited, and omitted from parameter calculations to prevent distortion of statistical moments. Second, a rainfall threshold filter of $X \ge 1.0\text{ mm}$ was applied to the daily time series to isolate active rainfall events from trace measurements and non-rainy days, following standard meteorological practices in tropical hydrological modeling (Hosking & Wallis, 1997; Rao & Hamed, 2000). Third, observational consistency and homogeneity were verified through chronological inspection and statistical screening. These quality assurance steps conform to established standards in hydrological engineering (Rao & Hamed, 2000; Stedinger et al., 1993).

---

## 3.4 L-MOMENTS THEORY

### 3.4.1 Definition of L-Moments

L-moments, formulated by Hosking (1990), are linear combinations of probability-weighted moments (PWMs) that provide an effective mathematical foundation for describing the shape of probability distributions and estimating model parameters. Relative to conventional product moments, L-moments exhibit distinct theoretical and computational advantages. First, because they represent linear functions of the ranked sample order statistics rather than powers, L-moments are markedly less sensitive to extreme outliers and heavy tails (Hosking & Wallis, 1997). Second, parameter estimators derived from sample L-moments suffer substantially less sample size bias and exhibit asymptotic normality across small to moderate sample records (Hosking, 1990; Vogel & Fennessey, 1993). Third, L-moment ratio estimators provide superior discriminative capability when identifying parent probability distributions, making them the preferred framework for environmental extreme value modeling (Stedinger et al., 1993; Hosking & Wallis, 1997).

### 3.4.2 Probability-Weighted Moments

For a real-valued random variable $X$ with continuous cumulative distribution function $F(X)$ and quantile function $x(F)$, the probability-weighted moments of order $p$, $r$, and $s$ are formally defined by Greenwood et al. (1979) as:

$$M_{p,r,s} = E\left[ X^p \{F(X)\}^r \{1 - F(X)\}^s \right] = \int_{0}^{1} \{x(F)\}^p F^r (1 - F)^s dF$$

In L-moment analysis, the special case $M_{1,r,0}$ is customarily denoted as $\beta_r$, defined as:

$$\beta_r = E\left[ X \{F(X)\}^r \right] = \int_{0}^{1} x(F) F^r dF$$

For a sample of size $n$ arranged in ascending order such that $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$, the unbiased sample estimator $b_r$ of the probability-weighted moment $\beta_r$ is calculated as (Hosking, 1990):

$$b_r = \frac{1}{n} \sum_{i=1}^{n} \frac{(i-1)(i-2)\cdots(i-r)}{(n-1)(n-2)\cdots(n-r)} x_{(i)}$$

Specifically, the first four sample estimators are given by:

$$b_0 = \frac{1}{n} \sum_{i=1}^{n} x_{(i)}$$

$$b_1 = \frac{1}{n} \sum_{i=1}^{n} \frac{i-1}{n-1} x_{(i)}$$

$$b_2 = \frac{1}{n} \sum_{i=1}^{n} \frac{(i-1)(i-2)}{(n-1)(n-2)} x_{(i)}$$

$$b_3 = \frac{1}{n} \sum_{i=1}^{n} \frac{(i-1)(i-2)(i-3)}{(n-1)(n-2)(n-3)} x_{(i)}$$

### 3.4.3 Calculation of L-Moments from PWMs

The first four population L-moments ($\lambda_1, \lambda_2, \lambda_3, \lambda_4$) are defined as scalar linear combinations of the probability-weighted moments (Hosking, 1990; Hosking & Wallis, 1997):

$$\lambda_1 = \beta_0 \tag{3.1}$$

$$\lambda_2 = 2\beta_1 - \beta_0 \tag{3.2}$$

$$\lambda_3 = 6\beta_2 - 6\beta_1 + \beta_0 \tag{3.3}$$

$$\lambda_4 = 20\beta_3 - 30\beta_2 + 12\beta_1 - \beta_0 \tag{3.4}$$

These scalar quantities correspond to fundamental properties of the probability distribution: $\lambda_1$ represents the L-location (equal to the distribution mean), $\lambda_2$ represents the L-scale (a measure of dispersion), $\lambda_3$ reflects the degree of asymmetry, and $\lambda_4$ reflects peakedness and tail weight. Unbiased sample L-moments ($l_1, l_2, l_3, l_4$) are calculated by replacing $\beta_r$ with the sample estimators $b_r$ in Equations (3.1) through (3.4).

### 3.4.4 L-Moment Ratios

To obtain dimensionless measures analogous to conventional coefficient of variation, skewness, and kurtosis, Hosking (1990) defined the L-moment ratios by scaling higher-order L-moments with the L-scale parameter:

$$\tau = \frac{\lambda_2}{\lambda_1} \tag{3.5}$$

$$\tau_3 = \frac{\lambda_3}{\lambda_2} \tag{3.6}$$

$$\tau_4 = \frac{\lambda_4}{\lambda_2} \tag{3.7}$$

where $\tau$ is the L-coefficient of variation (L-CV), $\tau_3$ is the L-skewness, and $\tau_4$ is the L-kurtosis. Because $|\tau_3| < 1$ and $\frac{1}{4}(5\tau_3^2 - 1) \le \tau_4 < 1$, L-moment ratios are strictly bounded, preventing extreme numerical distortions. Sample L-moment ratios ($t, t_3, t_4$) are constructed by substituting sample L-moments ($l_1, l_2, l_3, l_4$) into Equations (3.5) through (3.7). The pairing of sample L-skewness ($t_3$) and L-kurtosis ($t_4$) plotted on L-moment ratio diagrams provides a rigorous visual and diagnostic instrument for identifying appropriate candidate probability distributions (Vogel & Fennessey, 1993; Hosking & Wallis, 1997).

---

## 3.5 PROBABILITY DISTRIBUTIONS

### 3.5.1 Candidate Distributions

Nine probability distributions widely utilized in international and Malaysian flood frequency analysis were evaluated (Cunnane, 1989; Rao & Hamed, 2000). Table 3.2 lists the candidate distributions, their standard abbreviations, and their governing parameters.

**Table 3.2: Candidate Probability Distributions for Rainfall Frequency Analysis**

| Abbreviation | Distribution Name | Number of Parameters | Parameter Descriptions |
| :---: | :--- | :---: | :--- |
| GUM | Gumbel (Extreme Value Type I) | 2 | Location ($\xi$), Scale ($\alpha$) |
| NOR | Normal | 2 | Mean ($\mu$), Standard Deviation ($\sigma$) |
| EXP | Exponential | 2 | Location ($\xi$), Scale ($\alpha$) |
| GEV | Generalized Extreme Value | 3 | Location ($\xi$), Scale ($\alpha$), Shape ($k$) |
| GLO | Generalized Logistic | 3 | Location ($\xi$), Scale ($\alpha$), Shape ($k$) |
| GNO | Generalized Normal (Log-Normal III) | 3 | Location ($\xi$), Scale ($\alpha$), Shape ($k$) |
| GPA | Generalized Pareto | 3 | Location ($\xi$), Scale ($\alpha$), Shape ($k$) |
| PE3 | Pearson Type III | 3 | Location ($\xi$), Scale ($\alpha$), Skewness ($\gamma$) |
| KAP | 4-Parameter Kappa (K4D) | 4 | Location ($\xi$), Scale ($\alpha$), Shape 1 ($k$), Shape 2 ($h$) |

The Gumbel distribution has served as a benchmark in classical extreme value hydrology (Gumbel, 1958). The Generalized Extreme Value (GEV) distribution provides a three-parameter formulation that unifies Type I (Gumbel), Type II (Frechet), and Type III (Weibull) distributions into a single mathematical structure (Jenkinson, 1955; Coles, 2001). The 4-Parameter Kappa (K4D) distribution, formulated by Hosking (1994), offers exceptional tail flexibility by incorporating two shape parameters ($k$ and $h$), nesting the GEV, GLO, and GPA families as special cases. The K4D distribution has demonstrated superior capability in capturing extreme rainfall dynamics across tropical monsoon catchments characterized by severe right-skewness and heavy tails (Parida, 1999). Prior hydrological investigations in Malaysia have corroborated that three- and four-parameter distributions systematically outperform two-parameter models when characterizing extreme monsoonal precipitation (Zalina et al., 2002; Suhaila & Jemain, 2008; Zin et al., 2009).

### 3.5.2 Parameter Estimation Using L-Moments

Distribution parameters were estimated by equating the sample L-moments to theoretical expressions derived for each candidate distribution, a procedure designated as the method of L-moments (Hosking & Wallis, 1997). The estimation sequence proceeded through three steps. First, sample L-moments ($l_1, l_2, l_3, l_4$) were computed from the empirical data series. Second, mathematical relationships equating sample L-moments to distribution parameters were solved analytically or through iterative numerical algorithms. Third, the resulting parameter sets were verified to ensure they satisfied the physical boundary and existence criteria of each distribution family. Numerical parameter estimation was executed using the open-source Python library `lmoments3` (Hosking, 2017).

---

## 3.6 GOODNESS-OF-FIT ASSESSMENT

### 3.6.1 Gringorten Plotting Positions

To evaluate goodness-of-fit, empirical non-exceedance probabilities were assigned to ranked rainfall observations using the plotting position formula proposed by Gringorten (1963):

$$P_i = \frac{i - 0.44}{n + 0.12} \tag{3.8}$$

where $i$ denotes the rank of the observation in ascending order ($i = 1, 2, \dots, n$), $n$ represents the total sample size, and $P_i$ is the estimated cumulative probability for the $i$-th ranked event. The Gringorten formula is recognized as an approximately unbiased plotting position estimator for extreme value distributions, minimizing bias in quantile-quantile comparisons relative to classical Weibull or Hazen plotting positions (Cunnane, 1978; Stedinger et al., 1993).

### 3.6.2 Theoretical Quantiles

For each fitted candidate distribution, theoretical quantiles ($\hat{x}_i$) corresponding to the empirical non-exceedance probabilities were calculated using the inverse cumulative distribution function, also known as the quantile function (Rao & Hamed, 2000):

$$\hat{x}_i = Q(P_i) = F^{-1}(P_i) \tag{3.9}$$

where $F^{-1}$ represents the inverse CDF evaluated at plotting position probability $P_i$.

### 3.6.3 Mean Absolute Deviation Index (MADI)

The Mean Absolute Deviation Index (MADI) quantifies the average relative absolute difference between observed rainfall values and theoretical quantiles, normalized by the observed magnitude:

$$\text{MADI} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{x_i - \hat{x}_i}{x_i} \right| \tag{3.10}$$

where $x_i$ represents the $i$-th observed sample value arranged in ascending order, $\hat{x}_i$ is the corresponding theoretical quantile estimated from Equation (3.9), and $n$ is the total sample count. Normalizing each deviation by $x_i$ ensures that MADI provides a scale-independent, dimensionless performance metric suitable for cross-station regional comparison (D'Agostino & Stephens, 1986).

### 3.6.4 Mean Squared Deviation Index (MSDI)

The Mean Squared Deviation Index (MSDI) introduces quadratic penalization to accentuate larger discrepancies between empirical and theoretical quantiles:

$$\text{MSDI} = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{x_i - \hat{x}_i}{x_i} \right)^2 \tag{3.11}$$

By squaring the normalized residuals, MSDI imposes heavy penalties on candidate models that produce substantial local deviations, particularly in the critical upper tail where hydraulic design thresholds reside (Laio, 2004).

### 3.6.5 Best Distribution Selection

The probability distribution yielding the minimum MADI score was designated as the best-fitting model for each station, with MSDI values serving as secondary confirmatory criteria. Lower numerical indices denote closer convergence between theoretical distribution quantiles and empirical observations, following rigorous goodness-of-fit benchmarking in statistical hydrology (Filliben, 1975; Vogel, 1986).

---

## 3.7 RETURN PERIOD ANALYSIS

### 3.7.1 Return Period Definition

The return period ($T$), or average recurrence interval, defines the average elapsed time between consecutive occurrences of a hydrological event equal to or exceeding a specified design threshold $x$. In classical frequency analysis, $T$ is mathematically expressed as the reciprocal of the exceedance probability (Chow et al., 1988):

$$T = \frac{1}{1 - F(x)} \tag{3.12}$$

where $F(x) = P(X \le x)$ denotes the cumulative non-exceedance probability of design event $x$. Although return period is conventionally interpreted as a deterministic recurrence interval in engineering practice, it fundamentally represents the mean of a geometric distribution governing stochastic interarrival times (Koutsoyiannis, 2004; Stedinger & Griffis, 2008).

### 3.7.2 Quantile Estimation

For a prescribed design return period $T$, the design rainfall quantile ($x_T$) is calculated by evaluating the inverse cumulative distribution function of the optimal distribution at non-exceedance probability $F = 1 - (1/T)$:

$$x_T = F^{-1}\left(1 - \frac{1}{T}\right) \tag{3.13}$$

Evaluating Equation (3.13) across multiple return periods generates the complete design rainfall frequency curve for each rain gauge station (Kite, 1988; Rao & Hamed, 2000).

### 3.7.3 Return Periods Analyzed

Rainfall quantiles were systematically computed across twelve standardized return periods: 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100 years. This comprehensive spectrum captures frequent operational storms (2-year and 5-year events) utilized for urban drainage sizing, intermediate occurrences (10-year to 50-year events) governing retention structures, and rare extreme events (100-year recurrence) mandated for regional flood hazard zoning and major dam spillway safety evaluations (Interagency Advisory Committee on Water Data, 1982).

---

## 3.8 OVERESTIMATION QUANTIFICATION

### 3.8.1 Rationale

Conventional flood frequency analysis relies almost exclusively on the Annual Maximum Series (AMS) framework, wherein an entire year of daily hydrologic data is reduced to a single maximum value (Dalrymple, 1960; Cunnane, 1989). While this decimation protocol was developed for temperate climates where single distinct annual flood peaks predominate, it introduces structural distortion in tropical monsoonal regions where multiple catastrophic rainfall events regularly occur within a single wet season (Madsen et al., 1997; Papalexiou & Koutsoyiannis, 2013). By discarding all secondary storms that exceed the annual maxima of drier years, the AMS framework creates an artificial sample that distorts extreme frequency estimation. Volpi et al. (2019) demonstrated that eliminating data decimation through Complete Time-Series Analysis (CTA) restores true event probabilities. This study establishes a rigorous mathematical procedure to quantify the resulting overestimation bias across tropical catchments.

### 3.8.2 Methodology and Tropical Zero-Inflation Adaptation

Continuous probability distributions assume that the probability of observing an exact value is zero ($P(X = 0) = 0$). In tropical monsoon climates such as Terengganu, daily rainfall series contain approximately 40% to 55% completely dry days ($X = 0\text{ mm}$). Fitting continuous extreme value distributions directly to daily records with a heavy discrete mass at zero causes numerical divergence, distorts L-moment ratios, and renders parameter estimation invalid (Hosking & Wallis, 1997; Rao & Hamed, 2000).

To overcome zero-inflation while preserving chronological integrity, this research implements an adapted two-component mixed modeling framework (Hosking & Wallis, 1997, Section 2.8; Rao & Hamed, 2000). The composite cumulative distribution function $F(x)$ is formulated as:

$$F(x) = p_0 + (1 - p_0) F_{\text{wet}}(x) \quad \text{for } x \ge x_0 \tag{3.14}$$

where $p_0$ represents the discrete proportion of dry days ($X < 1.0\text{ mm}$), and $F_{\text{wet}}(x)$ represents the continuous distribution fitted exclusively to positive rainfall days ($X \ge 1.0\text{ mm}$) using L-moments. Under this formulation, frequency benchmarking at specified extreme percentiles (e.g., the 99th percentile magnitude, $M$) is derived across the complete daily time series to preserve genuine multi-year occurrence rates as advocated by Volpi et al. (2019), while L-moments distribution fitting is executed on positive rainfall amounts ($X \ge 1.0\text{ mm}$) according to Hosking and Wallis (1997).

The comparative analytical sequence proceeds through four sequential calculations:

First, the best-fitting distribution is fitted to the AMS, and the return period ($T_{\text{AM}}$) corresponding to magnitude $M$ is computed in years.

Second, the best-fitting distribution is fitted to positive daily rainfall records ($X \ge 1.0\text{ mm}$), and the daily return period ($T_{\text{daily}}$) for magnitude $M$ is calculated in days:

$$T_{\text{daily}}(M) = \frac{1}{1 - F_{\text{wet}}(M)} \tag{3.15}$$

Third, the Overestimation Factor (formalized as the return period ratio, $R_T$) is computed by dividing the annual maximum return period by the annualized daily return period:

$$R_T(M) = \frac{T_{\text{AM}}(M)}{T_{\text{daily}}(M) / 365.25} \tag{3.16}$$

where division by 365.25 converts the daily recurrence interval into an equivalent annual basis, enabling direct dimensional comparison with $T_{\text{AM}}(M)$.

Fourth, the relative percentage excess or overestimation percentage ($\Delta_T$) is calculated as:

$$\Delta_T(M) = [R_T(M) - 1] \times 100\% \tag{3.17}$$

Subtracting 1 removes the parity baseline ($R_T = 1.0$ represents 0% bias), quantifying the net percentage excess by which the AMS approach overstates recurrence intervals (Rao & Hamed, 2000; Stedinger et al., 1993). For instance, an overestimation ratio of $R_T = 8.50$ corresponds to a relative percentage excess of $\Delta_T = 750\%$, demonstrating that the AMS framework models an extreme event as recurring once in 8.50 years when daily observational data demonstrate that it recurs on average once every year.

### 3.8.3 Interpretation of Overestimation Metrics

The return period ratio $R_T$ provides an intuitive diagnostic metric for evaluating statistical bias. When $R_T = 1.0$, the annual maximum and daily approaches yield identical recurrence estimates. When $R_T > 1.0$, the annual maximum approach overestimates the return period, creating the erroneous impression that extreme rainfall events are rarer than empirical observations indicate. Conversely, $R_T < 1.0$ indicates underestimation. Across the twenty monitoring stations in Terengganu, the empirical results at the 99th percentile demonstrate a mean overestimation ratio of 8.50 (an average recurrence of 43 days versus an AMS estimate of 1.06 years), providing definitive quantitative evidence of severe conservative bias in conventional design practices.

---

## 3.9 COMPUTATIONAL ENVIRONMENT AND SOFTWARE

### 3.9.1 Programming Environment and Software Packages

The computational workflows were developed within Python 3 (Van Rossum & Drake, 2009). The analytical architecture integrated four core scientific computing libraries. The `lmoments3` package was employed for probability-weighted moment calculations, sample L-moment derivation, and distribution fitting via numerical optimization (Hosking, 2017). The `pandas` library provided high-performance data manipulation, missing value filtering, and chronological series extraction (McKinney, 2010). The `numpy` library supported vectorized multidimensional numerical computations and matrix transformations (Harris et al., 2020). The `matplotlib` visualization engine generated high-resolution diagnostic graphics, including L-moment ratio diagrams and quantile-quantile verification plots (Hunter, 2007).

### 3.9.2 Data Processing Architecture

Hydrological datasets were structured in standardized comma-separated values (CSV) format containing validated timestamp and precipitation depth fields. Analytical scripts executed batch processing routines across all twenty rainfall stations simultaneously, ensuring consistent parameter estimation and identical numerical convergence thresholds. Automated exception handling mechanisms were embedded to isolate numerical singularities and record goodness-of-fit statistics systematically into unified relational tables.

---

## 3.10 Research Framework

Figure 3.1 presents the methodological research framework formulated for this study, outlining the sequential progression from hydrometric data acquisition to empirical overestimation quantification across the four research objectives:

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA COLLECTION                          │
│         Daily Rainfall Data from 20 DID Stations                │
│              (DID Malaysia, 2009)                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA PREPROCESSING                         │
│    • Extract Annual Maximum Series (AMS)                        │
│    • Filter Daily Data (≥1mm)                                   │
│    • Handle missing values and verify series homogeneity        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              OBJECTIVE 1: PARAMETER ESTIMATION                  │
│         Calculate L-moments (L₁, L₂, τ₃, τ₄)                    │
│         (Hosking, 1990; Greenwood et al., 1979)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            OBJECTIVE 2: DISTRIBUTION SELECTION                  │
│    • Fit 9 distributions using L-moments                        │
│    • Calculate MADI and MSDI (Gringorten, 1963)                 │
│    • Select best-fitting distribution (lowest MADI)             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            OBJECTIVE 3: RETURN PERIOD ANALYSIS                  │
│    • Calculate return values for T = 2 to 100 years             │
│    • Using best-fitting distribution for each station           │
│    (Chow et al., 1988; Rao & Hamed, 2000)                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│         OBJECTIVE 4: OVERESTIMATION QUANTIFICATION              │
│    • Compare return periods: AM vs Daily                        │
│    • Calculate Overestimation Factor and Percentage             │
│    (Volpi et al., 2019; Hosking & Wallis, 1997)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESULTS AND DISCUSSION                       │
│              Conclusions and Recommendations                    │
└─────────────────────────────────────────────────────────────────┘
```

**Figure 3.1: Methodological Research Framework for L-Moments Flood Frequency Analysis and Overestimation Quantification.**

---

## 3.11 SUMMARY

This chapter has established the comprehensive methodological framework for conducting flood frequency analysis and overestimation quantification using L-moments across twenty rainfall gauge stations in Terengganu, Malaysia. The analytical methodology systematically addresses the four research objectives formulated in Chapter 1:

First, sample L-moments and dimensionless L-moment ratios were computed from probability-weighted moments for both Annual Maximum Series and complete daily rainfall records, establishing a robust statistical baseline resilient against outlier contamination.

Second, parameters for nine candidate probability distributions were estimated via the method of L-moments. The optimal model for each station was identified using the Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI) computed against Gringorten plotting positions.

Third, design rainfall quantiles were derived across standardized recurrence intervals ranging from 2 to 100 years, providing empirical design thresholds for hydraulic engineering.

Fourth, a mathematical overestimation quantification framework adapted for zero-inflated tropical precipitation was implemented, benchmarking return periods at the 99th percentile to isolate the systematic error introduced by annual maximum data decimation.

The critical research gaps in existing flood frequency literature addressed by this methodology are elaborated in Chapter 4, and the empirical results produced by applying this framework are presented and discussed in Chapter 5.

*(See References chapter for complete reference list)*
