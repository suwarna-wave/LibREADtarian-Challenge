"""Check prepared outputs and report external items separately."""
from pathlib import Path
import sys,json,hashlib,zipfile,io
import pandas as pd
import nbformat
from pypdf import PdfReader
from pptx import Presentation
root=Path(__file__).resolve().parents[1]
notebook_path = root/'analysis.ipynb'
if not notebook_path.exists():
    notebook_path = next(root.glob('LDD2026_*_Working.ipynb'))
nb=nbformat.read(notebook_path,as_version=4)
code=[c for c in nb.cells if c.cell_type=='code']
assert all(c.execution_count is not None for c in code)
assert not any(o.output_type=='error' for c in code for o in c.get('outputs',[]))
assert len(code)==17
ci=pd.read_csv(root/'figures/chart_index.csv')
for row in ci.itertuples():
 assert f'# FIGURE {row.figure[3:]}:' in nb.cells[int(row.notebook_cell)-1].source
 assert (root/row.file).exists() and (root/row.data).exists()
 facts=pd.read_csv(root/row.data)
 assert not facts.empty
assert len(ci)==8
results=pd.read_csv(root/'outputs/growth_results.csv');policy=pd.read_csv(root/'outputs/selected_cases.csv')
assert len(results)==8 and len(policy)==10
assert results.post_cagr_pct.notna().all()
assert results.loc[results.pre_years_available.lt(5),'pre5_cagr_pct'].isna().all()
assert (results.excess_pp - (results.post_cagr_pct-results.benchmark_cagr_pct)).abs().lt(1e-10).all()
figure_results=pd.read_csv(root/'outputs/Fig6_data.csv').sort_values('iso3')
expected=results.sort_values('iso3')
assert (figure_results.excess_pp.to_numpy()==expected.excess_pp.to_numpy()).all()
context=json.loads((root/'research/submission_context.json').read_text())
label='LDD2026_'+context['label']
pdf=PdfReader(root/'deck'/f'{label}_Deck.pdf');ppt=Presentation(root/'deck'/f'{label}_Deck.pptx')
manifest=json.loads((root/'deck/slide_manifest.json').read_text())
assert len(pdf.pages)==len(ppt.slides)==len(manifest)==16
assert sum(not s['appendix'] for s in manifest)==10
assert all(s['appendix'] for s in manifest[10:])
assert 'Suwarna Pyakurel' in pdf.metadata.author
assert '4/8' in pdf.pages[6].extract_text()
assert '3 of 5' in pdf.pages[5].extract_text()
assert '20%' in pdf.pages[8].extract_text()
links=sum(len(p.get('/Annots',[])) for p in pdf.pages)
assert links>=19
with zipfile.ZipFile(root/'deck'/f'{label}_Deck.pptx') as z:
 media=[z.read(p) for p in z.namelist() if p.startswith('ppt/media/')]
 hashes={hashlib.sha256(v).hexdigest() for v in media}
 for p in (root/'figures').glob('Fig*.png'):assert hashlib.sha256(p.read_bytes()).hexdigest() in hashes
clean=json.loads((root/'outputs/clean_runtime_verification.json').read_text())
assert clean['embedded_originals_restored_and_hash_matched'] and clean['errors']==0
report={'computational_checks':'PASS','executed_code_cells':len(code),'figures':len(ci),'main_cases':len(results),'screened_cases':len(policy),'pdf_pages':len(pdf.pages),'content_slides':10,'appendix_pages':6,'pdf_source_links':links,'pptx_embeds_exact_notebook_pngs':True,'fresh_directory_execution':True,'external_pending':['Participant review','Organiser dataset scope/release acceptance','Approved dataset declaration','Exact deadline','Signed-out sharing test if using a link','Participant submission']}
(root/'outputs/submission_validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
