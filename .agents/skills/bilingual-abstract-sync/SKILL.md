---
name: bilingual-abstract-sync
description: >-
  Synchronizes, aligns, and validates bilingual abstracts (English and Bahasa Melayu) for Malaysian
  postgraduate theses (e.g. UniSZA standards). Verifies exact parity of quantitative results, statistical notation,
  and standardized technical terminology (Momen-L, Taburan Kappa 4-Parameter, Siri Maksimum Tahunan).
---

# Bilingual Abstract Synchronization Skill

This skill enforces strict quantitative, structural, and terminological parity between the English abstract (`abstract_nos.md`) and the Bahasa Melayu abstract (`abstract_nos_malay.md`).

## Verification Checklist

1. **Numerical & Statistical Consistency**:
   - Ensure all numerical figures match exactly across both versions (e.g., 20 stations, 40% vs 100%, L-skewness ranges $\tau_3 \approx 0.47\text{--}0.55$, overestimation factors, and return period days).

2. **Standard Malaysian Academic Hydrology Terminology**:
   - L-moments $\rightarrow$ Momen-L
   - Annual Maximum Series (AMS) $\rightarrow$ Siri Maksimum Tahunan (AMS)
   - Complete Time-series Analysis (CTA) $\rightarrow$ Analisis Siri Masa Lengkap (CTA)
   - 4-Parameter Kappa distribution $\rightarrow$ Taburan Kappa 4-Parameter
   - Mean Absolute Deviation Index (MADI) $\rightarrow$ Indeks Sisihan Mutlak Min (MADI)
   - Mean Squared Deviation Index (MSDI) $\rightarrow$ Indeks Sisihan Kuasa Dua Min (MSDI)
   - Gringorten plotting positions $\rightarrow$ Kedudukan pemplotan Gringorten
   - Return period $\rightarrow$ Kala ulangan
   - Exceedance probability $\rightarrow$ Kebarangkalian melampaui
   - Overestimation factor $\rightarrow$ Faktor lebihan anggaran

3. **Section Headings & Word Counts**:
   - Ensure corresponding headings match UniSZA guidelines: Introduction / Pengenalan, Methodology / Metodologi, Results / Keputusan, Conclusion / Kesimpulan.
   - Maintain word count limits: **300 – 500 words** (as specified in `Abstract/Abstract Guidelines.jpeg`, Item #6).
