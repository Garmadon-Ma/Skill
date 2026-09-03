---
name: ieee-reference
description: Normalize and verify LaTeX/BibTeX bibliographies for IEEE journal and conference submissions. Use when editing IEEE references, checking venue abbreviations, or verifying BibTeX metadata against the target venue style.
---

# IEEE Reference Normalization

Use this skill to audit, normalize, and verify the references of any IEEE journal or conference manuscript. Work from the active `.bib` file through the generated `.bbl` and final PDF. Do not judge correctness from the `.bib` source alone.

## Authority and preference order

Resolve conflicting formats in this order:

1. The user's explicit instruction for the current manuscript.
2. The target IEEE journal or conference template and bibliography style.
3. Recent published papers from the same target venue.
4. The current IEEE Reference Guide and official publication-title abbreviation list.
5. The manuscript's existing convention when the sources above do not decide the issue.

Do not present a personal preference or one sample paper's convention as a universal IEEE rule.

## User's reusable output preferences

Unless the user overrides them for a particular manuscript:

- Preserve every existing BibTeX citation key exactly.
- Remove `doi` and DOI URLs from the output.
- Remove ordinary web URLs, access dates, `biburl`, `bibsource`, `timestamp`, `abstract`, and other import-only metadata when they are not required to identify an online-only source.
- Do not print a publisher, organization, or editor for an ordinary journal article or conference paper. Retain the fields required for books, book chapters, standards, reports, theses, datasets, and proceedings series.
- Prefer concise venue names and avoid duplicating a formal venue name with the same acronym. Apply parenthetical aliases only when the target venue convention requires them.

These are user preferences applied across IEEE manuscripts, not claims that every IEEE publication imposes them.

## Metadata invariants

- Use `--` for page ranges in BibTeX.
- Preserve capitalization that must survive BibTeX by bracing acronyms and proper names, for example `{RF}`, `{OOD}`, `{UAV}`, `{CVAE}`, `{ETF}`, `{5G}`, and `{DroneRF}`.
- Do not manually shorten author lists to `et al.` in the `.bib`; let the bibliography style control author truncation.
- Do not embed punctuation that the `.bst` file generates, such as quotation marks around titles or a trailing period inside a venue field.
- Do not invent or silently alter authors, title, year, volume, issue, pages, article number, venue, or entry type. Verify questionable metadata before changing it.
- Prefer the final published record over an arXiv or early-access record. If only early-access metadata exists, do not invent volume, issue, or pages.

## Required fields by source type

- **Journal article:** authors, article title, standard journal abbreviation, year, and available volume, issue, page range or article number. Month is optional unless required by the target style.
- **Conference paper:** authors, paper title, established proceedings or conference abbreviation, official event location, month, year, and available pages. Include the location and month whenever they can be verified from an official conference or proceedings record, unless the user or target venue explicitly requires their omission.
- **Book:** authors or editors, title, edition when applicable, city, publisher, and year.
- **Book chapter or proceedings chapter:** chapter authors and title, book or proceedings title, editors when required, volume or series when identifying, pages, publisher, and year.
- **Standard, report, thesis, dataset, software, or online-only source:** use its correct entry type and retain the organization, institution, report number, version, repository, or URL needed to identify it. Do not force it into an article or conference template.

## Venue names

Use official IEEE periodical abbreviations for journals. Do not derive abbreviations by guesswork. Examples include `IEEE Trans. Cogn. Commun. Netw.`, `IEEE Wireless Commun. Lett.`, `IEEE Internet Things J.`, and `IEEE Trans. Inf. Forensics Security`.

The supplied IEEE examples use these direct conference forms. Use them when consistent with the target venue:

| Venue | `booktitle` |
|---|---|
| International Conference on Learning Representations | `Proc. ICLR` |
| International Conference on Machine Learning | `Proc. ICML` |
| European Conference on Computer Vision | `Proc. ECCV` |
| Conference on Neural Information Processing Systems | `Proc. NeurIPS` for 2018 onward; use `Proc. NIPS` only for historical records that officially use NIPS |

For other venues, verify the established form first. For example, `Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.` is preferable to an improvised abbreviation. Do not mix a full conference title, an abbreviated title, dates, and the same acronym in one redundant `booktitle`.

## Conference location and month

Use separate BibTeX fields for conference place and month so that the active IEEE bibliography style controls their position and punctuation:

```bibtex
booktitle = {Proc. ICML},
address   = {Sydney, NSW, Australia},
month     = aug,
year      = {2017},
pages     = {2642--2651},
```

- Record the official event location, not the publisher's office, an author's affiliation, or the online publication location.
- Use the compact IEEE place form shown by the official record, such as `Nashville, TN, USA`, `Vancouver, BC, Canada`, `Kigali, Rwanda`, or `Singapore`.
- Use the standard BibTeX month macros `jan` through `dec`; do not place a full date range in `month` unless the target style explicitly requires it.
- For a fully virtual event, use `address = {Virtual Conference}` and retain the verified event month. For a hybrid event, use the physical host location when the official conference record identifies one.
- If the official record gives a month but no location, retain the month and report the unresolved location instead of guessing. Do not infer a location from a planned venue after an event moved online.
- Keep location and month out of `booktitle`. A normalized IEEE result should read in the order `in Proc. [venue], [location], [month] [year], pp. [pages]` when all fields are available.

## Verification sources

Use primary sources in this order when metadata is uncertain:

1. IEEE Xplore or the official publisher landing page.
2. Official conference proceedings or journal website.
3. Crossref or DBLP for structured cross-checking.
4. Google Scholar or other aggregators only for discovery, never as the sole authority when a primary record is available.

Check title, complete author order, venue, year, volume, issue, pages or article number, and publication state. Distinguish the online publication year from the final issue year.

## Workflow

1. Locate every relevant `.tex`, `.bib`, `.bst`, `.bbl`, and PDF. Read the bibliography command in the active manuscript instead of assuming that a similarly named `.bib` file is used.
2. Record the target venue and its style evidence. Identify any explicit user preferences before editing.
3. Audit cited keys, duplicate keys, duplicate publications under different keys, missing required fields, stale early-access metadata, malformed page ranges, unprotected acronyms, inconsistent venue names, and missing conference locations or months.
4. Verify uncertain publication metadata using primary sources. For conference papers, verify the final event location and month as well as the paper metadata. Keep the original citation key while replacing incorrect fields.
5. Edit only the in-scope entries. Preserve unrelated user changes.
6. Regenerate the bibliography explicitly. For BibTeX projects, run BibTeX after the `.bib` edit and then run LaTeX enough times to resolve citations; do not rely on a stale `.bbl` or an incremental build that skipped BibTeX.
7. Inspect the exact changed entries in the new `.bbl`, then inspect the reference pages in the final PDF when available.
8. Report what changed, which items remain uncertain, and the final rendered form of representative entries.

## Verification checklist

- Every `\cite{...}` key still resolves.
- Citation keys are unchanged unless explicitly authorized.
- There are no duplicate BibTeX keys or unintended duplicate publications.
- Authors, titles, years, venues, volumes, issues, pages, and article numbers agree with authoritative records.
- Acronyms and proper names retain their intended capitalization in the `.bbl` and PDF.
- DOI and URL output follows the user's reusable preference or an explicit override.
- Journal and conference names use established abbreviations consistently.
- Every conference reference includes a verified event location and month, or the unresolved field is explicitly reported.
- No duplicate venue information remains.
- The `.bbl` modification time and content confirm that the bibliography was regenerated after the `.bib` edit.
- Compilation completes without undefined citations, missing bibliography entries, BibTeX errors, or relevant metadata warnings.

