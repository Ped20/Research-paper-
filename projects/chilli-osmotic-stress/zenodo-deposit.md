# Zenodo deposit — metadata and instructions

## Read this first: Zenodo is a repository, not a journal

**Zenodo is CERN's general-purpose research repository.** It is operated by CERN and built under the OpenAIRE programme, it is free to deposit into and free to read from, and every deposit receives a DataCite DOI (prefix `10.5281`).

It is not a journal. Specifically:

| Expectation | Reality at Zenodo |
| --- | --- |
| Peer review | **None.** There is no editorial board, no referees and no editorial screening. |
| Journal indexing | **None.** A Zenodo DOI does not make the work a journal article, and the deposit is not indexed as journal literature in Scopus or Web of Science. |
| "Published" status | A Zenodo record is citable and permanent, but it is a *deposit*, not a publication in the peer-reviewed sense. |
| Cost | Free. No deposit fee, no APC. |
| What you do get | A permanent DOI, an open-access landing page, long-term preservation at CERN, ORCID linkage, versioning, and immediate global visibility. |

Two consequences worth stating plainly, because they affect how this counts for you:

1. **A Zenodo DOI is not a peer-review credential.** It is a persistent identifier and an archiving service.
2. **Many institutions do not count repository deposits as publications** for promotion, appraisal or PhD requirements. If that matters to you, check before you decide that Zenodo is where this ends.

This does not make Zenodo a poor choice. It makes it a poor *only* choice. See the recommended sequence below.

---

## Recommended sequence

**Deposit to Zenodo now, and still send the manuscript to a peer-reviewed venue.**

1. **Deposit the preprint to Zenodo** (or to AgriRxiv, the agriculture preprint server). Free, immediate, citable, permanent. This establishes priority and puts the work in front of readers today.
2. **Submit the same manuscript to a zero-cost peer-reviewed venue** — for example *Journal of Horticultural Sciences* (Society for Promotion of Horticulture at ICAR-IIHR Bengaluru; no APCs; Scopus and Web of Science ESCI; publishes reviews). Most journals permit preprints; confirm the policy on the venue's own page before depositing.
3. **When it is accepted, publish a new version of the Zenodo record** containing the accepted or published version, and add the journal DOI as a related identifier. Zenodo versions the record automatically and keeps the concept DOI stable.

This gives you the thing you actually want — free, open, citable, permanent — without giving up peer review. The cost is one extra submission step.

**If peer review is not required for your purpose**, depositing to Zenodo alone is entirely legitimate. Just describe it accurately.

---

## Metadata to paste into the Zenodo upload form

**Upload type:** `Publication` → `Preprint`
*Use `Journal article` only if and when a peer-reviewed version is published, in the versioned update.*

**Title**

> Screening for drought tolerance in *Capsicum* and the Solanaceae: methodological assumptions, an unresolved predictive link, and a cost-tiered path to markers

**Creators**

> [YOUR FULL NAME] — ORCID: [0000-0000-0000-0000]
> Affiliation: [Department, Institution, City, India]

**Description** (paste as plain text; Zenodo accepts basic HTML if you want the italicised species names)

> Drought limits productivity across the Solanaceae, and early-stage screening using polyethylene glycol (PEG) has become the standard low-cost route to identifying tolerant genotypes in chilli pepper, tomato and eggplant. This review assesses what that screening can support. Four findings emerge. First, the physicochemical basis of the treatment is less secure than its customary presentation implies: PEG solutions are non-colligative, their osmotic potential is temperature- and molecular-weight-dependent, and the assumption that PEG does not enter plant tissue is contradicted by direct measurement, including in Capsicum itself. Second, the field's default statistical treatment of germination data is inappropriate to the conditions osmotic screening creates, which drive means toward 0% and 100% where normal-error assumptions fail. Third, whether early-stage rankings transfer to field performance is genuinely unresolved: of the studies testing transfer across developmental stages, four support it and four contradict it, and the disagreement tracks identifiable design choices rather than biology alone. In Capsicum specifically, the question remains untested. Fourth, the molecular route is more accessible than pepper's transformation recalcitrance suggests, with virus-induced gene silencing and heritable virus-induced gene editing now providing tissue-culture-free validation. The review proposes a four-stage framework and a fifteen-item minimum reporting standard, of which six items require no additional experiment. The single substantive change — reporting the proportion of screen-selected genotypes that prove superior in the field — would resolve the central question using data that screening programmes already generate.
>
> Generative AI disclosure: [TOOL NAME, VERSION, PROVIDER] was used to assist with literature synthesis, drafting and language editing. The author set the scope and framing, verified every cited source against primary records and publisher metadata, drew the figures from published equations and data, and reviewed and edited all content, and takes full responsibility for the content of this deposit.

**Keywords** (Zenodo takes these one per field)

> Capsicum annuum · polyethylene glycol · drought tolerance · genotype screening · Solanaceae · osmotic stress · reporting standards · germination

**License**

> Creative Commons Attribution 4.0 International (CC BY 4.0)

**Language:** English

**Version:** `v1.0 — preprint, not peer reviewed`

**Related identifiers**
Add each of these after the preprint is up, if you also deposit to a server:

> `is identical to` → AgriRxiv DOI, if you cross-post
> `is supplemented by` → the supplementary tables file

**Files to upload**

| File | Notes |
| --- | --- |
| `deposit/REVIEW-deposit.pdf` | The manuscript. 28 pages, ~657 KB. |
| `supplementary-table-S1.md` | Supplementary Tables S1–S2. Convert to PDF first if you prefer a single format. |
| Figure files (optional) | `figures/figure-1-framework.png` … `figure-5-concordance-reporting.png`, all 300 dpi. Upload so readers can reuse them individually. |

**Do not upload** `REVIEW-final.md`. It contains the author notes, the venue note and the word-count audit — internal working documents.

---

## Before you publish the record

- [ ] Replace `[AUTHOR NAME]`, `[Department, Institution, City, India]` and the ORCID placeholder. Both appear on the PDF cover page and in the metadata.
- [ ] Fill in `[TOOL NAME, VERSION, PROVIDER]` in the AI disclosure. **Do not omit this.** Every major publisher and both main preprint servers require it, and a disclosed AI-assisted review is permitted while an undisclosed one is a policy violation.
- [ ] Decide whether to deposit the supplementary tables as a separate file or as part of the PDF.
- [ ] If you intend to submit to a journal afterwards, check that venue's preprint policy first and note the embargo terms, if any.

---

## Regenerating the PDF

If the manuscript changes, rebuild the deposit files:

```bash
cd projects/chilli-osmotic-stress
python3 make-deposit.py \
    --author "Your Name" \
    --orcid "0000-0002-1825-0097" \
    --affiliation "Department, Institution, City, India"
```

Outputs `deposit/REVIEW-deposit.pdf` and `deposit/REVIEW-deposit.html`. The script strips the author notes automatically, embeds Figures 1–5 with their legends after the Conclusion, and uses DejaVu Serif so that italics and the Greek and mathematical characters in the manuscript render correctly.

If `xhtml2pdf` is unavailable, the HTML output is a complete fallback: open it in a browser and print to PDF.
