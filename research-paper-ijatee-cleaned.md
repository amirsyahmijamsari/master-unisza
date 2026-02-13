# Identifying and Validating Optimal Probability Distributions for Improved Return Period Estimation of Extreme Events

**Authors:** Mohammad Amir Syahmi¹, Zahrahtul Amani Zakaria¹,²*, and Nor Aida Mahiddin¹,²

**Affiliations:**
- ¹Faculty of Computing and Informatics, Universiti Sultan Zainal Abidin, Kampus Besut, 22200 Besut, Terengganu, Malaysia
- ²East Coast Environmental Research Institute (ESERI), Universiti Sultan Zainal Abidin, Kampus Gong Badak, 21300, Kuala Terengganu, Terengganu, Malaysia

**Journal:** International Journal of Advanced Technology and Engineering Exploration, Vol 12(123)  
**ISSN (Print):** 2394-5443 | **ISSN (Online):** 2394-7454  
**DOI:** http://dx.doi.org/10.19101/IJATEE.2024.111101018

**Received:** 13-June-2024 | **Revised:** 12-February-2025 | **Accepted:** 18-February-2025

©2025 Mohammad Amir Syahmi et al. This is an open access article distributed under the Creative Commons Attribution (CC BY) License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

---

## Abstract

This engineering-focused study analyzes annual maximum daily rainfall data from the Department of Irrigation and Drainage (DID) Kemaman station in Terengganu, Malaysia, to enhance flood risk management and infrastructure resilience in the region. The study aims to identify the most effective probability distribution for modeling extreme rainfall and to estimate return periods for critical events. Using the robust L-moment method, various distributions were rigorously tested and initially selected through the L-moment ratio diagram (LMRD). The four-parameter Kappa distribution (K4D) emerged as the best fit, as determined by the mean absolute deviation index (MADI) and the mean squared deviation index (MSDI). The validated model enabled the estimation of return periods, indicating that a 2-year event corresponds to 188.66 mm of rainfall, while a 100-year event is expected to reach 475.48 mm. These quantitative insights are essential for designing durable, flood-resilient infrastructure, ensuring that regional development is both sustainable and adaptable to increasing weather variability.

## Keywords

Extreme rainfall analysis, Probability distributions, Return period estimation, Flood risk management, L-moment method, Four-parameter kappa distribution.

---

## 1. Introduction

Global communities are increasingly susceptible to natural disasters, especially floods intensified by climate change and urbanization. These disasters, often triggered by significant rainfall events in poorly drained or flood-prone areas, necessitate a deep understanding of rainfall variability and distribution. Historically, frequency analysis has played a crucial role in modeling these events, relying heavily on the accuracy of probability distributions to predict and mitigate potential impacts on public safety and economic stability [1].

The challenges in predicting extreme weather events lie in the variability and complexity of rainfall data. Traditional frequency analysis methods, although useful, often fall short when dealing with outliers and non-stationary data, which are prevalent in climate datasets [2].

This research addresses these limitations by utilizing the L-moment method, which offers a more robust and less outlier-sensitive approach to parameter estimation in hydrological studies.

L-moments are a powerful tool in hydrological data analysis, providing robust measures to summarize a data distribution's shape, scale, and location [3]. One of the primary benefits of employing the L-moment approach for parameter estimation in hydrological studies is its reduced sensitivity to outliers, leading to more stable and reliable parameter estimates [4]. The L-moment method has been successfully applied in flood frequency analysis in many countries, including Malaysia [5, 6], China [7], India [8], Norway [9], Iran [10, 11], Poland [12], and Turkey [13]. This widespread utilization highlights its critical role in hydrology. Implementing this methodology in regions with adequate data is essential for comprehensive analysis.

The primary objective of this study is to apply the L-moment method to analyze annual maximum rainfall data from the Department of Irrigation and Drainage (DID) Kemaman station in Terengganu, Malaysia. This analysis aims to identify the most suitable probability distribution and estimate return periods for extreme precipitation events.

This paper contributes to the field by applying the L-moment technique in distribution parameter estimation and return period estimation, demonstrating its effectiveness in improving flood risk management and infrastructure resilience. It provides a comprehensive analysis of the best-fit probability distribution for extreme rainfall events, facilitating more accurate predictions and preparedness strategies.

The paper is structured as follows: Section 2 reviews related studies, Section 3 describes the methodology, Section 4 presents the results, Section 5 discusses the findings, and Section 6 concludes the paper.

---

## 2. Literature Review

Understanding the variability and distribution of rainfall is critical for flood risk management. Numerous studies have focused on analyzing extreme rainfall events using different methodologies. This section discusses key studies in the field, highlighting their methodologies, results, advantages, and limitations.

### 2.1 Background of L-moments

L-moments, powerful statistical tools for describing the shape of probability distributions, have been widely adopted in hydrological and meteorological studies for extreme event analysis. This review traces the background of L-moments, highlighting significant milestones and advancements that have enhanced their application in various fields.

L-moments were introduced by Hosking as an alternative to conventional moments for summarizing the characteristics of probability distributions. Traditional moments, such as mean, variance, skewness, and kurtosis, are sensitive to outliers and can be unstable for distributions with heavy tails or extreme values. L-moments, derived from linear combinations of order statistics, provide robust estimates that are less influenced by outliers and can describe the distribution shape more accurately [3].

The initial application of L-moments focused on hydrology, particularly for flood frequency analysis. Hosking and Wallis expanded the theory, providing a comprehensive framework for regional frequency analysis (RFA) using L-moments. This approach allowed for the effective pooling of data from multiple sites, improving the reliability of extreme rainfall and flood event estimates [4].

### 2.2 L-moment Ratio Diagram (LMRD)

LMRDs have become an essential tool for hydrologists and statisticians. They are used to compare and select appropriate probability distributions for RFA and other applications. For example, LMRDs are employed to identify the best-fit distribution for rainfall, flood frequency, and other hydrological data.

Vogel and Fennessey demonstrated that LMRDs are superior to conventional moment ratio diagrams (MRDs) in hydrology. They found that LMRDs provided clearer insights into the distributional properties of daily streamflow data compared to traditional moment diagrams [14]. Peel et al. illustrated the utility of LMRDs for selecting regional probability distributions. They showed that LMRDs, combined with heterogeneity tests, effectively discriminate between distributions in both homogeneous and heterogeneous regional samples [15]. Haddad applied LMRDs to analyze temperature data in New South Wales, Australia, and found that LMRDs allowed for easy comparison of the fit of multiple distributions across several stations [16].

Similarly, Ouarda et al. used LMRDs to assess the fit of probability distributions for wind speed data in the United Arab Emirates, highlighting their effectiveness in various climatic contexts [17]. Hosking extended L-moments to trimmed L-moments for analyzing heavy-tailed distributions, proposing a trimmed LMRD as an enhancement for identifying distributions suited to extreme events. This approach further solidifies the utility of LMRDs in extreme value theory [18]. Bobée et al. emphasized the complementary nature of LMRDs with traditional MRDs, suggesting that integrating both can provide a more comprehensive understanding of distributional properties. Their study highlighted the adaptability of LMRDs in various hydrological applications [19].

LMRD have proven to be a robust and reliable tool for selecting and evaluating probability distributions, particularly in hydrology and environmental sciences. Their ability to provide nearly unbiased estimates and facilitate easy comparison of distributions makes them indispensable for statistical analysis of extreme events.

*[Note: The full literature review section continues with subsections on integration of L-moments with other methods, recent applications, limitations, and return period in hydrology. The complete content is preserved in the original file.]*

---

## 3. Materials and Methods

### 3.1 L-moments

*[Note: This section contains detailed mathematical formulations of L-moments, their calculation methods, and relationships to probability-weighted moments. The complete technical content is preserved in the original file.]*

### 3.2 Study Area and Dataset

The study focuses on the DID Kemaman station in Terengganu, Malaysia. The dataset consists of annual maximum daily rainfall measurements collected over several decades. The data quality and homogeneity were verified before analysis.

### 3.3 Goodness-of-Fit Criteria

The study employs two primary goodness-of-fit metrics:

- **Mean Absolute Deviation Index (MADI):** Measures the mean of absolute normalized differences between observed and theoretical quantiles.
- **Mean Squared Deviation Index (MSDI):** Measures the mean of squared normalized differences.

These metrics are calculated as:

\[
\text{MADI} = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{x_i - z_i}{x_i}\right|
\]

\[
\text{MSDI} = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{x_i - z_i}{x_i}\right)^2
\]

where \(x_i\) represents observed values and \(z_i\) represents theoretical quantiles.

### 3.4 Flow of Enhanced Return Period Estimation

The analytical workflow includes:
1. Data collection and preprocessing
2. L-moment calculation
3. Distribution fitting using L-moments
4. Initial selection via LMRD
5. Goodness-of-fit evaluation using MADI and MSDI
6. Selection of best-fit distribution
7. Return period estimation

### 3.5 Software and Hardware

The analysis was conducted using Python programming language with specialized libraries for statistical analysis and L-moments calculations.

---

## 4. Results and Discussion

### 4.1 Time Series Plot

The time series analysis of annual maximum daily rainfall data from DID Kemaman station reveals the temporal variability and trends in extreme rainfall events.

### 4.2 L-moment Ratio Diagram

The LMRD analysis was used to initially screen potential distributions. The L-skewness (τ₃) and L-kurtosis (τ₄) values for the DID Kemaman dataset were plotted against theoretical distribution curves to identify candidate distributions.

### 4.3 L-moment Parameter Estimation

The dataset containing the annual maximum daily rainfall measurements for DID Kemaman was subsequently subjected to computational analysis. The parameters for the distributions were estimated through the L-moment method. A comprehensive summary of the estimated parameters for each distribution is presented in Table 3. The selection of the distributions is based on the closeness of the τ₃ and τ₄ of DID Kemaman with the distributions' curves in the LMRD depicted in Figure 3.

**Table 3: Estimated Parameters of Probability Distributions for DID Kemaman Station**

| Distribution | Estimated Parameters |
|-------------|---------------------|
| Gumbel | ε̂ = 166.3341, α̂ = 65.9984 |
| GLO | ε̂ = 190.2906, α̂ = 43.0416, k̂ = -0.1913 |
| GEV | ε̂ = 165.3589, α̂ = 63.9563, k̂ = -0.0330 |
| GPA | ε̂ = 96.5760, α̂ = 146.4247, k̂ = -0.3576 |
| Pe3 | ε̂ = 204.4294, α̂ = 84.5408, k̂ = 1.1585 |
| GNO | ε̂ = 188.8249, α̂ = 75.9759, k̂ = -0.3950 |
| K4D | ε̂ = 158.9837, α̂ = 70.6798, k̂ = 0.0118, ĥ = 0.1582 |

#### 4.3.1 Parameter Implications to Rainfall Behavior

**Location Parameter (ε)**

The location parameter ε represents the central or median value of a distribution. Accurately estimating ε is crucial because it establishes the baseline for what is considered normal or typical rainfall within any model. A higher ε value indicates that extreme rainfall events occur more frequently within the region's climate pattern and are not merely outliers. Precise estimation of this parameter is essential, as minor errors can significantly misrepresent the central tendency, impacting decisions related to water resource management and agricultural planning.

**Scale Parameter (α)**

The scale parameter α determines the spread or variability of rainfall data. Accurately capturing α is vital for understanding the potential range of rainfall events. A larger α implies greater variability, suggesting that the region may experience a broad range of rainfall intensities. Precise estimation of α is critical because return periods are sensitive to changes in variability. Underestimating α could understate the risk of flooding, while overestimating might lead to economically inefficient infrastructure planning due to excessive caution.

**Shape Parameters (k & h)**

These parameters significantly influence the distribution's tail behavior and asymmetry. A positive k value indicates a heavier tail, which suggests a higher likelihood of severe events. The parameter h adjusts the asymmetry, impacting how skewed the data might appear toward higher extremes. Accurately estimating k and h is crucial as they determine the upper extremes of rainfall predictions, key for disaster preparedness and emergency management strategies. Errors in these estimates can lead to inadequate preparedness for extreme events.

The accurate and precise estimation of ε, α, k, and h is essential not only as a statistical concern but also as a practical necessity. Given how sensitive return period calculations are to these parameters, small deviations can lead to significantly different outcomes in model predictions. This highlights the need for robust statistical methods and high-quality data to ensure that models reliably reflect the true risks and characteristics of extreme rainfall events.

### 4.4 Goodness-of-Fit

#### 4.4.1 Goodness-of-Fit (MADI and MSDI)

Following the initial evaluation via the LMRD, the analytical methodology was expanded to include other goodness-of-fit metrics, specifically MADI and MSDI. The collective outcomes from these metrics indicate that the K4D yields the lowest value of MADI and MSDI of all the distributions, hence serves as the most fitting model for the dataset under study. The outcomes for the metrics are summarized in Table 4.

**Table 4: MADI and MSDI Goodness-of-Fit Tests**

| Distribution | MADI | MSDI |
|-------------|------|------|
| Gumbel | 0.0340 | 0.0018 |
| GLO | 0.0410 | 0.0029 |
| GEV | 0.0315 | 0.0015 |
| GPA | 0.0476 | 0.0042 |
| Pe3 | 0.0298 | 0.0014 |
| GNO | 0.0301 | 0.0013 |
| K4D | 0.0294 | 0.0013 |

Based on the results presented in Table 4, which summarizes the outcomes of the goodness-of-fit tests using MADI and MSDI, it is concluded that the K4D distribution provides the most suitable fit for the dataset among the distributions evaluated. This conclusion is drawn from the observation that the K4D distribution yields the lowest values for both MADI and MSDI, with scores of 0.0294 and 0.0013, respectively. These metrics are critical in assessing the goodness of fit, where lower values indicate a closer match between the observed data and the model's predictions.

#### 4.4.2 Goodness-of-Fit Visualization

Following the quantitative assessment of the goodness-of-fit through MADI and MSDI metrics, graphical visualization offers an intuitive means to further validate the model's fit. The visualization through the transformed Q-Q plot depicted in Figure 4 typically involves plotting the observed data against the model predictions to visually assess how well the model captures the underlying distribution of the data. The blue line represents theoretical quantiles, while the dashed black line represents actual data quantiles.

### 4.5 Return Period Estimation

Using the validated K4D distribution with estimated parameters, return periods were calculated for various rainfall magnitudes. The results indicate that:

- A 2-year return period corresponds to 188.66 mm of rainfall
- A 5-year return period corresponds to 265.29 mm of rainfall
- A 10-year return period corresponds to 316.51 mm of rainfall
- A 20-year return period corresponds to 365.55 mm of rainfall
- A 50-year return period corresponds to 428.61 mm of rainfall
- A 100-year return period corresponds to 475.48 mm of rainfall

For the peak observed value of 440.3 mm, the analysis determined that the probability of annual rainfall exceeding this threshold is 1.7% (Px = 0.017), corresponding to an estimated return period of approximately 59 years.

### 4.6 Sensitivity Analysis

Sensitivity analysis was conducted to assess the impact of parameter variations on return period estimates. The results highlight the importance of precise parameter estimation, particularly for the scale and location parameters, due to their pronounced impact on model outputs. Accurate parameter calibration is essential for enhancing the predictive accuracy and reliability of hydrological models. Employing L-moments for parameter estimation provides a significant advantage, as it predicts parameters more accurately compared to traditional methods.

---

## 5. Discussions

### 5.1 Summary of Key Findings

Through L-moment parameter estimation, various probability distributions were analyzed, with the K4D distribution emerging as the most suitable model for the dataset. This conclusion was supported by the goodness-of-fit tests using MADI and MSDI, where the K4D distribution yielded the lowest deviation values, indicating the best fit shown in Table 4. The study effectively utilized the K4D to estimate the return periods of extreme rainfall events at the DID Kemaman station.

A critical finding from this analysis is the calculation of return period for significant rainfall events, particularly those that match or exceed the peak observed value of 440.3 mm. By inserting the estimated parameters (ε = 158.9837, α = 70.6799, k = 0.0118, h = 0.1582) into the CDF of the K4D, it was determined that the probability of annual rainfall exceeding 440.3 mm is 1.7% (Px = 0.017). This corresponds to an estimated return period of approximately 59 years.

### 5.2 Implications of Findings

The methodology applied in this study extends beyond extreme rainfall events. For example, if an analyst wants to determine the return period of a 150 mm rainfall event, they can do so by adjusting the input value of x in the CDF function. By substituting x = 150 into the K4D CDF function, the probability Px of exceeding this threshold can be determined, followed by calculating its return period using the inverse probability formula. This model's flexibility enables stakeholders, including hydrologists and urban planners, to assess rainfall frequency for specific needs, such as agricultural water resource planning or infrastructure development.

The findings of this study have several implications for flood risk management in Terengganu and similar regions. The robust modeling of extreme rainfall events using the K4D distribution enables more accurate predictions of future events, which is critical for designing resilient infrastructure. The detailed return period analysis provides essential data for planning and decision-making, ensuring flood defenses and emergency response strategies rely on reliable statistical models.

Furthermore, L-moments and the K4D distribution apply to other regions with similar climatic and hydrological conditions, providing a valuable tool for comparative studies and hydrological risk assessment.

### 5.3 Limitations of Study

While the ability to adjust input magnitudes for calculating return periods offers significant advantages, it also introduces complexities that must be managed carefully. The accuracy of these calculations depends heavily on the model's reliability and the assumptions underpinning it, such as the stationarity of climate patterns and the quality of historical data. Changes in climatic conditions, particularly those driven by climate change, could alter precipitation patterns and challenge the assumption of stationarity on which many models rely. Furthermore, the sensitivity of return periods to specific model parameters highlights the need for precision in data collection and parameter estimation.

### 5.4 Recommendations for Future Research

To enhance the robustness and practical applicability of these findings, future research should focus on integrating non-stationary models to account for climate change impacts. Additionally, the incorporation of real-time data and advanced computational techniques, such as machine learning, could improve predictive accuracy and computational efficiency. Expanding the dataset to include more rainfall stations and longer observation periods would also provide a more detailed and reliable analysis. Comparative studies across different climatic regions using the L-moments method and the K4D distribution could further validate the effectiveness of these models.

---

## 6. Conclusion

This research embarked on a detailed examination of the annual maximum daily rainfall data at the DID Kemaman station, with the dual objectives of identifying the most fitting probability distribution and estimating the return periods of extreme rainfall events. Employing the L-moment method for parameter estimation, a variety of distributions were initially considered, guided by the insights provided by the LMRD. The subsequent employment of goodness-of-fit criteria, specifically through the MADI and MSDI, facilitated a meticulous evaluation of these distributions' suitability in modeling the observed rainfall data. The K4D distribution was identified as the most accurate model, exhibiting the lowest values in both MADI and MSDI assessments.

The results further reinforced this finding, confirming the superior accuracy of the K4D distribution. Moreover, the application of the K4D distribution for further analysis yielded significant insights into the return periods of extreme rainfall events. Notably, the analysis found that a 2-year return period corresponds to a rainfall event of 188.66 mm, while a 100-year return period predicts a significant rainfall event of 475.48 mm.

The study demonstrates the effectiveness of the L-moment method in providing robust parameter estimates for extreme value analysis, contributing valuable insights to flood risk management and infrastructure planning in tropical regions. The methodology and findings presented in this research provide a foundation for improved water resource management and disaster preparedness strategies.

---

## References

*[Note: The complete reference list is preserved in the original file. Key references include:*

- *Hosking (1990) - L-moments methodology*
- *Hosking & Wallis (1997) - Regional frequency analysis*
- *Various applications of L-moments in different countries*
- *Studies on goodness-of-fit criteria and return period estimation*

*The full reference list with proper citations is available in the original research-paper-ijatee.md file.]*

---

## Author Information

**Mohammad Amir Syahmi** - *[Author biography preserved in original file]*

**Dr. Zahrahtul Amani Zakaria** - *[Author biography preserved in original file]*

**Dr. Nor Aida Mahiddin** - *[Author biography preserved in original file]*

---

## Appendix I: Abbreviations

| S. No. | Abbreviation | Description |
|--------|--------------|-------------|
| 1 | CDF | Cumulative Distribution Function |
| 2 | CTA | Complete Time Series Analysis |
| 3 | DID | Department of Irrigation and Drainage |
| 4 | EV1 | Extreme Value Type I |
| 5 | GEV | Generalized Extreme Value |
| 6 | GLO | Generalized Logistic |
| 7 | GNO | Generalized Normal Distribution |
| 8 | GPA | Generalized Pareto |
| 9 | HEC-HMS | Hydrologic Engineering Center – Hydrologic Modeling System |
| 10 | K4D | Four-Parameter Kappa Distribution |
| 11 | LH-moments | Linear Combination of H-Statistics |
| 12 | L-moments | Linear Combination of Probability Weighted Moment |
| 13 | LMRD | L-Moment Ratio Diagram |
| 14 | LN3 | Three-Parameter Lognormal |
| 15 | LQ-moments | Linear combination of Quantile functions |
| 16 | MADI | Mean Absolute Deviation Index |
| 17 | MAE | Mean Absolute Error |
| 18 | MoM | Method of Moments |
| 19 | MRD | Moment Ratio Diagram |
| 20 | MSDI | Mean Squared Deviation Index |
| 21 | NOM | Normal Distribution |
| 22 | Pe3 | Pearson Type III Distribution |
| 23 | PL-moments | Partial L-Moments |
| 24 | PWM | Probability Weighted Moment |
| 25 | RFA | Regional Frequency Analysis |
| 26 | RMSE | Root Mean Square Error |

---

*Note: This cleaned version preserves all key content while improving readability. For complete details including all tables, figures, mathematical formulations, and the full reference list, please refer to the original research-paper-ijatee.md file.*

