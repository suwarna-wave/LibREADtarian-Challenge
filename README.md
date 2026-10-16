# Liberty Data Drive 2026 — Suwarna Pyakurel (solo)

Prepared 16–17 October 2026. Submission materials are ready for participant review; organiser approval and the exact deadline are not known.

## Open these first

- `deck/LDD2026_SuwarnaPyakurel_Deck.pdf`: ten content slides plus six verification appendix pages.
- `analysis.ipynb`: one reproducible working notebook, containing original data bytes and date metadata.
- `ANALYSIS_RECORD.md`: full history, methods, decisions, revisions and remaining external checks.
- `research/dataset_declaration.md`: prepared declaration and two explicit scope questions; not submitted.
- `SUBMISSION_CHECKLIST.md`: computational checks and remaining participant/organiser actions.

## Run locally

Python 3.12 was used for verification. From this directory:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python research/run_nb.py
```

Alternatively open `analysis.ipynb` in Colab and Run all. Both original datasets are embedded: no manual data upload is required. Missing numerical dependencies may be installed automatically by the first cell. The byte-identical originals are also included in `data/`. A pre-existing input with a different hash causes an error rather than being silently replaced.

Every figure saves PNG/PDF under `figures/` and exact input table under `outputs/`. `figures/chart_index.csv` includes actual notebook cell positions. `outputs/summary.json` drives the numerical statements in the deck; there are no manually typed chart values in the presentation.

## Rebuild reproducibly

`research/analysis_steps.py` is readable notebook-generation source; all calculations are copied into the main notebook. It is not imported during notebook execution. `research/build_notebook.py` embeds the original inputs and current reform ledger, and recreates the notebook. Rebuilding clears execution outputs: rerun afterwards. `research/build_deck.py` builds the PDF and editable PPTX from notebook exports and the source register.

```bash
.venv/bin/python research/build_notebook.py
.venv/bin/python research/run_nb.py
.venv/bin/python research/build_deck.py
```

`requirements-lock.txt` records the full verified environment. `research/sources.md` and `source_register.csv` contain public citations/access dates/locations. The final source archive is separate from numerical raw data. Earlier work remains in `research/archive_2026-10-13/`; it is historical and must not be confused with current results.

## Interpretation and pending items

Ten countries pass the raw-tariff screen. Eight enter the main event comparison; Bangladesh/Kenya are retained in screening and timing sensitivity. Four of eight exceed the broad comparator, with median excess about+0.06 pp/year. These are descriptive comparisons, not a causal estimate. Read the full results and sensitivity before citing this summary.

The notebook now uses both the required chain-linked EFW panel Area4 and raw tariff-specific Ratings data, separately labelled. Only organisers can confirm their acceptance of that interpretation and the supplied workbook release. The approved-declaration status and exact deadline must be confirmed by the participant. Test any shared notebook link from a signed-out browser. No organiser contact or submission has been made by the assistant.
