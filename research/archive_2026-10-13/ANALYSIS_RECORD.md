# Liberty Data Drive 2026 — Complete Analysis and Work Record

Last updated: 13 October 2026, Asia/Kathmandu.

**Submission format:** individual / solo. The user confirmed there is no team. The participant's name and desired submission label have not been supplied. A team contribution statement is therefore not required under the supplied guidelines; AI disclosure remains required.

**Status:** exploratory analysis exists and has been reproduced locally. Reform dating, dataset compliance, final inference, Nepal policy research, declaration approval, and the final deck remain unfinished. The six current charts are provisional.

**Purpose:** explain the entire recorded analytical process, from topic exploration to final submission planning, and preserve the distinction between calculations, documentary evidence, assumptions, and pending decisions. This is the master narrative record; `analysis.ipynb` remains the working file for calculations.

**Instruction update:** the user revoked the previously supplied AGENTS.md instructions. That file was read during the earlier audit but is no longer an active instruction source. Competition requirements below come from the participant guidelines. The earlier readiness report is a historical audit and predates this update and the confirmation of solo participation.

## Contents

1. Objective and competition requirements
2. What we inherited and what we did in this conversation
3. Topic exploration and choice
4. Research question and status
5. Original data and variable definitions
6. Loading, cleaning, and matching countries
7. Country selection
8. Reform dates and evidence
9. Event-time construction
10. Outcome calculations and benchmark
11. Provisional results and contrary evidence
12. Robustness checks
13. Figures and traceability
14. Nepal recommendation and liberty reasoning
15. Reproducibility, source audit, and runtime
16. Remaining work and submission plan
17. Source and AI records
18. Technical appendices with exact saved outputs and notebook code

## 1. Objective and competition requirements

Study a policy or institutional change that already happened in at least three countries. Use Fraser's Economic Freedom of the World (EFW) for the policy side and UNDP human-development components for the outcome side. Compare before and after actual reforms, align countries around reform years, retain contrary cases, and recommend exactly one concrete change for one South Asian country.

The guidelines are in `Instructions/Liberty Data Drive 2026.docx`; the accompanying `.docx.txt` contains all text nodes from the DOCX, as checked in the audit. The original document is the reference when interpretation is uncertain.

Required deliverables:

- PDF deck with at most ten content slides.
- Working file generating every chart, accessible to a judge.
- Chart index linking figure numbers to notebook cells or equivalent locations.
- Source list including publisher, title, version/year, public URL, and access date.
- AI disclosure; contribution statement only for teams.
- Approved dataset declaration; no approval evidence has been found in the workspace.

The guidelines specify the chain-linked EFW panel sheet and UNDP's all-composite-indices-and-components time series. They favour specific policy subcomponents and outcome components. Main analysis must not become overall economic freedom versus HDI.

The declaration must explain the research question, datasets/variables, and policy change. Scope queries go through that process. Dates in the document are relative: declaration in October's second week, feedback in the third, final submission at the challenge's end. The exact submission deadline remains unknown.

Scoring: research question 15%, data/reproducibility 20%, chart craft/integrity 15%, interpretation 15%, recommendation 20%, liberty reasoning 15%. A chart that cannot be reproduced scores zero; an inaccessible working file is treated as not submitted.

## 2. What we inherited and what we did

### Inherited work

At the start of the audit, the workspace already contained original datasets, instructions, a 32-cell notebook, six PNG charts, a chart index, scripts that generate/execute the notebook, policy notes, a reform-date CSV, and a large source archive. These were not all created during the present conversation.

The inherited policy notes describe tariff cuts and Nepal as previously confirmed. We can report what those notes say, but cannot reconstruct unrecorded discussions or claim an independently verified chronology for when every decision was made.

### Completed during this conversation

1. Inventoried the workspace and read the project documents, notebook, research scripts, reform table, and chart index.
2. Checked the guideline text against the DOCX.
3. Inspected workbook sheets, tariff columns, year coverage, missingness summaries, country codes, duplicates, and UNDP components.
4. Verified that working raw files exactly match the workspace originals by SHA-256.
5. Reproduced the tariff selection and checked country-code overlap.
6. Reviewed all six charts visually.
7. Classified/extracted the 418 archived source files; recorded unusable downloads.
8. Reran the existing notebook successfully in an isolated fresh local Jupyter kernel, preserving project outputs.
9. Created `research/readiness_report.md` and supporting audit files.
10. Located the renamed workspace: `LibREADtarian Challenge` became `LibREADtarian-Challenge`.
11. Recorded the user's confirmation of solo participation and revocation of earlier AGENTS.md instructions.
12. Continued source research: found and opened WTO and USTR accounts supporting Thailand's 1995 tariff programme; identified additional Mauritius reform leads.
13. Created this consolidated record from the project files and saved audit outputs.

Not completed: a final notebook rebuild, a final reform-date ledger, a submitted declaration, a researched current Nepal recommendation, publication, organiser contact, or a final presentation. No external messages or submissions have been sent.

## 3. Topic exploration and choice

The README proposes trade liberalisation, property rights, regulation, and sound money as starting directions. The notebook actually scans available EFW indicators for improvements of at least two rating points between 1995 and 2005. Candidate indicators include mean tariff ratings, tariffs, regulatory trade barriers, black-market exchange rates, property rights, contracts, business permits, and broad trade/legal areas when data exist.

The exploratory scan and final tariff screen are different rules. The two-point rule searches for possible topics; the twenty-percentage-point tariff rule selects cases for this topic. Neither threshold is a statistically estimated optimum.

Reasons tariff reduction is a plausible topic:

- A concrete intervention with a understandable mechanism: imported inputs and goods can become cheaper, competition can increase, and firms/consumers can gain choices.
- Multiple country cases appear under a checkable policy-data rule.
- Budgets, executive orders, and WTO reviews provide documentary leads.
- GNI per capita is measured in the required UNDP file.
- Nepal provides a relevant South Asian policy context.

These are reasons to investigate, not evidence that tariffs necessarily determine income. Tariff reforms often accompany stabilisation and wider reforms; changes in measurement or weighting may affect the recorded raw mean. Legal institutions are harder to date, business-regulation history is incomplete, and sound-money reforms often occur during crises. No formal scored topic-ranking exercise is present in the files; we should not claim one was done.

## 4. Research question and status

Working question, subject to verified dates and organiser scope approval:

> Among Bangladesh, Pakistan, India, China, Mauritius, Thailand, the Philippines, Kenya, Côte d'Ivoire, and Senegal, whose EFW-recorded mean tariff rates fell by at least 20 percentage points between 1995 and 2005, were documented tariff-reduction programmes followed by higher GNI per capita over the next ten years, and what does the pattern suggest for modification of Nepal's tariff schedule?

This names the screened countries and screening period. The final first-slide question must also state the calendar range of the verified reforms and resulting outcome windows. That range is not yet settled. Countries without defensible dates must be transparently identified rather than silently assigned a year.

Three separate questions must remain distinct:

- Did income rise after the reform year?
- Was annual growth faster than before that year?
- Was annual growth faster than a broad comparator over the same calendar years?

The current notebook addresses all three descriptively, with incomplete before-period evidence for some cases. It does not identify a causal effect.

## 5. Original data and variable definitions

### Fraser EFW

`data/EFW_original.xlsx` is byte-identical to `economic freedom.xlsx`. It contains `EFW Ratings`, `EFW Panel Dataset`, and `EFW Ratings 1950-1965`.

The Ratings sheet has 5,115 country-year records, 87 columns, and 165 jurisdiction codes, covering 1970–2024. Observations are five-yearly through 1995 and annual from 2000. There are no duplicate ISO/year keys in the audit.

The notebook reads Ratings with `header=3`, strips header whitespace, retains rows with numeric years, and converts year to integer.

Policy variables:

| Variable | Current location | Unit and role |
|---|---|---|
| Mean tariff rating | `4Aii  Mean tariff rate` | Rating, 0–10; higher generally indicates lower barriers |
| Raw mean tariff | Adjacent column, `data.10` | Percentage; current selection and policy charts |
| Tariff dispersion rating | `4Aiii  Standard deviation of tariff rates` | Rating; not used in current six-chart notebook |
| Raw tariff dispersion | Adjacent column, `data.11` | Tariff-rate dispersion; proposed builder extension |
| Chain-linked Area 4 | Panel sheet's `Area 4: Freedom to Trade Internationally` | Broader trade-policy area; required-sheet candidate context |

The raw rate is used in the current topic because high tariffs can be obscured by the zero floor of the rating. The policy notes describe that floor as around 50%; confirm the applicable Fraser methodology before stating the precise formula in the final submission.

**Unresolved requirement:** the supplied chain-linked panel sheet contains the overall index and five areas, not tariff subcomponents. The notebook uses Ratings only. We must explain this to organisers through the dataset declaration and resolve whether a panel-area series plus raw tariff evidence satisfies the requirement. Raw rates must not be relabelled chain-linked.

The local workbook reaches 2024; the guidelines' citation example names the 2025 annual report. The exact release/provenance has not been established. Preserve the provided workbook and verify its identity rather than automatically replacing it with the latest download.

### UNDP

`data/UNDP_original.csv` matches the original `HDR25_Composite_indices_complete_time_series.csv` by hash. The original folder name contains two newline characters; use the clean working path for execution.

The file has 206 rows and 1,112 columns. Of these, 195 have three-letter country/territory identifiers; 11 are regional/development-group aggregates. All are currently melted into the exploratory long table, but the case/benchmark filters use EFW identifiers. Do not call 206 the number of countries.

| Prefix | Measure | Analysis role |
|---|---|---|
| `gnipc_YYYY` | GNI per capita, labelled 2021 PPP dollars in the notebook | Primary outcome |
| `le_YYYY` | Life expectancy at birth, years | Secondary descriptive outcome |
| `eys_YYYY` | Expected years of schooling | Loaded, not a final chart in current notebook |
| `mys_YYYY` | Mean years of schooling | Loaded, not a final chart in current notebook |

All four series have year columns from 1990 to 2023. Country-only nonmissing counts and raw-file hashes are recorded in Appendix A. Missing values remain missing. Unit/metadata documentation should be retained with the final package.

Supplementary workbooks contain HDI levels/trends, IHDI, GDI, GII, PHDI, combined annex tables, and 2025 MPI. They were inspected at sheet level, not used as the primary longitudinal outcome dataset.

## 6. Loading, cleaning, and matching

UNDP is read using `encoding='latin1'`. For each outcome prefix, the notebook selects year-suffixed columns, melts from wide to long, extracts integer year, and combines outcomes on `(iso3, country, year)`. The resulting table includes 7,004 rows: 206 identifiers × 34 years.

EFW supplies `ISO_Code`; UNDP supplies `iso3`. ISO codes, rather than display names, link the files. EFW country names are used for plot labels.

Audit results: 164 shared identifiers; `TWN` is EFW-only. Afghanistan and Maldives are in UNDP but absent from the supplied EFW jurisdictions. Bangladesh, Bhutan, India, Nepal, Pakistan, and Sri Lanka appear in both.

The raw inputs were not overwritten. In-memory coercion of strings to numeric can produce missing values and needs reporting if unexpected. The current code uses `pivot_table`, which can silently aggregate duplicate keys; although source keys passed the audit, final code should explicitly assert uniqueness and validate merges. A successful merge returning rows is insufficient proof of correctness.

## 7. Country selection

Let `tariff(c,y)` be the raw mean tariff rate for country c and year y:

```text
change_pp(c) = tariff(c, 2005) - tariff(c, 1995)
selected(c) = change_pp(c) <= -20
```

Both tariff endpoints must exist. Current code also requires some GNI availability through `has_gni`; this is weaker than complete outcome coverage for every eventual reform window. Final eligibility must check the actual outcome endpoints separately.

The rule yields ten cases among 98 eligible countries. Exact saved selection output appears in Appendix B; values there were inserted from executed notebook outputs, not retyped.

The near-threshold countries are listed in the notebook. Listing them is not a completed sensitivity analysis. Before expanding the sample, apply the same reform-sourcing requirements to them.

Nepal does not meet this large-cut rule and is the recommendation target/context, not an additional reform case.

Important caveats: the 1995–2005 rule selects realised policy changes, not randomly assigned reforms. Several candidate programmes began before the screen starts. Explain the relationship between programme onset and continuing reductions. The notes assert rule-before-outcomes selection, but this audit found no independent timestamped proof of that ordering. We can preserve the rule prospectively without inventing an earlier preregistration.

## 8. Reform dates and evidence

Policy dates come from documentary evidence, not the year a plotted score appears to jump. Dating choices affect event alignment, before-history, post windows, and benchmark years.

There are currently conflicting records:

- Notebook cell 16 embeds ten dates; two are labelled verified and eight unverified.
- `research/reform_dates.csv` labels eight verified and excludes Mauritius/Thailand.
- `research/policy_notes.md` remains an earlier draft with undated leads.
- `research/nb_part2.py` would import the newer CSV when rebuilding, thereby changing analysis and figures.

The comparison and source ledger are reproduced in Appendix C. A VERIFIED text label does not itself establish legal commencement.

### Evidence assessment

- India: budget speech supports the tariff peak-cut announcement in 1991; check legal commencement and exceptions.
- China: open institutional chapter documents 1992 cuts; preserve exact source location and distinguish that programme from WTO accession in 2001.
- Bangladesh/Kenya: the newer CSV uses baseline years in retrospective reviews. These do not automatically establish when a specific reform took effect.
- Pakistan: SPDC/WTO evidence is year-level; identify the relevant budget or notification and commencement where possible.
- Philippines: executive orders provide a specific 1995 programme and an effective-date recital; preserve both sources and scope.
- Côte d'Ivoire/Senegal: transition and completion dates differ; a Togo review documents a regional programme, but country implementation should be confirmed. The two countries share a policy event.
- Mauritius: a dated comparable programme remains unresolved; the original 1999 assignment is not established.

### Thailand update from continued research

The [WTO 1995 Thailand review](https://www.wto.org/english/tratop_e/tpr_e/tp021_e.htm), in its press-release tariff paragraph and Secretariat section “Recent evolution,” explicitly identifies measures initiated in January 1995. The [USTR 1996 report](https://ustr.gov/archive/Document_Library/Reports_Publications/1996/1996_National_Trade_Estimate/1996_National_Trade_Estimate-Thail.html), under “Import Policies,” corroborates a phased restructuring completed by January 1997. Both pages were opened and read on 13 October 2026.

This supports 1995 as the onset of this particular programme, while earlier liberalisation also existed. It corrects the rationale that no dated open source was available. Thailand should not be excluded on that rationale. Record this correction in the authoritative ledger when synchronising files; the ledger and charts have not yet been changed.

### Mauritius update: research leads, not a final date

Searches located an official 2005–06 budget speech, a government trade-policy account describing the 2005/2006 changes, and an IMF 1999 report discussing a 1994 consolidation. These may describe different reform stages. The budget PDF could not be fully fetched by the web reader; no final date has been assigned from a search snippet. Open and read the relevant documents, locate commencement provisions, and select a comparable programme under the same dating standard.

## 9. Event-time dataset

For each country:

```text
event_time = calendar_year - reform_year
```

The current window is −5 through +10, inclusive. Event year zero is the chosen reform year, not necessarily the first full twelve months of implementation. Annual/fiscal and late-year reforms need consistent treatment.

Country-year rows retain country, ISO, calendar year, reform year, event time, tariff, GNI, life expectancy, and schooling measures. Annual UNDP rows are left-joined to observed EFW tariffs; missing EFW years stay blank. There is no explicit interpolation. Connecting observed points on a line should not be described as annual measurement where none exists.

The current dataset has 151 country-year rows. Exact country coverage is in Appendix D. India begins at event −1, China at −2, Kenya at −3 under the notebook's current dates; others reach −5. Date changes will change this coverage.

## 10. Outcome calculations and comparator

### Income index

```text
GNI_index(c,t) = 100 * GNI(c,t) / GNI(c,reform_year)
```

This compares proportional trajectories across countries with different income levels. Every country equals 100 at event zero by construction; that meeting point is not substantive evidence of reform effectiveness.

At each event year, the notebook plots the median index only if at least five nonmissing countries exist. Countries are equally weighted. Before reform, the contributing countries change with coverage. Show counts and test a balanced subset before interpreting changes in the median slope.

### Growth

```text
CAGR_percent(y0,y1) = 100 * ((GNI(y1)/GNI(y0)) ** (1/(y1-y0)) - 1)
```

Endpoints must exist and be positive. Current before-period start is `max(1990, reform_year-5)`; before-growth is reported only with at least three elapsed years. Post-growth spans reform year to reform year +10. Missing pre-growth is NaN, not zero. CAGR is a compound annualised endpoint change, not an arithmetic average of annual growth rates.

The three-year prehistory rule is an analytical choice requiring explanation, not a competition requirement. Figure labels should state actual elapsed years rather than describing all pre-bars as five years.

### Benchmark

The benchmark pool is the EFW/UNDP GNI countries minus all ten rule-selected cases. For each case's calendar window, calculate each pool country's valid CAGR and take the unweighted median:

```text
benchmark(c) = median(valid non-case CAGR over c's post-window)
excess_pp(c) = post_CAGR_percent(c) - benchmark_percent(c)
```

The current pool has 154 identifiers; the valid endpoint count can vary by window and must be reported. Benchmark countries may themselves reform, and differ in income, geography, institutions, shocks, and prior growth. This is contextual comparison, not a matched control, difference-in-differences estimate, or causal counterfactual.

### Life expectancy

```text
life_expectancy_gain(c,t) = LE(c,t) - LE(c,reform_year)
```

This is a difference in years, not a percentage. It is secondary description; a tariff-to-health causal interpretation needs separate support and consideration of health shocks.

## 11. Provisional results and contrary evidence

Exact reproduced country results and summary outputs are in Appendix E. They use the old embedded dates, including eight unverified ones. They must not be presented as final findings from the newer date table.

Five cases outperform the comparator and five do not. Pakistan, Thailand, Senegal, Kenya, and Côte d'Ivoire are contrary cases on that measure. Median country-level excess is about +0.06 percentage points per year, a modest descriptive difference.

Median post-CAGR and median benchmark-CAGR are calculated separately. Their difference is generally not equal to the median of within-country excess differences; do not substitute one statistic for the other.

Even a positive post-CAGR does not establish acceleration or causation. India and China lack sufficient before-years for the current pre-growth rule. Large gains in one country do not justify hiding weak or negative cases.

Use “was followed by,” “coincided with,” and “is consistent with.” Investigate country-specific alternatives such as broader reforms, macroeconomic recovery, the Asian crisis, conflict, commodity exposure, health shocks, and remittances. These are leads until sourced; a plausible alternative must not be presented as a verified explanation solely because it sounds reasonable.

## 12. Robustness checks

Completed in the current executed notebook: removing both Côte d'Ivoire and Senegal from the summary. This gives five of eight above benchmark and median excess around +0.91 percentage points. This is a sensitivity result, not an alternative preferred sample. The full sample remains visible.

Present in builder code but not incorporated into the current saved notebook: excluding China, shifting all reform years by −2/−1/0/+1/+2, and a five-year post-window. These proposed checks have not been validated as final outputs.

Still needed:

- Date uncertainty checks appropriate to documentary ambiguity, including programme onset versus completion.
- Usable endpoint counts in every result. A shift before 1990 may yield NaN and must not count as a failure to beat the benchmark.
- Retaining one shared-WAEMU case or summarising by distinct reform event as well as dropping both.
- A balanced event-time subset and transparent preperiod lengths.
- Reasonable selection thresholds/windows, sourcing any newly eligible cases consistently.
- Indicator-definition checks for unusual historical raw tariff rates.

No regression or advanced causal model is implemented in the recorded analysis. Add complexity only if it answers a necessary question and its assumptions can be defended.

## 13. Figures and traceability

The current chart index is reproduced in Appendix F. Its cell numbers refer to positions counting both markdown and code cells, not Jupyter execution counts. Slide numbers are proposed placements; no final deck exists.

Six current figures: raw tariff trajectories; reform-aligned income index; before/post/benchmark growth; excess growth and contrary cases; life expectancy gains; Nepal versus four South Asian peers with separate tariff/income panels.

All six were visually inspected. Signed bars originate at zero; negative growth bars may extend below it. No dual axes or pies were found. Line panels have units and source notes. Improvements needed: prominent provisional-date warnings, correct preperiod labels, valid sample counts, calendar coverage on event charts, and readable notes at slide size. Figure 6 labels dataset tariff coverage beginning 1970 while plotted observations begin later.

The builder proposes eight figures and changes the identities of Figures 5/6 while adding dispersion evidence. Rebuilding would invalidate the current six-figure mapping unless images, notebook, index, and deck are updated together.

Do not manually retype plot values into a design tool. Restyling an exported chart is permitted by the guidelines, but its numerical content must trace to the notebook. This record quotes saved outputs for documentation; it is not a substitute chart-generation file.

## 14. Nepal recommendation and liberty reasoning

Nepal is the intended target in existing notes. No exact policy modification has been chosen or researched sufficiently. Mean-tariff reductions in historical countries do not automatically justify tariff-dispersion reform in Nepal, nor does lower income by itself identify the right intervention.

Before recommending, establish the current named law/schedule/rule, provisions to change, authority empowered to change them, implementation scope, and likely revenue/adjustment costs through open current sources. Then write exactly one Addition, Removal, or Modification, linking its mechanism to numbered project figures.

Potential mechanism to assess: lower tariff costs on selected goods/inputs change purchase and production choices, with possible effects on competition, productivity, prices, and real incomes. Our current aggregate data do not measure all those intermediate steps.

Liberty questions: whose voluntary exchanges are restricted; who pays higher prices; who benefits from protection; how discretion affects entry and predictability; and what adjustment burden falls on workers, producers, or public revenue. State the strongest objection fairly. These are the framework for the eventual recommendation, not a completed policy conclusion.

## 15. Reproducibility and source audit

The existing notebook successfully executed all 19 code cells in a fresh local kernel during the earlier audit. The original notebook and figures were preserved; the audit copy and text log are stored under `research/audit/`. The kernel's sandbox socket restriction required an escalated verification run, which succeeded.

After the folder rename, the old project-local `.venv` is absent from the new folder, and the system Python import check failed because pandas is unavailable. The saved successful execution remains valid evidence of that earlier run, but we have not rerun the analysis in the current environment. Restore a reproducible environment before changing analytical outputs.

Colab setup currently relies on manual uploads and has no functioning public dataset URLs. Fresh judge execution needs provided data or URL loading as required. Check both files independently. Dependencies are unpinned; audited versions appear in Appendix A and should not be assumed to remain installed.

Source audit: 418 archived files, comprising eight PDF-signature files, 408 HTML/text files, and two empty files. Readable extraction is not verification of all their claims. `source_inventory.csv` records path, size, format, extraction status, text length, hash, and preview.

Unusable downloads: two empty Kenya IMF files; Bangladesh UNCTAD browser challenge saved as PDF; Mauritius IMF access-denied response saved as PDF; Thailand State Department technical-error page. Do not cite those downloaded responses as evidence.

Readable sources include budgets, executive orders, WTO reviews, SPDC research, and the PIIE chapter. Build a claim-by-claim manifest with actual publisher/title/year, URL, access date, page/paragraph, evidence, and interpretation. Do not infer metadata or successful access from filenames. Some archived PDFs may be image-only; text-extraction success/absence must be distinguished from document validity.

## 16. Remaining work, in order

| Priority | Task | Completion condition |
|---|---|---|
| 1 | Confirm declaration status, exact deadline, participant label, and EFW version | Written project record; solo status already confirmed |
| 2 | Resolve panel-sheet versus tariff-subcomponent requirements | Organiser scope response or approved declaration explicitly covering variables |
| 3 | Finish reform sourcing for every screened case | Consistent date basis, documentary locations, uncertainty and inclusion decisions |
| 4 | Correct Thailand exclusion; investigate Mauritius and baseline-dated cases | Ledger accurately reflects opened evidence; no outcome-based exclusions |
| 5 | Synchronise notebook, CSV, notes, and builder | One authoritative date record; provisional output preserved as history |
| 6 | Restore runtime and fix portable data loading | Analysis executes with provided inputs from fresh environment |
| 7 | Add merge, missingness, benchmark, and robustness checks | Country-by-country results with valid denominators and contrary evidence |
| 8 | Finalise research question and empirical interpretation | Exact cases/years/outcome; claim matches what data supports |
| 9 | Research one current Nepal policy change | Named rule, authority, mechanism, evidence, objection, liberty reasoning |
| 10 | Generate final figures and index together | Every displayed number traceable to final working file |
| 11 | Build PDF deck and appendices | ≤10 content slides, full supporting materials, AI disclosure |
| 12 | Package and test submission | Approved declaration, correct filenames, judge access, reproducibility |

Suggested content sequence: question; policy/case rule; policy evidence; raw income; event alignment; magnitude; contrary/robustness; limitations; one recommendation; liberty and strongest objection. This is a proposed structure, not an existing presentation. Appendix should contain chart index, sources and AI disclosure; no team contribution statement is needed for this solo entry.

## 17. Sources and AI record

The reform ledger reproduced below preserves existing citations and access fields but does not certify them. The comprehensive archive inventory is [source_inventory.csv](research/audit/source_inventory.csv).

Sources consulted during the audit/continuation:

- [UNDP documentation and downloads](https://hdr.undp.org/data-center/documentation-and-downloads), accessed 13 October 2026: identifies the composite component time series; linked metadata fetch did not succeed.
- [WTO Thailand review, December 1995](https://www.wto.org/english/tratop_e/tpr_e/tp021_e.htm), accessed 13 October 2026: opened and read for programme dating.
- [USTR 1996 National Trade Estimate: Thailand](https://ustr.gov/archive/Document_Library/Reports_Publications/1996/1996_National_Trade_Estimate/1996_National_Trade_Estimate-Thail.html), accessed 13 October 2026: opened and read to corroborate phase-in timing.
- [Mauritius 2005–06 budget speech](https://mof.govmu.org/Documents/Documents/Budget%202005-2006/speech05pdf.pdf), search lead on 13 October 2026: reader fetch failed; not yet a fully reviewed evidence source.
- [IMF Mauritius Selected Issues and Statistical Appendix, 1999](https://www.imf.org/-/media/websites/imf/imported-full-text-pdf/external/pubs/ft/scr/1999/_cr99125.pdf), accessed 13 October 2026: PDF opened, but relevant pages not yet read; programme-dating lead only.

A complete final bibliography still needs dataset release identities, every final policy/context citation, source locations, and verified access dates. Search snippets alone do not establish final policy dates.

AI disclosure draft: “OpenAI Codex assisted with inspecting files, checking data structure and reproducibility, extracting source text, researching documentary leads, and documenting methods and unresolved issues. The participant reviewed and remains responsible for the analysis, claims, and final recommendation.” Add any other AI tools actually used; do not invent them or claim human review that has not occurred.

## 18. Technical appendices

The following material is inserted programmatically from existing project files and the saved fresh-kernel notebook. Rounded table displays reflect notebook formatting; raw inputs and calculation code remain the numerical authority. These appendices document the current snapshot and do not implement the pending corrections.

### Appendix A — Dataset profile, hashes, and audited dependency versions

```json
{
  "audit_date": "2026-10-13",
  "efw": {
    "rows": 5115,
    "countries": 165,
    "years": [
      1970,
      1975,
      1980,
      1985,
      1990,
      1995,
      2000,
      2001,
      2002,
      2003,
      2004,
      2005,
      2006,
      2007,
      2008,
      2009,
      2010,
      2011,
      2012,
      2013,
      2014,
      2015,
      2016,
      2017,
      2018,
      2019,
      2020,
      2021,
      2022,
      2023,
      2024
    ],
    "sheets": [
      "EFW Ratings",
      "EFW Panel Dataset",
      "EFW Ratings 1950-1965"
    ],
    "duplicate_keys": 0,
    "raw_tariff_column": "data.10",
    "raw_tariff_dispersion_column": "data.11"
  },
  "undp": {
    "rows": 206,
    "columns": 1112,
    "country_territory_rows": 195,
    "aggregate_rows": 11,
    "duplicate_iso3": 0,
    "variables": {
      "gnipc": {
        "years": [
          1990,
          2023
        ],
        "nonmissing_country_values": 6478
      },
      "le": {
        "years": [
          1990,
          2023
        ],
        "nonmissing_country_values": 6630
      },
      "eys": {
        "years": [
          1990,
          2023
        ],
        "nonmissing_country_values": 6310
      },
      "mys": {
        "years": [
          1990,
          2023
        ],
        "nonmissing_country_values": 6081
      }
    }
  },
  "merge": {
    "intersection": 164,
    "efw_without_undp": [
      "TWN"
    ]
  },
  "selection": {
    "eligible_countries": 98,
    "selected": {
      "BGD": -64.4,
      "PAK": -46.5,
      "IND": -38.2,
      "CHN": -28.3,
      "MUS": -27.700000000000003,
      "THA": -25.4,
      "PHL": -22.200000000000003,
      "KEN": -21.9,
      "CIV": -20.4,
      "SEN": -20.200000000000003
    }
  },
  "versions": {
    "pandas": "3.0.6",
    "numpy": "2.5.4",
    "openpyxl": "3.1.5",
    "matplotlib": "3.11.2",
    "nbformat": "5.11.1",
    "nbclient": "0.11.0",
    "ipykernel": "7.4.0",
    "pypdf": "6.20.1"
  },
  "data_hashes": {
    "data/EFW_original.xlsx": "51a77026143bb941c1b9159bbea521a46b750eee3e4cb7ba9b75279203e17146",
    "data/UNDP_original.csv": "61ed82e5b66c88dfca8ff9fac775c63981ecab6a254862af97acacc41c143117"
  }
}
```

The two working dataset hashes matched their original copies in the audit. Recorded dependency versions describe that audited environment, not the current system Python.

### Appendix B — Exact country-selection output (cell 14)

```text
10 cases (tariff fell >= 20.0 pp, 1995->2005); 98 countries had both years + GNI

                country  tariff 1995 (%)  tariff 2005 (%)  change (pp)
ISO_Code                                                              
BGD          Bangladesh             81.2             16.8        -64.4
PAK            Pakistan             61.1             14.6        -46.5
IND               India             55.2             17.0        -38.2
CHN               China             37.5              9.2        -28.3
MUS           Mauritius             36.2              8.5        -27.7
THA            Thailand             36.0             10.6        -25.4
PHL         Philippines             27.6              5.4        -22.2
KEN               Kenya             34.0             12.1        -21.9
CIV       Côte d'Ivoire             33.0             12.6        -20.4
SEN             Senegal             34.2             14.0        -20.2
Just outside the rule (sensitivity only): Madagascar (-18.4), Rwanda (-17.6), Malawi (-17.3), Burundi (-17.3), Poland (-15.7)
```

### Appendix C1 — Notebook versus external date-table comparison

```csv
iso3,country,reform_year_notebook,status_notebook,reform_year_csv,status_csv
IND,India,1991,VERIFIED (primary source read),1991.0,VERIFIED (primary source: budget speech)
BGD,Bangladesh,1995,UNVERIFIED,1992.0,VERIFIED (WTO TPR; baseline-dated)
PAK,Pakistan,1997,UNVERIFIED,1997.0,VERIFIED (SPDC + WTO TPR; year-level)
CHN,China,1992,UNVERIFIED,1992.0,VERIFIED (open PIIE book chapter)
MUS,Mauritius,1999,UNVERIFIED,,EXCLUDED (no verifiable reform date)
THA,Thailand,1995,UNVERIFIED,,EXCLUDED (no verifiable reform date)
PHL,Philippines,1995,VERIFIED (primary source read),1995.0,VERIFIED (primary source: executive orders)
KEN,Kenya,1993,UNVERIFIED,1992.0,VERIFIED (WTO TPR; baseline-dated)
CIV,Cote d'Ivoire,2000,UNVERIFIED,1998.0,VERIFIED (WTO TPR; shared WAEMU reform)
SEN,Senegal,2000,UNVERIFIED,1998.0,VERIFIED (WTO TPR; shared WAEMU reform)
```

### Appendix C2 — Existing external reform ledger (not final verification)

```csv
iso3,country,reform_year,reform_description,effective_date,source_url,accessed,status
IND,India,1991,"Union Budget 1991-92: ad valorem customs peak capped at 150% (previously >300% on some lines)",July 1991 (budget day),https://www.indiabudget.gov.in/doc/bspeech/bs199192.pdf,2026-10-13,VERIFIED (primary source: budget speech)
CHN,China,1992,"Tariff cuts on 3,596 duty codes in Jan and Dec 1992 (avg -7.3%); 1986-91 cuts had touched only 81 of ~6300 codes",Jan 1992,https://www.piie.com/publications/chapters_preview/31/2iie2474.pdf,2026-10-13,VERIFIED (open PIIE book chapter)
BGD,Bangladesh,1992,"WTO TPR 2000: 'Since 1992 Bangladesh has continued to liberalize... greatly reducing tariffs'; bands 15 (1992/93) -> 5 (1999/2000); max tariff 300% -> 37.5%; avg MFN 58% -> 22%",FY1992/93 (baseline year),https://www.wto.org/english/tratop_e/tpr_e/tp132_e.htm,2026-10-13,VERIFIED (WTO TPR; baseline-dated)
PAK,Pakistan,1997,"After taking office in 1997 the government cut the maximum tariff from 65% to 45%; to 35% in March 1999 (SPDC budget evaluation); WTO TPR 2002 confirms max rate 30% then 25%",1997,https://spdc.org.pk/assets/upload/5f4efd6fbdd6c-Evaluation%20of%20the%20Federal%20Budget%201999%202000-RR-23.pdf; https://www.wto.org/english/tratop_e/tpr_e/tp185_e.htm,2026-10-13,VERIFIED (SPDC + WTO TPR; year-level)
PHL,Philippines,1995,"Executive Order 264 (signed 22 Jul 1995): industrial tariff reduction programme in effect from 28 Aug 1995 (per EO 288 recital)",28 Aug 1995,https://lawphil.net/executive/execord/eo1995/eo_264_1995.html; https://lawphil.net/executive/execord/eo1995/eo_288_1995.html,2026-10-13,VERIFIED (primary source: executive orders)
KEN,Kenya,1992,"WTO TPR 2000: max ad valorem rate lowered from 60% in 1992 to 25% in 1999; bands 8 (1994) -> 5",1992 (baseline year),https://www.wto.org/english/tratop_e/tpr_e/tp124_e.htm,2026-10-13,VERIFIED (WTO TPR; baseline-dated)
CIV,Cote d'Ivoire,1998,"WAEMU Common External Tariff (4 rates: 1/6/11/21%): transition began July 1998, completed Jan 2000 (WTO TPR Togo 1999). Same reform as SEN.",Jul 1998,https://www.wto.org/english/tratop_e/tpr_e/tp102_e.htm,2026-10-13,VERIFIED (WTO TPR; shared WAEMU reform)
SEN,Senegal,1998,"WAEMU Common External Tariff: transition began July 1998, completed Jan 2000 (WTO TPR Togo 1999). Same reform as CIV.",Jul 1998,https://www.wto.org/english/tratop_e/tpr_e/tp102_e.htm,2026-10-13,VERIFIED (WTO TPR; shared WAEMU reform)
MUS,Mauritius,,"No open source found that dates a tariff-cutting reform. WTO TPR 2001 still reports MFN rates up to 65% in 2000/01 Budget and ~20% average.",,https://www.wto.org/english/tratop_e/tpr_e/tp176_e.htm,2026-10-13,EXCLUDED (no verifiable reform date)
THA,Thailand,,"No open source found that dates a tariff-cutting reform. WTO TPR 1999 reports tariff INCREASES during 1995-99 review period, so a 1995 date could not be confirmed.",,https://www.wto.org/english/tratop_e/tpr_e/tp122_e.htm,2026-10-13,EXCLUDED (no verifiable reform date)
```

### Appendix D — Event-window coverage (cell 18)

```text
(151, 10)

               first  last  n_gni  n_tariff
country                                    
Bangladesh        -5    10     16         8
China             -2    10     13         5
Côte d'Ivoire     -5    10     16        12
India             -1    10     12         4
Kenya             -3    10     14         6
Mauritius         -5    10     16        11
Pakistan          -5    10     16         9
Philippines       -5    10     16         8
Senegal           -5    10     16        12
Thailand          -5    10     16         8
```

### Appendix E1 — Country-level provisional growth results (cell 20)

```text
  iso3        country  reform_year  pre_years_available  pre_cagr_%  post_cagr_%  benchmark_post_%  excess_vs_bench_pp
0  CHN          China         1992                    2         NaN         8.71              1.74                6.97
1  IND          India         1991                    1         NaN         3.97              1.70                2.27
2  MUS      Mauritius         1999                    5        3.78         3.85              2.33                1.53
3  BGD     Bangladesh         1995                    5        2.57         3.79              2.36                1.43
4  PHL    Philippines         1995                    5        1.52         2.76              2.36                0.39
5  PAK       Pakistan         1997                    5        0.11         2.33              2.60               -0.27
6  THA       Thailand         1995                    5        6.73         1.65              2.36               -0.71
7  SEN        Senegal         2000                    5        1.97         0.82              2.48               -1.66
8  KEN          Kenya         1993                    3       -3.45         0.10              1.88               -1.78
9  CIV  Côte d'Ivoire         2000                    5        0.29        -0.48              2.48               -2.96
Cases with post growth above benchmark: 5 of 10
Median post-reform CAGR: 2.54% | median benchmark: 2.36%
```

### Appendix E2 — Completed contrary-case and WAEMU check (cell 22)

```text
Cases at or below benchmark: ['Pakistan', 'Thailand', 'Senegal', 'Kenya', "Côte d'Ivoire"]
Excluding CIV & SEN (one shared reform): 5/8 beat benchmark; median excess 0.91 pp
All cases: median excess 0.06 pp
Note: borderline countries (-15 to -20 pp) listed in section 6 are not in the main sample.
```

### Appendix E3 — Existing final-check output (cell 32)

```text
    Fig  Slide                                      What it shows              Location in working file
0  Fig1      3  Raw mean tariff rate, 10 selected countries, w...  Notebook cell 25 -> figures/Fig1.png
1  Fig2      5  GNI per capita index aligned on reform year, 1...  Notebook cell 26 -> figures/Fig2.png
2  Fig3      6  Pre vs post GNI per capita CAGR and benchmark,...  Notebook cell 27 -> figures/Fig3.png
3  Fig4      7  Excess GNI growth over benchmark, counterexamp...  Notebook cell 28 -> figures/Fig4.png
4  Fig5      6        Life expectancy gain aligned on reform year  Notebook cell 29 -> figures/Fig5.png
5  Fig6      9  Nepal vs South Asian peers: tariff and GNI per...  Notebook cell 30 -> figures/Fig6.png
Checks passed. UNVERIFIED reform dates remaining: 8
```

The final-check message above reports eight unverified dates despite saying checks passed. It is an execution check, not evidence that all analytical requirements are satisfied.

### Appendix F — Current figure index

| Figure | Proposed slide | What it shows | Working-file location | Image |
|---|---|---|---|---|
| Fig1 | 3 | Raw mean tariff rate, 10 selected countries, with reform year | Notebook cell 25 | [Fig1.png](figures/Fig1.png) |
| Fig2 | 5 | GNI per capita index aligned on reform year, 10 cases + median | Notebook cell 26 | [Fig2.png](figures/Fig2.png) |
| Fig3 | 6 | Pre vs post GNI per capita CAGR and benchmark, by country | Notebook cell 27 | [Fig3.png](figures/Fig3.png) |
| Fig4 | 7 | Excess GNI growth over benchmark, counterexamples in red | Notebook cell 28 | [Fig4.png](figures/Fig4.png) |
| Fig5 | 6 | Life expectancy gain aligned on reform year | Notebook cell 29 | [Fig5.png](figures/Fig5.png) |
| Fig6 | 9 | Nepal vs South Asian peers: tariff and GNI per capita | Notebook cell 30 | [Fig6.png](figures/Fig6.png) |

### Appendix G — Notebook sections and exact current code

All cell numbers below count every cell, including markdown cells. Code is copied from the current notebook; this does not endorse its unresolved dating choices. The builder is a separate, newer proposal.

**Notebook cell 1 — saved narrative**

```markdown
# Liberty Data Drive 2026 — Working File
**Status:** sections 1–5 (setup → candidate scan). Sections 6–12 are added after the topic is chosen.

Data: Fraser Institute *Economic Freedom of the World* (EFW Ratings sheet, sub-components) and UNDP HDR composite-indices time series (1990–2023).
Raw files are never edited. Every number below is computed from them.
```

**Notebook cell 2 — saved narrative**

```markdown
## 1. Setup
```

**Notebook cell 3 — calculation code**

```python
import os, glob, sys
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 30)

# Colab: upload data/EFW_original.xlsx and data/UNDP_original.csv (or edit URLs below)
IN_COLAB = "google.colab" in sys.modules
if IN_COLAB and not os.path.exists("data/EFW_original.xlsx"):
    from google.colab import files
    os.makedirs("data", exist_ok=True)
    print("Upload EFW_original.xlsx and UNDP_original.csv"); up = files.upload()
    for k, v in up.items(): open(f"data/{k}", "wb").write(v)
EFW_PATH, UNDP_PATH = "data/EFW_original.xlsx", "data/UNDP_original.csv"
assert os.path.exists(EFW_PATH) and os.path.exists(UNDP_PATH), "data files missing"
```

**Notebook cell 4 — saved narrative**

```markdown
## 2. Load data
```

**Notebook cell 5 — calculation code**

```python
efw = pd.read_excel(EFW_PATH, sheet_name="EFW Ratings", header=3)
efw.columns = [str(c).strip() for c in efw.columns]
efw = efw[pd.to_numeric(efw["Year"], errors="coerce").notna()].copy()
efw["Year"] = efw["Year"].astype(int)
print("EFW:", efw.shape, "| years:", efw.Year.min(), "-", efw.Year.max(), "| countries:", efw.ISO_Code.nunique())

undp_wide = pd.read_csv(UNDP_PATH, encoding="latin1")
VARS = {"gnipc": "GNI per capita (2021 PPP$)", "le": "Life expectancy (years)",
        "eys": "Expected years of schooling", "mys": "Mean years of schooling"}
rows = []
for v in VARS:
    cols = [c for c in undp_wide.columns if c.startswith(v + "_") and c.split("_")[1].isdigit()]
    m = undp_wide.melt(id_vars=["iso3", "country"], value_vars=cols, var_name="k", value_name=v)
    m["year"] = m.k.str.split("_").str[1].astype(int)
    rows.append(m.set_index(["iso3", "country", "year"])[v])
undp = pd.concat(rows, axis=1).reset_index()
print("UNDP:", undp.shape, "| years:", undp.year.min(), "-", undp.year.max(), "| countries:", undp.iso3.nunique())
```

**Notebook cell 6 — saved narrative**

```markdown
## 3. Inspect
```

**Notebook cell 7 — calculation code**

```python
print("EFW years available:", sorted(efw.Year.unique())[:8], "... annual from 2000")
sub = ["4Aii  Mean tariff rate", "4A  Tariffs", "4B  Regulatory trade barriers", "4C  Black market exchange rates",
       "2C  Property rights", "2F Contracts", "5Dii Business Permits", "Area 4 Freedom to trade internationally"]
sub = [c for c in sub if c in efw.columns]
print("Missing sub-components:", [c for c in ["4Aii  Mean tariff rate","4A  Tariffs","4B  Regulatory trade barriers","4C  Black market exchange rates","2C  Property rights","2F Contracts","5Dii Business Permits"] if c not in efw.columns])
cov = efw.groupby("Year")[sub].agg(lambda s: pd.to_numeric(s, errors="coerce").notna().sum())
print("Non-missing obs per year (selected sub-components):"); display(cov.loc[[1990,1995,2000,2005,2010,2015,2020]])
print("UNDP non-missing by variable:"); display(undp[list(VARS)].notna().sum())
```

**Notebook cell 8 — saved narrative**

```markdown
## 4. Country matching (ISO3)
```

**Notebook cell 9 — calculation code**

```python
e_iso, u_iso = set(efw.ISO_Code.dropna()), set(undp.iso3.dropna())
print("EFW codes:", len(e_iso), "| UNDP codes:", len(u_iso), "| matched:", len(e_iso & u_iso))
print("In EFW, not in UNDP:", sorted(e_iso - u_iso))
print("(UNDP-only codes are mostly aggregates/regions, not needed.)")
SOUTH_ASIA = ["AFG","BGD","BTN","IND","MDV","NPL","PAK","LKA"]
print("South Asia in EFW:", sorted(set(SOUTH_ASIA) & e_iso), "| in UNDP:", sorted(set(SOUTH_ASIA) & u_iso))
NAME = efw.drop_duplicates("ISO_Code").set_index("ISO_Code")["Countries"]
```

**Notebook cell 10 — saved narrative**

```markdown
## 5. Candidate exploration
**Rule (applied identically to every indicator):** a country is a candidate case if its EFW sub-component score rose by **≥ 2.0 points** (0–10 scale) between **1995 and 2005**, both observations exist, and it has UNDP GNI per capita for 1990–2023.
Why 1995–2005? UNDP starts in 1990, so a reform needs ≥5 years of UNDP history before it and ≥10 after. EFW is 5-yearly before 2000, so the exact year is *not* read from EFW; it is dated later from public sources.
The threshold is a scan parameter, not a final selection. Final selection and reform dates come in section 6–7.
```

**Notebook cell 11 — calculation code**

```python
A, B, THRESH = 1995, 2005, 2.0
cands = ["4Aii  Mean tariff rate", "4A  Tariffs", "4B  Regulatory trade barriers", "4C  Black market exchange rates",
         "2C  Property rights", "2F Contracts", "5Dii Business Permits", "Area 4 Freedom to trade internationally",
         "Area 2 Legal System & Property Rights -- Without Gender Adjustment"]
cands = [c for c in cands if c in efw.columns]
num = efw.copy()
for c in cands: num[c] = pd.to_numeric(num[c], errors="coerce")
has_gni = set(undp.dropna(subset=["gnipc"]).iso3)
summ, detail = [], {}
for c in cands:
    p = num.pivot_table(index="ISO_Code", columns="Year", values=c)
    if A not in p or B not in p: continue
    d = (p[B] - p[A]).dropna()
    d = d[d.index.isin(has_gni)]
    hit = d[d >= THRESH].sort_values(ascending=False)
    neg = d[d <= -THRESH]
    detail[c] = hit
    summ.append({"indicator": c, "n_with_both_years": len(d), "n_rose_>=%.1f" % THRESH: len(hit),
                 "n_fell_>=%.1f" % THRESH: len(neg), "median_change": round(d.median(), 2),
                 "south_asia_hits": [i for i in hit.index if i in SOUTH_ASIA]})
scan = pd.DataFrame(summ).sort_values("n_rose_>=%.1f" % THRESH, ascending=False)
display(scan)
```

**Notebook cell 12 — calculation code**

```python
# Peek at the top countries for each indicator (so cases are chosen by rule, not by eye)
for c, hit in detail.items():
    print(f"\n{c}: {len(hit)} countries rose >= {THRESH}")
    print(", ".join(f"{NAME.get(i,i)} ({v:+.1f})" for i, v in hit.head(12).items()))
```

**Notebook cell 13 — saved narrative**

```markdown
## 6. Case selection (fixed rule)
**Rule:** every country whose **raw mean tariff rate (%)** fell by **≥ 20 percentage points between 1995 and 2005** (EFW Ratings, data column beside *4Aii Mean tariff rate*), with UNDP GNI per capita available.
The raw rate is used because the 0–10 score is floored at 0 for tariffs above ~50%, which hides most of the South Asian change.
No country is added or removed after seeing outcomes.
```

**Notebook cell 14 — calculation code**

```python
i = list(efw.columns).index("4Aii  Mean tariff rate")
efw["tariff_raw"] = pd.to_numeric(efw[efw.columns[i + 1]], errors="coerce")   # % mean tariff rate
tar = efw[["ISO_Code", "Year", "tariff_raw"]].dropna()
P = tar.pivot_table(index="ISO_Code", columns="Year", values="tariff_raw")
A, B, RULE_PP = 1995, 2005, 20.0
chg = (P[B] - P[A]).dropna()
chg = chg[chg.index.isin(has_gni)]
cases = chg[chg <= -RULE_PP].sort_values()
print(f"{len(cases)} cases (tariff fell >= {RULE_PP} pp, {A}->{B}); {len(chg)} countries had both years + GNI")
display(pd.DataFrame({"country": [NAME[c] for c in cases.index], f"tariff {A} (%)": P.loc[cases.index, A].round(1),
                      f"tariff {B} (%)": P.loc[cases.index, B].round(1), "change (pp)": cases.round(1)}))
near = chg[(chg <= -15) & (chg > -RULE_PP)].sort_values()
print("Just outside the rule (sensitivity only):", ", ".join(f"{NAME[c]} ({v:.1f})" for c, v in near.items()))
```

**Notebook cell 15 — saved narrative**

```markdown
## 7. Reform dates
`reform_year` = first year the government's main tariff cut took legal effect, confirmed in an open document (same logic for every country).
Rows marked **UNVERIFIED** are leads only and must be confirmed before the deck is final. Full log: `research/policy_notes.md`.
Côte d'Ivoire and Senegal share one WAEMU reform, so they are **not independent** — flagged and tested in section 10.
```

**Notebook cell 16 — calculation code**

```python
DATES_CSV = """iso3,country,reform_year,reform_description,effective_date,source_url,accessed,status
IND,India,1991,"Union Budget 1991-92: ad valorem customs peak capped at 150% (previously >300% on some lines)",July 1991 (budget day),https://www.indiabudget.gov.in/doc/bspeech/bs199192.pdf,2026-10-13,VERIFIED (primary source read)
BGD,Bangladesh,1995,"LEAD ONLY: FY1994/95 tariff restructuring (max rate cut sharply; fewer bands)",FY1994/95,,,UNVERIFIED
PAK,Pakistan,1997,"LEAD ONLY: 1997-98 budget tariff rationalisation; further cuts 2001-02",FY1997/98,,,UNVERIFIED
CHN,China,1992,"LEAD ONLY: tariff cuts from 1992 ahead of WTO accession (2001)",1992,,,UNVERIFIED
MUS,Mauritius,1999,"LEAD ONLY: tariff reform of late 1990s / 2000s",?,,,UNVERIFIED
THA,Thailand,1995,"LEAD ONLY: tariff structure reductions mid-1990s",?,,,UNVERIFIED
PHL,Philippines,1995,"Executive Order 264 (signed 22 Jul 1995; industrial tariff reduction programme in effect from 28 Aug 1995 per EO 288 recital)",28 Aug 1995,https://lawphil.net/executive/execord/eo1995/eo_264_1995.html; https://lawphil.net/executive/execord/eo1995/eo_288_1995.html,2026-10-13,VERIFIED (primary source read)
KEN,Kenya,1993,"LEAD ONLY: early-1990s import liberalisation",?,,,UNVERIFIED
CIV,Cote d'Ivoire,2000,"LEAD ONLY: WAEMU common external tariff",Jan 2000,,,UNVERIFIED
SEN,Senegal,2000,"LEAD ONLY: WAEMU common external tariff (same reform as CIV)",Jan 2000,,,UNVERIFIED
"""
from io import StringIO
dates = pd.read_csv(StringIO(DATES_CSV))
miss = set(cases.index) ^ set(dates.iso3)
assert not miss, f"cases vs reform-date table mismatch: {miss}"
display(dates[["iso3", "country", "reform_year", "effective_date", "status"]])
n_unv = dates.status.str.startswith("UNVERIFIED").sum()
print(f"WARNING: {n_unv} of {len(dates)} reform dates are still UNVERIFIED leads." if n_unv else "All reform dates verified.")
```

**Notebook cell 17 — saved narrative**

```markdown
## 8. Event-time dataset
`event_time = year − reform_year` (0 = reform year). Window: −5 … +10 years, clipped to UNDP coverage (1990–2023). Nothing is interpolated.
The EFW tariff series is 5-yearly before 2000, so some event years have no EFW value (left blank).
```

**Notebook cell 18 — calculation code**

```python
LO, HI = -5, 10
u = undp[undp.iso3.isin(cases.index)][["iso3", "year", "gnipc", "le", "eys", "mys"]].copy()
u = u.merge(dates[["iso3", "reform_year"]], on="iso3")
u["event_time"] = u.year - u.reform_year
panel = u[(u.event_time >= LO) & (u.event_time <= HI)].merge(
    tar.rename(columns={"ISO_Code": "iso3", "Year": "year"}), on=["iso3", "year"], how="left")
panel["country"] = panel.iso3.map(NAME)
panel = panel[["country", "iso3", "year", "reform_year", "event_time", "tariff_raw", "gnipc", "le", "eys", "mys"]]
print(panel.shape); display(panel.groupby("country").agg(first=("event_time", "min"), last=("event_time", "max"),
      n_gni=("gnipc", "count"), n_tariff=("tariff_raw", "count")))
base = panel[panel.event_time == 0].set_index("iso3")
panel["gni_index"] = panel.gnipc / panel.iso3.map(base.gnipc) * 100
panel["le_gain"] = panel["le"] - panel.iso3.map(base["le"])
```

**Notebook cell 19 — saved narrative**

```markdown
## 9. Main analysis (descriptive)
- **Growth:** average annual GNI per capita growth (CAGR) in the 5 years before vs the 10 years after the reform year. If fewer than 3 pre-years exist in UNDP data (1990 start), pre-growth is not computed (`NaN`).
- **Benchmark:** median CAGR of all *non-case* EFW countries over the **same calendar years** — a crude control for global conditions. Not a causal control.
```

**Notebook cell 20 — calculation code**

```python
def cagr(s, y0, y1):
    if y0 in s.index and y1 in s.index and s[y0] > 0 and s[y1] > 0:
        return (s[y1] / s[y0]) ** (1 / (y1 - y0)) - 1
    return np.nan
G = undp[undp.iso3.isin(e_iso)].pivot_table(index="iso3", columns="year", values="gnipc")
non_case = G.index.difference(cases.index)
def bench(y0, y1):
    return np.nanmedian([cagr(G.loc[c], y0, y1) for c in non_case])
rows = []
for iso, ry in dates.set_index("iso3").reform_year.items():
    s = G.loc[iso]; p0 = max(1990, ry - 5)
    pre = cagr(s, p0, ry) if ry - p0 >= 3 else np.nan
    post = cagr(s, ry, ry + 10)
    bpost = bench(ry, ry + 10)
    rows.append({"iso3": iso, "country": NAME[iso], "reform_year": ry, "pre_years_available": ry - p0,
                 "pre_cagr_%": pre * 100, "post_cagr_%": post * 100, "benchmark_post_%": bpost * 100,
                 "excess_vs_bench_pp": (post - bpost) * 100})
res = pd.DataFrame(rows).sort_values("excess_vs_bench_pp", ascending=False).reset_index(drop=True)
display(res.round(2))
print("Cases with post growth above benchmark:", (res.excess_vs_bench_pp > 0).sum(), "of", len(res))
print("Median post-reform CAGR: %.2f%% | median benchmark: %.2f%%" % (res["post_cagr_%"].median(), res["benchmark_post_%"].median()))
```

**Notebook cell 21 — saved narrative**

```markdown
## 10. Counterexamples and robustness
(a) The case(s) that do **not** beat the benchmark are charted, not hidden. (b) Dependence on the two WAEMU cases (CIV, SEN). (c) Sensitivity to the selection threshold (adding the borderline cases).
```

**Notebook cell 22 — calculation code**

```python
lag = res[res.excess_vs_bench_pp <= 0]
print("Cases at or below benchmark:", list(lag.country) or "none")
nw = res[~res.iso3.isin(["CIV", "SEN"])]
print("Excluding CIV & SEN (one shared reform): %d/%d beat benchmark; median excess %.2f pp"
      % ((nw.excess_vs_bench_pp > 0).sum(), len(nw), nw.excess_vs_bench_pp.median()))
print("All cases: median excess %.2f pp" % res.excess_vs_bench_pp.median())
print("Note: borderline countries (-15 to -20 pp) listed in section 6 are not in the main sample.")
```

**Notebook cell 23 — saved narrative**

```markdown
## 11. Final figures
Each figure is one cell; `register()` records it for the chart index.
```

**Notebook cell 24 — calculation code**

```python
import matplotlib as mpl
os.makedirs("figures", exist_ok=True)
mpl.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
                     "grid.alpha": .25, "font.size": 10})
SRC = "Sources: Fraser Institute EFW (Ratings sheet); UNDP HDR 2025 composite-indices time series."
CHART_INDEX = []
def register(fig_id, slide, what, cell):
    CHART_INDEX.append({"Fig": fig_id, "Slide": slide, "What it shows": what, "Location in working file": f"Notebook cell {cell} -> figures/{fig_id}.png"})
def finish(fig, fig_id, title, note):
    fig.suptitle(title, fontsize=12, fontweight="bold", x=0.01, ha="left")
    fig.text(0.01, 0.005, note + "\n" + SRC, fontsize=7.5, color="#444", va="bottom")
    fig.tight_layout(rect=[0, 0.07, 1, 0.95]); fig.savefig(f"figures/{fig_id}.png", dpi=200); plt.show()
order = list(res.iso3)
```

**Notebook cell 25 — calculation code**

```python
# Fig1: tariff trajectories (calendar years, markers = actual EFW observations)
fig, axes = plt.subplots(2, 5, figsize=(14, 6), sharey=True)
for ax, iso in zip(axes.flat, order):
    d = tar[tar.ISO_Code == iso].sort_values("Year"); d = d[d.Year <= 2024]
    ax.plot(d.Year, d.tariff_raw, "o-", ms=3, lw=1.2)
    ry = int(dates.set_index("iso3").loc[iso, "reform_year"]); ax.axvline(ry, color="crimson", ls="--", lw=1)
    ax.set_title(NAME[iso], fontsize=9)
ax.set_ylim(0, tar[tar.ISO_Code.isin(order) & (tar.Year <= 2024)].tariff_raw.max() * 1.05)   # full range, nothing clipped
for ax in axes[:, 0]: ax.set_ylabel("Mean tariff rate (%)")
finish(fig, "Fig1", "Fig 1. Mean tariff rate fell sharply in all 10 selected countries (EFW, all years available)",
       f"Red dashed line = reform year (see section 7; some UNVERIFIED). n = {len(order)} countries chosen by rule: fell >= {RULE_PP:.0f} pp, {A}-{B}. Points are 5-yearly before 2000, annual after; no interpolation.")
register("Fig1", 3, "Raw mean tariff rate, 10 selected countries, with reform year", 25)
```

**Notebook cell 26 — calculation code**

```python
# Fig2: GNI per capita indexed to reform year = 100
fig, ax = plt.subplots(figsize=(9, 5.2))
for iso in order:
    d = panel[panel.iso3 == iso].sort_values("event_time")
    ax.plot(d.event_time, d.gni_index, lw=1.1, alpha=.8, label=NAME[iso])
med = panel.groupby("event_time").gni_index.median()
cnt = panel.groupby("event_time").gni_index.count()
med = med[cnt >= 5]
ax.plot(med.index, med.values, "k-", lw=3, label="Median (>=5 countries)")
ax.axvline(0, color="crimson", ls="--"); ax.axhline(100, color="grey", lw=.8)
ax.set_xlabel("Years since reform year (0 = reform)"); ax.set_ylabel("GNI per capita, index (reform year = 100)")
ax.legend(fontsize=7, ncol=2, frameon=False)
finish(fig, "Fig2", "Fig 2. GNI per capita around each country's tariff-reform year",
       f"GNI per capita in 2021 PPP$, indexed to 100 in the reform year. Window -5 to +10 (shorter pre-window where UNDP data starts in 1990). n = {len(order)} countries.")
register("Fig2", 5, "GNI per capita index aligned on reform year, 10 cases + median", 26)
```

**Notebook cell 27 — calculation code**

```python
# Fig3: growth before vs after + benchmark (bars start at zero)
r = res.set_index("country")
x = np.arange(len(r)); w = .27
fig, ax = plt.subplots(figsize=(11, 5))
ax.bar(x - w, r["pre_cagr_%"], w, label="5 yrs before (if >=3 yrs of data)", color="#9aa5b1")
ax.bar(x, r["post_cagr_%"], w, label="10 yrs after", color="#1f6feb")
ax.bar(x + w, r["benchmark_post_%"], w, label="Benchmark: median non-case country, same years", color="#e8b04a")
ax.axhline(0, color="k", lw=.8); ax.set_xticks(x); ax.set_xticklabels(r.index, rotation=30, ha="right")
ax.set_ylabel("Average annual GNI per capita growth (%)"); ax.legend(frameon=False, fontsize=8)
finish(fig, "Fig3", "Fig 3. GNI per capita growth before vs after the reform, and vs the rest of the world",
       f"CAGR of GNI per capita (2021 PPP$). Missing grey bar = fewer than 3 pre-years in UNDP data. Benchmark = median of {len(non_case)} non-case EFW countries. n = {len(r)} cases.")
register("Fig3", 6, "Pre vs post GNI per capita CAGR and benchmark, by country", 27)
```

**Notebook cell 28 — calculation code**

```python
# Fig4: excess growth over benchmark (sorted) - shows who does NOT fit
fig, ax = plt.subplots(figsize=(9, 4.8))
colors = ["#1f6feb" if v > 0 else "crimson" for v in res.excess_vs_bench_pp]
ax.barh(res.country[::-1], res.excess_vs_bench_pp[::-1], color=colors[::-1])
ax.axvline(0, color="k", lw=.8); ax.set_xlabel("Post-reform CAGR minus benchmark CAGR (percentage points per year)")
finish(fig, "Fig4", "Fig 4. Which cases grew faster than the benchmark after reform? (red = did not)",
       f"Benchmark = median non-case country over the same 10 calendar years. {int((res.excess_vs_bench_pp>0).sum())} of {len(res)} cases above benchmark. CIV and SEN share one WAEMU reform.")
register("Fig4", 7, "Excess GNI growth over benchmark, counterexamples in red", 28)
```

**Notebook cell 29 — calculation code**

```python
# Fig5: life expectancy gain since reform year (secondary outcome)
fig, ax = plt.subplots(figsize=(9, 5))
for iso in order:
    d = panel[panel.iso3 == iso].sort_values("event_time")
    ax.plot(d.event_time, d.le_gain, lw=1.1, alpha=.8, label=NAME[iso])
m = panel.groupby("event_time").le_gain.median(); m = m[panel.groupby("event_time").le_gain.count() >= 5]
ax.plot(m.index, m.values, "k-", lw=3, label="Median (>=5 countries)")
ax.axvline(0, color="crimson", ls="--"); ax.axhline(0, color="grey", lw=.8)
ax.set_xlabel("Years since reform year (0 = reform)"); ax.set_ylabel("Life expectancy change since reform year (years)")
ax.legend(fontsize=7, ncol=2, frameon=False)
finish(fig, "Fig5", "Fig 5. Life expectancy change since the reform year (secondary outcome)",
       f"Life expectancy at birth, years, relative to the reform year. Includes HIV/AIDS-era dips (e.g. Kenya, Cote d'Ivoire). n = {len(order)} countries.")
register("Fig5", 6, "Life expectancy gain aligned on reform year", 29)
```

**Notebook cell 30 — calculation code**

```python
# Fig6: Nepal vs South Asian cases - tariff and GNI side by side (no dual axis)
SA = ["NPL", "BGD", "IND", "PAK", "LKA"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
for iso in SA:
    d = tar[(tar.ISO_Code == iso)].sort_values("Year"); lw = 3 if iso == "NPL" else 1.2
    a1.plot(d.Year, d.tariff_raw, "o-", ms=3, lw=lw, label=NAME[iso])
    g = undp[undp.iso3 == iso].sort_values("year"); a2.plot(g.year, g.gnipc, lw=lw, label=NAME[iso])
a1.set_ylabel("Mean tariff rate (%)"); a1.set_ylim(bottom=0); a1.set_title("Tariffs (EFW)", fontsize=10)
a2.set_ylabel("GNI per capita (2021 PPP$)"); a2.set_title("GNI per capita (UNDP)", fontsize=10); a1.legend(frameon=False, fontsize=8)
finish(fig, "Fig6", "Fig 6. Nepal vs South Asian peers: tariffs and income (1970-2024 / 1990-2023)",
       "Nepal (thick line) liberalised earlier and less than BGD/IND/PAK. Left: EFW 5-yearly before 2000. Right: UNDP annual. n = 5 countries.")
register("Fig6", 9, "Nepal vs South Asian peers: tariff and GNI per capita", 30)
```

**Notebook cell 31 — saved narrative**

```markdown
## 12. Chart index and final checks
```

**Notebook cell 32 — calculation code**

```python
ci = pd.DataFrame(CHART_INDEX); display(ci); ci.to_csv("figures/chart_index.csv", index=False)
for f in ci.Fig: assert os.path.exists(f"figures/{f}.png"), f
assert panel.groupby("iso3").size().min() > 0
print("Checks passed. UNVERIFIED reform dates remaining:", int(dates.status.str.startswith("UNVERIFIED").sum()))
```

### Appendix H — Supporting files and their roles

- [analysis.ipynb](analysis.ipynb): Current calculation notebook, provisional dates and six figures.
- [research/build_notebook.py](research/build_notebook.py): Regenerates and overwrites the notebook using nb_part2.py; do not run before date decisions.
- [research/nb_part2.py](research/nb_part2.py): Newer proposed sections 6–12, changed sample and eight figures.
- [research/run_nb.py](research/run_nb.py): Executes and rewrites the main notebook on success.
- [research/fetch_source.py](research/fetch_source.py): Downloads sources and extracts keyword context; validate responses before citation.
- [research/policy_notes.md](research/policy_notes.md): Historical topic/selection/dating notes, currently out of sync.
- [research/reform_dates.csv](research/reform_dates.csv): External proposed ledger, currently out of sync with the notebook.
- [research/readiness_report.md](research/readiness_report.md): Earlier audit; historical AGENTS/team references need reading with this record’s updates.
- [research/audit/data_profile.json](research/audit/data_profile.json): Computed data coverage, hashes, and versions.
- [research/audit/source_inventory.csv](research/audit/source_inventory.csv): Inventory and extraction status of all 418 archive files.
- [research/audit/source_contexts.txt](research/audit/source_contexts.txt): Searchable excerpts for selected source files, not complete verification.
- [research/audit/reform_date_comparison.csv](research/audit/reform_date_comparison.csv): Notebook and external CSV differences.
- [research/audit/execution_log.txt](research/audit/execution_log.txt): Plain outputs from the successful isolated rerun.
- [research/audit/reexecuted_notebook.ipynb](research/audit/reexecuted_notebook.ipynb): Executed audit copy with rich outputs; not a replacement submission notebook.
- [research/audit/verify_notebook.py](research/audit/verify_notebook.py): Isolated verifier; root derived from script location.
- [figures/chart_index.csv](figures/chart_index.csv): Current six-figure mapping.
- [requirements.txt](requirements.txt): Unpinned dependencies; helper requirements should be recorded explicitly.
- [README.md](README.md): Original workflow and project overview; several next-work statements are historical.

### Appendix I — Documentation snapshot integrity

These hashes identify the files used to create this record, so later changes can be distinguished from this snapshot.

```text
9b2bea6063670ee719bed767b8c4da231b48425b879b8deed770c92a51dc3a75  analysis.ipynb
7fca4ce8917f830c8b0a9ede653755e197f44a800eb1a94feda4fb34f5773d1d  research/reform_dates.csv
222277ad26885a56f2b9c865af66a8dbbcbfa481350e4ae08bccec453c220724  research/nb_part2.py
979a79f4f7a39735f4e93945af09096ba8e9adff2880afd7d4e10bec45db5be8  figures/chart_index.csv
1792a5d5609f9e4e45188cd0fe5097c4b977e52f8816afa12d64e8f6e7a5768f  research/audit/reexecuted_notebook.ipynb
```

Update this record when dates, case inclusion, calculations, figures, or recommendation change. Preserve prior provisional findings as history instead of attributing them to the revised analysis.
