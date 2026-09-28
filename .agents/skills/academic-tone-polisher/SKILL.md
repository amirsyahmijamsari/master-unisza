---
name: academic-tone-polisher
description: >-
  Audits and refines scientific and thesis text for natural, authentic human academic prose. Eliminates
  generic AI idioms, promotional hype words, formulaic sentence openers ("Key findings", "Crucially",
  "Notably", "Delves into"), and hollow fluff. Enforces rigorous statistical conventions, disciplined passive/active
  voice, and precise hydrological terminology.
---

# Human Academic Tone & Anti-AI Scientific Writing Skill

This skill provides an authoritative, comprehensive standard for crafting thesis chapters, journal articles, and abstracts that read like authentic, seasoned academic research rather than machine-generated text.

---

## 1. Supervisor Red Flags & AI "Tell" Words to Eliminate

AI text generators rely on predictable patterns, formulaic signposting, and artificial hype. The following categories of words and phrases are **strictly banned** or must be immediately replaced with natural academic syntax.

### A. The "Dead Giveaways" (Banned Vocabulary)
| AI Hot Word / Phrase | Why It Gets Flagged | Human Academic Replacement |
| :--- | :--- | :--- |
| **"Key findings" / "Key takeaways"** | Overused corporate & AI signpost; sounds like a blog summary | State the empirical result directly: *"Analysis indicates"*, *"The empirical results show"*, *"The data demonstrate"* |
| **"Crucially" / "Importantly" / "Notably"** | Artificial emotional steering; telling the reader what to feel | Delete the adverb. Lead directly with the subject and verb: *"The annual maximum series exhibited..."* |
| **"Delves into" / "Delve"** | Classic LLM cliché rarely used by human hydrologists | *"Examines"*, *"investigates"*, *"analyzes"*, *"evaluates"* |
| **"Testament to" / "Stands as a testament"** | Fluffy rhetoric, non-scientific | *"Evidence of"*, *"demonstrates"*, *"indicates"* |
| **"Pivotal" / "Pivotal role" / "Vital role"** | Empty intensifier; unquantified importance | *"Primary"*, *"governing"*, *"critical"*, or specify the exact mechanism |
| **"Shed light on" / "Illuminates"** | Metaphorical cliché | *"Quantifies"*, *"clarifies"*, *"delineates"*, *"measures"* |
| **"Beacon" / "Cornerstone" / "Tapestry"** | Literary metaphors inappropriate for quantitative engineering | Use literal nouns: *"foundation"*, *"primary assumption"*, *"heterogeneity"* |
| **"Plethora" / "Myriad" / "Multitude"** | Excessive, pompous AI filler | *"Numerous"*, *"multiple"*, *"a wide range of"*, or give exact counts |
| **"Fosters" / "Cultivates"** | Anthropomorphic buzzwords | *"Facilitates"*, *"produces"*, *"generates"*, *"yields"* |
| **"Underscores" / "Highlights" / "Showcases"** | Overused filler transitions | *"Demonstrates"*, *"indicates"*, *"confirms"*, or state the observation directly |
| **"In conclusion" / "To sum up"** | Primary school transition phrase | Begin with synthesis: *"The comparative evaluation confirms that..."* |
| **"It is worth noting that"** | Wordy Throat-clearing | Cut completely and state the proposition directly |
| **"Navigating the complexities"** | Generic AI metaphor | *"Addressing nonlinearities in"*, *"modelling extreme events"* |
| **"A game-changer" / "Revolutionary"** | Sensationalism / marketing speak | Scientific descriptions of performance gains (e.g., *"reduced MADI by 34%"*) |
| **"Holistic" / "Comprehensive" (as fluff)** | Vague boosterism | Detail what is actually included: *"incorporating both annual maxima and daily observations"* |

### B. Malay Language AI Hot Words (Padanan Bahasa Melayu)
| AI Hot Word (BM) | Masalah | Penggantian Akademik Semula Jadi |
| :--- | :--- | :--- |
| **"Penemuan utama"** | Ciri ketara teks terjana AI | Nyatakan dapatan secara terus: *"Hasil analisis menunjukkan bahawa..."* |
| **"Paling penting"** (sebagai pembuka ayat) | Terjemahan harfiah daripada *"Crucially"* | Gugurkan; mulakan terus dengan subjek: *"Pendekatan tradisional AMS menunjukkan..."* |
| **"Meneroka"** (dalam konteks teknikal) | Terjemahan harfiah *"delve into"* | *"Menganalisis"*, *"menyiasat"*, *"menilai"* |
| **"Memainkan peranan penting"** | Klise pengisi | *"Menjadi faktor penentu"*, *"mempengaruhi secara langsung"* |
| **"Menyuluh" / "Membuka tirai"** | Kiasan sastera yang tidak saintifik | *"Menjelaskan"*, *"mengkuantifikasi"*, *"mengenal pasti"* |
| **"Secara holistik"** | Pengisi umum | Terangkan skop sebenar (cth., *"merangkumi kedua-dua siri data harian dan tahunan"*) |

---

## 2. Structural Patterns That Expose AI Writing

Beyond vocabulary, supervisors and reviewers spot AI by its **sentence architecture**. Avoid the following structural traps:

### 1. The Adverbial Sentence Opener
- ❌ **AI Pattern:** *"Crucially, the 4-Parameter Kappa distribution accommodated high skewness."*
- ❌ **AI Pattern:** *"Notably, daily rainfall records exhibited elevated tail behavior."*
- ✅ **Human Academic:** *"The 4-Parameter Kappa distribution accommodated high skewness across all gauge stations."*
- ✅ **Human Academic:** *"Daily rainfall records exhibited elevated tail behavior relative to annual series."*

### 2. Rhetorical Inflation and False Drama
- ❌ **AI Pattern:** *"This groundbreaking methodology serves as a beacon of hope for regional flood risk mitigation in Malaysia."*
- ✅ **Human Academic:** *"These quantile estimates provide parameter inputs for hydraulic structure design in eastern Peninsular Malaysia."*

### 3. The Formulaic "Rule of Three" Parallelism
- ❌ **AI Pattern:** *"Essential for water resource management, hydraulic infrastructure design, and disaster risk reduction."* (Repeated endlessly in every paragraph)
- ✅ **Human Academic:** Vary rhythm and focus specifically on what the current analysis touches: e.g., *"necessary for sizing drainage culverts and retention basins"*.

### 4. Throat-Clearing Openers
- ❌ **AI Pattern:** *"It is important to emphasize that..."*, *"It is interesting to observe that..."*
- ✅ **Human Academic:** Remove the first 5 words completely.

---

## 3. Hydrological & Statistical Scientific Conventions

To ensure the prose reads as authentic technical hydrology:

1. **Named Statistical Frameworks**:
   - Always write out **Annual Maximum Series (AMS)** on first mention; do not use colloquial terms like "annual maxima" or "yearly peaks".
   - Use **Complete Time-series Analysis (CTA)** or **daily precipitation time series** rather than casual descriptions.
2. **Standard Mathematical Notations**:
   - L-moments: Mean ($L_1$ or $\lambda_1$), Scale ($L_2$ or $\lambda_2$), L-skewness ($\tau_3$), L-kurtosis ($\tau_4$), L-CV ($\tau$).
   - In Word / DOCX target files: Use exact Unicode (`λ₁`, `λ₂`, `τ₃`, `τ₄`, `τ`) to avoid uncompiled LaTeX symbols.
3. **Quantitative Precision**:
   - Avoid vague adjectives (*"very large error"*, *"substantially higher"*).
   - Use numbers: *"an overestimation factor of 8.50"*, *"an average difference of 329.5%"*, *"MADI value of 0.0142"*.
4. **Passive vs. Active Voice Balance**:
   - Methodology sections should primarily use **objective passive voice** (*"Datasets were compiled"*, *"Nine candidate distributions were fitted"*).
   - Results and discussion should let the data lead the sentence (*"The 4-Parameter Kappa distribution yielded lower MADI scores..."*). Avoid first-person pronouns (*"we"*, *"I"*, *"our"*).

---

## 4. Pre-Submission Self-Audit Checklist

Before finalizing any text, execute this fast verification:

- [ ] Does any sentence start with *"Crucially"*, *"Notably"*, *"Importantly"*, or *"Interestingly"*? $\rightarrow$ **Delete or rephrase.**
- [ ] Are the words *"key findings"*, *"delve"*, *"testament"*, *"pivotal"*, *"beacon"*, or *"tapestry"* present? $\rightarrow$ **Remove immediately.**
- [ ] Are performance differences quantified with actual values, percentages, or factors rather than hyperbolic praise?
- [ ] Are statistical symbols correctly formatted and readable in the target medium (LaTeX vs. Word Unicode)?
- [ ] Does every paragraph deliver hard factual substance without repetitive motivational summaries?
