#!/usr/bin/env python3
"""
Build a Journal of Horticultural Sciences submission file (.docx) from REVIEW-final.md.

Applies the JHS Author Guidelines:
  * Times New Roman: 14 pt title, 12 pt body
  * 1.5 line spacing, 2.5 cm margins on A4
  * figures and tables placed IN the text at their first mention, not at the end
  * blinded: no author names anywhere, including file properties
  * APA-style reference list

Usage
-----
    python3 make-jhs-docx.py                         # blinded, for submission
    python3 make-jhs-docx.py --named                 # with author details
    python3 make-jhs-docx.py --named --author "..." --affiliation "..." --email "..."

Output: deposit/JHS-submission.docx
"""

import argparse
import pathlib
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.shared import Cm, Pt

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "REVIEW-final.md"
FIGDIR = HERE / "figures"
OUT = HERE / "deposit"

FIGURES = [
    ("figure-1-framework.png", "Figure 1", 16.0),
    ("figure-2-peg-conversion.png", "Figure 2", 10.5),
    ("figure-3-stages.png", "Figure 3", 13.0),
    ("figure-4-evidence-map.png", "Figure 4", 16.0),
    ("figure-5-concordance-reporting.png", "Figure 5", 15.0),
]

# tables are appended directly beneath the paragraph in which they are first cited
TABLE_CITE = {
    "Table 1": "Table 1 \u2014 Osmotic agents compared",
    "Table 2": "Table 2 \u2014 Osmotic / PEG screening studies in the Solanaceae",
    "Table 3": "Table 3 \u2014 Tolerance indices",
    "Table 4": "Table 4 \u2014 Drought-responsive candidate genes in *Capsicum* and tomato",
    "Table 5": "Table 5 \u2014 Studies connecting two or more developmental stages",
    "Table 6": "Table 6 \u2014 Cross-crop comparison by developmental stratum",
    "Table 7": "Table 7 \u2014 Genotyping platforms compared",
    "Table 8": "Table 8 \u2014 Proposed minimum reporting standard",
}


# ---------------------------------------------------------------- markdown ---

def inline(par, text, size=12, base_bold=False):
    """Render **bold** and *italic* spans into a python-docx paragraph."""
    tokens = re.split(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*[^*]+?\*)", text)
    for tok in tokens:
        if not tok:
            continue
        bold, ital = base_bold, False
        if tok.startswith("***") and tok.endswith("***"):
            tok, bold, ital = tok[3:-3], True, True
        elif tok.startswith("**") and tok.endswith("**"):
            tok, bold = tok[2:-2], True
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            tok, ital = tok[1:-1], True
        run = par.add_run(tok)
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = ital


def style_doc(doc):
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(12)
    pf = st.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(6)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.5)


def para(doc, text, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, space_before=0):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    inline(p, text, size=size, base_bold=bold)
    return p


def heading(doc, text, size=12, upper=True):
    """JHS: main subheadings upper case on the left margin; sub-subheadings bold."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text.upper() if upper else text)
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(size)
    return p


def md_table(doc, lines, size=8):
    rows = []
    for ln in lines:
        if set(ln.replace("|", "").strip()) <= set("-: "):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return
    width = max(len(r) for r in rows)
    tbl = doc.add_table(rows=0, cols=width)
    tbl.style = "Table Grid"
    for i, r in enumerate(rows):
        cells = tbl.add_row().cells
        for j in range(width):
            txt = r[j] if j < len(r) else ""
            txt = re.sub(r"<br\s*/?>", " ", txt)
            p = cells[j].paragraphs[0]
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_after = Pt(1)
            inline(p, txt, size=size, base_bold=(i == 0))
    doc.add_paragraph()


# ------------------------------------------------------------------ build ---

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--named", action="store_true",
                    help="include author details (default is blinded for review)")
    ap.add_argument("--author", default="[AUTHOR NAME]")
    ap.add_argument("--affiliation", default="[Department, Institution, City, India]")
    ap.add_argument("--email", default="[corresponding.author@email]")
    args = ap.parse_args()

    text = SRC.read_text(encoding="utf-8")
    title_md = text.split("\n", 1)[0].lstrip("# ").strip()

    # ---- slice the manuscript into named blocks
    def block(start, end=None):
        i = text.find(start)
        if i == -1:
            sys.exit(f"FAIL: block not found: {start!r}")
        t = text[i + len(start):]
        if end:
            j = t.find(end)
            if j == -1:
                sys.exit(f"FAIL: end marker not found: {end!r}")
            t = t[:j]
        return t.strip("\n")

    abstract = block("## Abstract\n\n", "\n\n**Keywords:")
    keywords = re.search(r"\*\*Keywords:\*\*\s*(.*)", text).group(1).strip()
    intro = block("## 1. Introduction", "\n## 2. ")
    s2 = block("## 2. ", "\n## 3. ")
    s3 = block("## 3. ", "\n## 4. ")
    s4 = block("## 4. ", "\n## 5. ")
    s5 = block("## 5. ", "\n## 6. ")
    s6 = block("## 6. ", "\n## 7. ")
    s7 = block("## 7. ", "\n## 8. ")
    s8 = block("## 8. Future directions", "\n## 9. ")
    s9 = block("## 9. Conclusion", "\n\n---\n\n## Declarations")
    declarations = block("## Declarations\n", "\n\n## Figure legends")
    refs = block("## Reference list\n", "\n\n---\n\n## Notes for the author")

    table_blocks = {}
    for key, head in TABLE_CITE.items():
        i = text.find("### " + head)
        if i == -1:
            continue
        seg = text[i:]
        j = seg.find("\n---", len(head))
        table_blocks[key] = seg[:j if j != -1 else len(seg)].strip("\n")

    doc = Document()
    style_doc(doc)

    # ---- front matter
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    inline(p, title_md, size=14, base_bold=True)

    if args.named:
        p = doc.add_paragraph()
        r = p.add_run(args.author)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        para(doc, f"{args.affiliation}. Corresponding author e-mail: {args.email}", size=10,
             align=WD_ALIGN_PARAGRAPH.LEFT)
    else:
        para(doc, "[Author details removed for blind review]", size=10,
             align=WD_ALIGN_PARAGRAPH.LEFT)

    para(doc, "Running title: Drought screening in Capsicum and the Solanaceae", size=10,
         align=WD_ALIGN_PARAGRAPH.LEFT)

    heading(doc, "Abstract")
    para(doc, abstract)
    para(doc, f"Keywords: {keywords}")

    # ---- body, with figures and tables dropped in at first mention
    sections = [("1. INTRODUCTION", intro), ("2. " + s2.split("\n", 1)[0].strip("# "), s2),
                ("3. " + s3.split("\n", 1)[0].strip("# "), s3),
                ("4. " + s4.split("\n", 1)[0].strip("# "), s4),
                ("5. " + s5.split("\n", 1)[0].strip("# "), s5),
                ("6. " + s6.split("\n", 1)[0].strip("# "), s6),
                ("7. " + s7.split("\n", 1)[0].strip("# "), s7),
                ("8. " + s8.split("\n", 1)[0].strip("# "), s8),
                ("9. " + s9.split("\n", 1)[0].strip("# "), s9)]

    inserted_fig, inserted_tbl = set(), set()
    for head, body in sections:
        parts = body.split("\n", 1)
        heading(doc, head)
        rest = parts[1] if len(parts) > 1 else ""

        for chunk in re.split(r"\n\n+", rest):
            c = chunk.strip()
            if not c:
                continue
            if c.startswith("|"):                       # table markdown inside prose
                md_table(doc, c.split("\n"))
                continue
            if c.startswith(">"):
                para(doc, c.lstrip("> ").strip(), size=10)
                continue
            if re.fullmatch(r"-{3,}", c):
                continue
            if c.startswith("### "):
                heading(doc, c[4:].strip(), upper=False)
                continue
            if re.match(r"^[-*]\s", c):
                for item in re.split(r"\n(?=[-*]\s)", c):
                    para(doc, "\u2022 " + item.lstrip("-* ").strip())
                continue
            para(doc, c)

            # drop in any table first cited in this paragraph
            for key in TABLE_CITE:
                if key not in inserted_tbl and key in c and key in table_blocks:
                    inserted_tbl.add(key)
                    blk = table_blocks[key].split("\n")
                    cap = next((l for l in blk if l.startswith("### ")), None)
                    if cap:
                        heading(doc, cap[4:].strip(), size=11, upper=False)
                    md_table(doc, [l for l in blk if l.startswith("|")])
            # drop in any figure first cited in this paragraph
            for fname, label, width in FIGURES:
                if label not in inserted_fig and label in c:
                    path = FIGDIR / fname
                    if path.exists():
                        doc.add_picture(str(path), width=Cm(width))
                        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
                        inserted_fig.add(label)
                        print(f"  placed {label} inline in {head[:22]}")

    # ---- anything not cited inline goes to the end, flagged for the author
    for key, blk in table_blocks.items():
        if key not in inserted_tbl:
            heading(doc, f"{key.upper()} (not cited inline \u2014 place manually)")
            md_table(doc, [l for l in blk.split("\n") if l.startswith("|")])
    for fname, label, width in FIGURES:
        if label not in inserted_fig:
            path = FIGDIR / fname
            if path.exists():
                doc.add_picture(str(path), width=Cm(width))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    heading(doc, "DECLARATIONS")
    decl_text = declarations.strip()
    if not args.named:
        decl_text = decl_text.replace("[AUTHOR NAME]", "The Author")
    for chunk in re.split(r"\n\n+", decl_text):
        if chunk.strip():
            para(doc, chunk.strip())

    heading(doc, "REFERENCES")
    for line in refs.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith(">"):
            continue
        if line.startswith("- "):
            para(doc, line[2:].strip(), size=11)

    # ---- strip identifying metadata from file properties
    cp = doc.core_properties
    cp.author = "" if not args.named else args.author
    cp.last_modified_by = ""
    cp.title = title_md
    cp.comments = "Blinded for review" if not args.named else ""

    OUT.mkdir(exist_ok=True)
    dest = OUT / "JHS-submission.docx"
    doc.save(dest)

    mode = "named" if args.named else "blinded"
    print(f"\n{mode} DOCX written: {dest} ({dest.stat().st_size // 1024} KB)")
    print(f"figures placed inline: {len(inserted_fig)}/{len(FIGURES)}")
    print(f"tables placed inline : {len(inserted_tbl)}/{len(table_blocks)}")
    if len(inserted_tbl) < len(table_blocks):
        print("  not cited inline:", sorted(set(table_blocks) - inserted_tbl))


if __name__ == "__main__":
    main()
