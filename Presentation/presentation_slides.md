# L-Moments Flood Frequency Analysis in Tropical Climate
## MSc Progress Presentation

---

## Slide 1: Title

**L-Moments Flood Frequency Analysis:**
**A Comparative Study of Annual Maximum Series vs. Daily Rainfall Data in Terengganu, Malaysia**

*MSc Research - Final Semester*

---

## Slide 2: Research Background

- **Problem**: Conventional flood frequency analysis methods developed for temperate climates may inadequately represent tropical rainfall patterns
- **Study Area**: Terengganu, Malaysia (20 rainfall stations)
- **Climate**: Tropical monsoon with frequent and intense rainfall events
- **Challenge**: Multiple extreme events per year vs. single annual maxima in temperate regions

---

## Slide 3: Research Objectives

1. **Estimate distribution parameters** using L-moments method
2. **Identify best-fitting distribution** using MADI/MSDI criteria
3. **Conduct return period analysis** for extreme rainfall quantiles
4. **Quantify overestimation** when using Annual Maxima vs. daily rainfall data

---

## Slide 4: Methodology

- **Data**: 20 stations, both Annual Maximum Series (AMS) and Daily Rainfall Series
- **Method**: L-moments parameter estimation (Hosking, 1990)
- **Distributions Evaluated**: 9 distributions (Gumbel, Normal, Exponential, GEV, GLO, GNO, GPA, PE3, 4-Parameter Kappa)
- **Goodness-of-Fit**: Mean Absolute Deviation Index (MADI) and Mean Squared Deviation Index (MSDI)
- **Analysis**: Return periods 2-100 years, overestimation quantification at 99th percentile

---

## Slide 5: Key Finding 1 - Distribution Selection

![Figure 5.3: Best Distribution Summary](../Coding/Cursor%20Analysis/Figures/Figure_5_3_Best_Distribution_Summary.png)

**4-Parameter Kappa (K4D) Distribution:**
- **Daily Rainfall**: Best fit for **100%** of stations (20/20)
- **Annual Maximum**: Best fit for **40%** of stations (8/20)
- **Conclusion**: K4D is the most suitable distribution for tropical rainfall patterns

---

## Slide 6: Key Finding 2 - L-Moment Characteristics

![Figure 5.1: L-Moment Ratio Diagram](../Coding/Cursor%20Analysis/Figures/Figure_5_1_LMoments_Ratio_Diagram.png)

**Daily Rainfall Series:**
- Consistently high L-skewness (τ₃ ≈ 0.47-0.55)
- Tight clustering in L-moment ratio diagram (red squares)
- More right-skewed distributions than annual maxima

**Annual Maximum Series:**
- Variable L-skewness (τ₃ ≈ 0.02-0.47)
- Greater dispersion across distribution types (blue circles)
- Less consistent patterns across stations

---

## Slide 7: Key Finding 3 - Return Period Analysis

![Figure 5.5: Return Period Curves](../Coding/Cursor%20Analysis/Figures/Figure_5_5_Return_Period_Curves.png)

**100-Year Return Values:**
- **Annual Maximum Series**: 365.5 - 1124.9 mm
- **Daily Rainfall Series**: 129.9 - 169.3 mm
- **Ratio**: Daily values are 2.8-6.6x lower than Annual Maximum

**Implication**: Significant differences in extreme value estimates between approaches

---

## Slide 8: Spatial Patterns in Return Values

![Figure 5.6: Return Values Heatmap](../Coding/Cursor%20Analysis/Figures/Figure_5_6_Return_Values_Heatmap.png)

**Spatial Variability:**
- Distinct patterns across Terengganu stations
- Certain stations show higher return values (e.g., 0680071RF: Balai Polis Kg. Dura with 1124.9 mm)
- Clear gradient from low to high return periods (2-100 years)
- Regional differences in extreme rainfall characteristics

---

## Slide 9: Key Finding 4 - Overestimation Quantification

![Figure 5.7: Overestimation by Station](../Coding/Cursor%20Analysis/Figures/Figure_5_7_Overestimation_by_Station.png)

**At 99th Percentile (Extreme Events):**
- **Mean Overestimation Factor**: **8.50x**
- **Range**: 7.14x to 9.99x across all stations
- **Overestimation Percentage**: **750%**

**Critical Finding**: Events that AM analysis suggests occur once per year may actually occur approximately once every **43 days**

---

## Slide 10: Implications

**For Flood Risk Assessment:**
- Annual Maxima approach significantly underestimates extreme event frequency
- Daily data analysis provides more accurate representation for tropical climates
- Infrastructure design based on AM may be inadequate

**For Water Resource Management:**
- More frequent extreme events than previously estimated
- Need for revised flood preparedness strategies
- Better alignment with actual tropical rainfall behavior

---

## Slide 11: Contributions to SDGs

This research contributes to:

- **SDG 6** (Clean Water and Sanitation): Improved water resources management
- **SDG 11** (Sustainable Cities): Enhanced disaster risk reduction
- **SDG 13** (Climate Action): Better resilience to climate-related hazards

---

## Slide 12: Conclusions

1. **L-moments method** is highly effective for tropical rainfall analysis
2. **4-Parameter Kappa distribution** is recommended for Terengganu and similar tropical regions
3. **Daily rainfall data** provides more accurate extreme event frequency estimates
4. **8.5x overestimation** at 99th percentile highlights critical bias in AM approach
5. **Tropical climates require adapted methodologies** rather than direct application of temperate climate methods

---

## Slide 13: Recommendations

**For Practitioners:**
- Use daily rainfall data for flood frequency analysis in tropical regions
- Adopt 4-Parameter Kappa distribution for tropical rainfall modeling
- Apply 8.5x adjustment factor when using Annual Maxima data at extreme percentiles

**For Future Research:**
- Extend analysis to other tropical regions
- Investigate climate change impacts on extreme rainfall patterns
- Develop regional frequency analysis frameworks

---

## Slide 14: Thank You

**Questions & Discussion**

---
