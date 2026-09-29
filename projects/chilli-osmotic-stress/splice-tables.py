#!/usr/bin/env python3
"""Splice populated tables + verified reference list into REVIEW-final.md.

ONE-SHOT: the staging files _tables.md and _refs.md were deleted after the
splice succeeded, so REVIEW-final.md is the single source of truth. Re-running
this script is neither possible nor needed; it is kept as the audit record of
the table renumbering and the three late citations added at splice time.
"""

import pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE / "REVIEW-final.md"

text = SRC.read_text(encoding="utf-8")
tables = (HERE / "_tables.md").read_text(encoding="utf-8")
refs = (HERE / "_refs.md").read_text(encoding="utf-8")

fail = []

# ---- 1. Three additional in-text citations --------------------------------
adds = [
    ("with the reasons now understood: *Agrobacterium* induces a strong immune response in pepper, and the crop has low regeneration efficiency.",
     "with the reasons now understood: *Agrobacterium* induces a strong immune response in pepper, and the crop has low regeneration efficiency (Liu et al., 2024)."),
    ("Eggplant demonstrates a strategy both other crops under-use: systematic exploitation of wild relatives.",
     "Eggplant demonstrates a strategy both other crops under-use: systematic exploitation of wild relatives (Kouassi et al., 2021)."),
    ("BSA-seq is a reasonable option in pepper, but not the near-free one it is in small-genome crops.",
     "BSA-seq is a reasonable option in pepper, but not the near-free one it is in small-genome crops. Its extension to outcross populations (OcBSA) widens its applicability beyond inbred-line crosses (Zhang et al., 2024)."),
]
for old, new in adds:
    if text.count(old) != 1:
        fail.append((text.count(old), old[:70]))
    else:
        text = text.replace(old, new, 1)

# ---- 2. Split off the old tables + bibliography ---------------------------
body, marker, rest = text.partition("## Tables")
if not marker:
    fail.append(("no '## Tables' marker", ""))
notes_idx = rest.index("## Notes for the author")
notes = rest[notes_idx:]

# ---- 3. Renumber tables in the body (before the Tables section) ----------
body = body.replace("Table 7", "Table 8")
body = body.replace("Table 6", "Table 7")
cross = "**Table 5** — Cross-crop comparison of resources and strategies by developmental stratum."
if body.count(cross) != 1:
    fail.append((body.count(cross), cross[:60]))
body = body.replace(cross, "**Table 6** — Cross-crop comparison of resources and strategies by developmental stratum.")

if fail:
    print("FAILED:")
    for n, s in fail:
        print(f"  count={n}  {s!r}")
    raise SystemExit(1)

out = body + tables.rstrip() + "\n\n---\n\n" + refs.rstrip() + "\n\n---\n\n" + notes
SRC.write_text(out, encoding="utf-8")
print("Spliced OK.")
print(f"Words total: {len(out.split())}")
print(f"Tables in file: {sorted(set(__import__('re').findall(r'Table [0-9]', out)))}")
