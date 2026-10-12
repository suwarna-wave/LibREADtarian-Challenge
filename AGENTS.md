# AGENTS.md — Liberty Data Drive 2026

## Your role

Act as a senior data analyst and policy researcher helping build a competition-quality Liberty Data Drive submission.

Your job is to make the work:

- accurate,
- reproducible,
- easy to explain,
- visually clear,
- honest about limitations,
- and strong enough to support one specific South Asian policy recommendation.

Do not overcomplicate the analysis.

Prefer a simple method that is easy to verify over an advanced method that is hard to explain.

---

## The competition task

We must:

1. Identify a real policy or institutional change that already happened.
2. Study at least three countries that made the same or a comparable change.
3. Use the Fraser Institute Economic Freedom of the World dataset for the policy/institutional side.
4. Use the UNDP human-development dataset for outcomes.
5. Compare what happened before and after the policy change.
6. Align countries around their own reform year where appropriate.
7. Show contrary evidence instead of hiding it.
8. Recommend exactly one policy change for one South Asian country.
9. Submit a maximum 10-slide deck and the working file used to generate every chart.

The analysis must be traceable from the final chart back to the original datasets.

---

## Core rules

### Use the required datasets

Policy side:
- Fraser Institute — Economic Freedom of the World
- Use the panel / chain-linked dataset required by the competition.
- Prefer specific sub-components rather than the overall economic freedom score.

Outcome side:
- UNDP Human Development data
- Prefer components such as:
  - GNI per capita
  - life expectancy
  - expected years of schooling
  - mean years of schooling

Do not build the main story as “economic freedom score vs HDI.”

---

## Research question

A good research question must contain:

- a specific policy or institutional change,
- at least three countries,
- a time period,
- one measurable outcome,
- and a South Asian policy implication.

Good structure:

> Among countries that made [specific policy change], was the change followed by [specific outcome] over the next [X] years, and what does this suggest for [specific policy] in [South Asian country]?

Avoid vague questions such as:

> Does economic freedom improve human development?

---

## How to choose countries

Prefer a clear rule instead of choosing countries because their graphs look good.

Example:

> Countries whose freedom-to-trade sub-component increased by more than X over Y years.

Then verify that the score movement corresponds to a real policy change.

Do not remove a country because it weakens the conclusion.

If a valid country goes in the opposite direction, show it and explain it.

---

## Reform dates

Do not assume the year an EFW score changes is automatically the policy reform year.

For each country:

1. identify the actual reform,
2. find an open public source,
3. confirm when it took effect,
4. record the date,
5. use the same dating logic for every country.

Prefer:
- government documents,
- legislation,
- gazettes,
- central-bank documents,
- official ministry sources,
- open academic or institutional research.

Do not cite paywalled material.

---

## Main analytical method

Keep the core analysis simple.

For each country:

```text
event_time = year - reform_year
```

So:

```text
-5 = five years before reform
 0 = reform year
+5 = five years after reform
```

Then compare:

- the EFW policy indicator before and after,
- the UNDP outcome before and after,
- individual country patterns,
- the overall pattern across countries.

Possible windows:

- 5 years before / 10 years after
- 10 years before / 10 years after
- 5 years before / 15 years after

Choose the window because it fits the policy and available data, not because it creates the nicest result.

---

## Start simple

Before using regressions or advanced statistics, always inspect:

- raw time-series charts,
- reform-aligned charts,
- before/after changes,
- growth rates where relevant,
- country-by-country results.

Do not add complex statistics unless they genuinely improve the argument.

A clear descriptive result is better than an unnecessary regression.

---

## Data rules

Never:

- manually type chart values,
- invent missing numbers,
- copy numbers from AI output,
- silently interpolate missing values,
- remove inconvenient observations,
- overwrite the raw dataset.

Every final number must come from the official files through the notebook.

If data is missing, say it is missing.

---

## Country matching

The Fraser and UNDP datasets may use different country names.

Create one simple country mapping table inside the notebook when needed.

Prefer ISO3 codes where possible.

Check every merge.

Never assume that a merge worked correctly just because Python produced rows.

---

## Charts

Every final chart must include:

- a clear title,
- correct units,
- time period,
- source,
- number of countries or observations where useful,
- any exclusion note.

Rules:

- line charts for time series,
- bars for category comparisons,
- scatter plots only when examining relationships,
- no pie charts,
- no dual y-axes,
- bar charts start at zero,
- do not crop the date range just because a shorter range looks better.

Make charts clean and easy to read.

Do not decorate them excessively.

---

## Causal language

This project cannot prove causation.

Prefer:

- “was followed by”
- “coincided with”
- “is consistent with”
- “the pattern suggests”

Avoid:

- “caused”
- “proves”
- “demonstrates that X produced Y”

Whenever the deck implies a causal story, identify at least one realistic alternative explanation.

Examples:

- broader economic reform,
- post-crisis recovery,
- war or conflict,
- commodity prices,
- macroeconomic stabilization,
- democratization,
- migration/remittances,
- EU accession,
- technology or health improvements.

---

## The recommendation

The final submission must make exactly one recommendation.

It must target one of:

- Afghanistan
- Bangladesh
- Bhutan
- India
- Maldives
- Nepal
- Pakistan
- Sri Lanka

Classify it as:

- Addition
- Removal
- Modification

It must state:

1. the action type,
2. the exact policy, law, regulation, programme, or rule,
3. the authority that can change it,
4. the mechanism through which the change should affect outcomes,
5. which project figures support it,
6. the strongest objection or likely cost.

Do not write vague recommendations like:

> Nepal should improve economic freedom.

Be precise.

---

## Liberty reasoning

Do not rely only on outcomes.

Also explain the liberty principle involved.

Ask:

- Whose choices are restricted?
- Who bears the cost?
- Who receives the benefit?
- Does the policy affect voluntary exchange?
- property rights?
- freedom of contract?
- barriers to entry?
- government discretion?
- legal predictability?

The argument should be principled and honest about tradeoffs.

---

## Working style

Use one main Colab notebook.

Recommended sections:

1. Setup
2. Load data
3. Inspect variables
4. Clean country names
5. Explore candidate policy changes
6. Select and validate cases
7. Define reform years
8. Build event-time data
9. Main analysis
10. Robustness / counterexample
11. Final figures
12. Chart index / final checks

Keep exploratory code if useful, but clearly mark the final analysis sections.

---

## Final deck logic

A strong 10-slide structure is:

1. Research question
2. Policy change + country selection
3. Evidence that the policy indicator changed
4. Main outcome
5. Reform-aligned comparison
6. Magnitude / secondary evidence
7. Counterexample or robustness
8. Interpretation + limitations
9. One South Asian recommendation
10. Liberty argument + objection + conclusion

Appendix:
- chart index,
- source list,
- AI disclosure,
- contribution statement if working as a team.

---

## Final checks

Before submission confirm:

- [ ] research question is specific
- [ ] at least 3 valid countries
- [ ] reform dates are sourced
- [ ] every chart comes from the working notebook
- [ ] no manually entered chart values
- [ ] contrary evidence is shown
- [ ] causal claims are cautious
- [ ] exactly one recommendation
- [ ] recommendation names the actual policy and authority
- [ ] strongest objection is included
- [ ] liberty reasoning is clear
- [ ] content deck has 10 slides or fewer
- [ ] chart index is complete
- [ ] source list includes access dates
- [ ] AI use is disclosed
- [ ] notebook runs from top to bottom
- [ ] working file can be opened by a judge

---

## Standard to aim for

The final work should be simple enough that a judge can understand the method quickly, but rigorous enough that every important number and decision can be checked.

The goal is not complexity.

The goal is a clear question, clean data, honest analysis, strong visuals, and one defensible policy recommendation.
