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

# %% md
## 9. Archived extended presentation exports and disclosure (22 October)
This cell preserves the figures and historical slide mapping of the older extended presentation. Its 13-panel index is archival, not the current submission index. No new outcome estimates are added. Full tariff, trade-institution and income histories remain available here for verification. Section 10, the final compact cell, produces the six consecutive figure numbers and the canonical chart index for the current 14-page PDF. Notebook cell positions count both markdown and code cells from 1.

OpenAI Codex helped with coding, resolving errors, and researching supporting articles. It also assisted with dataset inspection, figures, reproducibility checks, documentation, slide text, speaker notes and presentation assembly. Suwarna Pyakurel is responsible for reviewing and explaining all submitted claims. This is a solo entry. Organiser scope/release acceptance, declaration approval and the exact deadline remain unconfirmed.
# %% code
# PUBLICATION CHARTS: existing values, readable panels and final slide mapping.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'axes.labelsize':16,'xtick.labelsize':14,'ytick.labelsize':14,'axes.titlesize':17,'legend.fontsize':12})
PUBLICATION_LAYOUT = __PRESENTATION_LAYOUT__
PUB_ROWS=[]
def publication_save(fig,key,title,caption,data):
    fig.suptitle(title,x=.015,y=.99,ha='left',fontsize=18,fontweight='bold',color=INK)
    fig.text(.015,.015,caption,ha='left',va='bottom',fontsize=11,color='#3D4F59')
    fig.tight_layout(rect=(0,.15,1,.91))
    for ext in ('png','pdf'): fig.savefig(ROOT/'figures'/f'{key}.{ext}',dpi=180,facecolor='white')
    data.to_csv(ROOT/'outputs'/f'{key}_data.csv',index=False)
    PUB_ROWS.append(dict(figure=key,slide=PUBLICATION_LAYOUT[key],title=title,data=f'outputs/{key}_data.csv',file=f'figures/{key}.png',notebook_cell=PUBLICATION_CELL))
    display(fig);plt.close(fig)

# Figure 1: all ten qualify; the main slide uses a legible endpoint comparison.
d=selected.reset_index().rename(columns={'ISO_Code':'iso3','index':'iso3'})
if 'iso3' not in d: d=d.rename(columns={d.columns[0]:'iso3'})
d['reduction_pp']=-d.change_pp
d['main_sample']=d.iso3.isin(MAIN)
fig,ax=plt.subplots(figsize=(12,6.3))
y=np.arange(len(d));ax.barh(y,d.reduction_pp,color=[BLUE if v else GREY for v in d.main_sample])
ax.set_yticks(y,[c+(' *' if not m else '') for c,m in zip(d.country,d.main_sample)]);ax.invert_yaxis()
ax.set_xlim(0,d.reduction_pp.max()*1.22);ax.set_xlabel('Fall in observed mean tariff, 1995–2005 (percentage points)')
for j,row in enumerate(d.itertuples()): ax.text(row.reduction_pp+.7,j,f'{row.reduction_pp:.1f}',va='center',fontsize=14)
ax.spines[['top','right']].set_visible(False)
publication_save(fig,'Fig1','Figure 1. Ten countries meet the same tariff-reduction rule',
 'Source: supplied Fraser EFW Ratings, raw mean tariff (%), 1995 and 2005; n=10 of 98 eligible countries.\n*Bangladesh/Kenya: timing uncertain, excluded from eight-case main event analysis; retained in separate checks.',d)

# Full observed tariff histories: retain all ten, split into two legible pages.
for part,group in zip(['a','b'],[ALL[:5],ALL[5:]]):
    d=policy[policy.iso3.isin(group)&policy.tariff_pct.notna()].sort_values(['iso3','year'])
    fig,axes=plt.subplots(2,3,figsize=(12,6.6),sharey=True)
    for ax,iso in zip(axes.flat,group):
        s=d[d.iso3.eq(iso)];ax.plot(s.year,s.tariff_pct,'o-',ms=3,color=BLUE if iso in MAIN else GREY)
        if iso in DATE:ax.axvline(DATE[iso],ls='--',color=RED,lw=1.4)
        ax.set_title(NAME[iso]+(' *' if iso not in MAIN else ''));ax.set_ylim(bottom=0);ax.set_xlabel('Year');ax.set_ylabel('Mean tariff (%)',fontsize=13)
        ax.set_xticks([1980,2000,2024]);ax.tick_params(labelsize=12)
    for ax in list(axes.flat)[len(group):]:ax.set_visible(False)
    publication_save(fig,'Fig1H'+part,f'Figure 1H{part}. Full observed tariff histories',
      'Source: supplied Fraser EFW Ratings; observed 1975–2024; n=5 shown per page, 10 across both pages.\nDashed=reform year; *no main date. Five-yearly before 2000, annual afterwards; no interpolation.',d)

# Chain-linked institutional context: not a tariff-only outcome.
for part,group in zip(['a','b'],[MAIN[:4],MAIN[4:]]):
    d=linked[linked.iso3.isin(group)&linked.trade_panel.notna()][['iso3','year','trade_panel']].sort_values(['iso3','year'])
    fig,axes=plt.subplots(2,2,figsize=(12,6.7),sharey=True)
    for ax,iso in zip(axes.flat,group):
        s=d[d.iso3.eq(iso)];ax.plot(s.year,s.trade_panel,'o-',ms=3,color=BLUE);ax.axvline(DATE[iso],ls='--',color=RED)
        ax.set_title(NAME[iso]);ax.set_ylim(0,10);ax.set_xlabel('Year');ax.set_ylabel('Area 4 (0–10)',fontsize=14);ax.set_xticks([1980,2000,2024])
    publication_save(fig,'Fig2'+part,f'Figure 2{part}. Broader freedom to trade: institutional context',
      'Source: Fraser chain-linked EFW Panel, Area 4, available 1970–2024; n=4 per page, 8 across both.\nHigher=greater trade freedom; includes non-tariff rules. Dashed=reform year. BGD/KEN: no main date.',d)

# Raw income histories: full period and clearly labelled country-specific scales.
for part,group in zip(['a','b','c'],[ALL[:4],ALL[4:8],ALL[8:]]):
    d=undp[undp.iso3.isin(group)][['iso3','year','gnipc']].sort_values(['iso3','year'])
    rows=2 if len(group)>2 else 1
    fig,axes=plt.subplots(rows,2,figsize=(12,6.6),squeeze=False)
    for ax,iso in zip(axes.flat,group):
        s=d[d.iso3.eq(iso)];ax.plot(s.year,s.gnipc,lw=2.2,color=BLUE)
        if iso in DATE:ax.axvline(DATE[iso],color=RED,ls='--')
        ax.set_title(NAME[iso]);ax.set_xlabel('Year');ax.set_ylabel('GNI/person (2021 PPP$)',fontsize=13);ax.set_xticks([1990,2005,2023])
        ax.tick_params(labelsize=12)
    publication_save(fig,'Fig3'+part,f'Figure 3{part}. Full income histories before event comparisons',
      f'Source: UNDP HDR25 components, 1990–2023; n={len(group)} shown, 10 across three pages. Country-specific y-scales.\nDashed=reform year where documented. Later years provide context beyond the ten-year event window.',d)

# Figures 4–6 and 8: restyle the same exported values for projected readability.
d=panel[['iso3','year','event_time','gni_index']].copy();fig,ax=plt.subplots(figsize=(12,6.4))
for iso in MAIN:
    s=d[d.iso3.eq(iso)].sort_values('event_time');ax.plot(s.event_time,s.gni_index,lw=1.7,alpha=.85,color=COLORS[iso],label=NAME[iso])
med=d.groupby('event_time').gni_index.median();cnt=d.groupby('event_time').gni_index.count()
ax.plot(med.index,med.values,color=INK,lw=3.5,label='Median (changing pre-sample)')
bal=d[d.iso3.isin(balanced_iso)].groupby('event_time').gni_index.median();ax.plot(bal.index,bal.values,color=GOLD,lw=3,ls=':',label='Fixed-member median (n=5)')
ax.axvline(0,ls='--',color=RED);ax.axhline(100,color=GREY,lw=1);ax.set_xlabel('Years from documented reform');ax.set_ylabel('Real GNI/person index (reform year=100)');ax.legend(ncol=2,fontsize=11,frameon=False,loc='upper left')
d['event_year_n']=d.event_time.map(cnt)
publication_save(fig,'Fig4','Figure 4. Income increased in seven of eight cases',
 'Source: UNDP HDR25; event −5 to +10, calendar coverage 1990–2008; n=8 after reform, 5–8 before.\nAll series equal 100 at zero by construction. BGD/KEN: separate timing checks. This is not a causal estimate.',d)

d=res.copy();fig,ax=plt.subplots(figsize=(12,6.5));x=np.arange(len(d));w=.26
ax.bar(x-w,d.pre5_cagr_pct,w,color=GREY,label='Five-year growth before reform');ax.bar(x,d.post_cagr_pct,w,color=BLUE,label='Ten-year growth after reform');ax.bar(x+w,d.benchmark_cagr_pct,w,color=GOLD,label='Same-years comparison median')
ax.axhline(0,color=INK);ax.set_xticks(x,d.country,rotation=25,ha='right');ax.set_ylabel('Annualised real GNI/person growth (%)');ax.legend(fontsize=11,frameon=False)
publication_save(fig,'Fig5','Figure 5. Growth accelerated in three of five complete comparisons',
 'Source: UNDP HDR25; reforms 1991–1998, ten-year endpoints 2001–2008; n=8; full prehistory n=5.\nMissing grey bars=unavailable, not zero. Comparison n=148–152; excludes all ten screened countries.',d)

d=res.sort_values('excess_pp');fig,ax=plt.subplots(figsize=(12,6.2));ax.barh(d.country,d.excess_pp,color=[BLUE if v>0 else RED for v in d.excess_pp]);ax.axvline(0,color=INK)
ax.set_xlabel('Post-reform growth minus comparison median (percentage points/year)')
publication_save(fig,'Fig6','Figure 6. Four of eight countries exceeded the benchmark',
 'Source: UNDP HDR25; ten-year windows starting 1991–1998; n=8 dated cases; median difference +0.06 pp/year.\nRed=below benchmark, not necessarily falling income. CIV/SEN share a reform; benchmark is not a causal control.',d)

# Figure 7 has two separate axes, not a dual y-axis: counts and median gaps.
d=rob[rob['check'].str.startswith('date shift')].copy();labels=d['check'].str.replace('date shift ','')
fig,axes=plt.subplots(1,2,figsize=(12,6.0));a,b=axes
a.bar(labels,d.above,color=BLUE);a.set_ylim(0,9);a.set_ylabel('Countries above benchmark');a.set_title('(a) Count / valid countries')
for j,row in enumerate(d.itertuples()):a.text(j,row.above+.13,f'{int(row.above)}/{int(row.n)}',ha='center',fontsize=16)
b.bar(labels,d.median_excess_pp,color=[BLUE if v>=0 else RED for v in d.median_excess_pp]);b.axhline(0,color=INK);b.set_ylim(-.27,.31);b.set_ylabel('Median growth gap (pp/year)');b.set_title('(b) Median difference changes sign')
for j,row in enumerate(d.itertuples()):b.text(j,row.median_excess_pp+(.015 if row.median_excess_pp>=0 else -.015),f'{row.median_excess_pp:+.2f}',ha='center',va='bottom' if row.median_excess_pp>=0 else 'top',fontsize=14)
for ax in axes:ax.set_xlabel('Years added to documented reform date')
publication_save(fig,'Fig7','Figure 7. Small timing changes affect the result',
 'Source: UNDP HDR25; ten-year windows, shifted reform years 1989–2000; n=7–8 valid cases.\n−2 loses one unavailable income start. Other checks: outputs/robustness.csv. No causal effect is identified.',d)

peers=['NPL','BGD','IND','PAK','LKA'];d=policy[policy.iso3.isin(peers)&policy.tariff_pct.notna()][['iso3','year','tariff_pct']].sort_values(['iso3','year'])
fig,ax=plt.subplots(figsize=(12,6.2))
for iso in peers:
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.tariff_pct,'o-',ms=3,lw=3.5 if iso=='NPL' else 1.7,label=NAME[iso])
ax.set_ylim(bottom=0);ax.set_ylabel('Observed mean tariff (%)');ax.set_xlabel('Year');ax.legend(frameon=False,ncol=3,fontsize=12)
publication_save(fig,'Fig8','Figure 8. Nepal began from a different tariff position',
 'Source: Fraser EFW Ratings, raw mean tariff, observed 1980–2024; n=5 regional peers; thick line=Nepal.\nNepal 2024: 12.9%. An average is not a statutory maximum or an estimate of current fiscal costs.',d)

ci=pd.DataFrame(PUB_ROWS)
ci.to_csv(ROOT/'figures/chart_index.csv',index=False)
assert ci.figure.is_unique and len(ci)==13
assert all((ROOT/p).exists() for p in ci.file) and all((ROOT/p).exists() for p in ci.data)
assert (res.post_cagr_pct.gt(0).sum(),res.excess_pp.gt(0).sum(),res.pre5_cagr_pct.notna().sum())==(7,4,5)
print('FINAL PUBLICATION CHECKS PASSED: 13 displayed chart panels, unchanged outcome calculations.')
display(ci)

# %% md
## 10. Compact submission: six displayed figures and a four-slide appendix
The final deck has ten content slides and four verification appendix slides. The six displayed figures below are numbered consecutively. Their values are recalculated from the same in-memory analysis tables, not retyped. Earlier charts, full histories, chain-linked panel context and extended sensitivity results remain in this working file and in archived exports; they are not additional presentation pages. Figure and CSV locations refer to the compact submission only.

The 20% cap is a policy design choice, not an optimum identified by this analysis. The working-file disclosure remains accurate: OpenAI Codex helped with coding, resolving errors, and researching supporting articles. It also assisted with dataset inspection, figures, reproducibility checks, documentation, slide text, speaker notes and presentation assembly. The participant is responsible for reviewing and explaining the work. Declaration approval, dataset scope/release acceptance, deadline and upload limits remain unconfirmed.
# %% code
# COMPACT CHARTS: Figures 1–6; identical data, updated presentation identifiers.
COMPACT_LAYOUT = __COMPACT_LAYOUT__
for folder in ('figures/compact','outputs/compact'):(ROOT/folder).mkdir(parents=True,exist_ok=True)
# Keep the previous chart-index mapping separately; the root index is canonical.
ci.to_csv(ROOT/'figures/chart_index_2026-10-22.csv',index=False)
COMPACT_ROWS=[]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.labelsize':14,'xtick.labelsize':12,'ytick.labelsize':12,'axes.titlesize':14,'legend.fontsize':11})
def compact_save(fig,number,title,caption,data):
    key=f'Fig{number}'
    fig.suptitle(f'Figure {number}. {title}',x=.015,y=.99,ha='left',fontsize=17,fontweight='bold',color=INK)
    fig.text(.015,.012,caption,ha='left',va='bottom',fontsize=11,color='#3D4F59')
    fig.tight_layout(rect=(0,.16,1,.91))
    for ext in ('png','pdf'):fig.savefig(ROOT/'figures/compact'/f'{key}.{ext}',dpi=180,facecolor='white')
    data.to_csv(ROOT/'outputs/compact'/f'{key}_data.csv',index=False)
    COMPACT_ROWS.append(dict(figure=key,slide=COMPACT_LAYOUT[key],title=title,data=f'outputs/compact/{key}_data.csv',file=f'figures/compact/{key}.png',notebook_cell=COMPACT_CELL))
    display(fig);plt.close(fig)

d=selected.reset_index().rename(columns={'ISO_Code':'iso3','index':'iso3'})
if 'iso3' not in d:d=d.rename(columns={d.columns[0]:'iso3'})
d['reduction_pp']=-d.change_pp;d['main_sample']=d.iso3.isin(MAIN)
fig,ax=plt.subplots(figsize=(12.2,4.9));y=np.arange(len(d));ax.barh(y,d.reduction_pp,color=[BLUE if b else GREY for b in d.main_sample])
ax.set_yticks(y,[c+(' *' if not b else '') for c,b in zip(d.country,d.main_sample)]);ax.invert_yaxis();ax.set_xlim(0,d.reduction_pp.max()*1.15)
ax.set_xlabel('Reduction in observed mean tariff, 1995–2005 (percentage points)')
for j,r in enumerate(d.itertuples()):ax.text(r.reduction_pp+.7,j,f'{r.reduction_pp:.1f}',va='center',fontsize=12)
ax.spines[['top','right']].set_visible(False)
compact_save(fig,1,'All ten countries meet the same tariff-reduction rule',
 'Fraser EFW Ratings, raw mean tariff, 1995 and 2005; n=10 of 98 eligible countries. Bar origin=0.\n*Bangladesh/Kenya: no precise main tariff-event date; excluded from eight-case main analysis, retained in timing checks.',d)

d=panel[['iso3','year','event_time','gni_index']].copy();fig,ax=plt.subplots(figsize=(12.2,4.9))
for iso in MAIN:
    s=d[d.iso3.eq(iso)].sort_values('event_time');ax.plot(s.event_time,s.gni_index,lw=1.6,color=COLORS[iso],label=NAME[iso])
med=d.groupby('event_time').gni_index.median();cnt=d.groupby('event_time').gni_index.count()
ax.plot(med.index,med.values,color=INK,lw=3.2,label='Median (changing pre-sample)')
fixed=d[d.iso3.isin(balanced_iso)].groupby('event_time').gni_index.median();ax.plot(fixed.index,fixed.values,color=GOLD,lw=2.8,ls=':',label='Fixed-member median (n=5)')
ax.axvline(0,ls='--',color=RED);ax.axhline(100,color=GREY,lw=1);ax.set_xlabel('Years from documented reform');ax.set_ylabel('Real GNI/person index (reform year=100)');ax.legend(ncol=3,fontsize=10.5,frameon=False,loc='upper left')
d['event_year_n']=d.event_time.map(cnt)
compact_save(fig,2,'Income rose in seven of eight cases over ten years',
 'UNDP HDR25; event −5 to +10, observed calendar years 1990–2008; n=8 after reform, 5–8 before.\nBGD/KEN: separate timing checks. All series equal 100 at zero by construction; medians do not identify a causal effect.',d)

d=res.copy();fig,ax=plt.subplots(figsize=(12.2,4.9));x=np.arange(len(d));w=.26
ax.bar(x-w,d.pre5_cagr_pct,w,color=GREY,label='Five-year growth before');ax.bar(x,d.post_cagr_pct,w,color=BLUE,label='Ten-year growth after');ax.bar(x+w,d.benchmark_cagr_pct,w,color=GOLD,label='Same-years comparison median')
ax.axhline(0,color=INK);ax.set_xticks(x,d.country,rotation=18,ha='right');ax.set_ylabel('Annualised real GNI/person growth (%)');ax.legend(fontsize=10.5,frameon=False)
compact_save(fig,3,'Growth accelerated in three of five complete comparisons',
 'UNDP HDR25; reforms 1991–1998; ten-year endpoints 2001–2008; n=8, complete five-year prehistory n=5.\nMissing grey bars=unavailable, not zero. Benchmark n=148–152; all ten screened countries excluded. Bars start at zero.',d)

d=res.sort_values('excess_pp');fig,ax=plt.subplots(figsize=(12.2,4.9));ax.barh(d.country,d.excess_pp,color=[BLUE if v>0 else RED for v in d.excess_pp]);ax.axvline(0,color=INK)
ax.set_xlabel('Post-reform growth minus comparison median (percentage points/year)')
compact_save(fig,4,'Half exceeded the benchmark; the median gap was near zero',
 'UNDP HDR25; ten-year windows beginning 1991–1998; n=8; median gap +0.06 pp/year. Bars start at zero.\nRed=below benchmark, not necessarily falling income. BGD/KEN: timing checks only. CIV/SEN share a regional reform.',d)

d=rob[rob['check'].str.startswith('date shift')].copy();labels=d['check'].str.replace('date shift ','')
fig,(a,b)=plt.subplots(1,2,figsize=(12.2,4.9));a.bar(labels,d.above,color=BLUE);a.set_ylim(0,9);a.set_ylabel('Countries above benchmark');a.set_title('(a) Count / valid countries')
for j,r in enumerate(d.itertuples()):a.text(j,r.above+.14,f'{int(r.above)}/{int(r.n)}',ha='center',fontsize=13)
b.bar(labels,d.median_excess_pp,color=[BLUE if v>=0 else RED for v in d.median_excess_pp]);b.axhline(0,color=INK);b.set_ylim(-.27,.31);b.set_ylabel('Median growth gap (pp/year)');b.set_title('(b) Median difference changes sign')
for j,r in enumerate(d.itertuples()):b.text(j,r.median_excess_pp+(.012 if r.median_excess_pp>=0 else -.012),f'{r.median_excess_pp:+.2f}',ha='center',va='bottom' if r.median_excess_pp>=0 else 'top',fontsize=12)
for ax in (a,b):ax.set_xlabel('Years added to documented reform date')
compact_save(fig,5,'Small timing changes reverse the median comparison',
 'UNDP HDR25; ten-year windows, shifted reform years 1989–2000; n=7–8 valid cases. Bars start at zero.\n−2 omits one unavailable income start; counts use valid cases. Complete sensitivity results: outputs/robustness.csv.',d)

peers=['NPL','BGD','IND','PAK','LKA'];d=policy[policy.iso3.isin(peers)&policy.tariff_pct.notna()][['iso3','year','tariff_pct']].sort_values(['iso3','year'])
fig,ax=plt.subplots(figsize=(12.2,4.9))
for iso in peers:
    s=d[d.iso3.eq(iso)];ax.plot(s.year,s.tariff_pct,'o-',ms=2.5,lw=3.3 if iso=='NPL' else 1.6,label=NAME[iso])
ax.set_ylim(bottom=0);ax.set_ylabel('Observed mean tariff (%)');ax.set_xlabel('Year');ax.legend(frameon=False,ncol=3,fontsize=11)
compact_save(fig,6,'Nepal began from a different tariff position',
 'Fraser EFW Ratings, raw mean tariff, observed 1980–2024; n=5 regional peers; thick line=Nepal; 2024 mean=12.9%.\nHistorical context only. A mean is not a statutory maximum, a current rate schedule, or a fiscal-impact estimate.',d)

ci=pd.DataFrame(COMPACT_ROWS);ci.to_csv(ROOT/'figures/chart_index.csv',index=False)
assert len(ci)==6 and list(ci.figure)==[f'Fig{i}' for i in range(1,7)]
assert all((ROOT/p).exists() for p in ci.file) and all((ROOT/p).exists() for p in ci.data)
assert (res.post_cagr_pct.gt(0).sum(),res.excess_pp.gt(0).sum(),res.pre5_cagr_pct.notna().sum())==(7,4,5)
print('COMPACT CHECKS PASSED: six numbered figures; existing numerical results unchanged.');display(ci)
