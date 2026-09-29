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
