"""
Assemble slides.html from _slides/_head.html, numbered slide files, _slides/_foot.html.
Run:  python build.py
"""
import os, glob

BASE = os.path.dirname(os.path.abspath(__file__))
DIR  = os.path.join(BASE, "_slides")
OUT  = os.path.join(BASE, "slides.html")

with open(os.path.join(DIR, "_head.html")) as f:
    parts = [f.read()]

for path in sorted(glob.glob(os.path.join(DIR, "[0-9]*.html"))):
    with open(path) as f:
        parts.append("\n" + f.read())

with open(os.path.join(DIR, "_foot.html")) as f:
    parts.append(f.read())

with open(OUT, "w") as f:
    f.write("".join(parts))

print(f"Built {OUT}  ({len(parts)-2} slides)")
