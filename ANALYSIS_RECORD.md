# Liberty Data Drive 2026 — Complete analysis and work record

Updated **17 October 2026 (Asia/Kathmandu)**. Participant: **Suwarna Pyakurel, solo**.

This is the current master record. The earlier 13 October record and original notebook are preserved under `research/archive_2026-10-13/`. Earlier AGENTS.md instructions were revoked by the user; competition requirements come from the participant guidelines. This record describes what has actually been done and keeps remaining external checks explicit.

## 1. Current outcome

The numerical analysis, portable notebook, source ledger, eight chart exports, ten-content-slide PDF, editable PPTX, declaration draft, run instructions and submission checklist are prepared for participant review. A fresh empty-directory run restored the original datasets and executed every code cell. **Organiser approval, exact deadline, participant review and final submission are not completed or inferred.**

The main dated sample has 8 countries. Income rose over the ten-year endpoint comparison in 7/8; 4/8 exceeded the same-years broad comparator. Only 5 have a full five-year preperiod, of which 3 accelerated. Median country-level excess is +0.0635 percentage points/year. This is descriptive and does not establish a tariff effect.

## 2. What the competition asks for

One specific policy question across at least three countries; fixed Fraser/UNDP datasets; actual policy dates; before/after and reform alignment; contrary evidence; exactly one South Asian Addition/Removal/Modification; named rule and authority, mechanism, own supporting figures and strongest objection; liberty reasoning; maximum ten content slides as PDF; reproducible working file, chart index, public sources/access dates and AI disclosure. An approved dataset declaration is required. Solo participation removes the team-contribution-statement requirement, not AI disclosure or responsibility for understanding the work.

The provided timeline says October second-week declaration, third-week feedback and challenge-end submission, but gives no exact deadline. The participant has supplied a name but not deadline or approval status. No organiser contact, sharing change, form submission or publication was made by the assistant.

## 3. History and decisions

- Inherited: original data, guideline documents, a 32-cell notebook, six preliminary figures, scripts, policy notes, reform table and source archive.
- 13 October audit: checked guideline extraction, data structure, hashes, ISO matching, source archive and figures; reran the old notebook locally; wrote readiness report and full historical record.
- User update: confirmed solo participation; revoked earlier AGENTS.md instructions. Workspace folder changed from `LibREADtarian Challenge` to `LibREADtarian-Challenge`.
- Continued research found dated Thailand and Mauritius reforms, correcting earlier proposed exclusions.
- 16 October user authorised finishing the remaining work and supplied **Suwarna Pyakurel** as participant name.
- Restored an isolated analysis environment, reviewed additional primary/open institutional sources, rebuilt the date ledger, notebook and figures, prepared one recommendation and the presentation, and tested embedded-input execution.

## 4. Topic selection: what is and is not recorded

The README proposed trade, property rights, regulation and sound money. The exploratory notebook screened available indicators for two-rating-point improvement during 1995–2005. Tariffs offered a concrete policy, multiple cases, documentary reform leads, a measurable income outcome and relevance to Nepal. No formal scored ranking or independently timestamped preregistration exists, and none is claimed.

The final case screen uses a raw tariff decline of at least20 percentage points, not the exploratory two-rating-point threshold. This avoids obscuring high raw tariffs behind the rating floor. The EFW2026 explanatory notes describe the mean-tariff rating approaching zero at50%. Current methodology is informative but does not establish perfect historical raw-data comparability.

## 5. Dataset choice and integrity

The original EFW workbook and UNDP HDR25 time series were preserved. SHA-256 checks prevent a silently substituted input. The notebook embeds compressed original bytes and restores them only when files are absent; existing mismatched files fail validation.

EFW Ratings: 5,115 records, 165 jurisdictions, 1970–2024, no duplicate ISO/year keys. Five-yearly before2000 and annual thereafter. Raw mean tariff is `data.10` adjacent to `4Aii Mean tariff rate`. The chain-linked panel contains overall and area scores; it has no tariff subcomponent. The rebuilt notebook uses the required panel's Area4 as a separately labelled institutional series and raw Ratings tariffs as specific policy evidence. Raw rates are never relabelled chain-linked. Organiser acceptance of that interpretation remains pending.

The publisher/co-publisher now describes EFW2026 as covering2024, consistent with the local file's coverage and modification metadata. This does not prove byte identity with a live release or establish which version organisers require. The preserved workbook is the provided input; the declaration asks for release confirmation rather than silently swapping it.

UNDP: 206 rows and1,112 columns before filtering;195 three-letter country/territory identifiers and11 aggregates. Outcome components cover1990–2023. Aggregates are explicitly excluded before the rebuilt analysis. GNI/person (2021 PPP dollars) is primary. Life expectancy and schooling components are loaded for inspection but do not displace the primary deck outcome. Supplementary HDI, IHDI, GDI, GII, PHDI and MPI workbooks were inspected at sheet level and are not substituted for the required longitudinal file.

## 6. Country selection and matching

Selection formula: `tariff_2005 − tariff_1995 <= −20 percentage points`, with both tariff endpoints and some UNDP GNI data. Ten of98 eligible countries pass: Bangladesh, Pakistan, India, China, Mauritius, Thailand, Philippines, Kenya, Côte d'Ivoire and Senegal. All ten remain visible. Nepal is the recommendation target, not a selected reform case. Borderline countries remain in the all-eligible table.

ISO3 codes link datasets. There are164 shared codes; Taiwan is EFW-only. Afghanistan and Maldives are absent from this EFW file. Duplicate-key checks and explicit merge validation now guard all analytical joins. `outputs/country_mapping.csv` records matches/unmatched identifiers; missing outcome values stay missing.

The policy screen selects realised changes, while several documented programmes started before1995. It does not produce random or otherwise exogenous exposure. These limits are stated in the notebook and declaration. Source-quality decisions followed earlier outcome inspection; no unobserved rule-before-outcomes chronology is invented.

## 7. Main sample and dating rationale

Eight main episodes: India1991, China1992, Mauritius1994, Thailand1995, Philippines1995, Pakistan1997, Côte d'Ivoire1998, Senegal1998. Dating means onset of a documented broad tariff-cutting phase, not first liberalisation ever, not an EFW jump and not necessarily full completion. Sources range from legal orders to open retrospective institutional accounts, so precision varies. India’s speech explicitly states customs/excise changes effective25 July1991 (paragraph148); the peak-cut proposal is paragraph107. Philippines’ EO288 identifies EO264's effective date as28 August1995. The remaining exact evidence locations and limitations are in the ledger below.

Mauritius and Thailand are retained after correcting the old unsupported exclusions. CIV/SEN are related national implementations of one regional programme; main national onset1998 and regional completion2000 are compared. Their rows are not two independent regional policy shocks.

Bangladesh’s source identifies acceleration in1991 and fiscal changes over several years; Kenya’s source describes a broad mid1993 structural programme with subsequent tariff changes. Neither identifies a comparable tariff-only effective event precisely enough for this main definition. They remain in the screen and a twelve-combination timing grid, not treated as zero growth or silently dropped. This documentary judgement can still create selection risk and is disclosed.

## 8. Event windows and calculations

Event time is calendar year minus documentary reform year. Main window−5…+10, clipped to observed data; actual outcome calendar coverage1990–2008. Annual event-zero conventions can include months before implementation. No missing EFW observation is interpolated; lines merely connect observed points.

Income index: `100 × GNI_t / GNI_event0`. Every country meets at100 by construction. Equal-country medians change membership before the event where prehistory is unavailable. A fixed five-country balanced-window median is also shown; event-year counts are exported.

CAGR: `100 × [(GNI_end/GNI_start)^(1/elapsed_years) − 1]`. Valid positive endpoints required. The main pre-CAGR now requires a full five-year window; short available-history CAGR is exported separately, never substituted in the full-pre acceleration count. Post-CAGR spans event0 to+10. Missing is not zero.

Comparator: median valid endpoint CAGR of other EFW/UNDP countries over each case’s same calendar window, excluding all ten screened countries. Valid n varies148–152. Countries in the comparator may also reform. It is an unweighted contextual benchmark, not an untreated/matched causal control. Excess is post-CAGR minus comparator-CAGR; median excess is not generally the difference of separately calculated medians.

## 9. Contrary evidence and interpretation

Cases not above the comparator: Pakistan, Thailand, Senegal, Côte d'Ivoire. They remain visible in red. Positive post-growth does not itself imply acceleration, and neither implies causation. The modest median excess crosses zero under some date shifts; removing China changes the median sign. This limits confident growth claims.

Thailand’s financial crisis and Côte d’Ivoire’s instability/conflict are documented alternative explanations; China/India's wider reform packages are also relevant. Those alternatives are not estimated contributions and do not explain away contrary evidence by assertion. The data do not identify an income gain to export to Nepal.

## 10. Robustness actually completed

- Every reform year shifted−2…+2, with unavailable outcome endpoints removed from denominators rather than counted as failures.
- Five-year post-window.
- Excluding China; excluding both WAEMU countries; retaining one WAEMU country at a time.
- WAEMU completion-year2000 rather than national onset1998.
- Fixed-membership event median.
- Twelve Bangladesh/Kenya timing combinations, all explicitly assumed.
- Threshold15/20/25 policy screens, with outcome summaries restricted to the dated subset and the number without precise dates reported. This is not falsely presented as a fully sourced expanded sample at15pp.

Exact tables appear below. No regression or advanced causal model is claimed. Sensitivity checks expose dependence; they do not create identification.

## 11. Figures, presentation and one recommendation

Eight figures are generated only by the notebook, with PNG/PDF and exact CSV data exports. The actual notebook has26 cells,17 executable. Source/input/missingness checks run before chart generation. A programmatically generated index maps figures to notebook positions, slide pages and files; raw full-period income Figure3 sits on appendix page12. Ten content slides carry the full argument; six appendix pages provide verification. An editable PowerPoint and speaker notes are supplied.

The sole recommendation is Modification of Schedule1 of Nepal's Customs Tariff Act2081 as amended: cap standard non-preferential ad valorem basic duties in HS25–97 at20% over three budgets, retaining lower rates. The Ministry of Finance proposes, Parliament enacts and Customs administers. This targets basic duties; it does not propose changes to VAT/excise/preferences/prohibitions or specific/mixed duties.

The20% ceiling and three-budget period are proposed choices, not estimated optimal parameters. Current official FY2083/84 tariff compilation was downloaded and visually checked: PDF page4 describes the legal basis and other charges, page5 identifies Schedule1, and page215 shows higher non-agricultural basic duties. The original Tariff Act’s first page identifies the enacted statute and Federal Parliament. The underlying law prevails over any compilation error.

Mechanism: lower import tax wedges could widen choice and competition and reduce affected input costs, depending on pass-through and market structure. Figures1–2 supply policy context;4–7 limit the outcome inference;8 shows Nepal’s different historical starting point. Mean tariffs do not reveal statutory peaks or a Nepal fiscal cost. There is no estimated gain, affected-line count, job effect or revenue prediction.

Liberty rationale: predictable rules and wider voluntary exchange; recognise costs borne by purchasers under protection. Strongest objection: potential revenue losses and concentrated adjustment costs for protected firms/workers. A transition changes timing, not existence of costs. Current descriptive evidence does not by itself establish the recommended cap’s welfare benefit.

## 12. Reproducibility and source audit

The original418-file archive was inventoried in the earlier audit. Five unusable downloads were identified (two empty files and three error/challenge responses). Extraction/readability is not claim verification. New sources are separately archived in `research/sources/final/`, with response/format metadata; failed responses must not be cited as documents. Some relevant PDFs are scanned, so original source pages were rendered and visually inspected, with verification images retained.

The rebuilt notebook is self-contained, uses hash-checked original inputs, validates merges and endpoint denominators, and exports all figure data. It passed an empty-directory run without external data files. This verifies embedded restoration and calculations in the recorded environment, not every future software environment or public sharing permissions. Requirements and full dependency lock are supplied. All computational changes were tested after corrections; no failed run is described as a successful one.

## 13. Source and AI use

`research/sources.md` and the source register supply publishers, titles, versions, public URLs, access dates and source locations. Only the free chapter excerpt is cited for the China book; no paywall is required. Policy-source dates are manually researched metadata; numerical chart outcomes and indicators come from the required datasets through the notebook.

Codex assisted with data inspection, coding/debugging, reproducibility, public-source research, documentation, figure generation and presentation assembly. Participant review has not been asserted. Suwarna Pyakurel remains responsible for understanding and reviewing the submission. Solo status means no team contribution statement is needed.

## 14. What remains outside the completed local work

- Participant reviews the question, data, recommendation, cost tradeoff and disclosure and can explain them.
- Organiser confirms the panel/subcomponent interpretation and accepted provided dataset release.
- Dataset declaration is submitted/approved; approval evidence retained.
- Exact deadline confirmed.
- Any shared link tested signed-out, or local bundle accepted through the entry form.
- Participant submits the approved materials.

These are real pending items; approval, deadline and submission are not inferred from silence. See `SUBMISSION_CHECKLIST.md`. No extra dataset or more complicated statistical model is necessary to make the current descriptive design reviewable.

## 15. Exact current records and outputs

The following blocks are copied programmatically from the authoritative current files; they are not manually retyped chart values.

### Reform-date ledger

```csv
iso3,country,reform_year,main_sample,effective_date_basis,policy_episode,source_location,source_url,dating_limit,source_id,archive_stem,accessed
IND,India,1991,1,1991-07-25,July 1991 tariff peak reduction,Budget speech paragraphs 107 and 148; PDF pages 24 and 31,https://www.indiabudget.gov.in/doc/bspeech/bs199192.pdf,Paragraph148 states customs/excise changes effective25 July1991; wider reform package concurrent,IND1991,ind1991,2026-10-16
CHN,China,1992,1,1992-01 and 1992-12,Broad reductions across tariff codes,"The Chinese Trade-Administration System, printed page 5; PDF page 3",https://www.piie.com/publications/chapters_preview/31/2iie2474.pdf,Documented implementation months; earlier and later reforms also exist,CHN1992,chn1992,2026-10-16
MUS,Mauritius,1994,1,1994 (year only),Tariff consolidation and broad duty reductions,"WTO 1995 review, Secretariat: Recent evolution",https://www.wto.org/english/tratop_e/tpr_e/tp015_e.htm,Implementation year documented; month not established; later 2005 programme is separate,MUS1994,mus1995,2026-10-16
THA,Thailand,1995,1,1995-01,Broad tariff restructuring phase,"WTO 1995 review, press release tariff paragraph and Recent evolution",https://www.wto.org/english/tratop_e/tpr_e/tp021_e.htm,Programme began January 1995; phase-in continued to 1997,THA1995,given_tha1995,2026-10-16
PHL,Philippines,1995,1,1995-08-28,Executive Order 264 industrial tariff programme,"Executive Order 288, first WHEREAS recital",https://lawphil.net/executive/execord/eo1995/eo_288_1995.html,Effective date of EO264 stated retrospectively in EO288,PHL1995,phl1995,2026-10-16
PAK,Pakistan,1997,1,1997 (year only),Maximum tariff cut under incoming government,"SPDC Evaluation of Federal Budget 1999-2000, PDF page 33, tax-reform discussion",https://spdc.org.pk/assets/upload/5f4efd6fbdd6c-Evaluation%20of%20the%20Federal%20Budget%201999%202000-RR-23.pdf,Implementation year documented by open institutional retrospective; month not established,PAK1997,pak1997,2026-10-16
CIV,Côte d'Ivoire,1998,1,1998-03,First implemented tariff reduction in WAEMU transition,"IMF Country Report 00/107, printed page 18, Box 2; PDF page 19 (visually inspected)",https://www.imf.org/external/pubs/ft/scr/2000/cr00107.pdf,Transition began March 1998; full CET in January 2000; shared regional reform,CIV1998,civ2000,2026-10-16
SEN,Senegal,1998,1,1998-04,National tariff streamlining ahead of WAEMU CET,"IMF Country Report 99/5, printed page 32, Table 27; PDF page 33 (visually inspected)",https://www.imf.org/external/pubs/ft/scr/1999/cr9905.pdf,National phase April 1998; regional transition July 1998; full CET January 2000,SEN1998,sen1999,2026-10-16
BGD,Bangladesh,1991,0,Not assigned for main sample,Tariff-reduction programme accelerated in 1991,"GATT BOP/W/160, paragraph 5; WTO 2000 government report tariff table",https://www.wto.org/gatt_docs/English/SULPDF/90080791.pdf,"Main event omitted: acceleration/start, fiscal label and discrete legal episode differ; sensitivity years 1991 1992 1994 1995",BGDtiming,bgd_gatt1995,2026-10-16
KEN,Kenya,1993,0,Not assigned for main sample,Structural/trade liberalisation from mid-1993,"Kenya Policy Framework Paper 1996-1998, paragraph 6; PDF page 5",https://www.imf.org/external/np/pfp/kenya/kenya.pdf,Main event omitted: broad programme start is not a tariff-specific effective year; sensitivity years 1993 1994 1995,KENtiming,ken1996,2026-10-16
```

### Main country results

```csv
iso3,country,reform_year,pre_years_available,pre5_cagr_pct,available_pre_cagr_pct,post_cagr_pct,benchmark_cagr_pct,benchmark_n,excess_pp,acceleration_pp
CHN,China,1992,2,,10.125846740161016,8.713756519524129,1.7409657057605887,148,6.97279081376354,
IND,India,1991,1,,-1.084806347368239,3.9702849023039777,1.697083495952001,148,2.2732014063519768,
MUS,Mauritius,1994,4,,3.5795596182486733,3.8673756740190246,2.3512177599023465,149,1.516157914116678,
PHL,Philippines,1995,5,1.5236117532655857,1.5236117532655857,2.755827070679473,2.361872603015458,152,0.393954467664015,1.2322153174138872
PAK,Pakistan,1997,5,0.11176975429825209,0.11176975429825209,2.332799228299365,2.5998415645008377,152,-0.2670423362014729,2.2210294740011127
THA,Thailand,1995,5,6.73109502169027,6.73109502169027,1.6519825806541322,2.361872603015458,152,-0.7098900223613258,-5.079112441036138
SEN,Senegal,1998,5,1.1023867553929811,1.1023867553929811,1.2875870166008996,2.591014542966674,152,-1.3034275263657746,0.18520026120791844
CIV,Côte d'Ivoire,1998,5,2.2462216143517733,2.2462216143517733,-1.7714724329107145,2.591014542966674,152,-4.362486975877388,-4.017694047262488
```

### Sensitivity results

```csv
check,missing_post,n,above,median_excess_pp,median_post_cagr_pct,n_post_positive,full_pre_n,accelerated,screen_n,without_precise_date
date shift -2,1,7,4,0.21419576303192134,2.0911727215670695,6,3,2,,
date shift -1,0,8,4,-0.011122972705335243,2.3400947871970113,7,3,2,,
date shift +0,0,8,4,0.06345606573127105,2.544313149489419,7,5,3,,
date shift +1,0,8,3,-0.17665520372300292,2.3867272021142694,7,6,2,,
date shift +2,0,8,4,0.06473243160800557,2.6318727677263287,7,6,2,,
five-year post,0,8,4,0.10150960057970226,2.204764858863739,6,5,3,,
without China,0,7,3,-0.2670423362014729,2.332799228299365,6,5,3,,
without both WAEMU,0,6,4,0.9550561908903465,3.311601372349249,6,3,2,,
one WAEMU: retain CIV,0,7,4,0.393954467664015,2.755827070679473,6,4,2,,
one WAEMU: retain SEN,0,7,4,0.393954467664015,2.755827070679473,7,4,3,,
WAEMU completion 2000,0,8,4,0.06345606573127105,2.544313149489419,7,5,2,,
cut >= 15 pp (dated subset),0,8,4,0.06345606573127105,2.544313149489419,7,5,3,15.0,7.0
cut >= 20 pp (dated subset),0,8,4,0.06345606573127105,2.544313149489419,7,5,3,10.0,2.0
cut >= 25 pp (dated subset),0,5,3,1.516157914116678,3.8673756740190246,5,2,1,6.0,1.0
```

### Bangladesh/Kenya timing grid

```csv
BGD_assumed_year,KEN_assumed_year,n,above,median_excess_pp,median_post_cagr_pct,n_post_positive,full_pre_n,accelerated
1991,1993,10,5,0.06345606573127105,2.544313149489419,9,5,3
1991,1994,10,5,0.06345606573127105,2.544313149489419,9,5,3
1991,1995,10,5,0.06345606573127105,2.544313149489419,9,6,4
1992,1993,10,5,0.06345606573127105,2.544313149489419,9,5,3
1992,1994,10,5,0.06345606573127105,2.544313149489419,9,5,3
1992,1995,10,5,0.06345606573127105,2.544313149489419,9,6,4
1994,1993,10,5,0.06345606573127105,2.544313149489419,9,5,3
1994,1994,10,5,0.06345606573127105,2.544313149489419,9,5,3
1994,1995,10,5,0.06345606573127105,2.544313149489419,9,6,4
1995,1993,10,5,0.06345606573127105,2.544313149489419,9,6,4
1995,1994,10,5,0.06345606573127105,2.544313149489419,9,6,4
1995,1995,10,5,0.06345606573127105,2.544313149489419,9,7,5
```

### Event-window coverage

```csv
iso3,first_event,last_event,n_gni,n_tariff,n_panel
CHN,-2,10,13,5,5
CIV,-5,10,16,10,10
IND,-1,10,12,4,4
MUS,-4,10,15,7,7
PAK,-5,10,16,9,9
PHL,-5,10,16,8,8
SEN,-5,10,16,10,10
THA,-5,10,16,8,8
```

### Final chart index

```csv
figure,slide,title,data,file,notebook_cell
Fig1,3,All ten screened countries: observed tariff histories,outputs/Fig1_data.csv,figures/Fig1.png,17
Fig2,4,Broader trade institutions: the chain-linked EFW panel,outputs/Fig2_data.csv,figures/Fig2.png,18
Fig3,12,Raw income histories before making event comparisons,outputs/Fig3_data.csv,figures/Fig3.png,19
Fig4,5,Income around the documented tariff-cutting episodes,outputs/Fig4_data.csv,figures/Fig4.png,20
Fig5,6,"Income growth: before, after, and in other countries",outputs/Fig5_data.csv,figures/Fig5.png,21
Fig6,7,Which countries exceeded the broad comparator?,outputs/Fig6_data.csv,figures/Fig6.png,22
Fig7,7,Timing sensitivity: the denominator follows valid data,outputs/Fig7_data.csv,figures/Fig7.png,23
Fig8,9,Nepal: a different starting point from the largest cutters,outputs/Fig8_data.csv,figures/Fig8.png,24
```

### Computed summary

```json
{
  "n": 8,
  "above": 4,
  "median_excess_pp": 0.06345606573127105,
  "median_post_cagr_pct": 2.544313149489419,
  "n_post_positive": 7,
  "full_pre_n": 5,
  "accelerated": 3,
  "timing_grid_above_min": 5,
  "timing_grid_above_max": 5,
  "timing_grid_median_min": 0.06345606573127105,
  "timing_grid_median_max": 0.06345606573127105,
  "balanced_n": 5,
  "participant": "Suwarna Pyakurel",
  "main_cases": [
    "IND",
    "CHN",
    "MUS",
    "THA",
    "PHL",
    "PAK",
    "CIV",
    "SEN"
  ],
  "calendar_event_range": [
    1990,
    2008
  ],
  "benchmark_valid_n_range": [
    148,
    152
  ],
  "not_above": [
    "Pakistan",
    "Thailand",
    "Senegal",
    "C\u00f4te d'Ivoire"
  ],
  "positive_cases": [
    "China",
    "India",
    "Mauritius",
    "Philippines"
  ],
  "nepal_tariff_latest_year": 2024,
  "nepal_tariff_latest_pct": 12.9
}
```

### Computational and external flags

```json
{
  "raw_hashes_verified": true,
  "unique_source_keys": true,
  "validated_merges": true,
  "full_post_endpoints": true,
  "no_interpolation": true,
  "all_screened_visible": true,
  "all_main_contrary_visible": true,
  "n_main": 8,
  "dates_have_sources": true,
  "embedded_inputs": true,
  "organiser_scope_approved": null,
  "declaration_approved": null
}
```

### Empty-directory verification

```json
{
  "date": "2026-10-16",
  "fresh_directory": "/tmp/ldd-judge-3wyvs3s7",
  "input_files_present_before_execution": false,
  "embedded_originals_restored_and_hash_matched": true,
  "all_code_cells_executed": true,
  "n_code_cells": 17,
  "errors": 0
}
```

## 16. Exact current notebook source template

This readable template is expanded by `research/build_notebook.py`: embedded-input and date placeholders become the actual compressed original files and ledger in the notebook. Numerical calculations run inside the resulting notebook; no external analysis module is imported.

```python
# %% md
# Liberty Data Drive 2026 — reproducible working file
Participant: **Suwarna Pyakurel (solo)**. Prepared 16 October 2026.

Question: Among eight countries with documented tariff-cutting episodes in 1991–1998 (India, China, Mauritius, Thailand, Philippines, Pakistan, Côte d'Ivoire and Senegal), what happened to GNI per capita during the following ten years, and what does this suggest for Nepal's tariff schedule?

The original numerical screen covers ten countries: mean tariff decline ≥20 percentage points in 1995–2005. Bangladesh and Kenya remain in the screening figures and timing sensitivity, but are not assigned precise main-sample tariff dates. This is descriptive evidence, not a causal estimate. Date selection was documented after exploratory outcomes had been viewed; it is not a preregistered study.

Both supplied raw datasets are embedded below so the notebook can run without uploads or network data access. The EFW chain-linked panel's Area 4 is analysed separately from raw tariff subcomponents in Ratings; raw tariffs are not described as chain-linked. Organiser acceptance of this combined interpretation and exact supplied release remains an external submission requirement.
# %% code
import sys, subprocess, importlib.util, pathlib, json, hashlib, base64, zlib, io, re
required = {'numpy':'numpy','pandas':'pandas','matplotlib':'matplotlib','openpyxl':'openpyxl'}
missing = [pkg for mod,pkg in required.items() if importlib.util.find_spec(mod) is None]
if missing:
    subprocess.check_call([sys.executable,'-m','pip','install',*missing])
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from IPython.display import display
ROOT = pathlib.Path.cwd()
for folder in ('data','figures','outputs'):
    (ROOT/folder).mkdir(exist_ok=True)
EMBEDDED = __EMBEDDED_INPUTS__
for filename, payload in EMBEDDED.items():
    target = ROOT/filename
    if not target.exists():
        target.write_bytes(zlib.decompress(base64.b64decode(payload['content'])))
    assert hashlib.sha256(target.read_bytes()).hexdigest() == payload['sha256'], f'Unexpected input: {filename}'
DATES_CSV = __DATES_LITERAL__
dates = pd.read_csv(io.StringIO(DATES_CSV))
main = dates[dates.main_sample.eq(1)].copy()
assert dates.iso3.is_unique and main.reform_year.notna().all() and len(main)>=3
main['reform_year'] = main.reform_year.astype(int)
MAIN = list(main.iso3)
DATE = main.set_index('iso3').reform_year.to_dict()
print('Embedded input hashes verified. Main sample:',len(MAIN),'Screened cases:',len(dates))
# %% md
## 1. Load and inspect the two fixed datasets
The Ratings sheet supplies raw mean tariffs (`data.10`, %) next to rating 4Aii. The panel sheet supplies chain-linked Area 4 (0–10). We load both, without replacing either with the overall freedom index. The supplied workbook spans 1970–2024; exact release identity must match the organiser declaration. UNDP's HDR25 file spans 1990–2023.
# %% code
EFW = ROOT/'data/EFW_original.xlsx'
UNDP = ROOT/'data/UNDP_original.csv'
ratings = pd.read_excel(EFW,sheet_name='EFW Ratings',header=3)
ratings.columns = ratings.columns.str.strip()
ratings = ratings[pd.to_numeric(ratings.Year,errors='coerce').notna()].copy()
ratings['Year'] = ratings.Year.astype(int)
assert not ratings.duplicated(['ISO_Code','Year']).any()
col = ratings.columns.get_loc('4Aii  Mean tariff rate')
assert ratings.columns[col+1]=='data.10'
ratings['tariff_pct'] = pd.to_numeric(ratings['data.10'],errors='coerce')
assert ratings.tariff_pct.dropna().ge(0).all()
policy = ratings[['ISO_Code','Countries','Year','tariff_pct']].rename(columns={'ISO_Code':'iso3','Countries':'country','Year':'year'})
linked = pd.read_excel(EFW,sheet_name='EFW Panel Dataset')
assert not linked.duplicated(['ISO_Code','Year']).any()
linked = linked.rename(columns={'ISO_Code':'iso3','Year':'year','Area 4: Freedom to Trade Internationally':'trade_panel'})
linked['trade_panel'] = pd.to_numeric(linked.trade_panel,errors='coerce')
assert linked.trade_panel.dropna().between(0,10).all()
wide = pd.read_csv(UNDP,encoding='latin1')
assert wide.iso3.is_unique
aggregate = ~wide.iso3.str.fullmatch('[A-Z]{3}')
print('EFW records:',len(policy),'jurisdictions:',policy.iso3.nunique(),'years:',policy.year.min(),policy.year.max())
print('UNDP country/territory rows:',int((~aggregate).sum()),'aggregates excluded:',int(aggregate.sum()))
wide = wide[~aggregate].copy()
parts=[]
for measure in ['gnipc','le','eys','mys']:
    cols=[c for c in wide.columns if re.fullmatch(measure+r'_\d{4}',c)]
    m=wide.melt(id_vars=['iso3','country'],value_vars=cols,var_name='variable',value_name=measure)
    m['year']=m.variable.str[-4:].astype(int)
    m[measure]=pd.to_numeric(m[measure],errors='coerce')
    parts.append(m.set_index(['iso3','country','year'])[measure])
undp=pd.concat(parts,axis=1).reset_index()
assert not undp.duplicated(['iso3','year']).any()
NAME=wide.set_index('iso3').country.to_dict()
common=set(policy.iso3)&set(undp.iso3)
print('Matched codes:',len(common),'EFW-only:',sorted(set(policy.iso3)-set(undp.iso3)))
country_map=policy[['iso3','country']].drop_duplicates().rename(columns={'country':'efw_name'}).merge(wide[['iso3','country']].rename(columns={'country':'undp_name'}),on='iso3',how='outer',validate='one_to_one',indicator=True)
country_map.to_csv(ROOT/'outputs/country_mapping.csv',index=False)
display(country_map[country_map._merge.ne('both')])
missingness=undp.groupby('year')[['gnipc','le','eys','mys']].count()
missingness.to_csv(ROOT/'outputs/outcome_coverage.csv')
display(missingness.loc[[1990,1995,2000,2005,2010,2023]])
# %% md
## 2. Preserve topic exploration, then apply the tariff screen
An exploratory scan considered multiple EFW indicators. The final screen uses raw mean tariffs rather than a floored rating: a fall of at least 20 percentage points from 1995 to 2005, with both tariff observations and some UNDP GNI data. Actual event-window coverage is checked separately. This is a transparent descriptive selection, not random assignment; earlier programme starts and the later selection window are an acknowledged design limitation.
# %% code
scan_rows=[]
for name in ['4Aii  Mean tariff rate','4A  Tariffs','4C  Black market exchange rates','2C  Property rights','2F Contracts','Area 4 Freedom to trade internationally']:
    if name not in ratings: continue
    x=ratings.pivot(index='ISO_Code',columns='Year',values=name).apply(pd.to_numeric,errors='coerce')
    d=(x[2005]-x[1995]).dropna()
    scan_rows.append({'indicator':name,'n_both_years':len(d),'n_improved_2_points':int(d.ge(2).sum())})
scan=pd.DataFrame(scan_rows);display(scan);scan.to_csv(ROOT/'outputs/topic_scan.csv',index=False)
P=policy.pivot(index='iso3',columns='year',values='tariff_pct')
has_gni=set(undp.loc[undp.gnipc.notna(),'iso3'])
screen=pd.DataFrame({'tariff_1995_pct':P[1995],'tariff_2005_pct':P[2005]}).dropna()
screen=screen[screen.index.isin(has_gni)]
screen['change_pp']=screen.tariff_2005_pct-screen.tariff_1995_pct
screen['country']=[NAME.get(c,c) for c in screen.index]
screen['selected']=screen.change_pp.le(-20)
selected=screen[screen.selected].sort_values('change_pp')
assert set(selected.index)==set(dates.iso3), 'Screen/date coverage mismatch'
assert set(MAIN)<=set(selected.index)
ALL=list(selected.index)
BENCH=set(common)-set(ALL)
print('Eligible screen:',len(screen),'Selected:',len(selected),'Main dated sample:',len(MAIN))
display(selected)
display(screen[screen.change_pp.between(-20,-15,inclusive='right')].sort_values('change_pp'))
screen.to_csv(ROOT/'outputs/selection_all_eligible.csv')
selected.to_csv(ROOT/'outputs/selected_cases.csv')
# %% md
## 3. Policy evidence and reform dating
One dating logic: year of an implemented broad tariff-cutting episode identified in an open source; not the first liberalisation ever and not an EFW score jump. We use the start of the documented phase rather than its final completion. Announcement-only and year-level sources have less temporal precision than legislation; ±2-year shifts and completion dates address this limitation, not eliminate it.

India 1991; China 1992; Mauritius 1994; Thailand/Philippines 1995; Pakistan 1997; Côte d'Ivoire/Senegal 1998. Mauritius and Thailand are retained, correcting earlier proposed exclusions. Senegal's national phase began April 1998 and Côte d'Ivoire's March 1998; full WAEMU CET in January 2000 is an alternative date. They are two countries but one regional reform family.

Bangladesh's programme acceleration and Kenya's broad programme onset do not identify the same tariff-only effective event precisely enough for the main sample. Both remain in screening figures and a separate timing grid. The main-sample decision is based on documentary precision, after prior exploratory outcomes had already been inspected. No country is removed for a weak result.
# %% code
display(dates[['iso3','country','reform_year','main_sample','effective_date_basis','dating_limit','source_location']])
assert dates.source_url.notna().all() and dates.source_location.notna().all()
assert dates.loc[dates.main_sample.eq(1),'effective_date_basis'].ne('Not assigned for main sample').all()
dates.to_csv(ROOT/'outputs/reform_date_snapshot.csv',index=False)
# %% md
## 4. Build the event panel
`event_time = year − reform_year`, window −5…+10, clipped to observed UNDP years. Missing years are not interpolated. The annual reform year includes any pre-implementation months; this is an annual descriptive convention.
# %% code
panel=undp[undp.iso3.isin(MAIN)].merge(main[['iso3','reform_year']],on='iso3',validate='many_to_one')
panel['event_time']=panel.year-panel.reform_year
panel=panel[panel.event_time.between(-5,10)].copy()
panel=panel.merge(policy[['iso3','year','tariff_pct']],on=['iso3','year'],how='left',validate='one_to_one')
panel=panel.merge(linked[['iso3','year','trade_panel']],on=['iso3','year'],how='left',validate='one_to_one')
assert not panel.duplicated(['iso3','year']).any()
base=panel[panel.event_time.eq(0)].set_index('iso3')
assert set(base.index)==set(MAIN) and base.gnipc.gt(0).all()
panel['gni_index']=100*panel.gnipc/panel.iso3.map(base.gnipc)
panel['le_gain']=panel['le']-panel.iso3.map(base['le'])
coverage=panel.groupby('iso3').agg(first_event=('event_time','min'),last_event=('event_time','max'),n_gni=('gnipc','count'),n_tariff=('tariff_pct','count'),n_panel=('trade_panel','count'))
assert coverage.last_event.eq(10).all()
display(coverage)
coverage.to_csv(ROOT/'outputs/event_coverage.csv')
panel.to_csv(ROOT/'outputs/event_panel.csv',index=False)
# %% md
## 5. Growth and a broad comparator
CAGR = `100 × [(GNI_end/GNI_start)^(1/elapsed_years) − 1]`.
Main pre-growth requires a **full five-year window**; available-history growth is exported separately and never substituted for five-year growth. Missing values are not zero. Ten-year post-growth runs from event 0 to +10. Acceleration compares post-CAGR to full-five-year pre-CAGR only.

Comparator = median valid CAGR of other matched EFW jurisdictions over the same calendar years, excluding all ten screened cases. Count the valid endpoint pairs separately for each window. This is an unweighted contextual comparator, not an untreated/matched control or causal counterfactual. A country that did not pass our screen may still have reformed.
# %% code
G=undp.pivot(index='iso3',columns='year',values='gnipc')
def cagr(iso,start,end):
    if end<=start or start not in G.columns or end not in G.columns: return np.nan
    a,b=G.loc[iso,[start,end]]
    return 100*((b/a)**(1/(end-start))-1) if pd.notna(a) and pd.notna(b) and a>0 and b>0 else np.nan
def benchmark(start,end):
    values=pd.Series({iso:cagr(iso,start,end) for iso in sorted(BENCH)}).dropna()
    return (float(values.median()) if len(values) else np.nan,len(values))
def results(date_map,post=10):
    rows=[]
    for iso,year in date_map.items():
        year=int(year);b,n=benchmark(year,year+post)
        pst=cagr(iso,year,year+post);pre=cagr(iso,year-5,year)
        available=max(1990,year-5)
        rows.append({'iso3':iso,'country':NAME[iso],'reform_year':year,'pre_years_available':max(0,year-available),
          'pre5_cagr_pct':pre,'available_pre_cagr_pct':cagr(iso,available,year),'post_cagr_pct':pst,
          'benchmark_cagr_pct':b,'benchmark_n':n,'excess_pp':pst-b,'acceleration_pp':pst-pre})
    return pd.DataFrame(rows)
res=results(DATE).sort_values('excess_pp',ascending=False).reset_index(drop=True)
assert res.post_cagr_pct.notna().all() and res.excess_pp.notna().all()
assert res.benchmark_n.gt(0).all()
assert res.loc[res.pre_years_available.lt(5),'pre5_cagr_pct'].isna().all()
display(res.round(3))
res.to_csv(ROOT/'outputs/growth_results.csv',index=False)
def stats(frame):
    valid=frame[frame.excess_pp.notna()]
    pre=frame[frame.pre5_cagr_pct.notna()]
    return {'n':len(valid),'above':int(valid.excess_pp.gt(0).sum()),'median_excess_pp':float(valid.excess_pp.median()),
      'median_post_cagr_pct':float(valid.post_cagr_pct.median()),'n_post_positive':int(valid.post_cagr_pct.gt(0).sum()),
      'full_pre_n':len(pre),'accelerated':int(pre.acceleration_pp.gt(0).sum())}
summary=stats(res)
print(json.dumps(summary,indent=2))
print('Cases not above comparator:',', '.join(res.loc[res.excess_pp.le(0),'country']))
# %% md
## 6. Robustness and timing uncertainty
All shifts use the same eight-country date map; invalid endpoint pairs are reported as unavailable, excluded from denominators rather than counted as unsuccessful. WAEMU dependence and China are checked without changing the full-sample headline. Bangladesh/Kenya enter only a separate grid of plausible programme-year conventions; those dates remain assumptions. Threshold sensitivity is limited to countries with documented dates; newly screened countries without dates remain explicitly unresolved.
# %% code
rob=[]
for shift in [-2,-1,0,1,2]:
    r=results({c:y+shift for c,y in DATE.items()})
    rob.append({'check':f'date shift {shift:+d}','missing_post':int(r.excess_pp.isna().sum()),**stats(r)})
rob.append({'check':'five-year post','missing_post':0,**stats(results(DATE,post=5))})
rob.append({'check':'without China','missing_post':0,**stats(res[res.iso3.ne('CHN')])})
rob.append({'check':'without both WAEMU','missing_post':0,**stats(res[~res.iso3.isin(['CIV','SEN'])])})
rob.append({'check':'one WAEMU: retain CIV','missing_post':0,**stats(res[res.iso3.ne('SEN')])})
rob.append({'check':'one WAEMU: retain SEN','missing_post':0,**stats(res[res.iso3.ne('CIV')])})
alternate=DATE.copy();alternate.update({'CIV':2000,'SEN':2000})
rob.append({'check':'WAEMU completion 2000','missing_post':0,**stats(results(alternate))})
for threshold in [15,20,25]:
    eligible=set(screen[screen.change_pp.le(-threshold)].index)
    known=res[res.iso3.isin(eligible)]
    rob.append({'check':f'cut >= {threshold} pp (dated subset)','missing_post':0,'screen_n':len(eligible),'without_precise_date':len(eligible-set(MAIN)),**stats(known)})
rob=pd.DataFrame(rob);display(rob.round(3));rob.to_csv(ROOT/'outputs/robustness.csv',index=False)
timing=[]
for bgd in [1991,1992,1994,1995]:
    for ken in [1993,1994,1995]:
        mapping=DATE|{'BGD':bgd,'KEN':ken}
        timing.append({'BGD_assumed_year':bgd,'KEN_assumed_year':ken,**stats(results(mapping))})
timing=pd.DataFrame(timing);display(timing.round(3));timing.to_csv(ROOT/'outputs/uncertain_timing_grid.csv',index=False)
counts=panel.groupby('event_time').gni_index.count()
balanced_iso=list(coverage[coverage.first_event.eq(-5)].index)
print('Balanced full-window subset:',balanced_iso)
summary['timing_grid_above_min']=int(timing.above.min());summary['timing_grid_above_max']=int(timing.above.max())
summary['timing_grid_median_min']=float(timing.median_excess_pp.min());summary['timing_grid_median_max']=float(timing.median_excess_pp.max())
summary['balanced_n']=len(balanced_iso)
# %% md
## 7. Final charts and exact chart-data exports
All chart values below come from the supplied files through these cells. Each figure exports PNG/PDF and a table of the exact chart data. Dates are documentary metadata, not invented outcome data. Sources, units, years, sample sizes and exclusions appear on each chart. Plot connectors do not fill missing observations. Bars include zero. No dual axes.
# %% code
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.18,'figure.dpi':110})
BLUE='#176B87';RED='#B33F46';GOLD='#C28A24';INK='#162D3D';GREY='#89959D'
COLORS=dict(zip(MAIN,plt.cm.tab10(np.linspace(0,.9,len(MAIN)))))
INDEX=[]
def finish(fig,number,title,note,data,slide):
    fig.suptitle(f'Figure {number}. {title}',x=.015,y=.99,ha='left',fontsize=14,fontweight='bold',color=INK)
    fig.text(.015,.015,note,ha='left',va='bottom',fontsize=8,color='#3D4F59',wrap=True)
    fig.tight_layout(rect=(0,.13,1,.92))
    filename=f'Fig{number}'
    fig.savefig(ROOT/'figures'/f'{filename}.png',dpi=180,facecolor='white')
    fig.savefig(ROOT/'figures'/f'{filename}.pdf',facecolor='white')
    data.to_csv(ROOT/'outputs'/f'{filename}_data.csv',index=False)
    INDEX.append({'figure':filename,'slide':slide,'title':title,'data':f'outputs/{filename}_data.csv','file':f'figures/{filename}.png'})
    display(fig);plt.close(fig)
# %% code
# FIGURE 1: include every screened country, even those without a main date.
d=policy[policy.iso3.isin(ALL)&policy.tariff_pct.notna()].sort_values(['iso3','year'])
fig,axes=plt.subplots(2,5,figsize=(14,6.4),sharey=True)
for ax,iso in zip(axes.flat,ALL):
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.tariff_pct,'o-',lw=1.3,ms=2.5,color=BLUE if iso in MAIN else GREY)
    if iso in DATE:ax.axvline(DATE[iso],ls='--',color=RED,lw=1)
    ax.set_title(NAME[iso]+(' *' if iso not in MAIN else ''),fontsize=10)
    ax.set_ylim(bottom=0);ax.set_xlabel('Year')
for ax in axes[:,0]:ax.set_ylabel('Mean tariff (%)')
finish(fig,1,'All ten screened countries: observed tariff histories',
 f'Fraser EFW Ratings, raw 4Aii (%); observed {d.year.min()}–{d.year.max()}; n=10 screened. Dashed=episode year. *BGD/KEN: no main event date; retained.\nScreen: decline ≥20 pp, 1995–2005. Five-yearly before 2000; annual afterwards. Lines connect observations; no interpolation.',d,3)
# %% code
# FIGURE 2: required chain-linked policy context, separate from raw tariffs.
d=linked[linked.iso3.isin(MAIN)&linked.trade_panel.notna()][['iso3','year','trade_panel']].sort_values(['iso3','year'])
fig,axes=plt.subplots(2,4,figsize=(13,6),sharey=True)
for ax,iso in zip(axes.flat,MAIN):
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.trade_panel,'o-',ms=2,lw=1.4,color=BLUE);ax.axvline(DATE[iso],color=RED,ls='--',lw=1)
    ax.set_title(NAME[iso],fontsize=10);ax.set_ylim(0,10);ax.set_xlabel('Year')
for ax in axes[:,0]:ax.set_ylabel('Chain-linked Area 4 (0–10)')
finish(fig,2,'Broader trade institutions: the chain-linked EFW panel',
 f'Fraser EFW Panel Dataset, Area 4 (higher=more freedom to trade); {d.year.min()}–{d.year.max()}; n=8 dated countries.\nDashed=episode year. BGD/KEN omitted from dated sample (timing precision). Area 4 includes non-tariff institutions; it is not a tariff-only measure.',d,4)
# %% code
# FIGURE 3: raw outcome inspection, full supplied UNDP period.
d=undp[undp.iso3.isin(ALL)][['iso3','year','gnipc']].sort_values(['iso3','year'])
fig,axes=plt.subplots(2,5,figsize=(14,6.4))
for ax,iso in zip(axes.flat,ALL):
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.gnipc,color=BLUE,lw=1.8)
    if iso in DATE:ax.axvline(DATE[iso],color=RED,ls='--',lw=1)
    ax.set_title(NAME[iso],fontsize=10);ax.set_xlabel('Year');ax.set_ylabel('GNI/person (2021 PPP$)',fontsize=8)
finish(fig,3,'Raw income histories before making event comparisons',
 'UNDP HDR25 components, GNI/person (2021 PPP$), 1990–2023; n=10 screened countries. Country panels use different labelled y-scales.\nDashed=dated episode where available. Later outcomes are context, not part of the ten-year event estimate. No interpolation.',d,12)
# %% code
# FIGURE 4: all-country and fixed-subset median; sample composition visible in data.
d=panel[['iso3','year','event_time','gni_index']].copy();fig,ax=plt.subplots(figsize=(10,5.8))
for iso in MAIN:
    s=d[d.iso3.eq(iso)].sort_values('event_time');ax.plot(s.event_time,s.gni_index,lw=1.1,alpha=.75,color=COLORS[iso],label=NAME[iso])
med=d.groupby('event_time').gni_index.median();cnt=d.groupby('event_time').gni_index.count()
ax.plot(med.index,med.values,color=INK,lw=3,label='Median (changing pre-sample)')
bal=d[d.iso3.isin(balanced_iso)].groupby('event_time').gni_index.median()
ax.plot(bal.index,bal.values,color=GOLD,lw=2,ls=':',label=f'Balanced median (n={len(balanced_iso)})')
ax.axvline(0,ls='--',color=RED);ax.axhline(100,color=GREY,lw=.8);ax.set_xlabel('Years from documented episode');ax.set_ylabel('GNI/person index (event 0=100)');ax.legend(ncol=2,fontsize=8,frameon=False)
d['event_year_n']=d.event_time.map(cnt)
finish(fig,4,'Income around the documented tariff-cutting episodes',
 f'UNDP HDR25 GNI/person; event −5…+10 ({panel.year.min()}–{panel.year.max()}); n=8 dated cases, preperiod n={cnt.min()}–{cnt.max()}.\nBGD/KEN: timing-only sensitivity. Normalisation forces 100 at zero. Dotted line fixes membership; no causal effect is estimated.',d,5)
# %% code
# FIGURE 5: honest prehistory; only full five-year pre-CAGR bars.
d=res.copy();fig,ax=plt.subplots(figsize=(11,5.6));x=np.arange(len(d));w=.26
ax.bar(x-w,d.pre5_cagr_pct,w,color=GREY,label='Full five-year pre-CAGR')
ax.bar(x,d.post_cagr_pct,w,color=BLUE,label='Ten-year post-CAGR')
ax.bar(x+w,d.benchmark_cagr_pct,w,color=GOLD,label='Same-years comparator median')
ax.axhline(0,color=INK,lw=.8);ax.set_xticks(x,d.country,rotation=25,ha='right');ax.set_ylabel('Annualised GNI/person growth (%)');ax.legend(fontsize=8,frameon=False)
finish(fig,5,'Income growth: before, after, and in other countries',
 f'UNDP HDR25; reform years 1991–1998, post endpoints 2001–2008; n=8, full five-year prehistory n={summary["full_pre_n"]}.\nMissing grey=unavailable, not zero. Comparator valid n={res.benchmark_n.min()}–{res.benchmark_n.max()}; all ten screened cases excluded from comparator.',d,6)
# %% code
# FIGURE 6: retain every contrary case.
d=res.sort_values('excess_pp');fig,ax=plt.subplots(figsize=(10,5.3))
ax.barh(d.country,d.excess_pp,color=[BLUE if v>0 else RED for v in d.excess_pp]);ax.axvline(0,color=INK,lw=.8)
ax.set_xlabel('Post-CAGR minus comparator CAGR (percentage points/year)')
finish(fig,6,'Which countries exceeded the broad comparator?',
 f'UNDP HDR25, ten-year windows beginning 1991–1998; n=8 dated cases. {summary["above"]}/{summary["n"]} above comparator; median excess {summary["median_excess_pp"]:+.2f} pp/year.\nRed=not above. BGD/KEN timing sensitivity separate. CIV/SEN share one regional reform; comparator is not a causal counterfactual.',d,7)
# %% code
# FIGURE 7: shifts and valid denominators; no treating unavailable as failure.
d=rob[rob['check'].str.startswith('date shift')].copy();fig,ax=plt.subplots(figsize=(9,5))
ax.bar(d['check'].str.replace('date shift ',''),d.above,color=BLUE);ax.set_ylim(0,len(MAIN)+1);ax.set_ylabel('Countries above comparator');ax.set_xlabel('Years added to every episode year')
for x,row in enumerate(d.itertuples()):ax.text(x,row.above+.12,f'{row.above}/{row.n}',ha='center')
finish(fig,7,'Timing sensitivity: the denominator follows valid data',
 'UNDP HDR25; shifted episode years 1989–2000, ten-year post windows. n=valid endpoint pairs printed above each bar.\nA pre-1990 start can be unavailable and is omitted from the denominator. Exact results and other checks: outputs/robustness.csv.',d,7)
# %% code
# FIGURE 8: Nepal context, not proof that the historical cases transport.
peers=['NPL','BGD','IND','PAK','LKA'];d=policy[policy.iso3.isin(peers)&policy.tariff_pct.notna()][['iso3','year','tariff_pct']].sort_values(['iso3','year'])
fig,ax=plt.subplots(figsize=(10,5))
for iso in peers:
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.tariff_pct,'o-',ms=2,lw=3 if iso=='NPL' else 1.2,label=NAME[iso])
ax.set_ylim(bottom=0);ax.set_ylabel('Mean tariff (%)');ax.set_xlabel('Year');ax.legend(frameon=False,ncol=3,fontsize=9)
finish(fig,8,'Nepal: a different starting point from the largest cutters',
 f'Fraser EFW Ratings, raw 4Aii (%), observed {d.year.min()}–{d.year.max()}; n=5 regional peers. Thick=Nepal.\nContext only: a mean tariff is not a maximum statutory rate or a current fiscal-cost estimate. No post-2024 tariff values are assumed.',d,9)
# %% md
## 8. Interpretation and one recommendation
The calculations describe heterogeneous trajectories. More income after reform, acceleration, and outperformance are different claims. Broader reforms, global conditions, financial crises and conflict can produce the same patterns. We cannot attribute a growth premium to tariffs or extrapolate a numerical gain to Nepal.

Recommendation wording and its current legal-source checks are maintained in `research/policy_recommendation.md` and the deck. Exactly one modification is proposed. The panel/subcomponent interpretation, supplied dataset release acceptance, declaration approval and deadline are external submission checks, not assertions made by this notebook.
# %% code
ci=pd.DataFrame(INDEX)
assert len(ci)==8 and ci.figure.is_unique
for row in ci.itertuples():
    assert (ROOT/row.file).exists() and (ROOT/row.data).exists()
summary['participant']='Suwarna Pyakurel'
summary['main_cases']=MAIN
summary['calendar_event_range']=[int(panel.year.min()),int(panel.year.max())]
summary['benchmark_valid_n_range']=[int(res.benchmark_n.min()),int(res.benchmark_n.max())]
summary['not_above']=list(res.loc[res.excess_pp.le(0),'country'])
summary['positive_cases']=list(res.loc[res.excess_pp.gt(0),'country'])
summary['nepal_tariff_latest_year']=int(policy.loc[policy.iso3.eq('NPL')&policy.tariff_pct.notna(),'year'].max())
summary['nepal_tariff_latest_pct']=float(policy.loc[policy.iso3.eq('NPL')&policy.year.eq(summary['nepal_tariff_latest_year']),'tariff_pct'].iloc[0])
(ROOT/'outputs/summary.json').write_text(json.dumps(summary,indent=2))
ci.to_csv(ROOT/'figures/chart_index.csv',index=False)
checks={'raw_hashes_verified':True,'unique_source_keys':True,'validated_merges':True,'full_post_endpoints':True,'no_interpolation':True,'all_screened_visible':True,'all_main_contrary_visible':True,'n_main':len(MAIN),'dates_have_sources':True,'embedded_inputs':True,'organiser_scope_approved':None,'declaration_approved':None}
(ROOT/'outputs/validation.json').write_text(json.dumps(checks,indent=2))
display(ci)
print('COMPUTATIONAL CHECKS PASSED. Organiser scope/release acceptance and declaration approval remain external pending checks.')

```

## 17. Source bibliography

# Sources — final analysis and policy research

Access date: 16 October 2026. Public URLs are the citation targets; local hashes identify archived evidence. Search snippets were not used to assign main dates.

## IND1991

Government of India, Ministry of Finance. **Union Budget Speech 1991–92**. 1991. [Public source](https://www.indiabudget.gov.in/doc/bspeech/bs199192.pdf) (accessed 2026-10-16).

Location/use: Budget speech paragraphs 107 and 148; PDF pages 24 and 31.

Archive: `research/sources/final/ind1991.pdf`. SHA-256: `9e20921dd7ec11367be7c7e584e3e7f9971a7de0db206363ad1d936c8b028791`.

## CHN1992

Zhang Yansheng, Wan Zhongxin and Zhang Shuguang; Institute for International Economics. **Measuring the Costs of Protection in China, chapter 2 (open excerpt)**. 1998. [Public source](https://www.piie.com/publications/chapters_preview/31/2iie2474.pdf) (accessed 2026-10-16).

Location/use: The Chinese Trade-Administration System, printed page 5; PDF page 3.

Archive: `research/sources/final/chn1992.pdf`. SHA-256: `436b608d08632335e50f3b2d155ee596920c0836c351d958d60d5e240179497f`.

## MUS1994

World Trade Organization. **Trade Policy Review: Mauritius, Secretariat summary**. 1995. [Public source](https://www.wto.org/english/tratop_e/tpr_e/tp015_e.htm) (accessed 2026-10-16).

Location/use: WTO 1995 review, Secretariat: Recent evolution.

Archive: `research/sources/final/mus1995.html`. SHA-256: `89583109934eb878fe7693503a60d064920e770f45b4f81afc8c9588e6f0c609`.

## THA1995

World Trade Organization. **Trade Policy Review: Thailand, Secretariat summary**. 1995. [Public source](https://www.wto.org/english/tratop_e/tpr_e/tp021_e.htm) (accessed 2026-10-16).

Location/use: WTO 1995 review, press release tariff paragraph and Recent evolution.

Archive: `research/sources/final/given_tha1995.html`. SHA-256: `1aeabf3ddbc8ce4d116feed0431daad23aaf7d68df27694eff5fbf82c64cef69`.

## PHL1995

President of the Philippines; Lawphil public reproduction. **Executive Order No. 288, recital concerning EO264**. 1995. [Public source](https://lawphil.net/executive/execord/eo1995/eo_288_1995.html) (accessed 2026-10-16).

Location/use: Executive Order 288, first WHEREAS recital.

Archive: `research/sources/final/phl1995.html`. SHA-256: `c43d77c4ef96c045ea4a2893ffcdefdb343c2ef3e98e9676ff6a9405deedb433`.

## PAK1997

Social Policy and Development Centre. **Evaluation of the Federal Budget 1999–2000, Research Report 23**. 1999. [Public source](https://spdc.org.pk/assets/upload/5f4efd6fbdd6c-Evaluation%20of%20the%20Federal%20Budget%201999%202000-RR-23.pdf) (accessed 2026-10-16).

Location/use: SPDC Evaluation of Federal Budget 1999-2000, PDF page 33, tax-reform discussion.

Archive: `research/sources/final/pak1997.pdf`. SHA-256: `1edf4225adf91b3cf0a78d9705a1dff3024a8180b6c7e5f0f516046caa4bce02`.

## CIV1998

International Monetary Fund. **Côte d’Ivoire: Selected Issues and Statistical Appendix, Country Report 00/107**. 2000. [Public source](https://www.imf.org/external/pubs/ft/scr/2000/cr00107.pdf) (accessed 2026-10-16).

Location/use: IMF Country Report 00/107, printed page 18, Box 2; PDF page 19 (visually inspected).

Archive: `research/sources/final/civ2000.pdf`. SHA-256: `8a58c0f42f466411097621628b826c88e68832229a2a7823c81c473405a563b1`.

## SEN1998

International Monetary Fund. **Senegal: Statistical Appendix, Country Report 99/5**. 1999. [Public source](https://www.imf.org/external/pubs/ft/scr/1999/cr9905.pdf) (accessed 2026-10-16).

Location/use: IMF Country Report 99/5, printed page 32, Table 27; PDF page 33 (visually inspected).

Archive: `research/sources/final/sen1999.pdf`. SHA-256: `cd55e76b89b54adab68ab17d15e13458c0497bd1fac4af3ae4fd12ee8941fb46`.

## BGDtiming

GATT. **Bangladesh balance-of-payments review, BOP/W/160**. 1995. [Public source](https://www.wto.org/gatt_docs/English/SULPDF/90080791.pdf) (accessed 2026-10-16).

Location/use: GATT BOP/W/160, paragraph 5; WTO 2000 government report tariff table.

Archive: `research/sources/final/bgd_gatt1995.pdf`. SHA-256: `8408580b4cd71fcad22770a67da3aefbeb26ff60953c97d84c998909a7e9f81a`.

## KENtiming

Government of Kenya / IMF. **Enhanced Structural Adjustment Facility Policy Framework Paper 1996–1998**. 1996. [Public source](https://www.imf.org/external/np/pfp/kenya/kenya.pdf) (accessed 2026-10-16).

Location/use: Kenya Policy Framework Paper 1996-1998, paragraph 6; PDF page 5.

Archive: `research/sources/final/ken1996.pdf`. SHA-256: `9ab7eafa768cd143e9d845d4c8af9eb64c6ff63a4a46efc7289033381dffbbdb`.

## EFW

Fraser Institute. **Competition-supplied EFW workbook: chain-linked panel and raw Ratings**. Coverage 1970–2024; release acceptance pending. [Public source](https://www.efotw.org/economic-freedom/dataset) (accessed 2026-10-16).

Location/use: Panel Area4 and Ratings raw 4Aii; original workbook hash preserved.

Archive: `data/EFW_original.xlsx`. SHA-256: `51a77026143bb941c1b9159bbea521a46b750eee3e4cb7ba9b75279203e17146`.

## UNDP

UNDP Human Development Report Office. **All composite indices and components time series**. HDR25; 1990–2023. [Public source](https://hdr.undp.org/data-center/documentation-and-downloads) (accessed 2026-10-16).

Location/use: GNI/person 2021 PPP dollars; components and country codes.

Archive: `data/UNDP_original.csv`. SHA-256: `61ed82e5b66c88dfca8ff9fac775c63981ecab6a254862af97acacc41c143117`.

## EFW2026

Cato Institute / Fraser Institute. **Economic Freedom of the World 2026, publisher landing page**. 2026. [Public source](https://www.cato.org/economic-freedom-world/2026) (accessed 2026-10-16).

Location/use: Confirms release covers 2024; does not establish supplied file byte identity.

## EFWMETHOD

Fraser Institute / Cato Institute. **EFW 2026: Explanatory Notes and Data Sources**. 2026. [Public source](https://www.cato.org/sites/cato.org/files/2026-10/EFW-2026-Appendix.pdf) (accessed 2026-10-16).

Location/use: Area4 A(ii), printed page94 / PDF page8; rating floor methodology.

## NPLTARIFF

Nepal Department of Customs. **Integrated Customs Tariff FY2083/84**. 2026/27. [Public source](https://www.customs.gov.np/content/46/integrated-tariff-rate/) (accessed 2026-10-16).

Location/use: PDF pages4–5: legal basis and Schedule1; page215: higher non-agricultural basic duties.

Archive: `research/sources/final/nepal_tariff2026.pdf`. SHA-256: `0569e39916b8bf2878913b49e490b2a81586969e0c3baf34d2580d4d212f12e3`.

## NPLACT

Nepal Law Commission. **Customs Tariff Act 2081**. 2024. [Public source](https://lawcommission.gov.np/category/1767/) (accessed 2026-10-16).

Location/use: Act first page and import Schedule1; direct PDF URL in fetch_law_manifest.json.

Archive: `research/sources/final/nepal_tariff_act2081.pdf`. SHA-256: `cf34adb79a46d64d228818dd585bea321c9b88fbc44f0133464d7efc601f83c2`.

## NPLFIN

Nepal Law Commission / Department of Customs. **Finance Act 2083 listing**. 2026. [Public source](https://lawcommission.gov.np/content/13588/economic-ann--2083/) (accessed 2026-10-16).

Location/use: Current legislation listing; use current integrated tariff for implemented rate context.

Archive: `research/sources/final/nepal_finance_act.html`. SHA-256: `f88f8956e7f0c8a45fdc93660c1a47f239f851d27341b224af65591b0a820a06`.

## THACRISIS

World Trade Organization. **Trade Policy Review: Thailand**. 1999. [Public source](https://www.wto.org/english/tratop_e/tpr_e/tp122_e.htm) (accessed 2026-10-16).

Location/use: Financial crisis is a realistic competing explanation for growth slowdown.

## CIVCONFLICT

World Bank. **Côte d’Ivoire: Strengthening Public Expenditure Management and Controls, Report27141-IVC**. 2003. [Public source](https://documents1.worldbank.org/curated/en/221511468243587148/pdf/271410IVC.pdf) (accessed 2026-10-16).

Location/use: Summary: instability since1999 and civil conflict2002; alternative explanation, not quantified here.


## 18. Supporting file map

- [analysis.ipynb](analysis.ipynb): Main self-contained working notebook.
- [README.md](README.md): Run/rebuild instructions.
- [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md): Completed versus external pending checks.
- [research/reform_dates.csv](research/reform_dates.csv): Authoritative current reform metadata.
- [research/analysis_steps.py](research/analysis_steps.py): Readable notebook-generation template.
- [research/build_notebook.py](research/build_notebook.py): Embeds inputs and derives chart-cell positions.
- [research/run_nb.py](research/run_nb.py): Executes with the chosen interpreter.
- [research/build_deck.py](research/build_deck.py): Builds PDF/PPTX from calculated outputs and cited research.
- [research/policy_notes.md](research/policy_notes.md): Current analysis decisions.
- [research/policy_recommendation.md](research/policy_recommendation.md): One recommendation, legal evidence, mechanism and cost.
- [research/dataset_declaration.md](research/dataset_declaration.md): Prepared declaration; not submitted or approved.
- [research/source_register.csv](research/source_register.csv): Full source/access/location manifest.
- [outputs/summary.json](outputs/summary.json): Calculated facts used by deck builder.
- [outputs/clean_runtime_verification.json](outputs/clean_runtime_verification.json): Empty-directory execution evidence.
- [deck/speaker_notes.md](deck/speaker_notes.md): Explanations for all16 pages.
- [deck/slide_manifest.json](deck/slide_manifest.json): Ten content/six appendix page classification.
- [research/archive_2026-10-13/ANALYSIS_RECORD.md](research/archive_2026-10-13/ANALYSIS_RECORD.md): Historical detailed record, original decisions and provisional32-cell analysis.
