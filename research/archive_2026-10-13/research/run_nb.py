"""Execute analysis.ipynb; on failure print the failing cell's source + error. Usage: python research/run_nb.py"""
import nbformat, sys
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

nb = nbformat.read("analysis.ipynb", as_version=4)
client = NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": "."}})
try:
    client.execute()
    nbformat.write(nb, "analysis.ipynb")
    print("OK: notebook executed top to bottom")
except CellExecutionError as e:
    idx = next((i for i, c in enumerate(nb.cells) if c.cell_type == "code" and any(o.get("output_type") == "error" for o in c.get("outputs", []))), None)
    print("FAILED in cell", idx and idx + 1)
    if idx is not None:
        print(nb.cells[idx].source[:1500])
    print(str(e)[-900:])
    sys.exit(1)
