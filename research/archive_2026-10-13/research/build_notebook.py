"""Generates analysis.ipynb (sections 1-5). Re-run to rebuild the notebook skeleton."""
import sys
import nbformat as nbf

nb = nbf.v4.new_notebook()
C = []
md = lambda s: C.append(nbf.v4.new_markdown_cell(s))
code = lambda s: C.append(nbf.v4.new_code_cell(s))

md("""# Liberty Data Drive 2026 — Working File
**Status:** sections 1–5 (setup → candidate scan). Sections 6–12 are added after the topic is chosen.

Data: Fraser Institute *Economic Freedom of the World* (EFW Ratings sheet, sub-components) and UNDP HDR composite-indices time series (1990–2023).
Raw files are never edited. Every number below is computed from them.""")

md("## 1. Setup")
code('''import os, glob, sys
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
assert os.path.exists(EFW_PATH) and os.path.exists(UNDP_PATH), "data files missing"''')

md("## 2. Load data")
code('''efw = pd.read_excel(EFW_PATH, sheet_name="EFW Ratings", header=3)
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
print("UNDP:", undp.shape, "| years:", undp.year.min(), "-", undp.year.max(), "| countries:", undp.iso3.nunique())''')

md("## 3. Inspect")
code('''print("EFW years available:", sorted(efw.Year.unique())[:8], "... annual from 2000")
sub = ["4Aii  Mean tariff rate", "4A  Tariffs", "4B  Regulatory trade barriers", "4C  Black market exchange rates",
       "2C  Property rights", "2F Contracts", "5Dii Business Permits", "Area 4 Freedom to trade internationally"]
sub = [c for c in sub if c in efw.columns]
print("Missing sub-components:", [c for c in ["4Aii  Mean tariff rate","4A  Tariffs","4B  Regulatory trade barriers","4C  Black market exchange rates","2C  Property rights","2F Contracts","5Dii Business Permits"] if c not in efw.columns])
cov = efw.groupby("Year")[sub].agg(lambda s: pd.to_numeric(s, errors="coerce").notna().sum())
print("Non-missing obs per year (selected sub-components):"); display(cov.loc[[1990,1995,2000,2005,2010,2015,2020]])
print("UNDP non-missing by variable:"); display(undp[list(VARS)].notna().sum())''')

md("## 4. Country matching (ISO3)")
code('''e_iso, u_iso = set(efw.ISO_Code.dropna()), set(undp.iso3.dropna())
print("EFW codes:", len(e_iso), "| UNDP codes:", len(u_iso), "| matched:", len(e_iso & u_iso))
print("In EFW, not in UNDP:", sorted(e_iso - u_iso))
print("(UNDP-only codes are mostly aggregates/regions, not needed.)")
SOUTH_ASIA = ["AFG","BGD","BTN","IND","MDV","NPL","PAK","LKA"]
print("South Asia in EFW:", sorted(set(SOUTH_ASIA) & e_iso), "| in UNDP:", sorted(set(SOUTH_ASIA) & u_iso))
NAME = efw.drop_duplicates("ISO_Code").set_index("ISO_Code")["Countries"]''')

md("""## 5. Candidate exploration
**Rule (applied identically to every indicator):** a country is a candidate case if its EFW sub-component score rose by **≥ 2.0 points** (0–10 scale) between **1995 and 2005**, both observations exist, and it has UNDP GNI per capita for 1990–2023.
Why 1995–2005? UNDP starts in 1990, so a reform needs ≥5 years of UNDP history before it and ≥10 after. EFW is 5-yearly before 2000, so the exact year is *not* read from EFW; it is dated later from public sources.
The threshold is a scan parameter, not a final selection. Final selection and reform dates come in section 6–7.""")
code('''A, B, THRESH = 1995, 2005, 2.0
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
display(scan)''')
code('''# Peek at the top countries for each indicator (so cases are chosen by rule, not by eye)
for c, hit in detail.items():
    print(f"\\n{c}: {len(hit)} countries rose >= {THRESH}")
    print(", ".join(f"{NAME.get(i,i)} ({v:+.1f})" for i, v in hit.head(12).items()))''')
sys.path.insert(0, "research")
from nb_part2 import add_part2
add_part2(C, md, code)

nb["cells"] = C
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nbf.write(nb, "analysis.ipynb")
print("wrote analysis.ipynb")
