#!/usr/bin/env python3
"""Generate Figures 1-5 for the review.

Figure 2 is COMPUTED from the Michel & Kaufmann (1973) empirical relation.
Figures 1, 3 and 4 are conceptual schematics.
Figure 5 is compiled from the nine connecting studies.

Output: 300 dpi PNG, single-column width (90 mm) or double-column (180 mm).
"""

import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import numpy as np

OUT = pathlib.Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.linewidth": 0.8,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

INK = "#1a1a1a"
BLUE = "#2b6cb0"
RED = "#b03030"
GREEN = "#2f7d4f"
GREY = "#8a8a8a"
LIGHT = "#eef2f7"


def mk(michel_kaufmann):
    return michel_kaufmann


# --------------------------------------------------------------------------
# Michel & Kaufmann (1973) empirical relation for PEG 6000.
#   psi_s (bar) = -(1.18e-2)C - (1.18e-4)C^2 + (2.67e-4)CT + (8.39e-7)C^2 T
#   C = g PEG-6000 per kg water, T = temperature in C, valid 15-35 C.
# Validated against a published application: C = 123 g/L at 30 C gives
# -0.19 MPa and C = 169 g/L gives -0.33 MPa (Sivakumar et al. -0.2/-0.35).
# --------------------------------------------------------------------------
def psi_bar(C, T):
    return (-(1.18e-2) * C - (1.18e-4) * C**2
            + (2.67e-4) * C * T + (8.39e-7) * C**2 * T)


def psi_mpa(C, T):
    return psi_bar(C, T) / 10.0


def figure1():
    """Four-stage framework with decision points."""
    fig, ax = plt.subplots(figsize=(7.0, 2.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.0)
    ax.axis("off")

    stages = [
        ("Stage 1\nSCREEN", "Panels, osmoticum,\nGLMM analysis", BLUE),
        ("Stage 2\nVALIDATE", "Managed drought,\nmulti-season", GREEN),
        ("Stage 3\nCHARACTERISE", "Candidate genes,\nVIGS / VIGE", "#8a5a2b"),
        ("Stage 4\nDEPLOY", "KASP/CAPS assay,\nassociation test", "#6b4c8a"),
    ]
    w, h, y = 1.85, 1.5, 1.9
    for i, (title, sub, col) in enumerate(stages):
        x = 0.25 + i * 2.45
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06,rounding_size=0.12",
                             linewidth=1.1, edgecolor=col, facecolor=LIGHT)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h - 0.42, title, ha="center", va="center",
                fontsize=8.4, fontweight="bold", color=col)
        ax.text(x + w / 2, y + 0.42, sub, ha="center", va="center", fontsize=6.2, color=INK)
        if i < 3:
            ax.add_patch(FancyArrowPatch((x + w + 0.04, y + h / 2), (x + 2.45 - 0.04, y + h / 2),
                                         arrowstyle="-|>", mutation_scale=11,
                                         linewidth=1.0, color=GREY))
    decisions = [
        "which genotypes\nadvance?",
        "does the screen\npredict the field?",
        "expression,\nsequence, or both?",
        "does the marker\ntrack the trait?",
    ]
    for i, d in enumerate(decisions):
        x = 0.25 + i * 2.45 + w / 2
        ax.text(x, y - 0.42, "\u25c6", ha="center", va="center", fontsize=7, color=RED)
        ax.text(x, y - 1.02, d, ha="center", va="center", fontsize=6.3, color=RED, style="italic")
    ax.text(5.0, 1.12, "Decision point", ha="center", fontsize=6.4,
            color=RED, style="italic")
    fig.savefig(OUT / "figure-1-framework.png", dpi=300)
    plt.close(fig)


def figure2():
    """PEG-6000 concentration vs osmotic potential, computed."""
    fig, ax = plt.subplots(figsize=(3.5, 2.9))
    C = np.linspace(0, 300, 400)
    for T, col, lab in [(15, "#9ec5e8", "15 \u00b0C"), (25, BLUE, "25 \u00b0C"),
                        (35, "#14406b", "35 \u00b0C")]:
        ax.plot(C / 10.0, psi_mpa(C, T), color=col, lw=1.5, label=lab)

    # validity shading
    ax.axvspan(0, 30, color="#f2f2f2", zorder=0)

    # Annotate the range used by most screening studies
    for pct, lab in [(10, "\u22120.15"), (20, "\u22120.49"), (25, "\u22120.74")]:
        ax.plot([pct], [psi_mpa(pct * 10, 25)], "o", ms=3.4, color=RED, zorder=5)
        ax.annotate(lab, (pct, psi_mpa(pct * 10, 25)),
                    textcoords="offset points", xytext=(4, -7),
                    fontsize=6.2, color=RED)

    ax.set_xlabel("PEG-6000 concentration (% w/v)", fontsize=7.5)
    ax.set_ylabel("Osmotic potential (MPa)", fontsize=7.5)
    ax.set_xlim(0, 30)
    ax.set_ylim(-1.15, 0.05)
    ax.legend(frameon=False, fontsize=6.4, loc="lower left")
    ax.tick_params(labelsize=6.5)
    ax.text(0.97, 0.06,
            "Computed from Michel & Kaufmann (1973);\nvalid 15\u201335 \u00b0C",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=5.8, color=GREY, style="italic")
    fig.savefig(OUT / "figure-2-peg-conversion.png", dpi=300)
    plt.close(fig)


def figure3():
    """Developmental stages as partially overlapping sets."""
    fig, ax = plt.subplots(figsize=(4.2, 2.85))
    ax.set_xlim(0.15, 9.95)
    ax.set_ylim(0.35, 7.5)
    ax.axis("off")

    sets = [
        (3.05, 4.45, "Germination", "5 screens"),
        (5.35, 5.05, "Seedling", "many"),
        (7.30, 4.45, "Vegetative", "1\u20132"),
        (8.10, 2.62, "Reproductive", "1 (GWAS)"),
    ]
    for x, y, name, n in sets:
        ax.add_patch(Ellipse((x, y), 3.5, 2.5, angle=-14,
                             facecolor="#dce9f7", edgecolor=BLUE, lw=1.0, alpha=0.72))
        ax.text(x, y + 0.42, name, ha="center", va="center", fontsize=7.0,
                fontweight="bold", color="#14406b")
        ax.text(x, y - 0.30, n, ha="center", va="center", fontsize=6.0, color=INK)

    ax.annotate("", xy=(4.6, 3.05), xytext=(4.25, 3.55),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))
    ax.annotate("", xy=(8.25, 1.52), xytext=(8.45, 1.16),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5))
    ax.text(4.35, 2.62, "1 study: transfer\nconfirmed", fontsize=6.1, color=GREEN,
            ha="center", va="top")
    ax.text(8.45, 1.05, "0 studies in\nCapsicum", fontsize=6.1, color=RED,
            ha="center", va="top", style="italic")
    ax.text(5.0, 6.95, "Overlap = studies testing two or more stages together",
            ha="center", fontsize=6.4, color=GREY, style="italic")
    fig.savefig(OUT / "figure-3-stages.png", dpi=300)
    plt.close(fig)


def figure4():
    """Evidence map: crop x stage-pair."""
    pairs = ["Germ \u2192 Seedling", "Seedling \u2192 Vegetative",
             "Vegetative \u2192 Yield", "Any stage \u2192 Field yield"]
    crops = ["Tomato", "Potato", "Barley", "Wheat", "*Capsicum*"]
    # 1 = supports, -1 = contradicts, 0 = none
    grid = np.array([
        [0, 1, 0, 0],     # tomato  (C1 supports across stages)
        [0, 0, 1, 0],     # potato  (C7)
        [0, 0, 0, -1],    # barley  (C3 contradicts; C4 supports)
        [-1, 0, 0, 1],    # wheat   (C6 contradicts; C5 supports)
        [0, 0, 0, 0],     # Capsicum
    ])

    fig, ax = plt.subplots(figsize=(4.6, 2.30))
    for i in range(len(crops)):
        for j in range(len(pairs)):
            v = grid[i, j]
            col = "#ffffff" if v == 0 else (GREEN if v > 0 else RED)
            ax.add_patch(plt.Rectangle((j, len(crops) - 1 - i), 1, 1,
                                       facecolor=col, edgecolor="#c9c9c9", lw=0.7))
            if v != 0:
                ax.text(j + 0.5, len(crops) - 1 - i + 0.5, "+" if v > 0 else "\u2212",
                        ha="center", va="center", fontsize=11, color="white",
                        fontweight="bold")
    ax.set_xlim(0, len(pairs))
    ax.set_ylim(0, len(crops))
    ax.set_xticks(np.arange(len(pairs)) + 0.5)
    wrapped = [p.replace(" \u2192 ", " \u2192\n") for p in pairs]
    ax.set_xticklabels(wrapped, fontsize=6.0, rotation=0, ha="center",
                       linespacing=1.35)
    ax.set_yticks(np.arange(len(crops)) + 0.5)
    ax.set_yticklabels([c.replace("*", "") for c in crops[::-1]], fontsize=6.5)
    ax.get_yticklabels()[0].set_fontstyle("italic")   # Capsicum
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(0.0, -0.34, "+ supports transfer      \u2212 contradicts      empty = not tested",
            transform=ax.transAxes, fontsize=6.0, color=INK)
    fig.savefig(OUT / "figure-4-evidence-map.png", dpi=300)
    plt.close(fig)


def figure5():
    """What the connecting studies actually report."""
    labels = [
        "Pessoa 2023 (tomato)",
        "Sallam 2018 (wheat)",
        "Slawin 2024 (barley)",
        "Badr 2025 (barley)",
        "El-Rawy 2014 (wheat)",
        "Mohamed 2023 (wheat)",
        "K\u00f6hl 2023 (potato)",
        "Sahitya 2019 (Capsicum)",
        "Yadav 2025 (tomato)",
    ]
    # (trait correlation reported?, concordance label or None)
    trait = [1, 1, 1, 1, 1, 1, 1, 0, 1]
    concord = [None, "1 genotype", "22% (2/9)", None, None, None, None, None, None]

    fig, ax = plt.subplots(figsize=(4.9, 2.9))
    y = np.arange(len(labels))[::-1]
    for yi, t, c in zip(y, trait, concord):
        ax.barh(yi, 1, height=0.62, color="#dce9f7", edgecolor="#c2d6ea", lw=0.6)
        if t:
            ax.text(0.04, yi, "trait correlation", va="center", fontsize=5.9, color="#14406b")
        else:
            ax.text(0.04, yi, "mechanism contrast only", va="center", fontsize=5.9,
                    color=GREY, style="italic")
        ax.barh(yi, 1, height=0.62, left=1.06,
                color=GREEN if c else "#f4f4f4",
                edgecolor="#c9c9c9", lw=0.6)
        if c:
            ax.text(1.10, yi, c, va="center", fontsize=5.9, color="white",
                    fontweight="bold")
        else:
            ax.text(1.10, yi, "not reported", va="center", fontsize=5.9, color=GREY)

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=6.1)
    ax.set_xticks([])
    ax.set_xlim(0, 2.1)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(0.5, len(labels) - 0.25, "Trait correlation", ha="center",
            fontsize=6.4, fontweight="bold", color="#14406b")
    ax.text(1.58, len(labels) - 0.25, "Genotype concordance rate", ha="center",
            fontsize=6.4, fontweight="bold", color=GREEN)
    fig.savefig(OUT / "figure-5-concordance-reporting.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    figure1(); figure2(); figure3(); figure4(); figure5()
    print("Written to", OUT)
    for p in sorted(OUT.glob("*.png")):
        print(f"  {p.name}  {p.stat().st_size/1024:.0f} KB")

    # Report the conversion values used in the text
    print("\nMichel & Kaufmann at 25 C:")
    for pct in (5, 10, 15, 20, 25, 30):
        print(f"  {pct:2d}% -> {psi_mpa(pct*10, 25):+.3f} MPa")
