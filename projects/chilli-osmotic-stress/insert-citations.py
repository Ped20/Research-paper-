#!/usr/bin/env python3
"""Insert in-text citations into REVIEW-final.md.

Each replacement is an exact-substring swap. The script asserts that every
anchor appears exactly once, so a silent failure is impossible: it reports
any anchor that is missing or ambiguous instead of corrupting the text.
"""

import sys, pathlib

SRC = pathlib.Path(__file__).parent / "REVIEW-final.md"

REPLACEMENTS = [
    # ---- §1 Introduction ------------------------------------------------
    ("it has produced concrete tolerant germplasm in chilli, tomato and eggplant alike.",
     "it has produced concrete tolerant germplasm in chilli (Sharma et al., 2024), tomato (Yadav et al., 2025) and eggplant (Krommydas et al., 2025) alike."),

    ("The physicochemical behaviour of PEG has been characterised in detail, including several behaviours",
     "The physicochemical behaviour of PEG has been characterised in detail (Lagerwerff et al., 1961; Lawlor, 1970; Michel and Kaufmann, 1973; Money, 1989), including several behaviours"),

    ("most comprehensively for molecular and genetic mechanisms, and separately for tomato omics and genome editing, and for pepper stress genomics.",
     "most comprehensively for molecular and genetic mechanisms (Pang et al., 2024), and separately for tomato omics and genome editing, and for pepper stress genomics ⟦VERIFY-1⟧."),

    # ---- §2.1 -----------------------------------------------------------
    ("not equivalent treatments, yet screening papers routinely report a percentage without stating molecular weight",
     "not equivalent treatments (Money, 1989), yet screening papers routinely report a percentage without stating molecular weight"),

    ("In common bean root tips, PEG 4000 acted mainly in the cytoplasm while PEG 6000 acted additionally in the apoplast.",
     "In common bean root tips, PEG 4000 acted mainly in the cytoplasm while PEG 6000 acted additionally in the apoplast ⟦VERIFY-2⟧."),

    ("using PEG of molecular weights 400, 600, 1000, 1540 and 4000.",
     "using PEG of molecular weights 400, 600, 1000, 1540 and 4000 (Lagerwerff et al., 1961; Janes, 1974)."),

    # ---- §2.2 -----------------------------------------------------------
    ("Solution measurements showed that PEG produces a greater osmotic effect than the number of dissolved molecules accounts for,",
     "Solution measurements showed that PEG produces a greater osmotic effect than the number of dissolved molecules accounts for (Money, 1989),"),

    ("over a validity range of 15–35 °C.",
     "over a validity range of 15–35 °C (Michel and Kaufmann, 1973; McClendon, 1981)."),

    ("and judges the psychrometer closer to correct for bulk solutions.",
     "and judges the psychrometer closer to correct for bulk solutions (Michel and Kaufmann, 1973)."),

    # ---- §2.3 -----------------------------------------------------------
    ("entered plants at approximately 1 mg per gram leaf fresh weight per week,",
     "entered plants at approximately 1 mg per gram leaf fresh weight per week (Lawlor, 1970),"),

    ("As noted above, the same behaviour was documented in pepper.",
     "As noted above, the same behaviour was documented in pepper (Janes, 1974)."),

    ("concluded that mannitol simulated osmotic stress better than PEG for most attributes and concentrations.",
     "concluded that mannitol simulated osmotic stress better than PEG for most attributes and concentrations (Tajaragh et al., 2022)."),

    ("finding PEG superior and noting that mannitol's effects were reversible, consistent with uptake.",
     "finding PEG superior and noting that mannitol's effects were reversible, consistent with uptake ⟦VERIFY-3⟧."),

    # ---- §2.4 -----------------------------------------------------------
    ("with slower recovery after relief; even brief exposure was more damaging than soil drought.",
     "with slower recovery after relief; even brief exposure was more damaging than soil drought (Fan and Blake, 1997)."),

    (" Longer exposure to PEG 400 has been associated with increased cation accumulation in the root xylem of pepper, an ionic effect in a nominally non-ionic treatment.", ""),

    ("and maize growth was unaffected.",
     "and maize growth was unaffected (Lawlor, 1970)."),

    ("comparison with non-ionic detergents ruled this out.",
     "comparison with non-ionic detergents ruled this out (Lawlor, 1970)."),

    ("and concluded that PEG solutions served as a satisfactory medium for studying the effect of true drought on seed germination.",
     "and concluded that PEG solutions served as a satisfactory medium for studying the effect of true drought on seed germination (Sharma, 1973)."),

    # ---- §2.6 -----------------------------------------------------------
    ("and describing such experiments as drought or water stress misleads readers.",
     "and describing such experiments as drought or water stress misleads readers (Kylyshbayeva et al., 2025)."),

    # ---- §3.1 -----------------------------------------------------------
    ("despite a pepper pan-genome that has identified abiotic stress tolerance genes carried in *C. baccatum* introgressions.",
     "despite a pepper pan-genome that has identified abiotic stress tolerance genes carried in *C. baccatum* introgressions (Liu et al., 2023)."),

    ("Almost all studies use a completely randomised design with three or four replications.",
     "Almost all studies use a completely randomised design with three or four replications (e.g. Sharma et al., 2024)."),

    # ---- §3.2 -----------------------------------------------------------
    ("An integration study in maize makes the consequence explicit: index choice directly influences genotype ranking and selection decisions.",
     "An integration study in maize makes the consequence explicit: index choice directly influences genotype ranking and selection decisions (Muzafarov et al., 2026)."),

    ("The same inconsistency is documented in chickpea, where several indices produced conflicting rankings.",
     "The same inconsistency is documented in chickpea, where several indices produced conflicting rankings (Basavaraj et al., 2025)."),

    # ---- §3.3 -----------------------------------------------------------
    ("identified UARChH 42, UARChH 43 and Arka Swetha as tolerant.",
     "identified UARChH 42, UARChH 43 and Arka Swetha as tolerant (Sharma et al., 2024)."),

    ("resolving four clusters by agglomerative clustering at a cophenetic correlation of 0.668.",
     "resolving four clusters by agglomerative clustering at a cophenetic correlation of 0.668 (Molla et al., 2019)."),

    ("A 22-genotype study identified C7 as tolerant across all measured traits.",
     "A 22-genotype study identified C7 as tolerant across all measured traits (Millah et al., 2021)."),

    ("In tomato, a five-genotype screen identified NGRCO9569, Monoprecos and Khumal 2 as maintaining germination, vigour and biomass under stress, while a susceptible genotype failed to germinate entirely at 6% PEG.",
     "In tomato, a five-genotype screen identified NGRCO9569, Monoprecos and Khumal 2 as maintaining germination, vigour and biomass under stress, while a susceptible genotype failed to germinate entirely at 6% PEG (Yadav et al., 2025)."),

    ("a 100-accession vegetative-stage screen identified three accessions as resistant through 21 days of water withholding, corroborated under greenhouse conditions.",
     "a 100-accession vegetative-stage screen identified three accessions as resistant through 21 days of water withholding, corroborated under greenhouse conditions (Thin et al., 2026)."),

    ("The reasoning is sound and the approach is the single most transferable methodological improvement identified in this review.",
     "The reasoning is sound and the approach is the single most transferable methodological improvement identified in this review (Alnaddaf et al., 2026)."),

    # ---- §3.4 -----------------------------------------------------------
    ("A systematic critique of statistical practice in seed germination and viability research examined 429 studies and reported the following.",
     "A systematic critique of statistical practice in seed germination and viability research examined 429 studies and reported the following (Sileshi, 2012)."),

    ("a transformation now specifically discouraged for binomial data on the grounds that logistic regression offers greater interpretability and higher power, and that the transformation produces nonsensical predictions for non-binomial proportions.",
     "a transformation now specifically discouraged for binomial data on the grounds that logistic regression offers greater interpretability and higher power, and that the transformation produces nonsensical predictions for non-binomial proportions (Warton and Hui, 2011)."),

    ("analysed as a factorial design. A chilli gibberellic acid study used 240 seeds across 12 Petri plates with three replications, analysed by ANOVA.",
     "analysed as a factorial design. A chilli gibberellic acid study used 240 seeds across 12 Petri plates with three replications, analysed by ANOVA ⟦VERIFY-4⟧."),

    ("A direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible.",
     "A direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible ⟦VERIFY-5⟧."),

    ("Most tomato genotypes failed to germinate entirely above −0.35 MPa, and comparable results are reported in wheat and barley at high PEG concentrations.",
     "Most tomato genotypes failed to germinate entirely above −0.35 MPa ⟦VERIFY-6⟧, and comparable results are reported in wheat and barley at high PEG concentrations (El-Rawy and Hassan, 2014; Slawin et al., 2024)."),

    # ---- §4.1 -----------------------------------------------------------
    ("The authors recommended that breeding for seedling tolerance and for yield be studied separately under controlled and field conditions.",
     "The authors recommended that breeding for seedling tolerance and for yield be studied separately under controlled and field conditions (Sallam et al., 2018)."),

    ("a transfer rate of approximately 22% within a purpose-built experiment.",
     "a transfer rate of approximately 22% within a purpose-built experiment (Slawin et al., 2024)."),

    ("and concluded that testing the same genotypes across growth stages is essential.",
     "and concluded that testing the same genotypes across growth stages is essential (Mohamed et al., 2023)."),

    # ---- §4.2 -----------------------------------------------------------
    ("At 20% PEG the correlations weakened and the root:shoot ratio became non-significant.",
     "At 20% PEG the correlations weakened and the root:shoot ratio became non-significant (El-Rawy and Hassan, 2014)."),

    ("This directly contradicts the 164-line barley study above. Both are recent, both use large populations, and both use PEG.",
     "This directly contradicts the 164-line barley study above (Badr et al., 2025). Both are recent, both use large populations, and both use PEG."),

    ("This is the only connecting study in the Solanaceae, and it supports transfer.",
     "This is the only connecting study in the Solanaceae, and it supports transfer (Pessoa et al., 2023)."),

    ("but it demonstrates that some early-measured traits carry predictive signal.",
     "but it demonstrates that some early-measured traits carry predictive signal (Köhl et al., 2023)."),

    # ---- §4.3 -----------------------------------------------------------
    ("If tolerance at different stages is controlled by largely non-overlapping loci, then a single-stage screen cannot function as a general proxy, and the search for one is misdirected.",
     "If tolerance at different stages is controlled by largely non-overlapping loci, then a single-stage screen cannot function as a general proxy, and the search for one is misdirected (Okunlola et al., 2017; Sallam et al., 2018)."),

    # ---- §5.1 -----------------------------------------------------------
    ("CRISPR validation exists, with *SlMAPK3* mutants showing enlarged stomatal apertures, elevated H₂O₂ and malondialdehyde, increased electrolyte leakage, reduced antioxidant enzyme activity, and down-regulation of *SlDHN*, *SlDREB* and *SlGST*.",
     "CRISPR validation exists, with *SlMAPK3* mutants showing enlarged stomatal apertures, elevated H₂O₂ and malondialdehyde, increased electrolyte leakage, reduced antioxidant enzyme activity, and down-regulation of *SlDHN*, *SlDREB* and *SlGST* (Pang et al., 2024)."),

    ("loci on chromosomes 5 and 6 harboured candidate genes including *GRL1*, *CYP77A19* and an endoglucanase-like gene, with effects attributed to possible *cis*-regulatory variation.",
     "loci on chromosomes 5 and 6 harboured candidate genes including *GRL1*, *CYP77A19* and an endoglucanase-like gene, with effects attributed to possible *cis*-regulatory variation (Rai et al., 2026)."),

    ("A screen of 100 accessions identified resistant material at the vegetative stage.",
     "A screen of 100 accessions identified resistant material at the vegetative stage (Thin et al., 2026)."),

    ("with principal component analysis identifying catalase activity, proline, stomatal conductance, transpiration rate, root length and shoot dry weight as the traits driving differences and explaining 80.2% of total variation.",
     "with principal component analysis identifying catalase activity, proline, stomatal conductance, transpiration rate, root length and shoot dry weight as the traits driving differences and explaining 80.2% of total variation (Anagha et al., 2026)."),

    ("the wild species *S. macrocarpon* essentially maintained biomass and *S. dasyphyllum* showed an intermediate response.",
     "the wild species *S. macrocarpon* essentially maintained biomass and *S. dasyphyllum* showed an intermediate response (Krommydas et al., 2025)."),

    # ---- §5.2 -----------------------------------------------------------
    ("with silencing increasing malondialdehyde under stress.",
     "with silencing increasing malondialdehyde under stress (Ma et al., 2021)."),

    ("all twelve examined aquaporins were up-regulated in tolerant KCa-4884 and down-regulated in susceptible G-4.",
     "all twelve examined aquaporins were up-regulated in tolerant KCa-4884 and down-regulated in susceptible G-4 (Sahitya et al., 2019)."),

    # ---- §5.3 -----------------------------------------------------------
    ("with recent work reaching approximately 5% effective efficiency through vacuum treatment, avoidance of pre-culture, and co-expression of a growth-regulating factor.",
     "with recent work reaching approximately 5% effective efficiency through vacuum treatment, avoidance of pre-culture, and co-expression of a growth-regulating factor (Tang et al., 2025); earlier work established stable editing in both hot and bell pepper cultivars (Park et al., 2021)."),

    ("with efficiencies between 67% and 79%, and the literature now describes VIGS as often the key, and sometimes the only viable, tool for high-throughput functional screening in this crop.",
     "with efficiencies between 67% and 79% (Choi et al., 2019), and the literature now describes VIGS as often the key, and sometimes the only viable, tool for high-throughput functional screening in this crop."),

    ("with a second gene edited to produce a visible phenotype, and the method is tissue-culture-free.",
     "with a second gene edited to produce a visible phenotype, and the method is tissue-culture-free (Kang et al., 2025)."),

    # ---- §6 -------------------------------------------------------------
    ("Markers Hpms1172 and CAMS177 have been associated with a stress tolerance index in chilli across a 78-genotype panel, with principal coordinate analysis aligning with marker-assisted selection output.",
     "Markers Hpms1172 and CAMS177 have been associated with a stress tolerance index in chilli across a 78-genotype panel, with principal coordinate analysis aligning with marker-assisted selection output (Bukhari et al., 2024)."),

    ("interrogates the genes the literature already implicates — *CaNAC46*, *CaDREBLP1*, the *CaDREB*, *CaP5CS* and aquaporin families — across the genotype panel, identifying sequence polymorphism within them.",
     "interrogates the genes the literature already implicates — *CaNAC46*, *CaDREBLP1*, the *CaDREB*, *CaP5CS* and aquaporin families (Ma et al., 2021; Sahitya et al., 2019) — across the genotype panel, identifying sequence polymorphism within them."),

    ("two pools of extreme-phenotype individuals are sequenced, and allele-frequency differences localise the contributing region. It requires only two sequencing reactions.",
     "two pools of extreme-phenotype individuals are sequenced, and allele-frequency differences localise the contributing region (Majeed et al., 2022). It requires only two sequencing reactions."),

    ("*Capsicum annuum* has an approximately 3.5 Gb genome, among the larger among cultivated Solanaceae, which raises the sequencing requirement substantially relative to rice or *Arabidopsis*.",
     "*Capsicum annuum* has an approximately 3.5 Gb genome, among the larger among cultivated Solanaceae, which raises the sequencing requirement substantially relative to rice or *Arabidopsis* (Liu et al., 2023)."),

    ("Genotyping-by-sequencing provides genome-wide markers at approximately US$10–50 per sample and has been applied in pepper, including for combined QTL and association mapping of *Phytophthora capsici* resistance.",
     "Genotyping-by-sequencing provides genome-wide markers at approximately US$10–50 per sample and has been applied in pepper, including for combined QTL and association mapping of *Phytophthora capsici* resistance (Sahoo et al., 2025)."),

    ("A published comparison of PCR-based SNP genotyping platforms positions KASP and PACE as the most cost-effective options for small laboratories, noting that the ability to run these assays on standard real-time instruments makes them accessible to laboratories with limited resources.",
     "A published comparison of PCR-based SNP genotyping platforms positions KASP and PACE as the most cost-effective options for small laboratories, noting that the ability to run these assays on standard real-time instruments makes them accessible to laboratories with limited resources (Sahoo et al., 2025)."),

    ("The figures used above are drawn from a peer-reviewed review of PCR-based SNP genotyping and from the same source for sequencing-based approaches.",
     "The figures used above are drawn from a peer-reviewed review of PCR-based SNP genotyping (Sahoo et al., 2025) and from the same source for sequencing-based approaches."),
]


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    original = text
    failures, applied = [], []

    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n != 1:
            failures.append((n, old[:90]))
            continue
        text = text.replace(old, new, 1)
        applied.append(old[:70])

    if failures:
        print("FAILED ANCHORS (not applied):")
        for n, snippet in failures:
            print(f"  count={n}  {snippet!r}")
        print("\nNo changes written — fix the anchors and re-run.")
        return 1

    SRC.write_text(text, encoding="utf-8")
    print(f"Applied {len(applied)} replacements cleanly.")
    print(f"Words: {len(original.split())} -> {len(text.split())}")
    print(f"Citations now in body: {text.count('et al., ') + text.count(' and Kaufmann, ')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
