#!/usr/bin/env python3
"""Resolve all six VERIFY markers in REVIEW-final.md with verified citations."""

import pathlib, sys

SRC = pathlib.Path(__file__).parent / "REVIEW-final.md"

REPLACEMENTS = [
    # ---------------- VERIFY-1 : competing reviews ------------------------
    ("most comprehensively for molecular and genetic mechanisms (Pang et al., 2024), and separately for tomato omics and genome editing, and for pepper stress genomics \u27e6VERIFY-1\u27e7.",
     "most comprehensively for molecular and genetic mechanisms across the family (Pang et al., 2024), and separately for tomato omics, non-coding RNAs and genome editing (Taheri et al., 2022)."),

    # ---------------- VERIFY-2 : site of action ---------------------------
    ("In common bean root tips, PEG 4000 acted mainly in the cytoplasm while PEG 6000 acted additionally in the apoplast \u27e6VERIFY-2\u27e7. The treatments differ in the cellular site of their effect.",
     "In common bean root tips the site of action depends on molecular weight: glycerol and PEG 4000 act mainly in the cytoplasm, whereas PEG 6000 additionally dehydrates the apoplast and reduces cell-wall porosity (Yang et al., 2010). High-molecular-weight PEG is thus not merely excluded from the tissue; it dehydrates a specific compartment."),

    # ---------------- VERIFY-3 : durum wheat osmotica ---------------------
    ("finding PEG superior and noting that mannitol's effects were reversible, consistent with uptake \u27e6VERIFY-3\u27e7.",
     "finding PEG superior and noting that mannitol's effects were reversible, consistent with uptake (Bousba et al., 2021)."),

    # ---------------- VERIFY-4 : chilli statistical practice --------------
    ("Chilli-specific practice conforms to the pattern. A 2025 study optimising chilli germination used a completely randomised 8 \u00d7 3 factorial design with 30 seeds per replicate across 24 Petri dishes and analysed results by analysis of variance. A chilli seed-priming study used a completely randomised design with three replications and 50 seeds per replication, analysed as a factorial design. A chilli gibberellic acid study used 240 seeds across 12 Petri plates with three replications, analysed by ANOVA \u27e6VERIFY-4\u27e7.",
     "Practice in this crop conforms to the pattern. The 16-genotype chilli screen described in Section 3.3 used a completely randomised factorial design with three replications and analysed its results by analysis of variance (Sharma et al., 2024); the tomato screen cited above fitted ANOVA to germination percentage, germination rate and vigour index across a genotype \u00d7 concentration factorial (Yadav et al., 2025). Neither reports an alternative model or a check on the distributional assumption."),

    # ---------------- VERIFY-5 : the ANOVA qualification ------------------
    ("A direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible \u27e6VERIFY-5\u27e7.",
     "A tractable treatment of germination data makes the boundary explicit: wide differences in variance do not arise for purely binomial data in the 0.3\u20130.7 range of proportions, where analysis of variance is defensible, whereas data outside that range require an angular transformation or a different model altogether (Gianinetti, 2020)."),

    # ---------------- VERIFY-6 : the tomato ceiling -----------------------
    ("Most tomato genotypes failed to germinate entirely above \u22120.35 MPa \u27e6VERIFY-6\u27e7, and comparable results are reported in wheat and barley at high PEG concentrations (El-Rawy and Hassan, 2014; Slawin et al., 2024).",
     "In a 32-genotype tomato screen, most genotypes failed to germinate at all at \u22120.35 MPa, and even the best-performing line fell from 100% germination in the control to 60% at that potential (Sivakumar et al., 2013). In an independent five-genotype study the most susceptible line reached 0% at \u22120.36 MPa (Yadav et al., 2025). Comparable floor effects are reported in wheat and barley at high PEG concentrations (El-Rawy and Hassan, 2014; Slawin et al., 2024)."),

    # ---------------- Table 1 : solidified PEG citation -------------------
    ("| Solidified PEG; raft-and-membrane systems | Prevent PEG uptake while imposing osmotic stress | Designed to solve the penetration problem; rarely used in Solanaceae screening | \u27e6VERIFY-3\u27e7 |",
     "| Solidified PEG; raft-and-membrane systems | Prevent PEG uptake while imposing osmotic stress | Designed to solve the penetration problem; rarely used in Solanaceae screening | Comeau et al. (2010) |"),

    # ---------------- §2.2 : the conversion observation -------------------
    ("Nominal concentration-to-potential conversion tables therefore carry an error of unstated magnitude.",
     "Nominal concentration-to-potential conversion tables therefore carry an error of unstated magnitude, and applying the standard relation shows how large that can be. At 25 \u00b0C, 10% PEG-6000 corresponds to approximately \u22120.15 MPa and 20% to approximately \u22120.49 MPa (Figure 2), values that agree with published applications of the equation (Sivakumar et al., 2013). Screens reporting substantially more negative potentials at the same nominal percentage are not necessarily wrong \u2014 molecular weight, temperature and whether the percentage is w/v or w/w all shift the answer \u2014 but the discrepancy is large enough that stated potentials should be traced to the primary source before studies are compared or pooled."),

    # ---------------- Figure legends updated for drawn figures -----------
    ("**Figure 2.** Osmotic potential of PEG-6000 solutions as a function of concentration, compiled from published relationships. The shaded region indicates the 15\u201335 \u00b0C validity range of the underlying empirical equation. The measurement-method discrepancy between thermocouple psychrometry and vapour pressure osmometry, and the deviation from colligative behaviour, are annotated. Compiled, not experimental.",
     "**Figure 2.** Osmotic potential of PEG-6000 solutions as a function of concentration at 15, 25 and 35 \u00b0C, computed from the empirical relation of Michel and Kaufmann (1973), which is valid over the 15\u201335 \u00b0C range shown. Points mark the three concentrations most frequently used in the screening literature. Computed, not experimental."),

    ("**Figure 5.** Genotype-level concordance among screening studies: the proportion of genotypes ranked tolerant at an early stage that were also superior under later-stage or field drought, compiled from the studies reviewed. Compiled, not experimental.",
     "**Figure 5.** What the studies connecting developmental stages actually report. For each of the nine connecting studies, the left column indicates whether a trait-level correlation was reported and the right column whether a genotype-level concordance rate was reported. One study reports such a rate (22%, two of nine lines); one permits it to be inferred (a single genotype). The remaining six report only trait correlations. Compiled from the studies reviewed."),
]


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    before = text
    failures = []

    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n != 1:
            failures.append((n, old[:80]))
            continue
        text = text.replace(old, new, 1)

    if failures:
        print("FAILED ANCHORS:")
        for n, s in failures:
            print(f"  count={n}  {s!r}")
        return 1

    SRC.write_text(text, encoding="utf-8")
    remaining = text.count("\u27e6VERIFY")
    print(f"Applied {len(REPLACEMENTS)} replacements.")
    print(f"Remaining VERIFY markers: {remaining}")
    print(f"Words: {len(before.split())} -> {len(text.split())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
