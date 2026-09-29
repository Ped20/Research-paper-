# Reference Verification Log

**Date of check:** 2026-09-29
**Method:** Crossref REST API (`api.crossref.org`), queried per DOI and by bibliographic search. Metadata compared field by field — title, authors, journal, volume, issue, pages, year.
**Scope:** all 46 references in the completed bibliography, plus every DOI carried in the working drafts.

---

## 1. Summary

| Outcome | Count |
| --- | --- |
| References verified exactly as cited | 30 |
| **DOIs that resolved to a different paper — corrected** | **10** |
| Entries rebuilt from bibliographic search after the DOI failed | 4 |
| Entries that could not be verified | 2 |
| In-text citations present in the manuscript body | 0 → **59 sites** |

**The headline finding: ten DOIs cited in the working bibliography pointed at different papers.** This is a high rate — roughly one in three of the DOIs present. It is worth understanding why, because the cause is systematic rather than careless.

Every one of the ten was plausible. They had the right shape, the right journal family, the right year. None was a random string. The most likely explanation is that they were **constructed rather than copied** — assembled from a remembered pattern (journal prefix + plausible article number) rather than resolved from the source. That is exactly the failure mode that memory-generated citations produce, and exactly what Frontiers' reference checks are designed to catch. Three were caught only because the title returned by Crossref was obviously unrelated; several others differed only in volume, page or article number and would have passed a casual glance.

**This matters for the review's own argument.** The review's thesis is that unverified claims propagate through citation loops. The reference list is where that propagation is most mechanical, and it happened here at a rate of one in three.

---

## 2. DOIs that resolved to a different paper

Each row: the DOI as written → what it actually is → the correct DOI.

| # | DOI as cited | Actually resolves to | Corrected to |
| --- | --- | --- | --- |
| 1 | `10.1017/S0960258512000088` | Not found in Crossref | `10.1017/S0960258512000025` — Sileshi (2012) |
| 2 | `10.1016/j.scienta.2025.114315` | Guan et al., *Citrus reticulata* flavonoid metabolomics, *Sci. Hortic.* 350:114315 | `10.1016/j.hpj.2024.11.008` — Thin et al. (2026), *Capsicum* accessions |
| 3 | `10.1016/j.xplc.2023.100744` | Zhou et al., MYB30/MYB75 anthocyanin biosynthesis in *Arabidopsis*, *Plant Commun.* 5(3) | `10.1016/j.hpj.2023.07.003` — Liu et al. (2024), *hisI* in pepper |
| 4 | `10.1016/j.molp.2024.02.006` | Wu et al., MYC2–PUB22–JAZ4 jasmonate signalling in tomato, *Mol. Plant* 17(4):598–613 | `10.1016/j.molp.2024.02.011` — Zhang et al. (2024), OcBSA, 17(4):648–657 |
| 5 | `10.1016/j.scienta.2017.09.049` | Beyaz, mechanical damage in apples, *Sci. Hortic.* 228:49–55 | `10.1016/j.scienta.2017.06.020` — Okunlola et al. (2017) |
| 6 | `10.1111/j.1469-8137.1970.tb02473.x` (drafted) | — | `10.1111/j.1469-8137.1970.tb02446.x` — Lawlor (1970) |
| 7 | `10.11648/j.jps.20190704.12` | Not indexed in Crossref | Unresolved — see §4 |
| 8 | `10.1186/s12870-02764-y` variants | — | `10.1186/s12870-020-02764-y` — Ma et al. (2021) |
| 9 | `10.1242/...` (Sallam wheat diallel) | — | `10.9787/PBB.2014.2.3.276` — El-Rawy and Hassan (2014) |
| 10 | `10.1093/jxb/erab...` (pepper GWAS draft) | — | `10.1093/jxb/erag385` — Rai et al. (2026) |

**Journal-level errors corrected.** Three entries named the wrong journal entirely:

| Entry | Cited journal | Actual journal |
| --- | --- | --- |
| Thin et al., *Capsicum* accessions | *Scientia Horticulturae* | *Horticultural Plant Journal* |
| Liu et al., *hisI* pepper | *Plant Communications* | *Horticultural Plant Journal* |
| Sahoo et al., SNP genotyping | *Molecular Breeding* (drafted) | *Discover Plants* |

**Author-list errors corrected.** Several entries carried an incorrect first author or a wrong author count, including Molla et al. (2019), Muzafarov et al. (2026), and Thin et al. (2026).

---

## 3. Entries recovered by bibliographic search

These citations were substantively correct — the paper exists — but the identifier was wrong or absent. The correct record was located by searching Crossref on the title.

| Reference | Recovered as |
| --- | --- |
| Lawlor (1970), *New Phytologist* 69(2):501–513 | doi:10.1111/j.1469-8137.1970.tb02446.x |
| Lagerwerff, Ogata and Eagle (1961), *Science* 133(3463):1486–1487 | doi:10.1126/science.133.3463.1486 |
| Janes (1974), *Plant Physiology* 54(3):226–230 | doi:10.1104/pp.54.3.226 |
| Sharma (1973), *Agronomy Journal* 65(6):982–987 | doi:10.2134/agronj1973.00021962006500060041x |
| Choi et al. (2019), *Plant Physiology* 181(3):867–880 | doi:10.1104/pp.19.00836 |
| Sahitya et al. (2019), *Physiol. Mol. Biol. Plants* 25(3):637–647 | doi:10.1007/s12298-019-00655-7 |
| Kang et al. (2025), *The Plant Journal* 122(5) | doi:10.1111/tpj.70257 |
| Tang et al. (2025), *Plant Biotechnology Journal* 23(11):4752–4754 | doi:10.1111/pbi.70216 |
| Alnaddaf et al. (2026), *BMC Plant Biology* 26(1) | doi:10.1186/s12870-026-08989-7 |
| Tajaragh et al. (2022), *Horticulturae* 8(12):1117 | doi:10.3390/horticulturae8121117 |
| Pang et al. (2024), *Biology* 13(12):1076 | doi:10.3390/biology13121076 |
| Park et al. (2021), *IJMS* 22(8):3921 | doi:10.3390/ijms22083921 |
| Zhang et al. (2024), OcBSA, *Molecular Plant* 17(4):648–657 | doi:10.1016/j.molp.2024.02.011 |

Two of these substantially improved the review. **Thin et al. (2026)** turned out to be the 100-accession *Capsicum* vegetative screen whose source had been recorded only as "ScienceDirect (2025)" — the citation is now exact. **Tang et al. (2025)** confirmed the ~5% transformation efficiency figure that §5.3 rests on.

---

## 4. Unresolved

| Item | Status | Disposition |
| --- | --- | --- |
| **Molla et al. (2019)**, *J. Plant Sci.* 7(4):76–85, doi:10.11648/j.jps.20190704.12 | DOI does not resolve in Crossref; Science Publishing Group is not consistently indexed | Verify against the publisher's own record. The data are used in Table 2 (47 genotypes, BD-10906 series) |
| **⟦VERIFY-1⟧** — §1.2, citations for the tomato omics and pepper genomics reviews | Reviews named generically; the identity of each is known but no verified record was captured | Supply both citations or generalise the sentence |
| **⟦VERIFY-2⟧** — §2.1, PEG 4000 in cytoplasm vs PEG 6000 in apoplast of common bean root tips | Source not recorded during drafting; not located in the verification pass | Locate the primary source or delete the sentence |
| **⟦VERIFY-3⟧** — §2.3 and Table 1, durum wheat osmotica comparison; and solidified-PEG raft systems (*Cereal Research Communications* 2010) | Two separate sources; neither located in Crossref | Locate both. The solidified-PEG point is load-bearing for the §2.5 recommendation |
| **⟦VERIFY-4⟧** — §3.4, three chilli studies used as statistical-practice examples | Not located; the examples were drawn from a search that did not capture identifiers | Locate or replace with the Sileshi (2012) aggregate |
| **⟦VERIFY-5⟧** — §3.4, "a direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible" | Source not captured | Locate or soften |
| **⟦VERIFY-6⟧** — §3.4, most tomato genotypes fail to germinate above −0.35 MPa | Source not captured; claim is repeated in §3.3 of the draft notes | Locate or delete; **this claim carries weight in the ceiling-effect argument** |

**Priority:** ⟦VERIFY-3⟧ and ⟦VERIFY-6⟧ are the two that matter. The first supports a concrete methodological recommendation; the second supports the case for genotype-specific stress levels. The remainder can be resolved by deletion without weakening the argument.

---

## 5. Claim deleted for want of a source

One sentence was removed from §2.4 rather than left uncited:

> "Longer exposure to PEG 400 has been associated with increased cation accumulation in the root xylem of pepper, an ionic effect in a nominally non-ionic treatment."

It was flagged in the study inventory as "⚠️ verify primary source" and could not be confirmed. The sentence was plausible and would have strengthened the section, which is precisely why it was removed: an uncitable but attractive claim is the kind that survives into print. Its deletion does not weaken §2.4, which retains the Lawlor penetration findings and the Fan and Blake comparison.

---

## 6. What this exercise indicates

**Verification changed the manuscript's content, not just its formatting.** The single largest consequence was not a reference fix at all: it was the discovery that **the body contained no in-text citations whatsoever.** A 9,300-word review with a 46-item bibliography and no citations in the text is not a review, and it would have been rejected before review. Fifty-nine citation sites were inserted.

**Absence claims remain the most dangerous form.** Three claims of the form "no study exists" had already been withdrawn earlier in this project. The reference audit surfaced a fourth class of problem — not absent evidence, but *misaddressed* evidence.

**A workable rule, learned at some cost here:** verify each identifier by resolving it and reading the returned title. Never accept a DOI because it looks right, and never accept one because a search engine surfaced the article — the search engine will surface the article for a wrong DOI if the surrounding text is close enough.

---

## 7. Round-5 addendum: the six remaining markers, resolved

Every marker in §4 was traced to a primary source and replaced in the body. No placeholder remains anywhere in `REVIEW-final.md`. Each source below was confirmed through Crossref (DOI resolving to the expected title) or, where the journal is not indexed, against the publisher's own PDF.

| Marker | Claim it supported | Source located | Identifier |
| --- | --- | --- | --- |
| VERIFY-1 (§1.2) | Two competing reviews of tomato omics and pepper genomics, named generically | Taheri, Gantait, Azizi and Mazumdar (2022), *3 Biotech* 12(3):63 — tomato drought omics, non-coding RNAs, CRISPR/Cas9, with a gene list | doi:10.1007/s13205-022-03132-3 |
| VERIFY-2 (§2.1) | Glycerol and PEG 4000 act mainly in the cytoplasm; PEG 6000 additionally dehydrates the apoplast | Yang, Eticha, Rao and Horst (2010), *J. Exp. Bot.* 61(12):3245–3258 — common bean root tips, cell-wall porosity | doi:10.1093/jxb/erq146 |
| VERIFY-3 (§2.3, Table 1) | (a) PEG-6000 outperforms mannitol in durum wheat; (b) solidified-PEG raft systems block PEG entry | (a) Bousba et al. (2021), *J. Bioresour. Manag.* 8(3):57–66; (b) Comeau et al. (2010), *Cereal Res. Commun.* 38(4):471–481 | doi:10.35691/JBM.1202.0195; doi:10.1556/CRC.38.2010.4.3 |
| VERIFY-4 (§3.4) | Three chilli studies used as statistical-practice examples | The screening studies themselves, now cited in full: Sharma et al. (2024), Millah et al. (2021) and the studies in Table 2 | see Table 2 |
| VERIFY-5 (§3.4) | "A direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible" | Gianinetti (2020), *Data* 5(1):6 — binomial germination data; ANOVA defensible only in the 0.3–0.7 proportion range, outside which an angular transform or another model is required | doi:10.3390/data5010006 |
| VERIFY-6 (§3.4) | Most tomato genotypes fail to germinate above −0.35 MPa | Sivakumar, Durga Devi and Chandrasekar (2014), *Madras Agric. J.* 101(10–12):369–373 — 32 genotypes screened at −0.2 and −0.35 MPa; the best line germinated at 60.0% at the higher stress. Reworded in the manuscript to "germination was arrested in most genotypes at −0.35 MPa" | no DOI (not indexed); publisher PDF retrieved |

**What resolution changed.** Two of the six were not merely citations but corrections to the claim as drafted.

1. **VERIFY-5 was a nearer miss than it appeared.** The sentence as drafted implied that a direct model comparison *supported* ANOVA. The located source says the opposite in its detail: ANOVA on untransformed germination proportions is defensible in a narrow band around the middle of the scale and fails at the extremes — which is exactly where osmotic screening operates, because the treatment is designed to drive germination toward 0%. The claim is now stated conditionally and carries the source's own range, not the review's paraphrase of it.
2. **VERIFY-6 was reworded, not merely cited.** The source reports the strong line LE 18 at 60.0% germination at −0.35 MPa against 96.7% at −0.2 MPa, with most of the 32-genotype panel failing entirely at the higher stress. That supports "arrested in most genotypes"; it does not support a statement about a universal ceiling. The distinction matters because the manuscript uses the value to argue for genotype-specific rather than fixed stress levels, and a fixed-ceiling reading would undercut the argument it is cited to support.

**A false lead rejected.** A frequently surfaced candidate for VERIFY-6 — PMC160610, *Plant Physiology* 101(2):607 — reports −0.35 MPa as a *threshold water potential for a seed population* (ψb), not as a panel-wide germination ceiling. It was discarded. Two sources reporting the same number for different quantities is precisely the failure mode this audit exists to catch.

**Bonus correction.** The Madras Agricultural Journal paper's own footer reads December 2014, resolving an ambiguity in the working bibliography between 2013 and 2014. The two in-text citations were changed to 2014 and the reference entry rebuilt from the retrieved PDF. Note that this journal assigns no Crossref DOI, so the entry cannot be DOI-verified; it is PDF-verified.

**Figure 2 is a computed check on this literature, not an illustration.** The Michel and Kaufmann (1973) relation was implemented in `make-figures.py`: at 25 °C, 10% PEG-6000 is approximately −0.15 MPa and 20% approximately −0.49 MPa. Sivakumar et al.'s stated solution strengths (123 g and 169 g per 1000 mL for −0.2 and −0.35 MPa) reproduce against the same equation, which is an independent check on both the implementation and that paper's reporting. Screening studies that state potentials several-fold more negative than the equation at the same nominal percentage are therefore flagged in Supplementary Table S1 rather than silently pooled.

**Two entries remain outside Crossref** and are honestly marked as such: Molla et al. (2019), Science Publishing Group, and Sivakumar et al. (2014), Madras Agricultural Journal. Neither is a fabricated identifier; both are publisher-verified only.


---

## 8. Round-6 addendum: three unresolved cells in Table 4, and what one of them broke

The round-5 claim that no placeholder markers remained was **too narrow**. It covered the `⟦VERIFY-n⟧` glyphs only. Three cells in Table 4 still read "⚠️ confirm" in the validation-host column, and the manuscript carried nine emoji as table status symbols. Both are now cleared.

**The three cells are resolved:**

| Cell | Source located through Crossref | Validation host established |
| --- | --- | --- |
| *CaDREBLP1* | Hong and Kim (2005), *Planta* 220(6):875–888, doi:10.1007/s00425-004-1412-5 | **None in planta.** Yeast trans-activation and in vitro DRE/CRT binding only; expression profiling in pepper. Level lowered to L0–L1 |
| *CaDIM1* (the row also carried a redundant "*MYB1*") | Lim, Lim and Lee (2022), *Front. Plant Sci.* 13:1028392, doi:10.3389/fpls.2022.1028392 | **VIGS in pepper** plus overexpression in *Arabidopsis*. Positive regulator via ABA signalling. L1–L2 |
| *CaSBP13* (previously paired with *CaDR1*) | Zhang, Zhang and Zhang (2024), *Front. Plant Sci.* 15:1412685, doi:10.3389/fpls.2024.1412685 | **VIGS in pepper** (94% silencing) plus overexpression in *N. benthamiana*. **Negative regulator** — silencing improved tolerance. L1–L2 |

*CaDR1* remains in the table as a GWAS/RNA-seq candidate with no functional validation, which is what the evidence supports; it was previously merged into a row with *CaSBP13*, obscuring the difference between a validated gene and a candidate.

**What the resolution broke.** The manuscript's Table 4 commentary claimed "**only one of the six *Capsicum* entries has functional evidence in pepper**." With *CaDIM1* and *CaSBP13* both validated by VIGS in pepper, the count is **three of eight**. The claim has been corrected. This is a correction in the field's favour: the review's argument does not depend on pepper being behind on functional validation, only on the cross-stage transfer question being untested, which it remains.

**A second error caught in the same pass.** *CaSBP13* is a **negative** regulator — silencing it improves drought tolerance. It was listed among "drought-responsive candidate genes" with no direction indicated. For a review whose thesis concerns how findings are misread downstream, listing a negative regulator without its sign is precisely the failure being described. The direction is now stated in the table.

**A third error, from a stale flag.** The Liu et al. (2023) reference in *Nature Communications* carried a note reading "⚠️ article number to confirm", with 5320. Crossref returns **5487**. Corrected.

**Emoji removed.** Nine emoji (⚠️ ×5, ✅ ×4, ❌ ×3) functioned as status symbols in Tables 4 and 5 and in Supplementary Tables S1–S2. Status is now carried by words ("Supports", "Contradicts", "Untested", "None"). Emoji are not acceptable in a journal manuscript and would have been flagged at typesetting.

**One caveat recorded rather than resolved.** The Zhang et al. (2024) author list is taken from Crossref, which returns three authors. If the published byline carries more, the reference list should be completed from the article page. The DOI and title were confirmed against Crossref and match the published record, including the grammatical error in the title, which is reproduced verbatim.

**Unicode check on the whole manuscript.** No zero-width characters, bidirectional control characters, Cyrillic homoglyphs, non-breaking spaces, tab characters or CRLF line endings. There are no hidden characters of the kind sometimes called watermarks, and there is nothing of that sort to remove.
