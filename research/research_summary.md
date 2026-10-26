# Research summary: Tariff Cuts, Uneven Gains

Suwarna Pyakurel · solo · Liberty Data Drive 2026. Summary prepared 24 October 2026 from the existing analysis and source archive; no new numerical estimates or current-law verification.

## Why this topic

Tariffs connect a specific policy to the cost of trade, household choice, business inputs and government revenue. Trade, property rights, regulation and sound money were explored. Tariffs offered a measurable policy variable, several countries with documented changes and relevance to Nepal. There was no formal scored topic ranking or preregistration. The case/date choices followed exploratory inspection, which limits claims about selection.

## Question and evidence

After documented tariff-cutting episodes in India, China, Mauritius, Thailand, the Philippines, Pakistan, Côte d’Ivoire and Senegal during 1991–1998, did real GNI per person grow faster over the following ten years than before reform and than other countries, and what does this suggest for Nepal?

The two supplied numerical inputs are Fraser EFW and UNDP HDR25. Raw mean tariff percentages establish the specific policy screen; chain-linked Area 4 provides separate institutional context. UNDP GNI per person is measured in constant 2021 PPP dollars, 1990–2023. Institutional scores, tariff percentages, levels of income and annual growth rates are different quantities.

## How the analysis was built

1. Preserve original inputs and verify hashes. Inspect schemas, identifiers, duplicates, matching and missingness.
2. Screen matched countries for an observed mean tariff fall of at least 20 percentage points in 1995–2005, requiring both tariff endpoints and income data. Ten qualify.
3. Read public policy documents and record actual implementation years: India 1991, China 1992, Mauritius 1994, Thailand 1995, Philippines 1995, Pakistan 1997, Côte d’Ivoire 1998 and Senegal 1998. The screen is not the implementation window and postdates some reforms.
4. Retain Bangladesh and Kenya in full histories and separate timing checks because comparable event timing is less precise. Côte d’Ivoire and Senegal share a regional reform, limiting independence.
5. Align outcomes from five years before to ten years after reform. Index reform-year income to 100. Do not interpolate missing values or treat them as zero. Distinguish changing-membership and balanced medians.
6. Compute ten-year post-reform compound annual growth and complete five-year pre-reform growth where available. Only five cases have the full prehistory.
7. Compare each case with the median valid endpoint growth in other countries over the same calendar years, excluding all ten screened countries. Comparator membership ranges from 148 to 152. These are not matched or untreated controls.
8. Check shifted dates, alternative windows, country composition, related regional cases, balanced membership, screening thresholds and assumed Bangladesh/Kenya timings. Export numerical tables and charts from code.

## What was found

| Test | Result |
|---|---|
| Countries meeting the screen | 10 |
| Main dated cases | 8 |
| Higher income after ten years | 7/8 |
| Faster growth than the complete preperiod | 3/5 |
| Growth above the broad comparator | 4/8 |
| Median growth difference | Approximately +0.06 percentage points/year |
| Excluding China | 3/7 above comparator; median approximately −0.27 pp/year |

The median difference is near zero and changes sign under reasonable timing/composition checks. Income rising is different from growth accelerating or exceeding a benchmark. Country-level comparisons do not isolate a causal effect of tariffs.

## What the external research contributes

Reform documents establish implementation timing and policy content; they do not establish income effects. Thailand’s financial crisis and Côte d’Ivoire’s conflict are documented alternative explanations. Wider reforms and macroeconomic conditions are also plausible influences; their separate contributions are not estimated.

Baunsgaard and Keen (2005), IMF WP/05/112, examine whether other taxes replaced lost trade-tax revenue across countries. Their findings make automatic revenue recovery an unsafe assumption, especially for low-income countries. This supplies a fiscal objection, not a Nepal revenue forecast.

Agbeyegbe, Stotsky and WoldeMariam (2004), IMF WP/04/178, study trade liberalisation, exchange rates and tax revenue in Sub-Saharan Africa. Results depend on measures and macroeconomic conditions; they do not imply inevitable revenue losses or automatic gains. This complements fiscal caution and does not identify a Nepal tariff optimum. Both papers are external context; their data are not merged into the competition’s fixed numerical datasets.

Laffer intuition does not establish a Nepal revenue peak or show that tariff cuts finance themselves. No standalone Laffer chart is used as empirical evidence for the cap.

## One Nepal proposal and its limits

Action type: Modification. Amend Schedule 1 of the Customs Tariff Act 2081, as amended, to cap standard non-preferential ad valorem basic duties in HS25–97 at 20% over three budgets, retaining lower rates. Finance Ministry proposes, Parliament enacts and Customs administers. VAT, excise, specific/mixed duties, prohibitions and preferences remain outside scope.

The proposed mechanism is a smaller import-tax wedge, with possible effects on input costs, prices and choice depending on competition and pass-through. The liberty argument supports voluntary exchange and predictable rules while recognising diffuse buyer costs and concentrated producer benefits. The strongest objection is public-revenue risk and concentrated adjustment costs for firms and workers. A transition changes timing, not the existence of those costs.

The 20% ceiling and three-budget period are normative choices, not empirically estimated optima. Historical Nepal average tariffs do not reveal statutory maxima. The archived schedule includes 30% basic-duty examples, subject to line-specific conditions. No Nepal fiscal cost, affected-line total, employment, income or price effect is estimated. Legal evidence remains archived as of 16 October; current-law completeness is unconfirmed.

## Where the figures are

The eight images used in the linked Google Slides deck retain original Figure 1–8 numbering. Their local copies, matching CSVs and index are in `outputs/figures and charts/`, excluded from Git. Figures 1 and 2 are on slide 3; Figures 3–8 are on slides 4–9. Their original calculation/chart cells are 17–24, counting all cells including Markdown from 1. Images were retrieved from the deck on 24 October; Google’s rendering may differ from locally generated PNGs.

The separate [compact PDF](../deck/compact_2026-10-23/LDD2026_SuwarnaPyakurel_Deck.pdf) uses six renumbered figures generated by notebook cell 30 and exported to figures/compact/. Do not substitute its index for the eight-image deck.

## Reproduction and responsibility

The [working notebook](../LDD2026_SuwarnaPyakurel_Working.ipynb) contains original input bytes and the reform ledger. Run cells top to bottom; see the root README and requirements.txt. The readable source is analysis_steps.py. The final compact-export cell follows the original charts and archived presentation exports.

[All 20 references and their archived copies](README.md) retain public URLs, access dates and available hashes. OpenAI Codex helped with coding, resolving errors and researching supporting articles, as well as figures, checks and drafting; [the disclosure](ai_disclosure.md) explains participant responsibility. Approval, submission and any competition score remain unclaimed.
