# UniSZA MSc Thesis Formatting Guidelines
**Faculty of Informatics and Computing (FIK) / Centre for Graduate Studies (Pusat Pengajian Siswazah)**  
**Universiti Sultan Zainal Abidin (UniSZA), Terengganu, Malaysia**

---

## 1. Document Page Setup & Margins

| Specification | Dimension / Setting | Notes |
| :--- | :--- | :--- |
| **Paper Size** | **A4** (210 mm × 297 mm) | Standard 80 gsm white paper |
| **Left Margin** | **4.0 cm** (or 3.8 cm / 1.5 in) | Binding margin allowance |
| **Right Margin** | **2.5 cm** (1.0 in) | |
| **Top Margin** | **2.5 cm** (1.0 in) | 3.0 cm for first page of chapters |
| **Bottom Margin** | **2.5 cm** (1.0 in) | |
| **Header / Footer** | **1.5 cm** from edge | For page numbers |

---

## 2. Typography & Font Specifications

| Document Element | Font Type | Size | Style / Case | Alignment |
| :--- | :--- | :---: | :--- | :--- |
| **Main Body Text** | **Times New Roman** | **12 pt** | Regular | **Justified** |
| **Chapter Titles** (e.g. `CHAPTER 1`) | **Times New Roman** | **14 pt** | **Bold**, ALL CAPS | **Centered** |
| **Chapter Name** (e.g. `INTRODUCTION`) | **Times New Roman** | **14 pt** | **Bold**, ALL CAPS | **Centered** |
| **Heading Level 1** (e.g. `1.1 INTRODUCTION`) | **Times New Roman** | **12 pt** | **Bold**, ALL CAPS | Left-aligned |
| **Heading Level 2** (e.g. `1.1.1 Problem Statement`) | **Times New Roman** | **12 pt** | **Bold**, Title Case | Left-aligned |
| **Heading Level 3** (e.g. `1.1.1.1 Climate Regime`) | **Times New Roman** | **12 pt** | **Bold / Italic**, Title Case | Left-aligned |
| **Table & Figure Captions** | **Times New Roman** | **10 pt** | Bold label, Regular text | Above tables, Below figures |
| **Table Contents & Data** | **Times New Roman** | **10 pt** | Regular | Left / Center / Right |
| **Footnotes** | **Times New Roman** | **10 pt** | Regular | Left-aligned |
| **Block Quotations (>4 lines)** | **Times New Roman** | **12 pt** | Regular, Single-spaced | Indented 1.27 cm (0.5 in) |
| **Hard Cover & Spine** | **Times New Roman** | **18 pt** | **Bold**, ALL CAPS | Centered, Gold stamped |

*(Note: For Arabic text, **Traditional Arabic** 16 pt is used).*

---

## 3. Spacing Guidelines

* **Main Body Paragraphs:** **2.0 (Double Spacing)**.
* **Paragraph Indentation:** First line indented by **1.27 cm (0.5 inch)** or 1 standard Tab.
* **Single Line Spacing (1.0 or 1.15):**
  * Abstract & Abstrak (to fit cleanly on a single page).
  * Table of Contents, List of Figures, List of Tables.
  * Captions and contents of tables.
  * Direct block quotations (>4 lines).
  * Bibliographic entries in the References chapter (double space between separate entries).

---

## 4. Abstract Formatting Checklist (UniSZA Standard)

Referenced directly from the UniSZA Abstract Review Checklist (`Abstract/Abstract Guidelines.jpeg`):

1. **Title Length:** Maximum **15 words** (excluding connecting words). Proper nouns count as one word (e.g., *Universiti Sultan Zainal Abidin*).
2. **Word Count:** Strictly between **300 – 500 words** per abstract.
3. **Structured Headings:** Must include four bolded sections:
   * **Introduction** (*Pengenalan*): Background, problem statement, objectives.
   * **Methodology** (*Metodologi*): Data, sampling, analytical framework (L-moments), candidate distributions, GOF evaluation.
   * **Results** (*Keputusan*): Best-fitting distribution (4-Parameter Kappa), empirical findings, overestimation factor (8.50 at 99th percentile, 43-day recurrence).
   * **Conclusion** (*Kesimpulan*): Technical recommendations, implications for flood mitigation and hydraulic design.
4. **Bilingual Parity:** English abstract followed by Malay abstract (*Abstrak*) on a separate page. Numerical figures and technical terms must match 1:1.
5. **No Em-Dashes:** Do not use `—` or ` - ` as sentence connectors.

---

## 5. Pagination & Page Numbering

1. **Preliminary Pages (Roman numerals):**
   * Includes: Title Page, Declaration, Dedication, Abstract, Abstrak, Acknowledgements, Table of Contents, List of Tables, List of Figures, List of Abbreviations.
   * Numbered in lowercase Roman numerals: `i`, `ii`, `iii`, `iv`...
   * Position: **Bottom center**, 1.5 cm from the bottom edge.
   * *Note: The Title Page counts as page `i` but the number is unprinted.*

2. **Main Thesis Chapters & Back Matter (Arabic numerals):**
   * Starts from **Chapter 1 (page 1)** through References and Appendices.
   * Numbered consecutively: `1`, `2`, `3`...
   * Position: **Top right corner**, 1.5 cm from the top edge and 2.5 cm from the right edge.
   * *(On chapter opening pages, the page number is typically centered at the bottom or omitted according to faculty practice).*

---

## 6. Mathematical & Statistical Notations

For thesis drafts and Word `.docx` documents:
* **L-moments:** $\lambda_1, \lambda_2$ (render as Unicode **λ₁, λ₂** in Word).
* **L-moment ratios:** L-skewness $\tau_3$ (**τ₃**), L-kurtosis $\tau_4$ (**τ₄**).
* **Mathematical ranges:** Use standard en-dashes without spaces (e.g., `2–100 years`, `0.47–0.55`).
* **Equations:** Centered with sequential numbering right-aligned in parentheses:
  $$T = \frac{1}{1 - F(x)} \tag{3.1}$$

---

## 7. Citation & Referencing Standard

* **Style:** **APA 7th Edition** throughout.
* **In-Text:** Single author: `Hosking (1990)` or `(Hosking, 1990)`; Two authors: `Hosking and Wallis (1997)` or `(Hosking & Wallis, 1997)`; 3+ authors: `Greenwood et al. (1979)`.
* **Central File:** All references must be indexed in `references/references.md`.

---

## 8. Writing Style & Anti-AI Language Rules

Full rules are detailed in `.agents/rules/plain-academic-language.md` and `AGENTS.md`:
* **No Em-Dashes (`—`)**: Use standard academic conjunctions (*"by"*, *"which"*, *"while"*), commas, or separate sentences.
* **No AI Hot Words**: Strictly avoid *"predominantly"*, *"substantially"*, *"crucially"*, *"notably"*, *"delves into"*, *"pivotal role"*, *"testament to"*, *"plethora"*, *"beacon"*, *"tapestry"*.
* **Plain Professional Vocabulary**: Use simple, direct human academic words. Let data and empirical metrics lead the sentences.
* **Legitimate Statistical Terms**: **"Robust"** is a mathematically valid and encouraged term when describing L-moments' resistance to outliers.
