# Implementation steps: Zenodo + Journal of Horticultural Sciences

Two destinations, six steps, one blocker. Steps 1–3 are free and can be done today. Step 4 is a decision point. Steps 5–6 follow from it.

---

## ⚠️ Read this before anything else

**The Journal of Horticultural Sciences caps papers at 3,000 words. This manuscript is 11,932.**

Their Author Guidelines state: *"The length of the paper should not exceed 3000 words for full-length and 2500 for short communication."* The guidelines do not carve out a separate limit for review articles, although the journal does publish them.

At 11,932 words this is roughly **four times** the stated limit. This is not a formatting problem and it cannot be solved by trimming. Cutting to 3,000 words would remove about 75% of the manuscript — the evidence tables, the cross-stage analysis, most of the reference list — and the review would no longer be the thing you wrote.

**So do not reformat for JHS yet.** Ask first (Step 1). If they hold to 3,000 words, the JHS route is closed for this manuscript and you should put the effort into a venue whose limits match its size. The Zenodo deposit (Steps 2–3) is worth doing either way.

---

## What is already done

Everything that can be prepared without your personal details is finished and committed:

| Item | Status |
| --- | --- |
| Manuscript, 9 sections, 11 figures/tables, 58 references, all cited | ✅ |
| Abstract trimmed to **250 words** (JHS limit) | ✅ |
| Table 3 built — it was cited in the text but had never been constructed | ✅ |
| Duplicate tables removed (one in §2, one in §7) | ✅ |
| All 5 figures now cited in the body — previously only Figure 2 was | ✅ |
| Blinded Word file with figures and tables placed inline | ✅ `deposit/JHS-submission.docx` |
| Deposit PDF for Zenodo, author apparatus stripped | ✅ `deposit/REVIEW-deposit.pdf` |
| Declaration block: CRediT, competing interests, funding, data availability, AI | ✅ in the manuscript |
| Molla et al. (2019) completed from the publisher's record | ✅ |

---

## Step 1 — Email the JHS editor (do this first)

Send this **before** formatting anything. It costs one email and decides whether Steps 5–6 are worth doing.

> **To:** the Editor-in-Chief, *Journal of Horticultural Sciences* — use the contact address on the journal's own site (jhs.iihr.res.in), or the editorial team page. Do not use an address you have not verified.
>
> **Subject:** Pre-submission enquiry — word limit for review articles
>
> Dear Editor,
>
> I am preparing a critical review on drought-tolerance screening in *Capsicum* and the Solanaceae for submission to the *Journal of Horticultural Sciences*, and I would be grateful for guidance on one point before I prepare the manuscript.
>
> The Author Guidelines state a maximum of 3,000 words for full-length papers. The manuscript I have prepared is a review of approximately 11,900 words, with 5 figures, 11 tables and 58 references. It synthesises the osmotic screening literature, the evidence on whether early-stage rankings transfer to field performance, and the low-cost genotyping options available to laboratories with limited infrastructure.
>
> Could you tell me whether review articles are subject to the same 3,000-word limit, or whether a different limit applies? If reviews are capped at 3,000 words, I would be glad to know whether the journal would consider a substantially shortened version, or whether you would advise me to submit elsewhere.
>
> I should also disclose that a preprint of this manuscript will be deposited on Zenodo, which your prior-publication policy permits. I am happy to provide the full manuscript if that would help.
>
> Thank you for your time.
>
> Yours sincerely,
> [YOUR NAME]
> [Affiliation]
> [ORCID]

**Three possible replies, and what each means:**

| Reply | Then do |
| --- | --- |
| Reviews are exempt, or a longer limit applies | Proceed to Step 5 |
| Reviews are capped at 3,000, but a shortened version is welcome | Decide whether a 3,000-word version is worth writing — realistically it is a different, shorter paper |
| Reviews are capped at 3,000, no exception | Keep the Zenodo deposit, and target a venue with a 12,000-word limit instead |

---

## Step 2 — Fill in your details

Four placeholders exist and all four must be replaced before anything is uploaded. They are in `REVIEW-final.md`:

| Placeholder | Where | What to put |
| --- | --- | --- |
| `[AUTHOR NAME]` | Declarations, CRediT statement | Your full name as you publish |
| `[Department, Institution, City, India]` | Cover page of the deposit PDF | Your institutional address |
| `[corresponding.author@email]` | JHS Word file only | Your email |
| `[TOOL NAME, VERSION, PROVIDER]` | Declarations, AI disclosure | The generative AI tool used, e.g. "Claude (Sonnet 4.5, Anthropic)" |

You also need an **ORCID iD** — free at orcid.org, takes two minutes, and JHS and Zenodo both use it.

Then rebuild both files:

```bash
cd projects/chilli-osmotic-stress

# Zenodo deposit PDF (named, not blinded)
python3 make-deposit.py \
    --author "Your Name" \
    --orcid "0000-0002-1825-0097" \
    --affiliation "Department, Institution, City, India"

# JHS submission file (blinded, figures and tables inline)
python3 make-jhs-docx.py
```

**Do not upload `REVIEW-final.md` to either destination.** It contains the author notes, the word-count audit and the venue note — internal working documents.

---

## Step 3 — Deposit to Zenodo

Zenodo is free, and JHS explicitly permits preprints, so nothing about this prejudges Step 1.

1. Sign in at **zenodo.org** with your ORCID.
2. **New upload.** Upload type: `Publication` → `Preprint`.
3. Upload these files:
   - `deposit/REVIEW-deposit.pdf` — the manuscript
   - `supplementary-table-S1.md` — Supplementary Tables S1–S2
   - the five PNGs from `figures/` — optional, but lets readers reuse them
4. Paste the metadata from **`zenodo-deposit.md`** — title, creators with ORCID, description, keywords, licence, version.
5. Set **licence** to CC BY 4.0 (or CC BY-NC-SA 4.0 if you prefer to match JHS).
6. Set **version** to `v1.0 — preprint, not peer reviewed`.
7. Click **Publish**. Zenodo mints the DOI immediately.

**Two things to remember:**

- The AI disclosure in the description is **required**. JHS also requires it in the manuscript. A disclosed AI-assisted review is permitted; an undisclosed one is a policy violation.
- If you later get the paper published, return to the record and **publish a new version** with the journal DOI added as a related identifier. Never upload a new record — version the existing one so the concept DOI stays stable.

---

## Step 4 — Note what a Zenodo DOI does and does not do

Depositing is worth doing, but be accurate about it:

| | |
| --- | --- |
| ✅ It gives you | A permanent DOI, an open-access landing page, CERN-backed preservation, ORCID linkage, immediate visibility, priority |
| ❌ It does not give you | Peer review, an editorial decision, journal indexing, or a "publication" in the sense most institutions mean |

If your institution counts peer-reviewed publications for appraisal or your degree, **the Zenodo deposit will not count** — but it will also not prevent the journal publication that does. Do both.

---

## Step 5 — Prepare the JHS submission (only if Step 1 clears the word limit)

The Word file is already built to their guidelines. What remains:

**5a. Trim to the limit if required.** If they allow, say, 6,000 words, the cut comes from tables and §5, not from the argument. Tell me the number and I will do it.

**5b. Convert references to strict APA.** Their example format is `Shikhamany, S.D. & Satyanarayana, G. (1973).` The current list uses `and` before the final author and `&` is standard APA. This is a mechanical change I can make in one pass.

**5c. Add a cover letter.** Required, and it must state that the manuscript is on a preprint server:

> Dear Editor,
>
> Please find enclosed our review article, "Screening for drought tolerance in *Capsicum* and the Solanaceae: methodological assumptions, an unresolved predictive link, and a cost-tiered path to markers", for consideration in the *Journal of Horticultural Sciences*.
>
> The review addresses a question of direct practical relevance to horticultural researchers: whether the polyethylene glycol screening that has become standard for identifying drought-tolerant *Capsicum* genotypes actually predicts performance in the field. It finds that the evidence divides four studies to four, that the disagreement tracks identifiable design choices rather than biology, and that the question is untested in *Capsicum* itself despite being the crop of most interest to Indian breeding programmes. It proposes a four-stage framework and a fifteen-item minimum reporting standard, six items of which require no additional experiment. The single substantive recommendation — reporting the proportion of screen-selected genotypes that prove superior in the field — would resolve the central question using data that screening programmes already generate.
>
> The work is a literature synthesis and reports no new experimental data. It is original, is not under consideration elsewhere, and all authors have approved the submission. **A preprint has been deposited on Zenodo [DOI], which the journal's prior-publication policy permits.** No competing interests are declared. Generative AI was used as disclosed in the manuscript.
>
> Suggested reviewers, with no conflict of interest:
> - [Name, institution, email — a *Capsicum* breeder]
> - [Name, institution, email — a seed physiologist working on germination statistics]
> - [Name, institution, email — a Solanaceae drought physiologist]
>
> Yours sincerely,
> [YOUR NAME]

**5d. Suggest reviewers honestly.** Two or three names, experts in the field, with a genuine reason for each. Do not suggest co-authors, collaborators or anyone at your own institution.

**5e. Submit through their OJS site.** Register at jhs.iihr.res.in, start a new submission, upload `JHS-submission.docx`, paste the cover letter, and answer the preprint question truthfully.

---

## Step 6 — If JHS does not work out

The manuscript is 11,932 words and unfixed to any publisher. Venues that take reviews of this length and charge nothing to publish:

- **ResearchGate/AgriRxiv** — preprint servers, not indexed as journals, but free and immediate. AgriRxiv is the agriculture-specific one.
- **Subscription-model plant journals** — free to publish, free to read under green open access after a 6–12 month embargo. This is the route that reaches the largest audience at no cost.
- **Diamond open-access journals with review sections** — verify any candidate directly in DOAJ and Scopus before submitting. The no-APC listicles circulating online mislabel hybrid journals as open access; two of the ones I checked described *New Phytologist* and *Molecular Plant Pathology* as free open access, which they are not.

Ask me and I will check a specific shortlist against the current guidelines and word limits.

---

## Order of operations, at a glance

```
1. Email the JHS editor about the 3,000-word limit     ← do this today
2. Fill in the four placeholders and your ORCID
3. Deposit to Zenodo                                    ← free, safe, reversible
4. Await the editor's reply
   ├── Limit is workable  → 5. Format, write the cover letter, submit to JHS
   └── Limit is firm      → 6. Retarget, keeping the Zenodo deposit
```

Step 3 does not depend on Step 1, and Step 1 does not depend on Step 2. Do both now.
