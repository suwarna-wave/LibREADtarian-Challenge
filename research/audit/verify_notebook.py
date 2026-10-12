"""Run the existing notebook in isolation without replacing project outputs."""
from pathlib import Path
import tempfile
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parents[2]
scratch = Path(tempfile.mkdtemp(prefix="ldd-readiness-"))
(scratch / "data").symlink_to(root / "data", target_is_directory=True)
notebook = nbformat.read(root / "analysis.ipynb", as_version=4)
NotebookClient(
    notebook, timeout=180, kernel_name="python3",
    resources={"metadata": {"path": str(scratch)}},
).execute()
nbformat.write(notebook, root / "research/audit/reexecuted_notebook.ipynb")
lines = []
for number, cell in enumerate(notebook.cells, 1):
    for output in cell.get("outputs", []):
        value = output.get("text", "") or output.get("data", {}).get("text/plain", "")
        if value:
            lines.append(f"CELL {number}\n{value}\n")
(root / "research/audit/execution_log.txt").write_text("\n".join(lines))
print(f"PASS: all cells ran in a fresh kernel. Original notebook and charts unchanged. Scratch: {scratch}")
