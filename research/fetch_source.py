"""Download a URL (follows redirects, time-limited), save to research/sources/, and print keyword contexts.
Usage: python research/fetch_source.py NAME URL "regex" [maxhits]"""
import sys, re, subprocess, pathlib, io

name, url, pat = sys.argv[1], sys.argv[2], sys.argv[3]
maxhits = int(sys.argv[4]) if len(sys.argv) > 4 else 8
out = pathlib.Path("research/sources") / name
r = subprocess.run(["curl", "-sSL", "--max-time", "45", "-A", "Mozilla/5.0", "-o", str(out), "-w", "%{url_effective} %{http_code} %{content_type}", url],
                   capture_output=True, text=True)
print("FETCH:", r.stdout, r.stderr[:200])
data = out.read_bytes() if out.exists() else b""
if data[:4] == b"%PDF":
    import pypdf
    text = " ".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(data)).pages)
else:
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", data.decode("utf-8", "ignore"), flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)
print("chars:", len(text))
n = 0
for m in re.finditer(pat, text, re.I):
    print(" >>", text[max(0, m.start() - 220): m.end() + 260]); n += 1
    if n >= maxhits: break
if n == 0: print(" (no match)")
