"""Sections 6-12 of the notebook. Called from build_notebook.py."""
import pathlib

def add_part2(C, md, code0):
    # cell number = 1-based position of the cell in the notebook (placeholder resolved at build time)
    code = lambda s: code0(s.replace("len(C_PLACEHOLDER)", str(len(C) + 1)))
    csv_text = pathlib.Path("research/reform_dates.csv").read_text()

    md("""## 6. Case selection (fixed rule)
**Rule:** every country whose **raw mean tariff rate (%)** fell by **≥ 20 percentage points between 1995 and 2005** (EFW Ratings, data column beside *4Aii Mean tariff rate*), with UNDP GNI per capita available.
The raw rate is used because the 0–10 score is floored at 0 for tariffs above ~50%, which hides most of the South Asian change.
The rule was fixed before looking at outcomes. No country is added or removed because of its outcome.""")
    code('''i = list(efw.columns).index("4Aii  Mean tariff rate")
efw["tariff_raw"] = pd.to_numeric(efw[efw.columns[i + 1]], errors="coerce")          # % mean tariff rate
j = list(efw.columns).index("4Aiii  Standard deviation of tariff rates")
efw["tariff_sd_raw"] = pd.to_numeric(efw[efw.columns[j + 1]], errors="coerce")       # std dev of tariff rates (pp)
tar = efw[["ISO_Code", "Year", "tariff_raw", "tariff_sd_raw"]].copy()
P = tar.dropna(subset=["tariff_raw"]).pivot_table(index="ISO_Code", columns="Year", values="tariff_raw")
A, B, RULE_PP = 1995, 2005, 20.0
chg = (P[B] - P[A]).dropna()
chg = chg[chg.index.isin(has_gni)]
cases = chg[chg <= -RULE_PP].sort_values()
print(f"{len(cases)} cases (tariff fell >= {RULE_PP} pp, {A}->{B}); {len(chg)} countries had both years + GNI")
display(pd.DataFrame({"country": [NAME[c] for c in cases.index], f"tariff {A} (%)": P.loc[cases.index, A].round(1),
                      f"tariff {B} (%)": P.loc[cases.index, B].round(1), "change (pp)": cases.round(1)}))
near = chg[(chg <= -15) & (chg > -RULE_PP)].sort_values()
print("Just outside the rule (not in sample):", ", ".join(f"{NAME[c]} ({v:.1f})" for c, v in near.items()))''')

    md("""## 7. Reform dates (sourced) and sample exclusions
`reform_year` = the earliest year an **open source** documents the start of the tariff-reduction programme (legislation, budget speech, WTO Trade Policy Review, or open institutional paper) — the **same logic for every country**. It is *not* read from the year an EFW score changes.
Where a source only gives a baseline year before the cuts (Bangladesh, Kenya), that year is used and flagged "baseline-dated"; section 10 shifts every date by ±2 years to test sensitivity.
Countries with **no verifiable open source** are excluded (Mauritius, Thailand) — decided on sourcing, not on outcomes — and are shown in Fig 1 for transparency.
Côte d'Ivoire and Senegal share one WAEMU reform: they are **not independent** (tested in section 10).
Full log with URLs and access dates: `research/reform_dates.csv`, `research/policy_notes.md`.""")
    code('DATES_CSV = """' + csv_text + '"""\n' + '''from io import StringIO
dates = pd.read_csv(StringIO(DATES_CSV))
miss = set(cases.index) ^ set(dates.iso3)
assert not miss, f"cases vs reform-date table mismatch: {miss}"
dates["verified"] = dates.status.str.startswith("VERIFIED")
main = dates[dates.verified].copy(); main["reform_year"] = main.reform_year.astype(int)
analysis_iso = list(main.iso3)
display(dates[["iso3", "country", "reform_year", "effective_date", "status"]])
print(f"Analysis sample: {len(analysis_iso)} of {len(dates)} rule-selected countries ->", ", ".join(main.country))
print("Excluded (no verifiable reform date):", ", ".join(dates[~dates.verified].country))''')

    md("""## 8. Event-time dataset
`event_time = year − reform_year` (0 = reform year). Window: −5 … +10 years, clipped to UNDP coverage (1990–2023). Nothing is interpolated.
The EFW tariff series is 5-yearly before 2000, so some event years have no EFW value (left blank).""")
    code('''LO, HI = -5, 10
u = undp[undp.iso3.isin(analysis_iso)][["iso3", "year", "gnipc", "le", "eys", "mys"]].copy()
u = u.merge(main[["iso3", "reform_year"]], on="iso3")
u["event_time"] = u.year - u.reform_year
panel = u[(u.event_time >= LO) & (u.event_time <= HI)].merge(
    tar.dropna(subset=["tariff_raw"]).rename(columns={"ISO_Code": "iso3", "Year": "year"})[["iso3", "year", "tariff_raw"]],
    on=["iso3", "year"], how="left")
panel["country"] = panel.iso3.map(NAME)
panel = panel[["country", "iso3", "year", "reform_year", "event_time", "tariff_raw", "gnipc", "le", "eys", "mys"]]
print(panel.shape); display(panel.groupby("country").agg(first=("event_time", "min"), last=("event_time", "max"),
      n_gni=("gnipc", "count"), n_tariff=("tariff_raw", "count")))
base = panel[panel.event_time == 0].set_index("iso3")
panel["gni_index"] = panel.gnipc / panel.iso3.map(base["gnipc"]) * 100
panel["le_gain"] = panel["le"] - panel.iso3.map(base["le"])''')

    md("""## 9. Main analysis (descriptive)
- **Growth:** average annual GNI per capita growth (CAGR) in the 5 years before vs the 10 years after the reform year. If fewer than 3 pre-years exist in UNDP data (1990 start), pre-growth is not computed (`NaN`).
- **Benchmark:** median CAGR of all *other* EFW countries (excluding every rule-selected case) over the **same calendar years** — a crude control for global conditions. Not a causal control.""")
    code('''def cagr(s, y0, y1):
    if y0 in s.index and y1 in s.index and s[y0] > 0 and s[y1] > 0:
        return (s[y1] / s[y0]) ** (1 / (y1 - y0)) - 1
    return np.nan
G = undp[undp.iso3.isin(e_iso)].pivot_table(index="iso3", columns="year", values="gnipc")
non_case = G.index.difference(cases.index)
def bench(y0, y1):
    return np.nanmedian([cagr(G.loc[c], y0, y1) for c in non_case])
def build_results(shift=0, post=10):
    rows = []
    for iso, ry0 in main.set_index("iso3").reform_year.items():
        ry = ry0 + shift; s = G.loc[iso]; p0 = max(1990, ry - 5)
        pre = cagr(s, p0, ry) if ry - p0 >= 3 else np.nan
        pst = cagr(s, ry, ry + post); bp = bench(ry, ry + post)
        rows.append({"iso3": iso, "country": NAME[iso], "reform_year": ry, "pre_years_available": ry - p0,
                     "pre_cagr_%": pre * 100, "post_cagr_%": pst * 100, "benchmark_post_%": bp * 100,
                     "excess_vs_bench_pp": (pst - bp) * 100})
    return pd.DataFrame(rows).sort_values("excess_vs_bench_pp", ascending=False).reset_index(drop=True)
res = build_results()
display(res.round(2))
print("Cases with post growth above benchmark:", (res.excess_vs_bench_pp > 0).sum(), "of", len(res))
print("Median post-reform CAGR: %.2f%% | median benchmark: %.2f%% | median excess: %.2f pp" % (
      res["post_cagr_%"].median(), res["benchmark_post_%"].median(), res.excess_vs_bench_pp.median()))''')

    md("""## 10. Counterexamples and robustness
(a) The case(s) that do **not** beat the benchmark are charted, not hidden. (b) Dependence on the two WAEMU cases (CIV, SEN) and on China (largest outlier). (c) Sensitivity to the reform year (shift every date by −2…+2 years) and to a 5-year post window.""")
    code('''lag = res[res.excess_vs_bench_pp <= 0]
print("Cases at or below benchmark:", list(lag.country) or "none")
def summarize(r, label):
    print(f"{label:<42} beat benchmark: {(r.excess_vs_bench_pp > 0).sum()}/{len(r)} | median excess {r.excess_vs_bench_pp.median():+.2f} pp")
summarize(res, "Main (10-yr post, dates as sourced)")
summarize(res[~res.iso3.isin(["CIV", "SEN"])], "Excluding CIV & SEN (shared WAEMU reform)")
summarize(res[res.iso3 != "CHN"], "Excluding China (largest outlier)")
rob = []
for s in (-2, -1, 0, 1, 2):
    r = build_results(shift=s); summarize(r, f"Reform year shifted {s:+d}")
    rob.append({"shift_years": s, "n_beat": int((r.excess_vs_bench_pp > 0).sum()), "n": len(r), "median_excess_pp": r.excess_vs_bench_pp.median()})
r5 = build_results(post=5); summarize(r5, "5-year post window")
rob = pd.DataFrame(rob)
for iso in ["IND", "CHN", "BGD", "KEN"]:
    print(iso, "pre-years available in UNDP:", int(res.loc[res.iso3 == iso, "pre_years_available"].iloc[0]), "(pre-growth not computed if < 3)")''')

    md("## 11. Final figures\nEach figure is one cell; `register()` records it for the chart index.")
    code('''import matplotlib as mpl
os.makedirs("figures", exist_ok=True)
mpl.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
                     "grid.alpha": .25, "font.size": 10})
SRC = "Sources: Fraser Institute EFW (Ratings sheet); UNDP HDR 2025 composite-indices time series."
CHART_INDEX = []
def register(fig_id, slide, what, cell):
    CHART_INDEX.append({"Fig": fig_id, "Slide": slide, "What it shows": what, "Location in working file": f"Notebook cell {cell} -> figures/{fig_id}.png"})
def finish(fig, fig_id, title, note):
    fig.suptitle(title, fontsize=12, fontweight="bold", x=0.01, ha="left")
    fig.text(0.01, 0.005, note + "\\n" + SRC, fontsize=7.5, color="#444", va="bottom")
    fig.tight_layout(rect=[0, 0.08, 1, 0.95]); fig.savefig(f"figures/{fig_id}.png", dpi=200); plt.show()
order = list(res.iso3)
n_cases = len(order)''')

    code('''# Fig1: tariff trajectories of ALL rule-selected countries (calendar years, markers = actual EFW observations)
allc = list(cases.index)
fig, axes = plt.subplots(2, 5, figsize=(14, 6), sharey=True)
ymax = tar[tar.ISO_Code.isin(allc) & (tar.Year <= 2024)].tariff_raw.max() * 1.05
for ax, iso in zip(axes.flat, allc):
    d = tar[(tar.ISO_Code == iso) & tar.tariff_raw.notna() & (tar.Year <= 2024)].sort_values("Year")
    ax.plot(d.Year, d.tariff_raw, "o-", ms=3, lw=1.2, color="#1f6feb" if iso in analysis_iso else "#999")
    if iso in analysis_iso:
        ax.axvline(int(main.set_index("iso3").loc[iso, "reform_year"]), color="crimson", ls="--", lw=1)
        ax.set_title(NAME[iso], fontsize=9)
    else:
        ax.set_title(NAME[iso] + " (excluded: no dated source)", fontsize=8, color="#666")
    ax.set_ylim(0, ymax)
for ax in axes[:, 0]: ax.set_ylabel("Mean tariff rate (%)")
finish(fig, "Fig1", "Fig 1. Mean tariff rate fell sharply in all 10 rule-selected countries (EFW, all years available)",
       f"Red dashed line = sourced reform year (section 7). Grey = excluded for lack of a verifiable reform date. n = {len(allc)} selected by rule (fell >= {RULE_PP:.0f} pp, {A}-{B}); {n_cases} analysed. Points are 5-yearly before 2000, annual after; no interpolation.")
register("Fig1", 3, "Raw mean tariff rate, 10 rule-selected countries, reform year marked", len(C_PLACEHOLDER))''')

    code('''# Fig2: GNI per capita indexed to reform year = 100
fig, ax = plt.subplots(figsize=(9, 5.2))
for iso in order:
    d = panel[panel.iso3 == iso].sort_values("event_time")
    ax.plot(d.event_time, d.gni_index, lw=1.1, alpha=.85, label=NAME[iso])
med = panel.groupby("event_time").gni_index.median()
cnt = panel.groupby("event_time").gni_index.count()
med = med[cnt >= 5]
ax.plot(med.index, med.values, "k-", lw=3, label="Median (>=5 countries)")
ax.axvline(0, color="crimson", ls="--"); ax.axhline(100, color="grey", lw=.8)
ax.set_xlabel("Years since reform year (0 = reform)"); ax.set_ylabel("GNI per capita, index (reform year = 100)")
ax.legend(fontsize=7, ncol=2, frameon=False)
finish(fig, "Fig2", "Fig 2. GNI per capita around each country's tariff-reform year",
       f"GNI per capita in 2021 PPP$, indexed to 100 in the reform year. Window -5 to +10 (shorter pre-window where UNDP data starts in 1990: IND, CHN, BGD, KEN). n = {n_cases} countries.")
register("Fig2", 5, "GNI per capita index aligned on reform year, cases + median", len(C_PLACEHOLDER))''')

    code('''# Fig3: growth before vs after + benchmark (bars start at zero)
r = res.set_index("country")
x = np.arange(len(r)); w = .27
fig, ax = plt.subplots(figsize=(11, 5))
ax.bar(x - w, r["pre_cagr_%"], w, label="5 yrs before (only if >=3 yrs of UNDP data)", color="#9aa5b1")
ax.bar(x, r["post_cagr_%"], w, label="10 yrs after", color="#1f6feb")
ax.bar(x + w, r["benchmark_post_%"], w, label="Benchmark: median non-case country, same years", color="#e8b04a")
ax.axhline(0, color="k", lw=.8); ax.set_xticks(x); ax.set_xticklabels(r.index, rotation=30, ha="right")
ax.set_ylabel("Average annual GNI per capita growth (%)"); ax.legend(frameon=False, fontsize=8)
finish(fig, "Fig3", "Fig 3. GNI per capita growth before vs after the reform, and vs the rest of the world",
       f"CAGR of GNI per capita (2021 PPP$). Missing grey bar = fewer than 3 pre-years in UNDP data. Benchmark = median of {len(non_case)} non-case EFW countries. n = {len(r)} cases.")
register("Fig3", 6, "Pre vs post GNI per capita CAGR and benchmark, by country", len(C_PLACEHOLDER))''')

    code('''# Fig4: excess growth over benchmark (sorted) - shows who does NOT fit
fig, ax = plt.subplots(figsize=(9, 4.8))
colors = ["#1f6feb" if v > 0 else "crimson" for v in res.excess_vs_bench_pp]
ax.barh(res.country[::-1], res.excess_vs_bench_pp[::-1], color=colors[::-1])
ax.axvline(0, color="k", lw=.8); ax.set_xlabel("Post-reform CAGR minus benchmark CAGR (percentage points per year)")
finish(fig, "Fig4", "Fig 4. Which cases grew faster than the benchmark after reform? (red = did not)",
       f"Benchmark = median non-case country over the same 10 calendar years. {int((res.excess_vs_bench_pp>0).sum())} of {len(res)} cases above benchmark. CIV and SEN share one WAEMU reform (not independent).")
register("Fig4", 7, "Excess GNI growth over benchmark, counterexamples in red", len(C_PLACEHOLDER))''')

    code('''# Fig5: robustness - result under shifted reform years (counts of cases beating benchmark)
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.bar(rob.shift_years.astype(str), rob.n_beat, color="#1f6feb")
ax.set_ylim(0, len(res)); ax.axhline(len(res) / 2, color="grey", ls=":", lw=1)
for k, v in zip(rob.shift_years.astype(str), rob.n_beat): ax.text(k, v + .1, f"{v}/{len(res)}", ha="center", fontsize=9)
ax.set_xlabel("Shift applied to every reform year (years)"); ax.set_ylabel("Cases growing faster than benchmark")
finish(fig, "Fig5", "Fig 5. Robustness: how many cases beat the benchmark if reform years are shifted?",
       f"10-year post-reform CAGR vs median non-case country over the same years. Dotted line = half of cases. n = {len(res)} cases per bar. Bars start at zero.")
register("Fig5", 7, "Robustness to +-2 year shifts in reform date", len(C_PLACEHOLDER))''')

    code('''# Fig6: life expectancy change since reform year (secondary outcome)
fig, ax = plt.subplots(figsize=(9, 5))
for iso in order:
    d = panel[panel.iso3 == iso].sort_values("event_time")
    ax.plot(d.event_time, d.le_gain, lw=1.1, alpha=.85, label=NAME[iso])
m = panel.groupby("event_time").le_gain.median(); m = m[panel.groupby("event_time").le_gain.count() >= 5]
ax.plot(m.index, m.values, "k-", lw=3, label="Median (>=5 countries)")
ax.axvline(0, color="crimson", ls="--"); ax.axhline(0, color="grey", lw=.8)
ax.set_xlabel("Years since reform year (0 = reform)"); ax.set_ylabel("Life expectancy change since reform year (years)")
ax.legend(fontsize=7, ncol=2, frameon=False)
finish(fig, "Fig6", "Fig 6. Life expectancy change since the reform year (secondary outcome)",
       f"Life expectancy at birth, years, relative to the reform year. Other health shocks (e.g. HIV/AIDS in Kenya and Cote d'Ivoire) also affect this series. n = {n_cases} countries.")
register("Fig6", 6, "Life expectancy gain aligned on reform year", len(C_PLACEHOLDER))''')

    code('''# Fig7: Nepal vs South Asian peers - tariffs and income side by side (no dual axis)
SA = ["NPL", "BGD", "IND", "PAK", "LKA"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
for iso in SA:
    d = tar[(tar.ISO_Code == iso) & tar.tariff_raw.notna()].sort_values("Year"); lw = 3 if iso == "NPL" else 1.2
    a1.plot(d.Year, d.tariff_raw, "o-", ms=3, lw=lw, label=NAME[iso])
    g = undp[undp.iso3 == iso].sort_values("year"); a2.plot(g.year, g.gnipc, lw=lw, label=NAME[iso])
a1.set_ylabel("Mean tariff rate (%)"); a1.set_ylim(bottom=0); a1.set_title("Tariffs (EFW)", fontsize=10)
a2.set_ylabel("GNI per capita (2021 PPP$)"); a2.set_title("GNI per capita (UNDP)", fontsize=10); a1.legend(frameon=False, fontsize=8)
finish(fig, "Fig7", "Fig 7. Nepal vs South Asian peers: tariffs and income",
       "Nepal (thick line) liberalised earlier and less than BGD/IND/PAK. Left: EFW (5-yearly before 2000). Right: UNDP annual 1990-2023. n = 5 countries.")
register("Fig7", 9, "Nepal vs South Asian peers: tariff and GNI per capita", len(C_PLACEHOLDER))''')

    code('''# Fig8: where Nepal stands today: level vs dispersion of tariffs (latest EFW year), bars from zero
LATEST = int(tar.Year.max())
lvl = tar[tar.Year == LATEST].set_index("ISO_Code")
names = ["NPL"] + analysis_iso
t = pd.DataFrame({"country": [NAME[c] for c in names], "mean": lvl.loc[names, "tariff_raw"].values,
                  "sd": lvl.loc[names, "tariff_sd_raw"].values})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
for ax, col, lab in ((a1, "mean", "Mean tariff rate (%)"), (a2, "sd", "Std. deviation of tariff rates (pp)")):
    s = t.sort_values(col, ascending=False)
    ax.bar(s.country, s[col], color=["crimson" if c == "Nepal" else "#7a8aa0" for c in s.country])
    ax.set_ylabel(lab); ax.tick_params(axis="x", rotation=40)
a1.set_title("Level", fontsize=10); a2.set_title("Dispersion (how uneven the tariff schedule is)", fontsize=10)
finish(fig, "Fig8", f"Fig 8. Nepal's tariff level is near the post-reform plateau, but its tariff dispersion is not ({LATEST})",
       f"Latest EFW year ({LATEST}); raw values from EFW 4Aii and 4Aiii data columns. n = {len(t)} countries (Nepal + {len(analysis_iso)} cases). Bars start at zero.")
register("Fig8", 9, "Nepal vs cases: tariff level and dispersion, latest year", len(C_PLACEHOLDER))
display(t.round(1).sort_values("sd", ascending=False))''')

    md("## 12. Chart index and final checks")
    code('''ci = pd.DataFrame(CHART_INDEX); display(ci); ci.to_csv("figures/chart_index.csv", index=False)
for f in ci.Fig: assert os.path.exists(f"figures/{f}.png"), f
assert panel.groupby("iso3").size().min() > 0
assert dates[dates.verified].source_url.notna().all()
print("Checks passed. Reform dates verified:", int(dates.verified.sum()), "| excluded:", int((~dates.verified).sum()))
res.round(3).to_csv("figures/results_table.csv", index=False); rob.round(3).to_csv("figures/robustness_table.csv", index=False)''')
