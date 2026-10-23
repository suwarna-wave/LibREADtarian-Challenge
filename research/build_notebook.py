"""Build the portable main notebook. All numerical calculations live in analysis_steps.py."""
from pathlib import Path
import base64,zlib,hashlib,re,nbformat,json
root=Path(__file__).resolve().parents[1]
embedded={}
for name in ['EFW_original.xlsx','UNDP_original.csv']:
    data=(root/'data'/name).read_bytes()
    embedded['data/'+name]={'sha256':hashlib.sha256(data).hexdigest(),'content':base64.b64encode(zlib.compress(data,9)).decode()}
source=(root/'research/analysis_steps.py').read_text()
source=source.replace('__PRESENTATION_LAYOUT__',repr(json.loads((root/'research/presentation_layout_2026-10-22.json').read_text())))
source=source.replace('__COMPACT_LAYOUT__',repr(json.loads((root/'research/presentation_layout.json').read_text())))
source=source.replace('__EMBEDDED_INPUTS__',repr(embedded)).replace('__DATES_LITERAL__',repr((root/'research/reform_dates.csv').read_text()))
nb=nbformat.v4.new_notebook();cells=[];chart_cells={}
for block in source.split('# %% ')[1:]:
    mode,body=block.split('\n',1);body=body.rstrip()
    if mode=='md':cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        compile(body,'notebook-cell','exec')
        cells.append(nbformat.v4.new_code_cell(body))
        if 'ci=pd.DataFrame(INDEX)' in body:index_cell=len(cells)-1
        if '# PUBLICATION CHARTS:' in body:
            cells[-1].source='PUBLICATION_CELL = '+str(len(cells))+'\n'+cells[-1].source
        if '# COMPACT CHARTS:' in body:
            cells[-1].source='COMPACT_CELL = '+str(len(cells))+'\n'+cells[-1].source
        m=re.search(r'# FIGURE (\d+):',body)
        if m:chart_cells['Fig'+m.group(1)]=len(cells)
# Chart positions are generated from actual notebook order, not guessed.
cells[index_cell].source += '\nCHART_CELLS = '+repr(chart_cells)+'\nci["notebook_cell"]=ci.figure.map(CHART_CELLS)\nci.to_csv(ROOT/"figures/chart_index.csv",index=False)\ndisplay(ci)'
nb.cells=cells
nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'ldd':{'participant':'Suwarna Pyakurel','date':'2026-10-23','embedded_original_inputs':True,'source_file':'research/analysis_steps.py'}}
nbformat.write(nb,root/'LDD2026_SuwarnaPyakurel_Working.ipynb')
print('Built',len(cells),'cells;',chart_cells)
