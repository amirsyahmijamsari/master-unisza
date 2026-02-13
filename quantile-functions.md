# Quantile Functions of Probability Distributions

This document presents the quantile functions (inverse cumulative distribution functions) for the nine probability distributions used in L-moments flood frequency analysis.

## Notation

- **F**: Cumulative distribution function (CDF), representing the non-exceedance probability (0 ≤ F ≤ 1)
- **x(F)**: Quantile function, representing the value of the random variable corresponding to probability F
- **ε** (epsilon): Location parameter
- **α** (alpha): Scale parameter
- **K, k**: Shape parameter(s)
- **h**: Second shape parameter (for K4D)
- **μ** (mu): Mean (for Normal distribution)
- **σ** (sigma): Standard deviation (for Normal distribution)
- **Φ⁻¹**: Inverse standard normal distribution function

---

## 1. Gumbel Distribution (GUM)

**Parameters:** Location (ε), Scale (α)

**Quantile Function:**

```
x(F) = ε - α × ln(-ln(F))
```

**Parameter Description:**
- F: Cumulative distribution function (CDF), location and scale parameter respectively
- ε: Location parameter
- α: Scale parameter

**Notes:**
- Also known as Extreme Value Type I (EV1) distribution
- Two-parameter distribution
- Commonly used for annual maximum series analysis

---

## 2. Normal Distribution (NOR)

**Parameters:** Location (μ = ε), Scale (σ = α)

**Quantile Function:**

```
x(F) = μ + σ × Φ⁻¹(F)
```

where Φ⁻¹(F) is the inverse of the standard normal cumulative distribution function.

**Alternative Notation:**

```
x(F) = ε + α × Φ⁻¹(F)
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε (or μ): Location parameter (mean)
- α (or σ): Scale parameter (standard deviation)

**Notes:**
- Two-parameter distribution
- Symmetric distribution
- Φ⁻¹(F) must be computed numerically (no closed-form expression)

---

## 3. Exponential Distribution (EXP)

**Parameters:** Location (ε), Scale (α)

**Quantile Function:**

```
x(F) = ε - α × ln(1 - F)
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter (threshold)
- α: Scale parameter

**Notes:**
- Two-parameter distribution
- Special case of Generalized Pareto distribution
- Used for modeling inter-arrival times and extreme values

---

## 4. Generalized Extreme Value Distribution (GEV)

**Parameters:** Location (ε), Scale (α), Shape (K)

**Quantile Function:**

```
x(F) = ε + (α/K) × {1 - (-ln F)^K}
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- K: Shape parameter

**Special Cases:**
- When K = 0, GEV reduces to Gumbel distribution
- When K > 0, distribution has a finite upper bound
- When K < 0, distribution has a heavy upper tail

**Notes:**
- Three-parameter distribution
- General form that includes Gumbel, Fréchet, and Weibull distributions
- Widely used in extreme value analysis

---

## 5. Generalized Logistic Distribution (GLO)

**Parameters:** Location (ε), Scale (α), Shape (K)

**Quantile Function:**

```
x(F) = ε + (α/K) × {1 - [(1-F)/F]^K}
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- K: Shape parameter

**Notes:**
- Three-parameter distribution
- Useful for modeling skewed data
- When K = 0, reduces to logistic distribution

---

## 6. Generalized Normal Distribution (GNO)

**Parameters:** Location (ε), Scale (α), Shape (K)

**Quantile Function:**

The quantile function for the Generalized Normal distribution (GNO) cannot be expressed in a simple closed-form equation. It requires numerical methods for evaluation.

**Alternative Representation:**

The GNO distribution is related to the three-parameter lognormal distribution. The quantile function involves the inverse of the standard normal distribution function applied to a transformed variable.

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- K: Shape parameter

**Notes:**
- Three-parameter distribution
- Also known as three-parameter lognormal distribution
- Requires numerical computation for quantile evaluation

---

## 7. Generalized Pareto Distribution (GPA)

**Parameters:** Location (ε), Scale (α), Shape (K)

**Quantile Function:**

```
x(F) = ε + (α/K) × {1 - [1-F]^K}
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- K: Shape parameter

**Notes:**
- Three-parameter distribution
- Used for modeling exceedances over thresholds
- When K = 0, reduces to exponential distribution
- Important in peaks-over-threshold (POT) analysis

---

## 8. Pearson Type III Distribution (PE3)

**Parameters:** Location (ε), Scale (α), Shape (skewness parameter)

**Quantile Function:**

The quantile function for the Pearson Type III distribution (PE3) cannot be expressed in a simple closed-form equation. It requires numerical methods or approximation techniques for evaluation.

**Alternative Approach:**

The PE3 distribution is related to the gamma distribution. The quantile function typically involves:
- Transformation to standard gamma distribution
- Numerical inversion of the incomplete gamma function
- Use of approximation formulas or iterative methods

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- Skewness: Shape parameter (often denoted as γ or skew)

**Notes:**
- Three-parameter distribution
- Also known as three-parameter gamma distribution
- Commonly used in hydrology, especially in the United States
- Requires numerical computation for quantile evaluation

---

## 9. Four-Parameter Kappa Distribution (K4D)

**Parameters:** Location (ε), Scale (α), Shape (k), Shape (h)

**Quantile Function:**

```
x(F) = ε + (α/k) × {1 - [(1-F^h)/h]^k}
```

**Parameter Description:**
- F: Cumulative distribution function (CDF)
- ε: Location parameter
- α: Scale parameter
- k: First shape parameter
- h: Second shape parameter

**Notes:**
- Four-parameter distribution
- Most flexible distribution among those considered
- Can approximate many other distributions
- Provides excellent fit for complex hydrological data
- Requires careful parameter estimation due to increased complexity

---

## Application Notes

### Return Period Calculation

The quantile functions are used to estimate return values for various return periods. The relationship between return period (T) and non-exceedance probability (F) is:

```
F = 1 - (1/T)
```

where:
- T: Return period in years
- F: Non-exceedance probability

### Exceedance Probability

To find the return period for a specific value x, the exceedance probability is calculated as:

```
P(X > x) = 1 - F(x)
```

```
T = 1 / P(X > x) = 1 / [1 - F(x)]
```

### Implementation

In practice, these quantile functions are implemented using:
- **Python**: `lmoments3` library provides `ppf()` method for each distribution
- **R**: `lmom` package provides quantile functions
- **MATLAB**: Statistical Toolbox functions

### Example Usage (Python)

```python
from lmoments3 import distr
import numpy as np

# Fit K4D distribution using L-moments
params = distr.kap.lmom_fit(data)

# Create distribution object
kap_dist = distr.kap(**params)

# Calculate return value for 100-year return period
F = 1 - (1/100)  # Non-exceedance probability
return_value = kap_dist.ppf(F)  # Quantile function
```

---

## References

1. Hosking, J. R. M. (1990). L-moments: Analysis and estimation of distributions using linear combinations of order statistics. *Journal of the Royal Statistical Society: Series B (Methodological)*, *52*(1), 105-124.

2. Hosking, J. R. M., & Wallis, J. R. (1997). *Regional frequency analysis: An approach based on L-moments*. Cambridge University Press.

3. Greenwood, J. A., Landwehr, J. M., Matalas, N. C., & Wallis, J. R. (1979). Probability weighted moments: Definition and relation to parameters of several distributions expressible in inverse form. *Water Resources Research*, *15*(5), 1049-1054.

---

*Note: For distributions without closed-form quantile functions (GNO and PE3), numerical methods such as Newton-Raphson iteration or approximation formulas are typically used in software implementations.*

