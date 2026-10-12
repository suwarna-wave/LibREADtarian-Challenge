# Workspace readiness audit — Liberty Data Drive 2026

Audited 13 October 2026 (Asia/Kathmandu). Ready to continue research and repair the analysis; **not ready to treat the existing figures as final evidence or submit a deck**.

## What was checked

- Read `AGENTS.md`, `README.md`, the participant guidelines, all research scripts, the policy notes, reform-date CSV, chart index, and all 32 cells of the existing notebook.
- Checked the original guidelines DOCX against its extracted text: every DOCX text node is present in the text file.
- Inspected the Fraser workbook sheets, data structure, years, keys, tariff columns, country coverage, and country matching with UNDP. Inspected UNDP time-series columns and supplementary workbook sheet names.
- Compared SHA-256 hashes of the two working raw files with their original workspace copies: both copies match exactly.
- Visually reviewed all six existing chart images and compared their index with notebook cells.
- Inventoried and extracted text from every one of the 418 source-archive files. This checks readability and provides searchable excerpts; it does **not** establish that every archived document is relevant or that every claim has been verified.
- Successfully reran the existing notebook in a fresh local Jupyter kernel, using a separate temporary output directory. Preserved the original notebook, charts, raw files, and research decisions.
- Consulted the official UNDP downloads page. Some external pages could not be fetched; local archived text was used for the source checks described below. Exact Fraser release provenance remains unresolved.

Audit evidence is in `research/audit/`: `data_profile.json`, `source_inventory.csv`, `source_contexts.txt`, `reform_date_comparison.csv`, `execution_log.txt`, `reexecuted_notebook.ipynb`, and the isolated verification script. The reexecuted notebook is an audit copy, not the submission working file.

## Competition requirements collected

The participant guidelines are the controlling competition document; README and AGENTS supply working conventions.

- Individuals or teams of at most two coordinators; original work for this competition.
- One research question, written as a question, naming a policy, countries, period, and measurable outcome; at least three countries that made the same or comparable change.
- Fixed datasets: Fraser EFW **chain-linked panel sheet** and UNDP all composite indices and components time series. Use specific policy indicators and outcome components rather than overall freedom versus HDI.
- Rule-based selection where possible; actual policy-effective dates; reform alignment; contrary cases shown.
- Every chart value derived in the working file from the original datasets. No manual retyping of chart values or silent interpolation.
- Charts carry units, period, sources, sample size, and exclusions. Bars originate at zero, including signed bars extending below it; no dual axes or pies.
- Descriptive language and plausible alternative explanations for causal interpretations.
- Exactly one South Asian recommendation: Addition, Removal, or Modification; named policy and authority, mechanism, supporting figure numbers, and strongest objection. An addition must explain why existing rules do not cover the need.
- Maximum ten **content** slides, submitted as PDF. Verification appendices do not count; essential argument must remain in content slides.
- Working file accessible to judges; fresh Colab execution needs URL-loaded or included data. A local submission must include datasets and run instructions.
- Chart index, sources with access dates, AI disclosure, and team contribution statement when applicable.
- Approved dataset declaration required for acceptance. No approval record or declaration draft found here.
- File names: `LDD2026_TeamName_Deck.pdf` and `LDD2026_TeamName_Working.[ext]`.

Judging weights: research question 15; handling/reproducibility 20; visualisation 15; interpretation 15; recommendation 20; liberty reasoning 15. An unreproducible chart scores zero, and claims relying on it are disregarded. An inaccessible working file is treated as absent.

The guidelines give only relative dates: declaration due October second week, feedback October third week, submission at the end of the challenge. An exact deadline, team identity, and declaration status need organiser/user confirmation. Today is 13 October; do not infer a specific deadline from “second week.” Scope questions should go through the declaration process; general guideline questions name Dhiraj KC as contact. No messages have been sent.

## Data available

| File | Verified local contents | Implication |
|---|---|---|
| `data/EFW_original.xlsx` | Same bytes as `economic freedom.xlsx`; Ratings sheet: 5,115 rows, 87 columns, 165 jurisdictions, 1970–2024, no duplicate ISO/year keys | Five-yearly before 2000, annual thereafter; exact report/release needs provenance |
| `EFW Panel Dataset` sheet | ISO/year identifiers, chain-linked overall and five area measures, area dispersion; **no tariff subcomponent columns** | Competition sheet requirement and preferred subcomponent analysis need reconciling |
| `data/UNDP_original.csv` | Same bytes as original HDR25 CSV; 206 rows, 1,112 columns; 195 three-letter country/territory codes and 11 aggregates; unique ISO identifiers | Do not call all 206 rows countries; do not treat aggregates as cases |
| UNDP outcome series | GNI per capita, life expectancy, expected schooling, mean schooling cover 1990–2023 | No five-year prehistory for reforms close to 1990 |
| Supplementary UNDP workbooks | HDI levels/trends, IHDI, GDI, GII, PHDI, combined annex tables, and 2025 MPI | Available as references; not replacements for required outcome time series |

There are 164 matching EFW/UNDP identifiers. Taiwan (`TWN`) is in EFW but absent from this UNDP CSV. Six eligible South Asian targets are in EFW: BGD, BTN, IND, LKA, NPL, PAK; AFG and MDV are absent. All eight targets are in UNDP. Check each analysis merge explicitly with key uniqueness, validation, and unmatched-row reporting.

The tariff score is `4Aii  Mean tariff rate`; its adjacent **raw percentage** column is `data.10`. Tariff dispersion is adjacent to `4Aiii  Standard deviation of tariff rates`, in `data.11`. The existing notebook uses the raw mean, not the 0–10 rating. Explain that distinction in the declaration and sources. Verify tariff definitions, weighting, underlying sources, and historical comparability before interpreting large changes.

The local EFW series extends through 2024 although the guideline example cites a 2025 report. Do not infer a release year from that alone or label it 2025 without verification. UNDP’s official downloads page still identifies the required composite component series as 1990–2023: https://hdr.undp.org/data-center/documentation-and-downloads (accessed 13 October 2026).

## Existing analytical direction

Policy notes record tariff cuts → GNI per capita growth, with Nepal’s tariff schedule as the intended recommendation target. They describe this as previously confirmed with the user; that statement is historical project context, not fresh approval of a particular recommendation.

Current rule: raw mean tariffs fell at least 20 percentage points from 1995 to 2005, with GNI data available. Independently reproduced: ten countries qualify out of 98 with usable endpoint tariff data and a UNDP match. They are Bangladesh, Pakistan, India, China, Mauritius, Thailand, Philippines, Kenya, Côte d’Ivoire, and Senegal. Borderline cases are Madagascar, Rwanda, Malawi, Burundi, and Poland. Their inclusion should be tested when dates can be sourced, not merely listed.

The current notebook constructs event time −5 to +10, indexes GNI at reform year = 100, computes before/after CAGR, and compares post-growth to the median of other EFW countries over the same calendar years. It also charts life expectancy and Nepal versus four regional peers.

The isolated rerun reproduces the **provisional** finding: five of ten cases outperform the benchmark; Pakistan, Thailand, Senegal, Kenya, and Côte d’Ivoire do not. The median within-country excess over benchmark is approximately +0.06 percentage points per year. Detailed calculated outputs are in the execution log. These results depend on unverified dates and are not final policy evidence. A rise in GNI, an acceleration from pre-growth, and outperformance of the benchmark are distinct findings.

## Critical inconsistencies and repairs

1. **Required sheet not used.** The notebook reads `EFW Ratings` only. The panel sheet lacks the detailed tariff variables. Prepare a declaration that explains using chain-linked Area 4 alongside the raw tariff component as specific policy evidence, and seek the organiser’s scope ruling. Do not silently substitute the broad area score for tariff policy or claim raw rates are chain-linked.
2. **Three incompatible project states.** The notebook embeds ten dates, eight explicitly unverified. `reform_dates.csv` labels eight dates verified and proposes excluding Mauritius/Thailand. `policy_notes.md` says dates are not verified and contains older leads. The notebook builder would generate eight charts rather than six, alter some figure identities, change dates, and introduce exclusions. Rebuilding it now would overwrite the current notebook. Select one documented authoritative date table before regenerating anything.
3. **Effective dates are not consistently established.** Bangladesh and Kenya CSV dates are baseline years from retrospective reviews, rather than demonstrated legal-effective dates. India’s budget speech is evidence of the announced policy but legal commencement should also be checked. WAEMU dates are inferred from a Togo review for Côte d’Ivoire/Senegal; seek country-specific implementation evidence and distinguish transition from completion. Shared WAEMU reform means two countries do not provide two independent policy events.
4. **Exclusion rationale needs correction.** The archived Thailand WTO review describes an ongoing trend of tariff reductions alongside some increases. This does not support the CSV’s general statement that the review reports tariff increases as grounds for exclusion. The Mauritius review documents tariff changes too, though no exact effective date is established by the existing log. Keep both as unresolved sourcing cases while searching, and record why a case is included or excluded independently of outcomes.
5. **Final checks do not enforce validity.** Current notebook ends with “Checks passed” while reporting eight unverified dates. A string marked VERIFIED in the newer builder is also insufficient proof. Require a documented effective-date basis, source location, source accessibility, data coverage, merge integrity, and honest exclusions before final export.
6. **Colab data-loading requirement unmet.** Setup requests manual upload and mentions URLs without providing any. It does not automatically load included/public data in a fresh runtime. Also check each input separately; the upload branch currently checks only EFW’s existence.
7. **No final question or recommendation.** There is no complete question naming final cases and period, no researched current Nepal rule/authority, and no final recommendation, deck, source appendix, declaration approval, or contribution statement. Do not infer a suitable tariff change from Nepal’s income rank alone.

The date comparison CSV documents every notebook/CSV difference: Bangladesh 1995→1992, Kenya 1993→1992, CIV/SEN 2000→1998, and removal of the provisional dates for Mauritius/Thailand. Unchanged years still need their evidence assessed.

## Method and chart improvements needed

- Preserve a simple descriptive design. The benchmark is a broad comparator, not an untreated or matched control: its countries may also have trade reforms, different income levels, conflicts, or commodity exposure. Report the number with usable endpoint GNI for each calendar window; the current legend gives the pool size of 154, not necessarily the usable count.
- The selection period is 1995–2005 while several proposed reforms precede 1995. Explain why the rule identifies continuing tariff programmes and why the outcome window begins before the screening window; test reasonable alternatives. The files assert selection was fixed before outcomes, but no independent timestamped record was found in this audit.
- Separate incomplete prehistories from full five-year comparisons. India/China do not have enough pre-years under current dates. The newer CSV would also leave Bangladesh/Kenya with only two. Missing pre-growth is not zero.
- The indexed median changes country composition before reform. Show event-year counts or a fixed balanced subset as a sensitivity check. No interpolation of missing EFW values; distinguish line connectors from observations.
- Current robustness only removes both WAEMU countries. Builder-only additions include date shifts, five-year post-windows, and excluding China; these have not been incorporated or validated. For shifts before 1990, count missing endpoints as unavailable rather than “did not outperform.” Consider retaining one WAEMU case or reporting reform-group summaries as well as removing both.
- All six chart files match the current chart index and cell positions. Figures 3–4 show signed bars originating at zero, and Figure 6 avoids dual axes. Fonts/footnotes need checking at actual slide size; Figures 1–2 and 5 are crowded.
- Figure 1 displays some provisional reform markers. Figures 2–5 do not prominently identify the unverified dating on the chart itself. Figure 3 calls available 3–5-year preperiods “5 yrs before.” Figure 6’s title says tariff years 1970–2024, but the displayed observations begin later; distinguish dataset coverage from plotted coverage.
- Add a raw GNI time-series view and tariff event-time view if they clarify the story. Give event charts the corresponding calendar coverage as well as event years. Do not automatically add more figures than the deck can explain.
- Tariff reductions and tariff dispersion are different policies. Builder Figure 8 introduces dispersion as a basis for Nepal’s recommendation; this requires separate evidence and cannot be inferred from mean-tariff case selection alone.
- Write country-specific alternative explanations and support their factual details with open sources: broader liberalisation/stabilisation, China’s wider reforms, Asian financial crisis, conflict, health shocks, remittances, and global conditions are research leads, not explanations already established by this audit.

## Source archive findings

Inventory: 418 files = eight PDF-signature files, 408 HTML/text files, two empty downloads. The HTML/text total includes two files misleadingly named `.pdf`.

Unusable for citation as downloaded:

- `ken_imf7.pdf` and `ken_imf8.pdf`: empty.
- `bgd_unctad.pdf`: browser challenge page.
- `mus_imf.pdf`: access-denied HTML.
- `tha_state.html`: technical-difficulties response.

Archived open sources include India’s budget speeches, Philippines executive orders, WTO trade-policy reviews, SPDC budget research, and a China PIIE chapter. `chn_piie.html` contains readable chapter text despite its extension; record its relationship to the cited PDF URL. The inventory contains content previews and checksums. Archive filenames and existing “accessed” fields are not proof of effective-date verification; add page/paragraph and a short evidence extract for each final claim. Duplicate or vaguely named downloads such as `x.pdf` need a source manifest, not deletion without understanding their role.

Relevant dating leads from readable local archives: Bangladesh WTO review reports tariff restructuring across 1992/93–1999/2000; WAEMU/Togo review describes a transition from July 1998 to January 2000; Thailand review discusses both reductions and selective increases. These establish research leads and dating ambiguity, not a harmonised final event definition.

## Ordered next work

1. Confirm team details, exact deadline, declaration status, and required EFW release. Resolve panel/subcomponent interpretation through the declaration.
2. Record one precise question and preserve the current case-selection rule as a documented starting point.
3. Reverify actual reforms for every qualifying country using one dating standard; correct source claims and explicitly separate exact dates from uncertain dates and unresolved cases.
4. Synchronise policy notes, date table, notebook and builder. Keep old provisional results identifiable; regenerate charts/index together once decisions are settled.
5. Strengthen merge, missingness, window, benchmark, and date checks; implement fresh-runtime data loading and record dependencies. `requirements.txt` is unpinned and does not explicitly list `nbclient`, `nbformat`, or `pypdf` used by helper scripts; audit versions are recorded in `data_profile.json`.
6. Run simple country-by-country analysis, alternative windows and threshold checks; retain contrary evidence. Choose the strongest claim actually supported after those checks.
7. Research the current Nepal policy and competent authority, then formulate exactly one recommendation with mechanism, numbered evidence, costs, and liberty reasoning. No specific change is endorsed by this audit.
8. Produce at most ten content slides, verification appendices and submission package; rerun from a fresh environment and test judge access.

AI disclosure for work in this session: Codex assisted with workspace inspection, reproducibility checking, source-file extraction, data profiling and readiness documentation. The participant remains responsible for final claims and decisions. No external publication, organiser contact, or submission was made.
