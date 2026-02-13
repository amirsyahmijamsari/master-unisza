# CHAPTER 4: RESEARCH GAP

## 4.1 Introduction

This chapter identifies the research gaps that motivate this study and demonstrates the advantages of using daily rainfall data over the traditional Annual Maximum (AM) method for hydrological analysis in tropical climates. The AM method, commonly used in hydrological studies worldwide, was initially designed for temperate regions where rainfall events are less intense and less variable. However, in tropical regions like Malaysia, where extreme rainfall events occur frequently and in quick succession, the AM method may fail to capture significant hydrological data, potentially underestimating flood risks and misrepresenting event return periods.

The chapter reviews the limitations of current approaches, discusses the concept of data decimation in hydrological analysis, and establishes the theoretical foundation for why daily rainfall analysis provides more reliable estimates in tropical climates. The research gaps identified here directly inform the objectives outlined in Chapter 1 and the methodology presented in Chapter 3.

---

## 4.2 Motivation

The motivation for this research stems from the observation that many hydrological models and methodologies applied in tropical regions are directly derived from studies conducted in temperate climates. Despite significant differences in climate patterns, researchers in tropical regions often continue to use these temperate-based models, which may not fully capture the dynamics of tropical rainfall. This is particularly problematic when analyzing extreme events, as tropical climates are characterized by seasonality and persistence—factors that are often missed by the AM method.

### 4.2.1 Origins of the Annual Maximum Method

The Annual Maximum Series (AMS) approach has been the cornerstone of flood frequency analysis since its introduction in the early 20th century. This method was developed primarily by researchers in temperate regions of Europe and North America, where:

- Extreme rainfall events are relatively infrequent (typically once or twice per year)
- Rainfall patterns show moderate variability
- Hydrological systems have longer response times
- Infrastructure design standards were based on annual risk assessments

The underlying assumption of the AM method is that selecting the single largest event per year provides sufficient information to characterize extreme event frequencies. This assumption holds reasonably well in temperate climates where extreme events are rare.

### 4.2.2 The Tropical Climate Challenge

Terengganu, located on the east coast of Peninsular Malaysia, experiences a tropical monsoon climate that fundamentally differs from temperate conditions:

- **High rainfall intensity**: Annual rainfall ranges from 2,500 to 4,000 mm
- **Multiple extreme events**: The Northeast Monsoon (November to March) brings numerous heavy rainfall events
- **Clustering of extremes**: Multiple significant rainfall events often occur within days or weeks
- **Rapid hydrological response**: Short catchment response times due to intense rainfall

In such environments, the AM method's selection of only one event per year discards potentially critical information about the frequency and magnitude of extreme events.

### 4.2.3 The Need for Complete Time-Series Analysis

This research advocates for Complete Time-series Analysis (CTA) using daily rainfall data, which provides a more comprehensive and accurate approach for understanding extreme rainfall events in tropical regions. By utilizing daily data, this study aims to offer a clearer framework for improving rainfall risk assessments and ensuring that hydrological models are better suited for tropical climates.

---

## 4.3 The Problem of Data Decimation

### 4.3.1 What is Data Decimation?

Data decimation refers to the reduction or discarding of observational data during the analysis process. In traditional hydrological frequency analysis, this occurs through:

1. **Annual Maximum Selection**: From thousands of daily observations spanning decades, only one value per year is retained
2. **Peak-Over-Threshold Filtering**: Only events exceeding an arbitrary threshold are considered
3. **Independence Requirements**: Events occurring close together may be combined or discarded to meet independence assumptions

For a 30-year record with daily observations, the AM method reduces approximately 10,950 data points to just 30 values—a decimation ratio of over 99.7%.

### 4.3.2 Volpi et al. (2019): Save Hydrological Observations!

The seminal paper by Volpi, Fiori, Grimaldi, Lombardo, and Koutsoyiannis (2019), titled "Save hydrological observations! Return period estimation without data decimation," provides a compelling argument against traditional data decimation practices. Their key findings include:

**The Complete Time-Series Analysis (CTA) Approach:**

Volpi et al. propose using the full observed time series to estimate return periods rather than discarding data through selection procedures. The fundamental insight is that the average interarrival time of potentially damaging events is not affected by dependence structures—seasonality or clustering—as long as the full chronological dataset is used.

**Key Findings from Volpi et al.:**

1. **More Conservative Estimates**: CTA yields more conservative (higher risk) return period estimates than AM methods, particularly for less frequent, long-return-period events

2. **Broader Applicability**: CTA provides reliable estimates over a broader range of return periods because it retains more information from the observational record

3. **Better Statistical Power**: Using more data points improves the statistical reliability of fitted distributions, especially in the distribution tails that govern extreme event estimation

4. **Reduced Uncertainty**: The increased sample size reduces confidence intervals around return period estimates

**Implications for Tropical Climates:**

The Volpi et al. study highlights that traditional methods were developed for contexts where data decimation had minimal impact. In tropical climates with frequent extremes, the loss of information through decimation is far more consequential.

### 4.3.3 Statistical Consequences of Data Decimation

The reduction from daily to annual data introduces several statistical problems:

**Reduced Sample Size:**
- Fewer data points lead to higher uncertainty in parameter estimates
- Extreme quantile estimates become unreliable
- Confidence intervals widen substantially

**Loss of Information:**
- Multiple significant events within a year are reduced to a single value
- Temporal patterns and clustering are obscured
- Seasonal variations in extreme events are not captured

**Potential for Bias:**
- If extreme events cluster (as in monsoon seasons), AM may systematically underestimate frequency
- The largest event may not represent the overall risk pattern
- Return periods may be overestimated, leading to under-designed infrastructure

---

## 4.4 Gaps in Current Research

### 4.4.1 Gap 1: Limited Application of CTA in Tropical Regions

While the Volpi et al. (2019) methodology has been validated in Mediterranean and temperate contexts, there is a notable lack of comprehensive studies applying Complete Time-series Analysis to tropical rainfall data. Specifically:

- Few studies compare AM and daily-based return periods in Southeast Asian tropical climates
- The degree of overestimation in tropical contexts remains unquantified
- Recommendations for best practices in tropical regions are lacking

**How this research addresses the gap:**
This study applies both AM and daily rainfall analysis to 20 stations in Terengganu, directly quantifying the overestimation factor and providing empirical evidence specific to tropical Malaysia.

### 4.4.2 Gap 2: Inadequate Distribution Selection for Tropical Data

Most flood frequency analysis guidelines recommend distributions (Gumbel, GEV, Log-Normal) that were validated primarily on temperate climate data. Questions remain:

- Are these distributions appropriate for tropical daily rainfall?
- Does the best-fitting distribution differ between AM and daily data?
- How does distribution choice affect return period estimates?

**How this research addresses the gap:**
By fitting nine probability distributions to both AM and daily data and using rigorous goodness-of-fit criteria (MADI, MSDI), this study identifies the most appropriate distributions for tropical rainfall analysis.

### 4.4.3 Gap 3: Lack of L-Moments Application to Tropical Daily Data

The L-moments method, while recognized for its robustness, has been primarily applied to AM series in most published studies. There is limited research on:

- L-moment characteristics of tropical daily rainfall
- Comparison of L-moment patterns between AM and daily data
- Performance of L-moments parameter estimation for high-volume daily datasets

**How this research addresses the gap:**
This study calculates L-moments for both AM and daily rainfall series across 20 stations, documenting the differences in L-moment ratios and their implications for distribution fitting.

### 4.4.4 Gap 4: No Standardized Overestimation Quantification

While researchers acknowledge that AM may overestimate return periods compared to daily analysis, there is no widely accepted metric or methodology for quantifying this overestimation. Questions include:

- How should overestimation be defined and measured?
- What is the typical range of overestimation in tropical climates?
- How does overestimation vary with event magnitude?

**How this research addresses the gap:**
This study proposes and applies a clear overestimation factor formula:

OE(M) = RP_AM(M) / (RP_daily(M) / 365.25)

This provides a standardized, reproducible metric for comparing return period estimates between methods.

### 4.4.5 Gap 5: Regional Studies for Malaysia

Despite Malaysia's vulnerability to flooding and heavy monsoon rainfall, there are few comprehensive studies on:

- L-moments characteristics of Malaysian rainfall data
- Best-fitting distributions for extreme rainfall in Terengganu
- Comparison of AM vs daily approaches for Malaysian stations

**How this research addresses the gap:**
This study provides detailed analysis for 20 stations across Terengganu, establishing a regional database of L-moments statistics, best-fitting distributions, and return period estimates.

---

## 4.5 Theoretical Framework for Daily Data Superiority

### 4.5.1 Information Content

Consider a rainfall station with N years of daily records. The information content differs dramatically:

**Annual Maximum Series:**
- Sample size: N values
- Information retained: Only the single largest event per year
- Events discarded: All other rainfall events, including the 2nd, 3rd, ... largest events each year

**Daily Rainfall Series:**
- Sample size: Approximately 365.25 × N values (minus non-rainfall days)
- Information retained: Complete temporal record of all rainfall events
- Events discarded: None (only non-rainfall days filtered)

For a typical 34-year record in Terengganu:
- AM approach: 34 data points
- Daily approach: ~6,000-9,000 rainfall days

### 4.5.2 Frequency Interpretation

The fundamental issue lies in how return periods are interpreted:

**AM Return Period:**
- Answers: "How often will the annual maximum exceed magnitude M?"
- Interpretation: Once every T years, the largest event of the year will exceed M

**Daily Return Period:**
- Answers: "How often will any day's rainfall exceed magnitude M?"
- Interpretation: On average, every T days, rainfall will exceed M

For tropical climates with multiple extreme events per year, the daily interpretation provides more actionable information for:
- Drainage system design (must handle multiple extreme events, not just one)
- Flood warning systems (need to respond to each event, not just annual maxima)
- Agricultural planning (crop damage from repeated heavy rainfall)
- Infrastructure maintenance (cumulative stress from multiple events)

### 4.5.3 The Multiplicity Effect

In tropical Terengganu, analysis shows that for moderate extreme thresholds (e.g., 100 mm):
- Average of 4-5 days per year exceed this threshold
- AM captures only 1 of these events
- 75-80% of extreme events are "lost" to data decimation

This multiplicity effect explains why AM-based return periods may significantly overestimate the rarity of extreme events—they ignore the repeated occurrence of similar-magnitude events throughout the year.

---

## 4.6 Research Questions Derived from Gaps

Based on the identified gaps, this research addresses the following questions:

1. **What are the L-moment characteristics of tropical rainfall in Terengganu, and how do they differ between AM and daily data?**
   - Addressing Gaps 3 and 5

2. **Which probability distribution best fits tropical rainfall data, and does this differ between AM and daily series?**
   - Addressing Gaps 2 and 5

3. **What are the return period estimates for extreme rainfall events in Terengganu?**
   - Addressing Gap 5

4. **What is the degree of overestimation when using the AM approach compared to daily data analysis?**
   - Addressing Gaps 1 and 4

---

## 4.7 Significance of Addressing These Gaps

### 4.7.1 Scientific Contribution

By addressing the identified gaps, this research contributes to:

- Validation of Complete Time-series Analysis concepts in tropical contexts
- Documentation of L-moment characteristics for Malaysian rainfall
- Empirical quantification of AM overestimation in tropical climates
- Evidence-based recommendations for distribution selection

### 4.7.2 Practical Implications

The findings have direct implications for:

**Infrastructure Design:**
If AM overestimates return periods (i.e., suggests events are rarer than they are), infrastructure designed using AM-based estimates may be under-designed for actual flood risk.

**Flood Risk Assessment:**
More accurate return period estimates enable better flood risk mapping and emergency preparedness planning.

**Climate Adaptation:**
Understanding the true frequency of extreme events supports more effective climate adaptation strategies in tropical regions.

**Policy Development:**
Evidence-based recommendations can inform updates to Malaysian design standards and hydrological guidelines.

---

## 4.8 Summary

This chapter has identified critical research gaps in the application of flood frequency analysis methods to tropical climates:

1. **Data Decimation**: The AM method discards over 99% of available rainfall data, losing critical information about extreme event frequencies

2. **Volpi et al.'s Contribution**: Complete Time-series Analysis preserves information and provides more conservative risk estimates, but has not been widely applied to tropical climates

3. **Regional Gap**: Limited comprehensive studies exist for Malaysian tropical rainfall using L-moments with both AM and daily data

4. **Quantification Gap**: No standardized method exists for measuring the overestimation induced by AM approaches

5. **Distribution Selection**: Uncertainty remains about appropriate distributions for tropical rainfall at different temporal scales

This research directly addresses these gaps through comprehensive analysis of 20 rainfall stations in Terengganu, applying L-moments methodology to both AM and daily data, and quantifying the degree of overestimation inherent in traditional AM approaches.

The results of this analysis, presented in Chapter 5, demonstrate the importance of reconsidering traditional temperate-based methodologies when applied to tropical climate contexts.

---

## References

Volpi, E., Fiori, A., Grimaldi, S., Lombardo, F., & Koutsoyiannis, D. (2019). Save hydrological observations! Return period estimation without data decimation. *Journal of Hydrology*, 571, 782-792. https://doi.org/10.1016/j.jhydrol.2019.02.017

Hosking, J. R. M. (1990). L-moments: Analysis and estimation of distributions using linear combinations of order statistics. *Journal of the Royal Statistical Society: Series B (Methodological)*, 52(1), 105-124.

Gringorten, I. I. (1963). A plotting rule for extreme probability paper. *Journal of Geophysical Research*, 68(3), 813-814.

