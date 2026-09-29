#!/usr/bin/env python3
"""
Build a repository-deposit PDF and HTML from REVIEW-final.md.

Strips the author-facing apparatus (word-count table, submission checklist,
venue note, AI-disclosure note) so the deposited document contains only the
review itself, and prepends proper front matter: title, author, ORCID,
affiliation, abstract, keywords.

Usage
-----
    python3 make-deposit.py --author "Your Name" --orcid "0000-0002-1825-0097" \
                            --affiliation "Department, Institution, City, India"

Outputs into ./deposit/ :
    REVIEW-deposit.pdf    the file to upload to Zenodo
    REVIEW-deposit.html   browser-printable fallback (Ctrl+P -> Save as PDF)

Requires: markdown, xhtml2pdf, reportlab, DejaVu fonts.
"""

import argparse
import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "REVIEW-final.md"
FIGDIR = HERE / "figures"
OUT = HERE / "deposit"
FONT_STAGE = HERE / "_fonts"   # xhtml2pdf blocks reads outside the workspace root

FONT_DIRS = [
    pathlib.Path("/usr/share/fonts/truetype/dejavu"),
    pathlib.Path("/usr/local/lib/python3.11/dist-packages/matplotlib/mpl-data/fonts/ttf"),
]

FONTS = {  # family variants -> filenames, resolved against FONT_DIRS
    "DejaVuSerif": "DejaVuSerif.ttf",
    "DejaVuSerif-Bold": "DejaVuSerif-Bold.ttf",
    "DejaVuSerif-Italic": "DejaVuSerif-Italic.ttf",
    "DejaVuSerif-BoldItalic": "DejaVuSerif-BoldItalic.ttf",
    "DejaVuSans": "DejaVuSans.ttf",
    "DejaVuSans-Bold": "DejaVuSans-Bold.ttf",
}

# (filename, label, display width in mm) -- widths chosen so no figure runs
# taller than about 90 mm on the page
FIGURES = [
    ("figure-1-framework.png", "Figure 1", 165),
    ("figure-2-peg-conversion.png", "Figure 2", 105),
    ("figure-3-stages.png", "Figure 3", 130),
    ("figure-4-evidence-map.png", "Figure 4", 165),
    ("figure-5-concordance-reporting.png", "Figure 5", 150),
]


def resolve(fname):
    """Locate a system font and stage a copy inside the workspace so xhtml2pdf,
    which sandboxes file reads to the workspace root, is allowed to load it."""
    staged = FONT_STAGE / fname
    if staged.exists():
        return staged
    src = next((d / fname for d in FONT_DIRS if (d / fname).exists()), None)
    if src is None:
        return None
    FONT_STAGE.mkdir(exist_ok=True)
    staged.write_bytes(src.read_bytes())
    return staged


def font_face_css():
    """xhtml2pdf keeps its own font registry, so fonts must be embedded via CSS."""
    faces = [
        ("DejaVuSerif", "normal", "normal", "DejaVuSerif.ttf"),
        ("DejaVuSerif", "normal", "bold", "DejaVuSerif-Bold.ttf"),
        ("DejaVuSerif", "italic", "normal", "DejaVuSerif-Italic.ttf"),
        ("DejaVuSerif", "italic", "bold", "DejaVuSerif-BoldItalic.ttf"),
        ("DejaVuSans", "normal", "normal", "DejaVuSans.ttf"),
        ("DejaVuSans", "normal", "bold", "DejaVuSans-Bold.ttf"),
    ]
    css, missing = [], []
    for family, style, weight, fname in faces:
        path = resolve(fname)
        if path is None:
            missing.append(fname)
            continue
        css.append(
            f'@font-face {{ font-family: "{family}"; font-style: {style}; '
            f'font-weight: {weight}; src: url("{path.as_uri()}"); }}'
        )
    return "\n".join(css), missing


def load_manuscript():
    """Return (title, body_markdown). Author notes are discarded."""
    text = SRC.read_text(encoding="utf-8")

    # title
    first = text.split("\n", 1)[0]
    title = first.lstrip("# ").strip()

    # drop everything from the author notes onward
    cut = text.find("\n## Notes for the author")
    if cut == -1:
        sys.exit("FAIL: could not find the '## Notes for the author' boundary.")
    text = text[:cut]

    # body begins at the abstract; strip the header block (article type/venue/status)
    start = text.find("\n## Abstract")
    if start == -1:
        sys.exit("FAIL: could not find '## Abstract'.")
    body = text[start:].strip()

    # demote '## Abstract' to a styled heading handled in front matter
    body = body.replace("## Abstract\n", "", 1)
    return title, body


def figure_section():
    """Raw-HTML figure block: image followed by its own legend, paired in order."""
    legends = []
    md = SRC.read_text(encoding="utf-8")
    m = re.search(r"## Figure legends\n(.*?)\n## Tables", md, re.S)
    if m:
        chunks = re.split(r"\n(?=\*\*Figure \d\.)", m.group(1).strip())
        legends = [c.strip() for c in chunks if c.strip()]

    legend_html = ""
    for i, (fname, label, width_mm) in enumerate(FIGURES):
        path = FIGDIR / fname
        if not path.exists():
            continue
        cap = ""
        for lg in legends:
            if lg.startswith("**" + label + "."):
                cap = lg
                break
        cap = re.sub(r"\*\*Figure (\d)\.\*\*\s*", r"<b>Figure \1.</b> ", cap)
        cap = re.sub(r"([A-Za-z])_([A-Za-z0-9]+)_", r"\1<i>\2</i>", cap)
        legend_html += (
            f'<div class="figwrap">'
            f'<p class="figimg"><img src="{path.as_uri()}" alt="{label}" '
            f'style="width:{width_mm}mm"/></p>'
            f'<p class="figcap">{cap}</p></div>\n'
        )
    return "\n<h2>Figures</h2>\n" + legend_html


def italicise(text):
    """Markdown-level italics for gene and species names in raw-HTML blocks."""
    return text


CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm;
        @bottom-center { content: counter(page); font-family: "DejaVuSans"; font-size: 8pt; color: #666; } }
body { font-family: "DejaVuSerif"; font-size: 9.4pt; line-height: 1.42; color: #111; text-align: justify; }
h1 { font-family: "DejaVuSans"; font-weight: bold; font-size: 16pt; line-height: 1.25; margin: 0 0 10pt 0; text-align: left; }
h2 { font-family: "DejaVuSans"; font-weight: bold; font-size: 11.5pt; margin: 15pt 0 5pt 0; text-align: left;
     border-bottom: 0.6pt solid #bbb; padding-bottom: 2pt; page-break-after: avoid; }
h3 { font-family: "DejaVuSans"; font-weight: bold; font-size: 9.8pt; margin: 11pt 0 4pt 0; text-align: left; page-break-after: avoid; }
p { margin: 0 0 5pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 14pt; }
li { margin-bottom: 2.5pt; }
table { width: 100%; border-collapse: collapse; font-family: "DejaVuSans"; font-size: 6.6pt;
        margin: 6pt 0 9pt 0; }
th { background: #eef2f7; border: 0.5pt solid #9aa7b4; padding: 2.5pt 3pt; text-align: left;
     font-family: "DejaVuSans"; font-weight: bold; }
td { border: 0.5pt solid #b9c2cc; padding: 2.5pt 3pt; vertical-align: top; }
blockquote { margin: 6pt 0 6pt 10pt; padding-left: 8pt; border-left: 2pt solid #c8d3de;
             font-size: 8.8pt; color: #333; }
hr { border: none; border-top: 0.5pt solid #ccc; margin: 10pt 0; }
.frontmatter { margin-bottom: 12pt; border-bottom: 1pt solid #999; padding-bottom: 10pt; }
.authors { font-family: "DejaVuSans"; font-size: 11pt; margin: 3pt 0 2pt 0; text-align: left; }
.affil { font-family: "DejaVuSans"; font-size: 8.4pt; color: #444; margin: 0 0 2pt 0; text-align: left; }
.meta { font-family: "DejaVuSans"; font-size: 8pt; color: #555; margin: 0; text-align: left; }
.abs { font-size: 8.9pt; margin-top: 8pt; }
.figwrap { margin: 10pt 0 14pt 0; }
.figimg { text-align: center; margin: 0 0 3pt 0; }
.figcap { font-family: "DejaVuSans"; font-size: 7.4pt; color: #222; text-align: left; margin: 0; }
.figcap { font-family: "DejaVuSans"; font-size: 7.4pt; color: #222; text-align: left; margin-top: 3pt; }
.kw { font-family: "DejaVuSans"; font-size: 8pt; color: #333; }
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--author", default="[AUTHOR NAME]")
    ap.add_argument("--orcid", default="")
    ap.add_argument("--affiliation", default="[Department, Institution, City, India]")
    ap.add_argument("--license", default="CC BY 4.0")
    args = ap.parse_args()

    import markdown
    from xhtml2pdf import pisa

    faces_css, missing = font_face_css()
    if missing:
        print("WARNING: fonts not found ->", ", ".join(missing))
    css = faces_css + "\n" + CSS

    title_md, body = load_manuscript()
    title = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", html.escape(title_md))
    # substitute the markdown legend list with the drawn figures + legends
    m = re.search(r"\n## Figure legends\n.*?(?=\n## Tables)", body, re.S)
    if not m:
        sys.exit("FAIL: could not find the figure-legend block to replace.")
    body = body[:m.start()] + figure_section() + body[m.end():]

    body_html = markdown.markdown(
        body, extensions=["tables", "sane_lists", "attr_list", "md_in_html"]
    )

    authors = args.author
    if args.orcid:
        authors += f' &nbsp;<span class="meta">ORCID: {args.orcid}</span>'

    front = f"""<div class="frontmatter">
<h1>{title}</h1>
<p class="authors">{authors}</p>
<p class="affil">{html.escape(args.affiliation)}</p>
<p class="meta">Review article &nbsp;&middot;&nbsp; Licence: {html.escape(args.license)} &nbsp;&middot;&nbsp; No new data were generated; this work analyses previously published literature.</p>
</div>"""

    doc = (f"<html><head><meta charset='utf-8'><style>{css}</style></head>"
           f"<body>{front}{body_html}</body></html>")

    OUT.mkdir(exist_ok=True)
    (OUT / "REVIEW-deposit.html").write_text(doc, encoding="utf-8")

    pdf_path = OUT / "REVIEW-deposit.pdf"
    with open(pdf_path, "wb") as fh:
        result = pisa.CreatePDF(doc, dest=fh, encoding="utf-8")

    if result.err:
        print(f"PDF reported {result.err} error(s); check {pdf_path}")
    else:
        print("PDF written:", pdf_path, f"({pdf_path.stat().st_size // 1024} KB)")
    print("HTML written:", OUT / "REVIEW-deposit.html")
    print("Author field:", authors)


if __name__ == "__main__":
    main()
