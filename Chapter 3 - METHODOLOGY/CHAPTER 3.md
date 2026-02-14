# CHAPTER 3: METHODOLOGY

## 3.1 Introduction

This chapter presents the methodology employed in this research for flood frequency analysis using L-moments. The chapter covers the study area, data collection, L-moments theory, distribution fitting procedures, goodness-of-fit assessment, return period analysis, and the approach used to quantify overestimation when comparing Annual Maximum Series (AMS) with daily rainfall data.

The L-moments method, introduced by Hosking (1990), provides a robust alternative to conventional moments for parameter estimation in frequency analysis. This methodology has been widely adopted in hydrological studies (Hosking & Wallis, 1997; Stedinger et al., 1993) and is particularly suitable for analyzing extreme events where sample sizes are limited (Vogel & Fennessey, 1993).

---

## 3.2 Study Area

The study focuses on Terengganu, a state located on the east coast of Peninsular Malaysia. Terengganu experiences a tropical monsoon climate characterized by:

- Heavy rainfall during the Northeast Monsoon season (November to March)
- Annual rainfall ranging from 2,500 mm to 4,000 mm
- Frequent extreme rainfall events that can cause flooding

The geographical location and monsoon climate make Terengganu an ideal study area for evaluating rainfall frequency analysis methods in tropical regions (Suhaila & Jemain, 2007; Wong et al., 2009). Previous studies have documented the unique rainfall characteristics of this region, including high variability and seasonal patterns (Desa & Niemczynowicz, 1996; Suhaila et al., 2010).

---

## 3.3 Data Collection

### 3.3.1 Data Source

Rainfall data were obtained from the Department of Irrigation and Drainage (DID), Malaysia. The dataset comprises daily rainfall records from twenty rainfall stations distributed across Terengganu. The DID maintains an extensive network of rainfall stations throughout Malaysia, providing reliable long-term hydrological data for research purposes (Department of Irrigation and Drainage Malaysia, 2009).

### 3.3.2 Rainfall Stations

Table 3.1 presents the twenty rainfall stations used in this study.

**Table 3.1: Rainfall Stations in Terengganu**

| No. | Station ID | Station Name |
|-----|------------|--------------|
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

Two types of rainfall data were analyzed:

1. **Annual Maximum Series (AMS)**: The highest daily rainfall value recorded in each year. This is the traditional approach used in flood frequency analysis (Dalrymple, 1960; Cunnane, 1989).

2. **Daily Rainfall Series**: All daily rainfall records filtered to include only rainfall days (values ≥ 1 mm). This approach captures the full spectrum of rainfall events throughout the year, as advocated by Volpi et al. (2019) in their Complete Time-series Analysis framework.

### 3.3.4 Data Preprocessing

The following preprocessing steps were applied:

1. Missing values were identified and excluded from analysis
2. Daily rainfall data were filtered to include only values ≥ 1 mm to exclude trace rainfall and non-rainfall days
3. Data quality was verified through visual inspection and statistical checks

These preprocessing procedures follow standard practices in hydrological data analysis (Rao & Hamed, 2000; Stedinger et al., 1993).

---

## 3.4 L-Moments Theory

### 3.4.1 Definition of L-Moments

L-moments are linear combinations of probability weighted moments (PWMs) that provide an alternative to conventional moments for describing probability distributions. L-moments were introduced by Hosking (1990) and offer several advantages over conventional moments:

- More robust to outliers (Hosking & Wallis, 1997)
- Less sensitive to sample size (Vogel & Fennessey, 1993)
- More reliable parameter estimation for small samples (Hosking, 1990)
- Better discrimination between distributions (Hosking & Wallis, 1995)

As noted by Stedinger et al. (1993), L-moments have become the preferred method for parameter estimation in flood frequency analysis due to their superior statistical properties compared to conventional product moments.

### 3.4.2 Probability Weighted Moments

The concept of probability weighted moments (PWMs) was introduced by Greenwood et al. (1979). PWMs are defined as:

β_r = E[X × F(X)^r]

Where:
- X = random variable
- F(X) = cumulative distribution function
- r = order of the moment (0, 1, 2, ...)

For a sample of size n with ordered observations x_(1) ≤ x_(2) ≤ ... ≤ x_(n), the unbiased estimators of PWMs are (Hosking, 1990):

b_0 = (1/n) × Σx_(i)

b_1 = (1/n) × Σ[(i-1)/(n-1)] × x_(i)

b_2 = (1/n) × Σ[(i-1)(i-2)/((n-1)(n-2))] × x_(i)

b_3 = (1/n) × Σ[(i-1)(i-2)(i-3)/((n-1)(n-2)(n-3))] × x_(i)

### 3.4.3 L-Moments from PWMs

The first four L-moments are calculated from PWMs as follows (Hosking, 1990; Hosking & Wallis, 1997):

- L₁ = β_0 (Location/Mean)
- L₂ = 2β_1 - β_0 (Scale)
- L₃ = 6β_2 - 6β_1 + β_0
- L₄ = 20β_3 - 30β_2 + 12β_1 - β_0

### 3.4.4 L-Moment Ratios

L-moment ratios are dimensionless quantities that characterize the shape of distributions (Hosking, 1990):

- τ₂ = L₂/L₁ (L-coefficient of variation, L-CV)
- τ₃ = L₃/L₂ (L-skewness)
- τ₄ = L₄/L₂ (L-kurtosis)

The L-skewness (τ₃) and L-kurtosis (τ₄) are used in L-moment ratio diagrams to identify suitable distributions for the data (Vogel & Fennessey, 1993). These diagrams provide a powerful visual tool for distribution selection, as different distributions occupy distinct regions in the τ₃-τ₄ space (Hosking & Wallis, 1997).

---

## 3.5 Probability Distributions

### 3.5.1 Distributions Used

Nine probability distributions commonly used in flood frequency analysis were fitted to the data (Cunnane, 1989; Rao & Hamed, 2000):

**Table 3.2: Probability Distributions**

| Abbreviation | Distribution Name | Parameters |
|--------------|-------------------|------------|
| GUM | Gumbel (Extreme Value Type I) | 2 (location, scale) |
| NOR | Normal | 2 (mean, standard deviation) |
| EXP | Exponential | 2 (location, scale) |
| GEV | Generalized Extreme Value | 3 (location, scale, shape) |
| GLO | Generalized Logistic | 3 (location, scale, shape) |
| GNO | Generalized Normal (Log-Normal Type III) | 3 (location, scale, shape) |
| GPA | Generalized Pareto | 3 (location, scale, shape) |
| PE3 | Pearson Type III | 3 (location, scale, shape) |
| KAP | 4-Parameter Kappa (K4D) | 4 (location, scale, shape1, shape2) |

The Gumbel distribution has been widely used in extreme value analysis since its introduction (Gumbel, 1958). The Generalized Extreme Value (GEV) distribution provides a flexible three-parameter family that includes Gumbel as a special case (Jenkinson, 1955; Coles, 2001). The 4-Parameter Kappa (K4D) distribution, introduced by Hosking (1994), offers additional flexibility and includes GEV, GLO, and GPA as special cases. The 4-Parameter Kappa distribution has been successfully applied to rainfall frequency analysis in various climatic conditions, including tropical monsoon regions (Parida, 1999).

For Malaysian rainfall data, previous studies have found that three-parameter distributions such as GEV, GLO, and PE3 generally provide better fits than two-parameter distributions (Zin et al., 2009; Zalina et al., 2002; Suhaila & Jemain, 2008).

### 3.5.2 Parameter Estimation Using L-Moments

For each distribution, the parameters were estimated by matching the sample L-moments to the theoretical L-moments of the distribution. This method, known as the method of L-moments, involves (Hosking & Wallis, 1997):

1. Calculate sample L-moments (L₁, L₂, L₃, L₄) from the data
2. Solve the equations that relate L-moments to distribution parameters
3. Obtain parameter estimates that produce L-moments matching the sample

The Python library `lmoments3` was used for L-moments calculation and distribution fitting (Hosking, 2017).

---

## 3.6 Goodness-of-Fit Assessment

### 3.6.1 Gringorten Plotting Positions

To assess the goodness-of-fit, the Gringorten plotting position formula was used to assign non-exceedance probabilities to ranked observations. Gringorten (1963) proposed the following formula:

P(i) = (i - 0.44) / (n + 0.12)

Where:
- i = rank of the observation (1 to n, from smallest to largest)
- n = total number of observations
- P(i) = estimated non-exceedance probability for the i-th ranked observation

The Gringorten formula is recommended for extreme value distributions and provides approximately unbiased plotting positions (Cunnane, 1978). Various plotting position formulas have been proposed in the literature, including those by Weibull (1939) and Hazen (1914), but the Gringorten formula is particularly suitable for Gumbel and GEV distributions (Stedinger et al., 1993).

### 3.6.2 Theoretical Quantiles

For each fitted distribution, theoretical quantiles were calculated using the percent point function (PPF), also known as the inverse cumulative distribution function (Rao & Hamed, 2000):

x̂(i) = F⁻¹(P(i))

Where:
- x̂(i) = theoretical quantile for the i-th observation
- F⁻¹ = inverse CDF (PPF) of the fitted distribution
- P(i) = Gringorten plotting position

### 3.6.3 Mean Absolute Deviation Index (MADI)

The Mean Absolute Deviation Index quantifies the average absolute deviation between observed and theoretical quantiles, normalized by the observed values:

d(i) = (x(i) - x̂(i)) / x(i)

MADI = (1/n) × Σ|d(i)|

Where:
- x(i) = observed value (sorted)
- x̂(i) = theoretical quantile
- n = number of observations

This index provides a scale-independent measure of fit quality (D'Agostino & Stephens, 1986).

### 3.6.4 Mean Squared Deviation Index (MSDI)

The Mean Squared Deviation Index provides a measure that penalizes larger deviations more heavily:

MSDI = (1/n) × Σ[d(i)]²

The use of squared deviations emphasizes larger discrepancies between observed and theoretical values, similar to the approach used in other goodness-of-fit statistics (Laio, 2004).

### 3.6.5 Best Distribution Selection

The distribution with the lowest MADI value was selected as the best-fitting distribution for each station. Lower values of MADI and MSDI indicate better agreement between the fitted distribution and the observed data. This approach is consistent with standard practices in distribution selection for hydrological applications (Vogel, 1986; Filliben, 1975).

---

## 3.7 Return Period Analysis

### 3.7.1 Return Period Definition

The return period (T) is the average recurrence interval of an event of a given magnitude. It is related to the exceedance probability (p) by (Chow et al., 1988):

T = 1 / p

Where p = P(X ≥ x), the probability that the variable X equals or exceeds a specified value x.

The concept of return period is fundamental to flood frequency analysis and infrastructure design (Stedinger & Griffis, 2008). However, it is important to note that return period represents an average recurrence interval, not a guaranteed inter-event time (Koutsoyiannis, 2004).

### 3.7.2 Quantile Estimation

For a given return period T, the corresponding return value (quantile) is calculated using (Kite, 1988; Rao & Hamed, 2000):

1. Calculate the non-exceedance probability: F = 1 - (1/T)
2. Apply the inverse CDF of the best-fitting distribution: x_T = F⁻¹(F)

### 3.7.3 Return Periods Analyzed

Return values were estimated for the following return periods:

2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100 years

This range of return periods covers both frequent events (2-year) and rare events (100-year), providing comprehensive information for various planning and design applications (Interagency Advisory Committee on Water Data, 1982).

---

## 3.8 Overestimation Quantification

### 3.8.1 Rationale

The Annual Maximum Series (AMS) approach, developed primarily for temperate climates, may not accurately represent the frequency of extreme rainfall events in tropical regions where multiple significant rainfall events occur throughout the year (Volpi et al., 2019; Koutsoyiannis, 2004). This research quantifies the degree of overestimation when using the AMS approach compared to daily rainfall data analysis.

As noted by Madsen et al. (1997), the choice between annual maxima and partial duration series can significantly affect return period estimates, particularly for shorter return periods. In tropical climates with frequent extreme events, this effect may be even more pronounced (Papalexiou & Koutsoyiannis, 2013).

### 3.8.2 Methodology

For each station, the overestimation was calculated at the 99th percentile of the complete daily time series (including zero rainfall days). This approach follows the Complete Time-series Analysis (CTA) framework advocated by Volpi et al. (2019), which emphasizes using the full observed time series rather than decimated data. Including zero rainfall days in percentile calculations provides a more accurate representation of the true frequency of events in the complete time series, as it accounts for all days in the record.

The 99th percentile was selected as the focus of this analysis because it represents the extreme tail of the distribution where the most severe rainfall events occur. In tropical regions, extreme daily rainfall events (99th percentile and above) are critical for flood risk assessment and infrastructure design, as these events often trigger significant flooding (Papalexiou & Koutsoyiannis, 2013; Volpi et al., 2019). The analysis at the 99th percentile provides insight into how the Annual Maximum Series approach performs for the most extreme events, which are of greatest concern for flood management. Additionally, the 99th percentile provides complete data coverage (all 20 stations) and demonstrates the most stable and reliable overestimation estimates, with the lowest variability across stations compared to lower percentiles.

**Important Note on Data Handling:**
- **Percentile calculation**: Uses ALL daily data (including zeros) to determine test magnitudes, ensuring true frequency representation in the complete time series
- **Distribution fitting**: Uses filtered daily data (≥1mm) to avoid zero-inflation issues in distribution fitting, as zeros create a mixed distribution that cannot be adequately modeled by continuous probability distributions
- This dual approach ensures both accurate frequency representation (via percentiles from complete data) and proper statistical modeling (via distribution fitting to rainfall amounts only)

1. **Annual Maximum Analysis**: Fit the best distribution to annual maxima and calculate the return period (RP_AM) for magnitude M in years.

2. **Daily Data Analysis**: Fit the best distribution to daily rainfall data (≥1mm) and calculate the return period (RP_daily) for magnitude M in days.

3. **Calculate Overestimation Factor**:

OE(M) = RP_AM(M) / (RP_daily(M) / 365.25)

Where:
- RP_AM(M) = return period in years from Annual Maxima analysis
- RP_daily(M) = return period in days from daily data analysis
- Division by 365.25 converts daily return period to years

4. **Calculate Overestimation Percentage**:

OE%(M) = (OE(M) - 1) × 100

The subtraction of 1 in this formula converts the overestimation factor from a ratio to a percentage change. The overestimation factor OE(M) represents the ratio of return periods (e.g., OE = 3.75 means the AM return period is 3.75 times the daily return period). To express this as a percentage change, the baseline value of 1 (representing no difference, or 100% of the true value) must be subtracted. This transformation follows the standard mathematical formula for percentage change: Percentage Change = ((New Value / Old Value) - 1) × 100, where the ratio (New Value / Old Value) is equivalent to OE(M), and subtracting 1 removes the baseline to quantify the excess above unity (Rao & Hamed, 2000; Stedinger et al., 1993). 

For example:
- OE(M) = 1.0 means no overestimation (1.0 - 1) × 100 = 0%
- OE(M) = 2.0 means 100% overestimation (2.0 - 1) × 100 = 100% (the AM return period is twice the daily return period)
- OE(M) = 8.50 means 750% overestimation (8.50 - 1) × 100 = 750% (the AM return period is 8.50 times the daily return period)

At the 99th percentile, the analysis revealed a mean overestimation factor of 8.50x across all 20 stations, indicating that the Annual Maximum Series approach significantly overestimates return periods for extreme rainfall events in tropical regions.

### 3.8.3 Interpretation

- OE = 1: No overestimation; both approaches give equivalent results
- OE > 1: Overestimation; AM approach suggests events are rarer than indicated by daily data
- OE < 1: Underestimation; AM approach suggests events are more frequent

This framework allows for direct comparison of return period estimates between AM and daily data approaches, providing quantitative evidence for the degree of bias introduced by the traditional AM method in tropical climates.

---

## 3.9 Software and Tools

### 3.9.1 Programming Environment

The analysis was conducted using Python 3 (Van Rossum & Drake, 2009) with the following libraries:

- **lmoments3**: L-moments calculation and distribution fitting (Hosking, 2017)
- **pandas**: Data manipulation and analysis (McKinney, 2010)
- **numpy**: Numerical computations (Harris et al., 2020)
- **matplotlib**: Data visualization (Hunter, 2007)

### 3.9.2 Data Processing

All rainfall data were stored in CSV format with a 'Value (mm)' column containing the rainfall measurements. The analysis scripts were designed to process multiple stations in batch mode, ensuring consistency across all analyses.

---

## 3.10 Research Framework

Figure 3.1 presents the overall research framework.

**Research Framework:**

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
│    • Handle missing values                                      │
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
│    (Volpi et al., 2019)                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESULTS AND DISCUSSION                       │
│              Conclusions and Recommendations                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.11 Summary

This chapter has presented the methodology for L-moments flood frequency analysis applied to rainfall data in Terengganu, Malaysia. The key methodological components include:

1. **Data**: Twenty rainfall stations with Annual Maximum Series and daily rainfall data from DID Malaysia
2. **L-Moments**: Robust parameter estimation method for distribution fitting (Hosking, 1990; Hosking & Wallis, 1997)
3. **Distributions**: Nine probability distributions fitted and evaluated (Cunnane, 1989)
4. **Goodness-of-Fit**: MADI and MSDI indices using Gringorten plotting positions (Gringorten, 1963)
5. **Return Period Analysis**: Quantile estimation for 2 to 100-year return periods (Chow et al., 1988)
6. **Overestimation**: Comparison of AM and daily approaches to quantify bias (Volpi et al., 2019)

The results of applying this methodology are presented in Chapter 5.
