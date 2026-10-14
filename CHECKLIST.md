# Rewrite Checklist

The paper was drafted with heavy AI assistance. **Goal: every unit below is rewritten in our own words by one of us, then read by a second person.** One unit = one file in [`sections/`](sections/) = one sitting (~10-25 min).

**Progress: 0 / 49 units rewritten, 0 / 49 reviewed** (update this line when you tick boxes)

## How to take a unit

1. Pick an unticked unit, write your name in `Owner:` and **commit + push that one-line change first** (so nobody else grabs it).
2. Open the unit's `.tex` file. The AI text is still in it - read it, close your eyes on it, then rewrite it in your own voice. Change `% Status: AI-DRAFT` to `% Status: REWRITTEN`.
3. Tick **Rewritten**, commit and push. One unit = one commit = one file, so merges never conflict.
4. A *different* person then reads it, fixes it, changes the status line to `REVIEWED` and ticks **Reviewed**.

## Rules

- **Edit only your unit file.** Never edit `main.tex` (it only `\input`s the units) or someone else's file. This is what makes auto-merging safe.
- **Do not change numbers, table values, citations (`\cite{...}`), `\ref`/`\label` keys or equations** unless you checked them against our logs/notebooks. Rewrite the *wording*, not the results. If a number looks wrong, write it under "Notes" below instead of silently changing it.
- **Check every claim against what we actually did.** If a sentence says something we did not run or do not understand, cut it or ask.
- Plain, direct sentences. Shorter is fine. If you would not say it out loud in a viva, rewrite it.
- Keep the full original in [`original/main_ai_draft.tex`](original/main_ai_draft.tex) for reference; do not copy-paste from it.
- Compile before pushing (Overleaf import or `pdflatex main && pdflatex main`).

Time estimates are rough (based on prose word count; tables/figures add checking time). ~words = prose only.


## Front matter

- **01** [Abstract](sections/01_abstract.tex) - ~190 words, ~15 min *Do this LAST (after the rest) so it matches. Journal limit: 150-250 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@seifheakal`  - Reviewer: `@____`

## 1 Introduction

- **02** [Motivation + paper organisation (1.1, 1.4)](sections/02_intro_motivation.tex) - ~159 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **03** [The ViT-B training recipe gap (1.2)](sections/03_intro_gap.tex) - ~169 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **04** [Contributions (1.3)](sections/04_intro_contrib.tex) - ~347 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 2 Related work

- **05** [CNN-era vehicle re-ID (2.1)](sections/05_rel_cnn.tex) - ~187 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **06** [Transformer-based vehicle re-ID (2.2)](sections/06_rel_transformer.tex) - ~307 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **07** [Cross-domain transfer and dataset bias (2.3)](sections/07_rel_crossdomain.tex) - ~121 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **08** [Re-ranking and post-processing (2.4)](sections/08_rel_rerank.tex) - ~214 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **09** [Positioning (2.5)](sections/09_rel_position.tex) - ~84 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 3 Methodology

- **10** [Overview figure + problem formulation (3.1)](sections/10_m_overview.tex) - ~95 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **11** [Stream 1: backbone architecture (3.2.1)](sections/11_m_backbone.tex) - ~104 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **12** [Stream 1: loss function + equations (3.2.2)](sections/12_m_loss.tex) - ~285 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **13** [Stream 1: augmentation + hyper-parameters (3.2.3-3.2.4)](sections/13_m_aug_hparams.tex) - ~133 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **14** [Stream 2: CLIP-SENet branch (3.3)](sections/14_m_stream2.tex) - ~186 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **15** [Post-processing: AQE, k-reciprocal, TTA (3.4)](sections/15_m_postproc.tex) - ~143 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **16** [Score-level fusion: definition + figure (3.5 part 1)](sections/16_m_fusion_def.tex) - ~136 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **17** [Score-level fusion: why score- not feature-level (3.5 part 2)](sections/17_m_fusion_why.tex) - ~192 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 4 Experimental setup

- **18** [Dataset, protocol, implementation details (4.1-4.3)](sections/18_s_setup.tex) - ~110 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **19** [Reproducibility (4.4)](sections/19_s_repro.tex) - ~309 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 5 Results

- **20** [Comparison with the state of the art (5.1)](sections/20_r_sota.tex) - ~115 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **21** [Pure ViT-B comparison (5.2)](sections/21_r_pure.tex) - ~103 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **22** [Matched-condition vs TransReID / CLIP-ReID (5.3)](sections/22_r_matched.tex) - ~260 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **23** [Ablation study (5.4)](sections/23_r_ablation.tex) - ~261 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **24** [Seed variance + fusion-weight sensitivity (5.5-5.6)](sections/24_r_seed_fusionw.tex) - ~278 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **25** [Hyper-parameter selection and selection bias (5.7 part 1)](sections/25_r_hp_selection.tex) - ~156 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **26** [Held-out validation (5.7 part 2)](sections/26_r_hp_heldout.tex) - ~236 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **27** [Post-proc plateau, calibration, bootstrap significance (5.7 part 3)](sections/27_r_hp_signif.tex) - ~203 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **28** [Post-processing contribution + input resolution (5.8-5.9)](sections/28_r_pp_resolution.tex) - ~172 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **29** [VeRi-Wild: setup, table, figure (5.10 part 1)](sections/29_r_vw_setup.tex) - ~155 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **30** [VeRi-Wild: observations 1-2, fusion does not transfer (5.10 part 2)](sections/30_r_vw_obs12.tex) - ~218 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **31** [VeRi-Wild: AQE, training-free fix (5.10 part 3)](sections/31_r_vw_obs34.tex) - ~306 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **32** [VeRi-Wild: literature context + reframing (5.10 part 4)](sections/32_r_vw_context.tex) - ~180 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **33** [Qualitative analysis (5.11)](sections/33_r_qualitative.tex) - ~87 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 6 Discussion

- **34** [What drives the ViT-B gain (6.1)](sections/34_d_gain.tex) - ~176 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **35** [Why fusion works + backbone scale (6.2-6.3)](sections/35_d_fusion_scale.tex) - ~170 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **36** [Cost: model and feature extraction (6.4 part 1)](sections/36_d_cost_model.tex) - ~158 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **37** [Cost: post-processing + domain transfer (6.4 part 2)](sections/37_d_cost_pp.tex) - ~259 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **38** [Cost: scalable sparse implementation + figure (6.4 part 3)](sections/38_d_cost_sparse.tex) - ~123 words, ~10 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **39** [Cost: accuracy/latency trade-offs, CA-Jaccard (6.4 part 4)](sections/39_d_cost_tradeoff.tex) - ~250 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **40** [Limitations (6.5)](sections/40_d_limitations.tex) - ~321 words, ~20 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## 7 Conclusion

- **41** [Conclusion](sections/41_conclusion.tex) - ~246 words, ~15 min  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## Back matter

- **42** [Statements and declarations](sections/42_statements.tex) - ~263 words, ~20 min *Facts only. Update "Author contributions" and "Use of large language models" so they are true after the rewrite.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **43** [References - verify entries 1-19 (do NOT rewrite)](sections/43_refs_a.tex) - ~386 words, ~25 min *Check authors/years/venues/page numbers against the real papers; fix typos only.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **44** [References - verify entries 20-37 (do NOT rewrite)](sections/44_refs_b.tex) - ~377 words, ~25 min *Check authors/years/venues/page numbers against the real papers; fix typos only.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## Biographies

- **45** [Bio: Seif T. Heakal (his own)](sections/45_bio_seif.tex) - ~63 words, ~10 min *Only this author writes this. 50-100 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **46** [Bio: Mohamed A. Ali (his own)](sections/46_bio_maali.tex) - ~58 words, ~10 min *Only this author writes this. 50-100 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **47** [Bio: Ali A. Ali (his own)](sections/47_bio_aali.tex) - ~61 words, ~10 min *Only this author writes this. 50-100 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **48** [Bio: Abdelrahman Hamdi (his own)](sections/48_bio_hamdi.tex) - ~64 words, ~10 min *Only this author writes this. 50-100 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`
- **49** [Bio: Ahmed H. Abdel-Gawad (supervisor, his own)](sections/49_bio_ahmed.tex) - ~51 words, ~10 min *Only this author writes this. 50-100 words.*  
  - [ ] Rewritten  - [ ] Reviewed  - Owner: `@____`  - Reviewer: `@____`

## Final pass (after all units are Reviewed)

- [ ] Whole paper read start-to-end by one person for flow and repeated phrases
- [ ] Every number in abstract / intro / conclusion matches the results tables
- [ ] Statement on LLM use updated to match what was actually done
- [ ] Compiles clean, no undefined refs/citations, abstract 150-250 words
- [ ] Author names, emails, ORCIDs, photos filled in

## Notes / suspicious numbers found while rewriting

- (add as `- unit NN: ...`)
