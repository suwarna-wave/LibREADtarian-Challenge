"""Run the working notebook with this interpreter; use from the project root."""
from pathlib import Path
import sys,nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
root=Path(__file__).resolve().parents[1]
path = root/'analysis.ipynb'
if not path.exists():
    path = next(root.glob('LDD2026_*_Working.ipynb'))
nb=nbformat.read(path,as_version=4)
km=KernelManager(kernel_name='python3');km.kernel_spec.argv=[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}']
NotebookClient(nb,timeout=300,km=km,resources={'metadata':{'path':str(root)}}).execute()
nbformat.write(nb,path)
print('PASS: all notebook cells executed. Check outputs/validation.json for computational and external statuses.')
