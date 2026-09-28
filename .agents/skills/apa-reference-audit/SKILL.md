---
name: apa-reference-audit
description: >-
  Audits, cross-references, and validates in-text citations against references/references.md
  according to APA 7th edition guidelines. Use when checking citation consistency, adding new citations,
  or resolving bibliographic discrepancies in thesis chapters.
---

# APA Reference Audit Skill

This skill provides a systematic procedure for cross-checking and validating citations across all thesis chapters against the master reference library in `references/references.md`.

## Workflow & Verification Steps

1. **In-Text Citation Extraction**:
   - Scan target chapter markdown file for parenthetical `(Author, Year)` and narrative `Author (Year)` citations.
   - Extract multi-author citations (`et al.`) and verify proper APA 7th rules (3+ authors use `et al.` on first mention).

2. **Master Reference Cross-Check**:
   - Read `references/references.md`.
   - Verify that every in-text citation exists in the master reference list.
   - Flag any orphaned citations (in-text citations missing from `references.md`) or unreferenced entries.

3. **Format & DOI Verification**:
   - Check hanging indents, journal italicization, sentence case for article titles, and title case for journal names.
   - Verify DOIs are formatted as `https://doi.org/10.xxxx/...`.
   - If a new reference must be added, place it under the appropriate topic category header in `references/references.md`.
