# Reporting Checklists — Hard Gates Before Submission

These are the checks that cause desk rejection or post-review rejection independently of scientific quality. Treat each as a gate, not a suggestion.

Companion files: `SKILL.md`, `manuscript-scaffold.md`, `figure-table-plan.md`.

---

## 0. Venue-Match Gate (run before the others)

**The single most avoidable rejection in the field is a venue/evidence mismatch.** A well-executed L1 study submitted to The Plant Cell is rejected for evidence, not writing; the same study at BMC Plant Biology is competitive. Complete this before working through the checklists below.

| Required level for your venue (SKILL.md §8) | Your current strongest level | Match? |
| --- | --- | --- |
| [ ] | [ ] | [ ] yes — proceed · [ ] no — add evidence or move tier |

- [ ] Venue family identified and its current Guide for Authors checked on [date]
- [ ] Evidence audit scored **after** the most recent experiment
- [ ] If planning-stage: reverse-engineering completed (`figure-table-plan.md` §0)
- [ ] If levels moved since the last audit, the abstract's causal verbs were revised
- [ ] Re-check scheduled for just before submission

**Only apply the checklists below that match your actual work.** No qPCR → skip §1. No field trial or phenotyping experiment → skip §2. Nothing deposited in a repository → §6 is a problem, not a formality.

---

## 1. qPCR / RT-qPCR — MIQE

Required. Reference gene validation is the item most often missing and most often caught.

**Assay design**
- [ ] Primer sequences and amplicon length reported (supplementary table is fine)
- [ ] Primer efficiency determined from a standard curve; report efficiency (%) and *R*²
- [ ] Specificity confirmed (melting curve, or gel, or sequencing)
- [ ] Probe/primer chemistry and supplier stated

**Reference genes — the critical block**
- [ ] ≥2 reference genes, ideally 3, used for normalisation
- [ ] Candidates validated for **stability in your specific tissue and treatment**
- [ ] Stability analysis performed (geNorm, NormFinder, BestKeeper, or equivalent)
- [ ] The normalisation strategy described explicitly

> A single, unvalidated reference gene (commonly *ACTIN* or *UBQ*) under a stress treatment is a standard reviewer target: those genes are themselves stress-responsive. Normalising to them can invert your result.

**Reaction and analysis**
- [ ] RNA extraction method, DNase treatment, RNA integrity measure (RIN or equivalent)
- [ ] Reverse transcription: kit, priming strategy, input amount
- [ ] Cycling conditions, platform, and detection chemistry
- [ ] Technical replicates per sample stated (and distinguished from biological replicates)
- [ ] Biological replicate number and what constitutes a replicate
- [ ] Relative quantification method stated (ΔΔCq or standard curve)
- [ ] Statistical treatment of Cq data described — tests applied to Cq or to fold-change, and whether log-transformed

**Reporting**
- [ ] MIQE compliance declared in Materials and Methods or supplementary
- [ ] Raw Cq values deposited as supplementary

---

## 2. Plant Phenotyping and Field Trials — MIAPPE

Required for phenotyping and field experiments. Also the basis of the metadata that makes your dataset reusable.

**Experiment-level**
- [ ] Investigation, study, and experiment identifiers
- [ ] Contact and institution
- [ ] Title and description of the experiment
- [ ] Licence and data availability statement
- [ ] Associated publications

**Environment**
- [ ] Site: name, country, latitude, longitude, altitude
- [ ] Environment type (field, greenhouse, growth chamber, screen house)
- [ ] Soil: classification, texture, pH, organic matter, nutrient status
- [ ] Weather/climate data for the season: source, variables, temporal resolution
- [ ] Water regime: rainfall, irrigation method and amounts
- [ ] Fertilisation: type, rate, timing, method

**Experimental design**
- [ ] Design type (randomised complete block, split-plot, lattice, etc.)
- [ ] Blocking structure and randomisation
- [ ] Number of replicates per treatment
- [ ] Plot dimensions, row spacing, plant density
- [ ] Sowing and harvest dates
- [ ] Site-years included

**Plant material**
- [ ] Species, genus
- [ ] Cultivar / accession / genotype identifier, with a persistent database reference
- [ ] Seed source and stock centre ID
- [ ] Biological status (wild, landrace, breeding line, mutant, transgenic)

**Observed variables**
- [ ] Trait name using a controlled vocabulary (Crop Ontology, Plant Ontology, TO)
- [ ] Units in a standard form
- [ ] Measurement method and instrument
- [ ] Timepoint or growth stage (use BBCH or Zadoks scales for cereals)
- [ ] Number of observations

> Mapping traits to **Crop Ontology / Plant Ontology terms** takes an hour and materially increases both discoverability and reviewer confidence. Do it.

---

## 3. Sequencing and Omics

**MINSEQE / general**
- [ ] Raw reads deposited in SRA/ENA/GEO with accession in the manuscript
- [ ] Processed data (count matrices, VCFs) deposited with a DOI
- [ ] Reference genome assembly **and version** stated (e.g. TAIR10, IRGSP-1.0, B73 RefGen_v5)
- [ ] Annotation version stated
- [ ] Library preparation kit, insert size, read length, strandedness
- [ ] Sequencing depth per sample
- [ ] Number of biological replicates per condition — **≥3 for differential expression**

**RNA-seq analysis**
- [ ] Alignment tool and version; or quantification tool (Salmon, kallisto) and version
- [ ] Filtering thresholds stated *a priori*
- [ ] Differential expression model (DESeq2, edgeR, limma-voom) and version
- [ ] Multiple-testing correction stated (Benjamini–Hochberg)
- [ ] Significance thresholds justified, not tuned
- [ ] Sensitivity analysis across thresholds reported, or at least the effect of threshold choice discussed
- [ ] Functional enrichment method and background/universe set stated — **the background choice changes the result and is frequently unjustified**

**GWAS / QTL**
- [ ] Population size, structure correction method (PCA, kinship, mixed model)
- [ ] Significance threshold and how it was derived
- [ ] Multiple-testing approach
- [ ] Effect sizes and allele frequencies for reported loci
- [ ] Confidence intervals for QTL, not just peak positions
- [ ] **Independent validation** of reported loci (this is what separates a discovery from a lead)

**If you report a candidate gene from a QTL/GWAS interval**
- [ ] Expression or functional evidence distinguishing it from other genes in the interval
- [ ] Statement acknowledging that interval-wide linkage makes candidate assignment provisional

---

## 4. Protein Work

- [ ] Antibodies: supplier, catalogue number, RRID, lot if relevant, dilution, validation data
- [ ] Primary data for antibody specificity (knockout lane, peptide competition, or vendor validation cited)
- [ ] Protein extraction buffer and method
- [ ] Gel percentage, loading amount, transfer method, membrane
- [ ] Imaging system and exposure; whether signal is within linear range
- [ ] Quantification across ≥3 biological replicates with statistical test
- [ ] Uncropped blots in supplementary
- [ ] For interaction assays (Y2H, BiFC, Co-IP, split-luc): bait/prey orientation, negative controls, and expression verification
- [ ] For BiFC: note the known artefact risk; support with an orthogonal assay
- [ ] For Co-IP: lysis stringency and whether interaction is direct or indirect

---

## 5. Statistics — Universal Gate

- [ ] Experimental unit correctly identified (plant, plot, field, batch) — **pseudo-replication is the most common fatal statistical error in plant biology**
- [ ] n reported, and it is the number of independent experimental units
- [ ] Model specification given, including fixed and random effects
- [ ] Assumptions checked (normality, homoscedasticity) and the response variable transformed if required
- [ ] Multiple-comparison correction stated and applied
- [ ] Effect sizes reported with confidence intervals, not just P values
- [ ] Exact P values given where possible
- [ ] Outlier policy defined *a priori*; any excluded data point disclosed with justification
- [ ] Software **and version** stated for every analysis
- [ ] Randomisation described for any experiment with treatment allocation
- [ ] Blinding described where measurement is subjective (lesion scoring, disease rating, phenotyping by eye)
- [ ] Power analysis or a statement of detectable effect size, for trials reporting null results

---

## 6. Data and Code Availability

- [ ] Sequencing accessions live and public (or embargoed with a stated release date)
- [ ] Proteomics in PRIDE; metabolomics in MetaboLights
- [ ] Processed data deposited with DOI
- [ ] Analysis code deposited with DOI and a licence
- [ ] Mutant lines and plasmids deposited in a stock centre or available on request with a stated mechanism
- [ ] Plant material available under terms that comply with the Convention on Biological Diversity / Nagoya Protocol and any national access legislation
- [ ] Data availability statement names the repository, not "available on request"

> "Data available on request from the authors" is treated as no data availability by a growing number of journals and reviewers.

---

## 7. Ethics, Permits, and Biosafety

- [ ] Field trial permissions and biosafety approvals obtained and cited
- [ ] Genetically modified material handled per national regulation; the regulatory status of field experiments stated
- [ ] Collection permits for wild material, and Nagoya Protocol compliance for genetic resources
- [ ] Access and benefit-sharing statement where the material originates from a country with ABS legislation
- [ ] Import/export permits for plant material where relevant
- [ ] No identifiable human subjects in field photographs (or consent obtained)

---

## 8. Integrity

- [ ] No fabricated data, images, or results
- [ ] No duplicated, mirrored, rotated, or recombined panels — check supplementary figures too
- [ ] No selective contrast/brightness adjustment of a region within an image
- [ ] All splicing in blots/gels clearly demarcated
- [ ] No "data not shown"; no "unpublished results" as support for a claim
- [ ] All citations verified against a database — none from memory
- [ ] No text recycled from the authors' own prior publications without clear citation (self-plagiarism)
- [ ] LLM assistance disclosed per venue policy
- [ ] Authorship list meets ICMJE criteria; no gift or ghost authorship
- [ ] Any competing interest declared
- [ ] Preprint (if any) disclosed and linked

---

## 9. The Three Questions Every Reviewer Will Ask

Answer these explicitly somewhere in the manuscript. If you cannot, the paper is not ready.

1. **"How do you know it is not the other gene / the other explanation?"**
   → Specificity evidence (L3) and an alternatives paragraph in the Discussion.

2. **"Does this work outside your one controlled condition?"**
   → Independently derived alleles, multiple environments, other species, or an explicit limitations statement about generalizability.

3. **"Would this still be true if someone repeated it?"**
   → Reproducibility block: n, model, version, accession numbers, deposited data, stock IDs.

All three are answerable. Reviewed papers that fail are almost never wrong — they are under-documented.
