# Plain Professional Academic Writing Rules (Anti-AI Style Guide)

This rule strictly enforces clear, concise, and professional human language in all thesis writing, eliminating overused AI vocabulary, pompous phrasing, and unnecessary adverbial hedging.

---

## 1. Core Principle: Clear Human Words Over AI Jargon
* **Directness over Complexity**: Use simple, precise, professional English (and Bahasa Melayu). Do not inflate simple concepts with heavy, robotic synonyms.
* **Eliminate Unnecessary Adverbs & Hedging**: AI models overuse adverbs ending in *-ly* to sound "profound." Human researchers state facts directly.
* **Legitimate Statistical Terms**: Words that are defined statistical properties—such as **"robust"** (referring to L-moments' mathematical robustness against outliers and heavy tails)—are scientifically accurate, legitimate, and encouraged in this thesis.
* **STRICT BAN ON EM-DASHES & PARENTHETICAL DASHES**:
  - NEVER use em-dashes (`—`) or spaced hyphens (` - `) as sentence breaks or parenthetical clauses (e.g., avoid *"method across nine candidate distributions—comparing traditional AMS..."*). This is an informal and overused AI habit.
  - Use proper academic connectors instead (e.g., *"by comparing"*, *"which compares"*), commas, or split the thought into two clear sentences.
  - *(Note: Standard technical hyphens in compound terms like "4-Parameter", "L-moments", "time-series", and en-dashes in numerical ranges like "2–100 years" remain valid).*

---

## 2. Forbidden & Discouraged AI Vocabulary Table

| Overused AI / Stilted Word | Why Avoid | Preferred Human Academic Word |
| :--- | :--- | :--- |
| **predominantly** | Heavy, robotic adverb | **primarily**, **largely**, **mainly**, or delete and state directly (*"relies on"*) |
| **substantially** | Overused intensifier | **notably**, quantify with numbers (*"by 8.50-fold"*), or delete |
| **significantly** *(non-statistical)* | Confuses statistical significance ($p < 0.05$) with general magnitude | **markedly**, **clearly**, or state exact difference |
| **crucially / notably / importantly** | Artificial emotional steering | Delete adverb; start directly with the subject |
| **delve / delves into** | Dead-giveaway LLM cliché | **examines**, **analyzes**, **investigates**, **evaluates** |
| **pivotal / vital role** | Generic empty booster | **primary**, **governing**, **key factor**, or specify the role |
| **testament to** | Pompous rhetoric | **evidence of**, **demonstrates**, **shows** |
| **plethora / myriad** | Artificial sophistication | **numerous**, **multiple**, **wide range of**, or state count |
| **beacon / cornerstone / tapestry** | Inappropriate literary metaphors | **foundation**, **basis**, **core element** |
| **fosters / cultivates** | Anthropomorphic buzzwords | **produces**, **generates**, **facilitates**, **yields** |
| **sheds light on / illuminates** | Literary cliché | **clarifies**, **quantifies**, **explains** |
| **sampling decimation** | Stilted, dramatic phrasing | **data omission**, **annual sampling reduction**, **data loss** |
| **is significantly enhanced by** | Passive boosterism | **improves with**, **is strengthened by** |

---

## 3. Bahasa Melayu Equivalents (Panduan Bahasa Melayu)

| Frasa AI / Berbunga | Mengapa Perlu Dielak | Frasa Akademik Manusia Semula Jadi |
| :--- | :--- | :--- |
| **sebahagian besarnya bergantung** | Terlalu berbelit / terjemahan *predominantly* | **bergantung kepada**, **berasaskan** |
| **penemuan utama** | Terjemahan harfiah *key findings* | Nyatakan terus dapatan: *"Hasil kajian menunjukkan..."* |
| **paling penting** (pembuka ayat) | Terjemahan harfiah *crucially* | Gugurkan perkataan pengisi; mulakan terus dengan subjek |
| **secara ketara / secara signifikan** | Pengisi hiperbola | Nyatakan angka atau bukti konkrit |
| **meneroka** (kajian teknikal) | Terjemahan *delve into* | **menganalisis**, **menilai**, **mengkaji** |
| **memainkan peranan penting** | Klise pengisi | **menjadi faktor penentu**, **mempengaruhi secara langsung** |

---

## 4. Sentence Construction Checklist
- [ ] Has every sentence with *"predominantly"*, *"substantially"*, or *"crucially"* been replaced or simplified?
- [ ] Does the sentence start directly with the subject rather than an introductory filler adverb?
- [ ] Are claims supported with concrete numbers rather than intensifiers?

---

## 5. Mathematical & Variable Typography (No Programming Underscores or Pseudo-Code)
* **Zero Tolerance for `snake_case` & Code Shorthand in Thesis Text**:
  - NEVER use computational script variables, raw underscores, or shorthand symbols (e.g., `RP_AM`, `RP_daily`, `OE_factor`, `OE%`, `OE%(M)`, `rp_am`, `madi_gev`) in thesis prose, equations, table headings, or figure captions. Underscores and `%` as variable names belong solely to scripts and spreadsheets.
* **Standard Hydrological Notation**:
  - Return periods / recurrence intervals must use the standard symbol $T$: $T_{\text{AM}}$ for Annual Maximum Series and $T_{\text{daily}}$ for complete daily series.
  - Overestimation metrics follow formal hydrological ratio and percentage excess notation:
    - Recurrence Ratio / Overestimation Factor: $R_T(M) = \frac{T_{\text{AM}}(M)}{T_{\text{daily}}(M) / 365.25}$
    - Relative Percentage Excess: $\Delta_T(M) = [R_T(M) - 1] \times 100\%$
  - Word subscripts must be upright roman: $F_{\text{wet}}(x)$, $T_{\text{daily}}$, $T_{\text{AM}}$ (never $F_{wet}$ or `F_wet`).
  - In flowchart boxes and overview diagrams, state stages conceptually without cramming horizontal equations into body text.
