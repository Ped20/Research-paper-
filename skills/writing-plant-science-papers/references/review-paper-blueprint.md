# Review Paper Blueprint

**Structural guidance for literature reviews in molecular biology, plant science, and agriculture.**

This mode is **missing from the systems-paper original** (which covered conference papers) and was missing from the first version of this skill. It exists because a review is not an IMRaD paper with the Results section deleted — it is a different genre with a different burden of proof.

Companion files: `SKILL.md` (research papers), `manuscript-scaffold.md`, `reporting-checklists.md`.

---

## 1. The First Fork: What Kind of Review?

Decide this before anything else. The type determines the structure, the Methods section, and the search obligation.

| Type | Structure | Search obligation | Suitable when |
| --- | --- | --- | --- |
| **Narrative / critical** | Thematic sections + synthesis | Documented search, but not exhaustive | The literature is heterogeneous and the contribution is **interpretation** |
| **Systematic (PRISMA)** | Methods with search string, screening diagram, then synthesis | Exhaustive, reproducible, with inclusion/exclusion criteria and a PRISMA flow diagram | A specific, answerable question exists and the corpus is bounded |
| **Scoping** | Broad mapping of what exists | Documented, systematic, but no quality appraisal | The field is emerging and the question is "what has been done?" |
| **Meta-analysis** | Systematic search + quantitative pooling | Exhaustive plus effect-size extraction | Studies report comparable quantitative outcomes — **rare in plant-science screening literature** |

**Honest guidance:** meta-analysis is usually not achievable in this space. Screening studies report different PEG concentrations, different traits, different indices, and often no variance measures. If you cannot extract a common effect size, do not pretend to — write a **critical review** with a documented search, and say so.

---

## 2. The Review Quality Ladder

The analogue of the research Evidence Ladder (§2 of `SKILL.md`). Score your draft against it. **A review that stops at R1 is a literature dump, and reviewers say so.**

| Level | What the review does | Verdict |
| --- | --- | --- |
| **R0** | Cites single studies as if they were general findings | Fails — overclaiming by proxy |
| **R1** | Lists studies sequentially, one paragraph each | Literature dump. Rejected or heavily criticised |
| **R2** | Tabulates studies on defined, comparable parameters | Acceptable minimum for a review |
| **R3** | Appraises study quality; reports conflicting evidence and explains it | A credible review |
| **R4** | Synthesis yields a **decision framework, standard, or testable recommendation** | A good review |
| **R5** | The framework identifies a specific falsifiable gap and predicts what would resolve it | A review people cite |

**Target R4 minimum.** R2 alone is what gets desk-rejected as "no added value over the primary literature."

### Rule: a review must have a thesis

Not a topic — a **thesis**. "Reviewing the literature on X" is a topic. "The standard method for X is widely used but its predictive validity is unestablished, and here is what follows from that" is a thesis.

State it in one sentence before drafting. If you cannot, you are not ready to write a review.

---

## 3. Structure

```
Title
Abstract
  S1  Why the topic matters
  S2  The problem with the current literature  (this is the thesis)
  S3  What this review does differently
  S4  The framework or conclusion proposed
  S5  Who should read it and why

1. Introduction
   - The subject and its stakes
   - Why early-stage / current approaches are attractive
   - ⭐ THE PROBLEM with the current literature (your thesis)
   - Scope, boundaries, and what this review does not cover
   - Search strategy (see §4)

2-6. THEMATIC SYNTHESIS SECTIONS
   These are the review's "Results". Ordered so the argument builds.
   Each ends with a synthesised claim, not a summary.

7. Synthesis / Integrated framework
   ⭐ The R4 deliverable. A decision framework, standard protocol,
      or normative recommendation — usually a figure plus a table.

8. Future directions
   Specific, testable, and tied to the gaps identified.

9. Conclusion
   The thesis restated, plus what would change it.

References
```

**Reviews have no Results section.** If yours does, you are either writing a systematic review (then it is "Results of the search" and belongs before synthesis) or you have drifted into primary research.

### Section ordering principle

Order thematic sections so each one sets up the next. The most common failure is parallel structure — sections that could be shuffled without loss. If yours can be reordered freely, the argument is missing.

Good ordering for a methods-and-applications review:

```
The tool/approach  →  its documented limitations  →  what it has produced
   →  whether the outputs hold up  →  how to get further (molecular/deployment)
```

This deliberately places the limitations section **before** the achievements, because the limitations are what make the synthesis section necessary.

---

## 4. Search Strategy — state it even in a narrative review

A review without a documented search is an opinion piece with citations. Report:

- [ ] Databases searched, with dates of search
- [ ] Full search strings, at least in supplementary
- [ ] Date range and justification
- [ ] Inclusion and exclusion criteria
- [ ] Language restrictions
- [ ] Number of records screened → included (PRISMA flow diagram if systematic)
- [ ] How disagreements or ambiguous inclusions were resolved
- [ ] **A stated acknowledgement that the search may not be exhaustive** (if narrative)

For a critical/narrative review, a short "Methodology of this review" subsection is sufficient — roughly 150–300 words. It costs little and pre-empts the "this is selective" criticism.

---

## 5. Handling Evidence in a Review

The evidence ladder from `SKILL.md` §2 applies to every **study you cite**, and it constrains what **you** may conclude from them.

| The cited study shows | You may write | You may not write |
| --- | --- | --- |
| Expression correlation | "expression was associated with tolerance (ref)" | "this gene confers tolerance" |
| A mutant phenotype | "was required for tolerance in that system" | "regulates drought tolerance" |
| Overexpression in a heterologous host | "conferred tolerance when expressed in *Arabidopsis*" | "confers tolerance in chilli" |
| One genotype panel, one season | "was identified as tolerant in that study" | "is drought tolerant" |

**Additional review-specific rules:**

- **Distinguish consistent from isolated findings.** One study is a report; three independent studies agreeing is a finding. Say which you have.
- **Report contradictions.** A review that omits disconfirming studies is advocacy. Where studies conflict, present both and propose why (different PEG concentration, different stage, different genotype set, different index).
- **Report negative and null results** where the literature contains them. Their absence is itself a finding worth stating.
- **Track study quality.** Small panels, single seasons, no replication detail, no checks — flag these. A table column for study limitations is the cheapest way to raise a review from R2 to R3.
- **Beware publication bias.** Positive results get published. If nobody has reported a failing screen, that does not mean none failed.
- **Do not launder weak evidence through repetition.** Ten studies repeating the same weak design is still weak evidence, and it is a reviewer's job to say so.

---

## 6. Tables and Figures — what a review actually delivers

### Tables are the currency

| Table type | Content | Why |
| --- | --- | --- |
| **Study comparison** | One row per study: system, n, treatment levels, traits, indices, outcome, **study limitations** | The core R2→R3 artefact |
| **Method/agent comparison** | Options × mechanism × cost × artefacts × suitability | Justifies the recommendation |
| **Gene/target inventory** | Gene, family, organism, evidence type (transgenic / expression only / mutant), level, reference | Prevents evidence inflation |
| **Platform comparison** | Technique × cost × throughput × equipment × skill × accessibility | The practical R4 output |
| **Proposed standard** | Parameter, recommended minimum, rationale, source | The R4→R5 artefact |

### Figures in reviews are conceptual, not empirical

- **Framework / decision flowchart** — the synthesis deliverable
- **Conceptual model** — mechanism or system, with solid = established and dashed = hypothesised
- **Compiled plot** — relationships extracted from multiple studies (e.g. concentration vs. osmotic potential), with sources; this is legitimate and valuable, but each point must be cited
- **Gap map** — what has been studied vs. what has not

**Never** present a schematic as if it were data. Label conceptual figures explicitly as conceptual. If you plot extracted values from multiple studies, state the extraction method and cite every source.

---

## 7. The R4 Deliverable — what makes the review worth citing

A review earns citations by producing something reusable. Pick at least one:

| Deliverable | Example |
| --- | --- |
| **Minimum standard** | A table of required parameters any future study should report |
| **Decision framework** | "If your lab has only PCR, do X; with NGS access, do Y" |
| **Tiered protocol** | A staged pipeline with decision rules at each stage |
| **Corrected relationship** | "The widely cited correlation between A and B does not hold under C" |
| **Gap map with falsifiable predictions** | "If X were true, we would observe Y; nobody has tested this" |

Without one of these, the review is a summary — and summaries get cited rarely and cited badly.

---

## 8. Integrity in Reviews — the distinctive risks

**Fabricating data is not the usual review failure. The usual failures are:**

- [ ] **Citation of studies that do not exist**, or misattribution of findings to the wrong paper. Every citation must be verified against the source. Memory-generated references are now a recognised LLM signature and trigger desk rejection.
- [ ] **Overstating cited findings** — describing an expression correlation as a functional demonstration.
- [ ] **Omission of contradicting evidence.**
- [ ] **Invented numerical summaries** — do not write "the mean improvement was 30%" unless you computed it from extracted data and said how.
- [ ] **Hypothetical data presented as results.** Modelling is legitimate; presenting modelled or illustrative values as findings is not.
- [ ] **Predatory or non-peer-reviewed sources** carrying equal weight to primary literature.
- [ ] **Self-citation inflation.**
- [ ] **Presenting a schematic as data.**

### On illustrative and hypothetical material

Legitimate:
- Generic placeholders in a conceptual schematic (`Genotype A`, `Genotype B`), clearly labelled as schematic
- A proposed panel size or design for **future** work, labelled as a recommendation
- A worked example explicitly labelled `illustrative example` with real cited values where possible

Not legitimate:
- Reporting results from genotypes that were never tested
- Presenting simulated values as findings
- A table of "representative genotypes" that are not real and cited

**The test:** could a reader reproduce or verify this? If not, it must be labelled as conceptual.

---

## 9. Venue Selection for Reviews

| Venue family | Review length | Fit |
| --- | --- | --- |
| *Trends in Plant Science*, *Annual Review of Plant Biology* | Invited / 6,000–10,000 | Usually commissioned; strong synthesis expected |
| *Frontiers in Plant Science* (Review) | 12,000 words | Open to unsolicited reviews; needs an R4 deliverable |
| *Agronomy for Sustainable Development* | ~8,000 | Applied/agronomic synthesis |
| *Scientia Horticulturae* (Review) | ~6,000–8,000 | Strong fit for horticultural crop reviews |
| *Plant Physiology Reports*, *Journal of Horticultural Sciences*, *Vegetable Science* | Regional/indices | Realistic for a well-executed R3–R4 review |
| *Plants* (MDPI), *Agronomy* (MDPI) | Variable | Accessible, fast, open access; APC applies |
| *CAB Reviews*, *Advances in Agronomy* | Variable | Strong for applied synthesis |

> Verify current limits and whether reviews are **invited only**. Many high-impact review venues do not accept unsolicited submissions — check before writing.

---

## 10. Workflow

```
1.  Decide the review type (§1). If meta-analysis is not possible, say so and pick critical.
2.  Write the THESIS in one sentence (§2). Without it, stop.
3.  Run and document the search (§4). Record numbers screened and included.
4.  Build the study comparison table FIRST (§6). This is the review's backbone.
5.  Identify what the tables show that no single paper says — that is your contribution.
6.  Appraise study quality; add a limitations column and fill it (§5).
7.  Order the thematic sections so each sets up the next (§3).
8.  Design the R4 deliverable — framework, standard, or corrected relationship (§7).
9.  Draft the synthesis section around that deliverable.
10. Draft Introduction backwards from the thesis.
11. Draft Abstract and Title last.
12. Verify EVERY citation against the source (§8).
13. Score the draft on the Review Quality Ladder. Below R4? Revise, do not submit.
14. Check venue: length, format, and whether reviews are invited.
```

---

## 11. Self-Check

- [ ] The review has a **thesis**, stated in one sentence
- [ ] Review type chosen deliberately, with the search documented
- [ ] Aiming at **R4 or above** on the quality ladder
- [ ] Study comparison table exists, with a study-limitations column
- [ ] Conflicting evidence reported, not smoothed over
- [ ] Cited findings are described at their true evidence level — no inflation
- [ ] Every citation verified against the source; none from memory
- [ ] Every numerical claim traceable to a source, or explicitly computed and its method stated
- [ ] Schematic and conceptual figures labelled as such
- [ ] No hypothetical data presented as results
- [ ] At least one reusable deliverable: standard, framework, protocol, or corrected relationship
- [ ] Future directions are specific and testable, tied to identified gaps
- [ ] Venue accepts unsolicited reviews, and length is within limit

---

## 12. Sources

1. Grant & Booth (2009) "A typology of reviews." *Health Information & Libraries Journal* 26:91–108. doi:10.1111/j.1471-1842.2009.00848.x — the review-type taxonomy in §1.
2. Page et al. (2021) "The PRISMA 2020 statement." *BMJ* 372:n71. doi:10.1136/bmj.n71 — required for systematic reviews.
3. Munn et al. (2018) "Systematic review or scoping review?" *BMC Medical Research Methodology* 18:143. doi:10.1186/s12874-018-0611-x.
4. Gopen & Swan (1990) "The Science of Scientific Writing." *American Scientist* 78:550–558 — paragraph-level construction.
5. Mensh & Kording (2017) "Ten simple rules for structuring papers." *PLoS Comput Biol* 13(9):e1005619 — context–content–conclusion logic applies to review sections too.
6. The current Guide for Authors for your target venue — **outranks every source above on matters of format.**
