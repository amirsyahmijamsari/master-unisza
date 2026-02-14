# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

This chapter provides a comprehensive review of the literature relevant to flood frequency analysis using L-moments, with particular emphasis on applications in tropical climates. The review covers the historical development of frequency analysis methods, the evolution of L-moments methodology, probability distributions used in hydrology, and previous studies conducted in Malaysia and other tropical regions.

The chapter is organized as follows: Section 2.2 discusses climate classification and the fundamental differences between temperate and tropical rainfall patterns. Section 2.3 reviews the historical development of flood frequency analysis. Section 2.4 covers probability distributions commonly used in hydrology. Section 2.5 presents a detailed review of L-moments theory and applications. Section 2.6 discusses goodness-of-fit assessment methods. Section 2.7 reviews return period analysis concepts. Section 2.8 summarizes Malaysian and tropical rainfall studies. Section 2.9 briefly identifies the research gap, which is elaborated in Chapter 4.

---

## 2.2 Temperate versus Tropical Climate Systems

### 2.2.1 Climate Classification

Climate classification systems, such as the Köppen-Geiger classification, distinguish between climate zones based on temperature and precipitation patterns (Peel et al., 2007). Temperate climates (classified as C and D in the Köppen system) are characterized by distinct seasons with moderate precipitation distributed throughout the year. In contrast, tropical climates (classified as A) experience high temperatures year-round with significant precipitation, often concentrated in monsoon seasons (Kottek et al., 2006).

Understanding these climatic differences is essential for selecting appropriate hydrological analysis methods, as methodologies developed for one climate zone may not be directly applicable to another (Koutsoyiannis & Montanari, 2015).

### 2.2.2 Temperate Climate Rainfall Characteristics

Temperate regions, which include most of Europe, North America, and parts of Asia, exhibit the following rainfall characteristics (Brutsaert, 2005):

- **Moderate annual rainfall**: Typically 500-1,500 mm per year
- **Even distribution**: Rainfall distributed relatively evenly across seasons
- **Infrequent extremes**: Major flood-producing rainfall events occur once or twice per year
- **Frontal systems**: Rainfall often associated with large-scale frontal weather systems
- **Extended duration**: Storm events may last several days

These characteristics influenced the development of classical flood frequency analysis methods, which were designed to analyze relatively rare extreme events (Stedinger et al., 1993).

### 2.2.3 Tropical Climate Rainfall Characteristics

Tropical regions, including Southeast Asia, exhibit distinctly different rainfall patterns (Nieuwolt, 1977; Suhaila & Jemain, 2007):

- **High annual rainfall**: Often exceeding 2,000-4,000 mm per year
- **Seasonal concentration**: Rainfall concentrated during monsoon seasons
- **Frequent extremes**: Multiple heavy rainfall events within short periods
- **Convective systems**: Intense localized thunderstorms common
- **Short duration, high intensity**: Storm events often brief but extremely intense

In Malaysia specifically, the Northeast Monsoon (November to March) brings particularly heavy rainfall to the east coast states, including Terengganu (Wong et al., 2009; Suhaila et al., 2010). During this period, daily rainfall totals frequently exceed 100 mm, with multiple such events occurring within weeks (Desa & Niemczynowicz, 1996).

### 2.2.4 Implications for Frequency Analysis

The fundamental differences between temperate and tropical rainfall patterns have significant implications for frequency analysis (Koutsoyiannis, 2004; Papalexiou & Koutsoyiannis, 2013):

1. **Sample size considerations**: In temperate climates, annual maximum series provide adequate sample sizes because extreme events are rare. In tropical climates, using only annual maxima discards numerous significant events.

2. **Independence assumptions**: Classical methods assume independence between events. In monsoon climates, clustering of events may violate this assumption (Serinaldi & Kilsby, 2015).

3. **Stationarity**: Climate change may affect stationarity assumptions differently in tropical versus temperate regions (Milly et al., 2008; Khaliq et al., 2006).

4. **Distribution selection**: The best-fitting probability distribution may differ between climate zones due to different generating mechanisms for extreme events (Papalexiou & Koutsoyiannis, 2013).

---

## 2.3 Historical Development of Flood Frequency Analysis

### 2.3.1 Early Foundations

The scientific study of flood frequency began in the early 20th century. Hazen (1914) introduced plotting positions for probability analysis, establishing a framework for relating observed data to theoretical distributions. Fuller (1914) developed empirical formulas for flood frequency estimation that remained influential for decades.

Gumbel (1941, 1958) made foundational contributions by applying extreme value theory to hydrological problems. His work established the Extreme Value Type I (Gumbel) distribution as a standard tool for flood frequency analysis. Gumbel's methods were widely adopted because they provided a theoretical basis for extrapolating beyond observed data.

### 2.3.2 The Annual Maximum Series Approach

The Annual Maximum Series (AMS) approach became the standard method for flood frequency analysis following the work of Dalrymple (1960) and the U.S. Geological Survey. This approach involves:

1. Selecting the single largest value from each year of record
2. Fitting a probability distribution to the resulting series
3. Estimating quantiles for various return periods

The AMS approach was formalized in official guidelines, including Bulletin 17B (Interagency Advisory Committee on Water Data, 1982), which became the standard reference for flood frequency analysis in the United States and influenced practices worldwide.

### 2.3.3 Alternative Approaches

Recognizing limitations of the AMS approach, researchers developed alternative methods:

**Partial Duration Series (PDS)**: Also known as peaks-over-threshold (POT), this approach includes all events exceeding a specified threshold rather than only annual maxima (Langbein, 1949; Madsen et al., 1997). The PDS approach captures more extreme events but requires careful selection of thresholds and treatment of dependent events.

**Complete Time-Series Analysis (CTA)**: Volpi et al. (2019) proposed using the entire observational record without decimation, arguing that traditional methods discard valuable information. This approach is particularly relevant for tropical climates where multiple extreme events occur annually.

### 2.3.4 Regional Frequency Analysis

Regional frequency analysis extends single-site analysis by pooling data from multiple stations to improve estimation reliability (Dalrymple, 1960; Hosking & Wallis, 1997). The index flood method, introduced by Dalrymple (1960), assumes that sites within a homogeneous region share a common frequency distribution scaled by a site-specific index.

Hosking and Wallis (1997) developed a comprehensive framework for regional frequency analysis using L-moments, which has become the standard approach. Their methodology includes:

- Screening of data for errors and outliers
- Identification of homogeneous regions
- Selection of a regional frequency distribution
- Estimation of the regional growth curve
- Combination with at-site indices

Burn (1990) introduced the region of influence approach, which defines regions based on similarity rather than geographic proximity. Lettenmaier et al. (1987) examined the effects of regional heterogeneity on flood frequency estimation.

---

## 2.4 Probability Distributions in Hydrology

### 2.4.1 Extreme Value Theory

Extreme value theory provides the mathematical foundation for analyzing the distribution of maxima or minima from a sample. Fisher and Tippett (1928) proved that the distribution of the maximum of a large sample converges to one of three types:

- **Type I (Gumbel)**: Unbounded exponential-type tails
- **Type II (Fréchet)**: Heavy polynomial-type tails
- **Type III (Weibull)**: Bounded upper tail

Jenkinson (1955) unified these three types into the Generalized Extreme Value (GEV) distribution, which has become widely used in hydrological applications (Coles, 2001).

### 2.4.2 Two-Parameter Distributions

**Gumbel Distribution**: The Gumbel distribution, also known as the Extreme Value Type I distribution, was introduced to hydrology by Gumbel (1941, 1958). It has been widely used for flood and rainfall frequency analysis due to its simplicity and theoretical justification for maxima of exponentially distributed variables. The distribution has two parameters: location (ξ) and scale (α).

**Normal Distribution**: The normal distribution is occasionally used for transformed hydrological variables or for variables that exhibit symmetric behavior (Haan, 1977). However, its symmetric nature limits its applicability for typically right-skewed hydrological data.

**Exponential Distribution**: The exponential distribution is a special case of several other distributions and is sometimes used for threshold exceedances in partial duration series analysis (Cunnane, 1979).

### 2.4.3 Three-Parameter Distributions

**Generalized Extreme Value (GEV)**: The GEV distribution includes a shape parameter (κ) that allows for different tail behaviors (Jenkinson, 1955; Hosking et al., 1985). When κ = 0, the GEV reduces to the Gumbel distribution. Positive κ produces bounded upper tails (Weibull type), while negative κ produces heavier tails (Fréchet type). The GEV is recommended by many national guidelines for flood frequency analysis (Cunnane, 1989).

**Generalized Logistic (GLO)**: The GLO distribution is the distribution of the median of a GEV distribution and has been recommended for flood frequency analysis in the United Kingdom by the Flood Estimation Handbook (Robson & Reed, 1999). It provides heavier tails than the GEV for the same skewness.

**Generalized Normal (GNO)**: Also known as the three-parameter log-normal distribution, the GNO has been widely used in hydrology (Stedinger, 1980). It is the distribution of a variable whose logarithm follows a normal distribution with a shift parameter.

**Generalized Pareto (GPA)**: The GPA distribution is commonly used for modeling exceedances over a threshold in partial duration series analysis (Hosking & Wallis, 1987). It is the limiting distribution of excesses over high thresholds.

**Pearson Type III (PE3)**: The PE3 distribution, also known as the three-parameter gamma distribution, was recommended by Bulletin 17B for flood frequency analysis in the United States (Interagency Advisory Committee on Water Data, 1982). It has been widely used in practice, particularly with the log-Pearson Type III variant (Bobée & Ashkar, 1991).

### 2.4.4 Four-Parameter Distributions

**4-Parameter Kappa Distribution (K4D)**: The 4-Parameter Kappa distribution was introduced by Hosking (1994) as a flexible distribution that includes GEV, GLO, and GPA as special cases. The additional parameter provides greater flexibility in fitting the upper tail of the distribution, which is critical for extreme event estimation. Studies have found the 4-Parameter Kappa distribution to provide excellent fits for rainfall data in various climatic conditions (Parida, 1999; Murshed et al., 2014).

**Wakeby Distribution**: The five-parameter Wakeby distribution, introduced by Houghton (1978), provides even greater flexibility but may be prone to overfitting with limited sample sizes (Hosking, 1986).

### 2.4.5 Distribution Selection

Selecting the appropriate distribution for a given dataset is a critical step in frequency analysis. Various criteria have been proposed (Cunnane, 1989; Rao & Hamed, 2000):

- **Physical reasoning**: The distribution should be consistent with the physical processes generating the data
- **Goodness-of-fit**: Statistical tests should confirm adequate fit to observed data
- **Robustness**: The distribution should provide stable estimates across sample sizes
- **Parsimony**: Simpler distributions with fewer parameters are preferred when they provide adequate fit

L-moment ratio diagrams, plotting sample L-skewness against L-kurtosis, provide a visual tool for distribution identification (Vogel & Fennessey, 1993; Hosking & Wallis, 1997).

---

## 2.5 L-Moments: Theory and Applications

### 2.5.1 Introduction to L-Moments

L-moments, introduced by Hosking (1990), are linear combinations of probability weighted moments (PWMs) that provide an alternative to conventional product moments for summarizing probability distributions and estimating parameters. The "L" in L-moments stands for "linear," referring to the linear combinations of order statistics used in their definition.

Conventional product moments (mean, variance, skewness, kurtosis) have been used extensively in statistics but have known limitations when applied to skewed distributions or small samples (Hosking, 1990). L-moments address these limitations by providing:

- More robust estimates in the presence of outliers
- Lower variance for small sample sizes
- Better discrimination between distributions
- Bounded L-moment ratios that facilitate comparison

### 2.5.2 Probability Weighted Moments

L-moments are derived from probability weighted moments (PWMs), introduced by Greenwood et al. (1979). PWMs are defined as:

M_{p,r,s} = E[X^p {F(X)}^r {1-F(X)}^s]

where X is a random variable and F(X) is its cumulative distribution function. The most commonly used PWMs are:

β_r = M_{1,r,0} = E[X {F(X)}^r]

Greenwood et al. (1979) showed that many distributions expressible in inverse form have parameters that can be easily related to PWMs. This work laid the foundation for Hosking's (1990) development of L-moments.

### 2.5.3 Definition of L-Moments

The first four L-moments are defined as linear combinations of PWMs (Hosking, 1990):

- λ₁ = β₀
- λ₂ = 2β₁ - β₀
- λ₃ = 6β₂ - 6β₁ + β₀
- λ₄ = 20β₃ - 30β₂ + 12β₁ - β₀

These can be interpreted as:
- λ₁: Location (equivalent to the mean)
- λ₂: Scale (related to dispersion)
- λ₃: Shape (related to skewness)
- λ₄: Shape (related to kurtosis)

### 2.5.4 L-Moment Ratios

L-moment ratios are dimensionless quantities defined as (Hosking, 1990):

- τ = λ₂/λ₁ (L-coefficient of variation, L-CV)
- τ₃ = λ₃/λ₂ (L-skewness)
- τ₄ = λ₄/λ₂ (L-kurtosis)

Unlike conventional moment ratios, L-moment ratios are bounded:
- -1 < τ₃ < 1
- (5τ₃² - 1)/4 ≤ τ₄ < 1

These bounds facilitate interpretation and comparison of distributional properties across samples and distributions (Hosking & Wallis, 1997).

### 2.5.5 Advantages of L-Moments

Hosking (1990) and subsequent studies have documented numerous advantages of L-moments over conventional moments:

**Robustness to outliers**: L-moments are less affected by extreme values because they use linear combinations of order statistics rather than powers of deviations. Hosking and Wallis (1997) demonstrated that L-moment estimators have smaller bias and variance than product moment estimators, particularly for skewed distributions.

**Small sample performance**: Vogel and Fennessey (1993) showed that L-moment estimators outperform product moment estimators for samples smaller than 50-100 observations, which is typical in hydrological applications.

**Distribution identification**: L-moment ratio diagrams provide a powerful visual tool for identifying appropriate distributions. Different distributions occupy distinct regions in the τ₃-τ₄ space, facilitating distribution selection (Hosking & Wallis, 1997).

**Regional frequency analysis**: L-moments are particularly well-suited for regional frequency analysis because L-moment ratios are site-independent under the index flood assumption, allowing direct comparison and pooling across sites (Hosking & Wallis, 1997).

### 2.5.6 Sample L-Moments

For a sample of size n with ordered observations x₁:ₙ ≤ x₂:ₙ ≤ ... ≤ xₙ:ₙ, sample L-moments are calculated from sample PWMs (Hosking, 1990):

b_r = (1/n) Σᵢ₌ᵣ₊₁ⁿ [(i-1)(i-2)...(i-r)] / [(n-1)(n-2)...(n-r)] × xᵢ:ₙ

Sample L-moments are unbiased estimators of population L-moments, unlike sample product moments which require bias corrections (Hosking & Wallis, 1995).

### 2.5.7 L-Moments for Parameter Estimation

The method of L-moments for parameter estimation involves equating sample L-moments to their theoretical expressions in terms of distribution parameters and solving for the parameters (Hosking, 1990). This approach:

- Provides explicit solutions for many distributions
- Yields estimators with good statistical properties
- Is computationally efficient

Hosking and Wallis (1997) provided L-moment expressions and parameter estimation formulas for numerous distributions commonly used in hydrology.

### 2.5.8 Applications of L-Moments

L-moments have been widely applied in hydrological studies worldwide:

**Flood frequency analysis**: L-moments are now the standard method for flood frequency analysis in many countries (Hosking & Wallis, 1997; Stedinger et al., 1993).

**Rainfall frequency analysis**: Studies have applied L-moments to rainfall data in various climatic settings (Zalina et al., 2002; Zin et al., 2009; Papalexiou & Koutsoyiannis, 2013).

**Regional frequency analysis**: The L-moments framework for regional analysis (Hosking & Wallis, 1997) has been adopted by numerous national agencies.

**Drought analysis**: L-moments have been applied to characterize drought severity and duration (Santos et al., 2011).

**Wind speed analysis**: Extreme wind speeds have been analyzed using L-moments for structural design (Holmes & Moriarty, 1999).

---

## 2.6 Goodness-of-Fit Assessment

### 2.6.1 Purpose of Goodness-of-Fit Testing

Goodness-of-fit assessment determines how well a fitted distribution matches observed data. This is essential for (D'Agostino & Stephens, 1986):

- Validating distribution selection
- Comparing alternative distributions
- Identifying systematic departures from the assumed model
- Assessing reliability of extrapolated quantiles

### 2.6.2 Plotting Positions

Plotting positions assign non-exceedance probabilities to ranked observations for graphical comparison with theoretical distributions. Numerous formulas have been proposed (Cunnane, 1978):

**Weibull formula**: P_i = i / (n+1)
Introduced by Weibull (1939), this formula is widely used but may be biased for extreme value distributions.

**Hazen formula**: P_i = (i - 0.5) / n
Proposed by Hazen (1914), this formula provides an approximation to the median plotting position.

**Gringorten formula**: P_i = (i - 0.44) / (n + 0.12)
Gringorten (1963) derived this formula specifically for Gumbel-distributed data. Cunnane (1978) showed it provides approximately unbiased estimates for extreme value distributions.

**General formula**: P_i = (i - a) / (n + 1 - 2a)
Cunnane (1978) proposed a general formula where a depends on the distribution. Values of a = 0.4 to 0.44 are commonly recommended for extreme value distributions.

### 2.6.3 Probability Plot Correlation Coefficient

The probability plot correlation coefficient (PPCC) test, introduced by Filliben (1975), measures the correlation between ordered observations and theoretical quantiles. High correlation indicates good fit. Vogel (1986) provided critical values for the PPCC test for normal, lognormal, and Gumbel distributions.

### 2.6.4 Chi-Square and Kolmogorov-Smirnov Tests

Classical goodness-of-fit tests include:

**Chi-square test**: Compares observed and expected frequencies in grouped intervals. Widely used but results depend on interval selection (D'Agostino & Stephens, 1986).

**Kolmogorov-Smirnov test**: Measures the maximum difference between empirical and theoretical distribution functions. Valid for fully specified distributions but requires modification when parameters are estimated from data (Lilliefors, 1967).

### 2.6.5 Anderson-Darling and Cramér-von Mises Tests

The Anderson-Darling and Cramér-von Mises tests are based on integrated measures of discrepancy between empirical and theoretical distributions:

**Cramér-von Mises**: W² = n ∫[Fₙ(x) - F(x)]² dF(x)

**Anderson-Darling**: A² = n ∫[Fₙ(x) - F(x)]² / [F(x)(1-F(x))] dF(x)

The Anderson-Darling statistic gives more weight to tail discrepancies, making it particularly suitable for extreme value applications (Laio, 2004). Laio (2004) provided tables for these tests when parameters are estimated from data.

### 2.6.6 L-Moment Based Tests

Hosking and Wallis (1997) developed goodness-of-fit measures based on L-moments for regional frequency analysis. The Z-statistic compares the regional average L-kurtosis to the theoretical value for the candidate distribution:

Z = (t₄ᴿ - τ₄) / σ(t₄ᴿ)

Distributions with |Z| < 1.64 are considered acceptable at the 10% significance level.

### 2.6.7 Mean Absolute Deviation and Mean Squared Deviation Indices

Normalized deviation measures provide scale-independent assessments of fit:

**Mean Absolute Deviation Index (MADI)**:
MADI = (1/n) Σ|xᵢ - x̂ᵢ| / xᵢ

**Mean Squared Deviation Index (MSDI)**:
MSDI = (1/n) Σ[(xᵢ - x̂ᵢ) / xᵢ]²

These indices quantify the average relative departure of observed from theoretical quantiles. Lower values indicate better fit. MSDI penalizes larger deviations more heavily than MADI.

---

## 2.7 Return Period Analysis

### 2.7.1 Return Period Concept

The return period (also called recurrence interval) is defined as the average time between occurrences of an event of a given magnitude (Chow et al., 1988). For annual maximum series, the return period T relates to the exceedance probability p by:

T = 1 / p

For example, a 100-year return period corresponds to a 1% annual exceedance probability.

Stedinger and Griffis (2008) emphasized that return period represents an average over many occurrences and does not imply regular periodicity. Koutsoyiannis (2004) provided a detailed discussion of the probabilistic interpretation of return period.

### 2.7.2 Return Period for Partial Duration Series

When using partial duration series (peaks-over-threshold), the relationship between return period and exceedance probability is modified (Langbein, 1949; Madsen et al., 1997):

T_AMS = T_PDS / (1 - e^(-1/T_PDS))

For large return periods, T_AMS ≈ T_PDS + 0.5.

### 2.7.3 Quantile Estimation

Quantile estimation involves calculating the magnitude corresponding to a given return period. For a distribution with CDF F(x), the T-year quantile is:

x_T = F⁻¹(1 - 1/T)

where F⁻¹ is the inverse CDF (quantile function). Analytical expressions for quantile functions exist for many distributions used in hydrology (Hosking & Wallis, 1997; Rao & Hamed, 2000).

### 2.7.4 Confidence Intervals

Uncertainty in quantile estimates arises from parameter estimation error and model uncertainty. Confidence intervals quantify this uncertainty (Stedinger, 1983; Coles, 2001):

**Asymptotic methods**: Use the delta method to approximate variance of quantile estimates from parameter covariance matrices.

**Bootstrap methods**: Resample from the data to empirically estimate the sampling distribution of quantile estimates.

**Bayesian methods**: Provide posterior distributions for quantiles that incorporate prior information and parameter uncertainty.

Stedinger et al. (1993) recommended reporting confidence intervals with all quantile estimates to communicate uncertainty to decision-makers.

### 2.7.5 Risk Assessment

Return period analysis supports risk assessment for infrastructure design and planning. The probability of at least one exceedance during a design life of n years is (Chow et al., 1988):

R = 1 - (1 - 1/T)ⁿ

For example, a structure with a 50-year design life has a 39.5% probability of experiencing a 100-year event.

---

## 2.8 Malaysian and Tropical Rainfall Studies

### 2.8.1 Malaysian Climate and Rainfall

Malaysia experiences an equatorial climate influenced by two monsoon seasons: the Northeast Monsoon (November to March) and the Southwest Monsoon (May to September) (Wong et al., 2009). The east coast states, including Terengganu, receive the highest rainfall during the Northeast Monsoon, which brings moisture-laden winds from the South China Sea.

Annual rainfall in Malaysia ranges from approximately 2,000 mm in lowland areas to over 5,000 mm in highland regions (Suhaila et al., 2010). The spatial and temporal variability of rainfall has been documented by Desa and Niemczynowicz (1996) for Kuala Lumpur and by Wong et al. (2009) for Peninsular Malaysia.

### 2.8.2 Rainfall Frequency Analysis in Malaysia

Several studies have applied frequency analysis methods to Malaysian rainfall data:

**Distribution selection**: Zalina et al. (2002) compared distributions for extreme rainfall in Malaysia and found that Generalized Pareto and Pearson Type III distributions provided good fits. Suhaila and Jemain (2007, 2008) evaluated multiple distributions and recommended the normal transform distribution for daily rainfall.

**L-moments applications**: Zin et al. (2009) applied L-moments and LQ-moments to annual maximum rainfall in Peninsular Malaysia, finding that three-parameter distributions (GEV, GLO, GNO) outperformed two-parameter alternatives.

**Design rainfall estimation**: The Department of Irrigation and Drainage Malaysia (2009) published Hydrological Procedure No. 1, which provides guidelines for design rainstorm estimation based on frequency analysis.

### 2.8.3 Regional Studies in Tropical Asia

Studies from other tropical Asian regions provide context for Malaysian research:

**Singapore**: Teo and Grobe (2015) analyzed rainfall extremes in Singapore using various distributions and found evidence of intensification trends.

**Indonesia**: Aldrian and Susanto (2003) characterized rainfall patterns in Indonesia and identified three main climate regions.

**Thailand**: Limsakul and Singhruck (2016) analyzed extreme rainfall trends in Thailand and found regional variations in patterns.

### 2.8.4 African Tropical Studies

Studies from tropical Africa also contribute to understanding of tropical rainfall:

**Nigeria**: Olofintoye et al. (2009) applied L-moments to rainfall data in Nigeria, finding that the Generalized Logistic distribution provided the best fit for annual maxima.

**South Africa**: Smithers and Schulze (2001) developed regional approaches for design rainfall estimation based on L-moments.

### 2.8.5 South American Tropical Studies

Tropical regions in South America have been studied extensively:

**Brazil**: Naghettini (2017) provided comprehensive coverage of frequency analysis methods applied to Brazilian hydrological data.

**Amazon basin**: Espinoza et al. (2009) characterized rainfall variability in the Amazon basin using long-term data.

### 2.8.6 Global Comparative Studies

Papalexiou and Koutsoyiannis (2013) conducted a global survey of extreme daily rainfall, analyzing data from thousands of stations worldwide. They found that:

- The Generalized Gamma distribution family provides good fits globally
- Tropical regions exhibit different extreme rainfall characteristics than temperate regions
- Heavy tails are common in extreme rainfall distributions

This global perspective supports the need for region-specific analysis approaches that account for local climatic conditions.

---

## 2.9 Research Gap

While extensive research has been conducted on flood frequency analysis using L-moments, several gaps remain in the literature:

### 2.9.1 Limited Tropical Applications

Most foundational work on L-moments and frequency analysis was developed using data from temperate regions (Hosking & Wallis, 1997). The applicability of these methods to tropical climates, where rainfall patterns differ substantially, requires further validation (Koutsoyiannis, 2004; Papalexiou & Koutsoyiannis, 2013).

### 2.9.2 Data Decimation Concerns

Volpi et al. (2019) highlighted that traditional approaches based on annual maxima or peaks-over-threshold discard substantial portions of the observational record. The implications of this data decimation for tropical regions, where multiple extreme events occur annually, have not been thoroughly investigated.

### 2.9.3 Comparative Analysis

Limited studies have systematically compared return period estimates from annual maximum series versus daily data approaches in tropical settings. Quantifying the potential overestimation when using temperate-based methodologies in tropical climates remains an important research need.

### 2.9.4 Malaysian-Specific Studies

While some studies have applied L-moments to Malaysian rainfall data (Zin et al., 2009; Zalina et al., 2002), comprehensive analysis across multiple stations with explicit comparison of annual and daily approaches is lacking.

These gaps motivate the present research, which aims to address them through systematic analysis of rainfall data from Terengganu, Malaysia. A detailed discussion of the research gap is provided in Chapter 4.

---

## 2.10 Summary

This chapter has reviewed the literature relevant to flood frequency analysis using L-moments in tropical climates. Key findings include:

1. **Climate differences**: Tropical and temperate climates exhibit fundamentally different rainfall patterns, with implications for frequency analysis methodology.

2. **Historical development**: Flood frequency analysis methods evolved primarily in temperate regions, with the annual maximum series approach becoming standard despite its limitations.

3. **Probability distributions**: Numerous distributions are available, with three- and four-parameter distributions generally providing better fits for extreme rainfall.

4. **L-moments**: The L-moments method offers significant advantages over conventional moments, particularly for hydrological applications with limited sample sizes.

5. **Goodness-of-fit**: Various methods exist for assessing distribution fit, with normalized deviation indices providing practical measures for distribution comparison.

6. **Return period analysis**: Standard methods for quantile estimation are well-established but assumptions may be violated in tropical settings.

7. **Malaysian studies**: Previous work has applied L-moments to Malaysian rainfall but gaps remain in comparative analysis of annual versus daily approaches.

8. **Research gap**: The need for systematic comparison of frequency analysis approaches in tropical climates motivates the present research.

The methodology for addressing these gaps is presented in Chapter 3, with detailed discussion of the research gap in Chapter 4 and results in Chapter 5.

---

## References

*(See References chapter for complete reference list)*

