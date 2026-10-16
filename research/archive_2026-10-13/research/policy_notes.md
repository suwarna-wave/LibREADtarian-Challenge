# Policy notes — tariff liberalisation (working draft)

Status: **case selection done by rule; reform dates NOT yet verified.** Nothing below may be used in the deck until each date is confirmed against a primary/open source that has been opened and read (not a search-engine summary).

## Topic (confirmed with user)
Tariff cuts (EFW 4Aii mean tariff rate) → GNI per capita growth. Recommendation target: Nepal (tariff schedule). Colab data via public URL (to be provided).

## Case-selection rule (proposed)
Countries whose **raw mean tariff rate** (EFW Ratings, column right after "4Aii Mean tariff rate", %) fell by **≥ 20 percentage points between 1995 and 2005**, with UNDP GNI per capita available.
Raw rate is used (not the 0–10 score) because the score is floored at 0 for tariffs above ~50%, which hides most of the Indian-subcontinent change.

Result from `economic freedom.xlsx` (computed, 1995 → 2005, pp change):
Bangladesh −64.4, Pakistan −46.5, India −38.2, China −28.3, Mauritius −27.7, Thailand −25.4, Philippines −22.2, Kenya −21.9, Côte d'Ivoire −20.4, Senegal −20.2 (10 countries).
Next just outside the rule: Madagascar −18.4, Rwanda −17.6, Malawi −17.3, Burundi −17.3 (borderline; mention as sensitivity).

Nepal for comparison: mean tariff 22.6 (1990) → 16.1 (1995) → 14.7 (2000) → 14.7 (2005) → 12.3 (2010). Smaller, earlier fall; does not meet rule — useful as the recommendation target, not a case.

## Reform-dating rule (proposed, to confirm with user)
`reform_year` = first fiscal/calendar year in which the government's **main multi-band tariff cut took legal effect** (budget/finance act/customs notification), confirmed in an open document. EFW years are only used as a sanity check.

## Per-country date log (fill in; every row needs URL + access date)
| Country | Candidate reform (UNVERIFIED lead) | Effective date | Source URL | Accessed |
|---|---|---|---|---|
| Bangladesh | FY1994/95 max tariff cut (~300%→60%), 6 bands — lead only | ? | ? | ? |
| Pakistan | 1997-98 budget tariff rationalisation; 2001-02 further cut — lead only | ? | ? | ? |
| India | 1991-92 peak 150%; 1997-98 peak 50%→40% — lead only | ? | ? | ? |
| China | ? | ? | ? | ? |
| Mauritius | ? | ? | ? | ? |
| Thailand | ? | ? | ? | ? |
| Philippines | ? (EO 470 / 1995 tariff programme) | ? | ? | ? |
| Kenya | ? | ? | ? | ? |
| Côte d'Ivoire | ? (WAEMU common external tariff, 2000) | ? | ? | ? |
| Senegal | ? (WAEMU common external tariff, 2000) | ? | ? | ? |

## Known issues to disclose
- EFW is 5-yearly before 2000 → EFW cannot date reforms before 2000 precisely.
- UNDP starts 1990: reforms in 1991–94 (e.g. India 1991) have <5 pre-years. Shorter pre-window must be stated on charts.
- Côte d'Ivoire and Senegal share one WAEMU tariff reform → not independent cases; handle explicitly.
- Concurrent reforms (exchange rate, IMF programmes, privatisation) are the main alternative explanation.
