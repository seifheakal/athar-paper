# Review notes exported from main_review_highlighted.pdf

Page numbers are PDF pages of main_review_highlighted.pdf (page 1 is the added summary page; paper page N = PDF page N+1).
Notes repeated on consecutive lines of one phrase are merged.

## 1. PDF page 2 | YELLOW AI-style/AI-draft
- Highlighted text: "Transformer backbones dominate vehicle re-identifica"
- PROBLEM: Abstract: about 77% of its 5-word sequences are copied from original/main_ai_draft.tex. This is the first thing a detector or reviewer reads.
- SUGGESTED FIX: Rewrite the abstract from scratch in your own words, after the body is final (150-250 words).

## 2. PDF page 2 | RED factual/inconsistency
- Highlighted text: "This paper revisits the ViT-Base/16 pipeline on VeRi-776 and separates recipe effects from post-processing effects. We use a specific recipe that we just build "
- PROBLEM: Broken sentence; it does not parse.
- SUGGESTED FIX: e.g. 'Our pipeline combines CLIP-pretrained initialisation, AdamW with layer-wise learning-rate decay, a tuned metric objective and a three-step post-processing chain (...)'.

## 3. PDF page 2 | YELLOW AI-style/AI-draft
- Highlighted text: "Vehicle re-identification is heavily used in intelligent t"
- PROBLEM: Unit 02 (Motivation): about 75% copied from the AI draft.
- SUGGESTED FIX: Rewrite in your own words; vary sentence length.

## 4. PDF page 2 | YELLOW AI-style/AI-draft
- Highlighted text: "changed how people approached"
- PROBLEM: Unit 03: about 70% copied from the AI draft.
- SUGGESTED FIX: Rewrite in your own words.

## 5. PDF page 2 | PURPLE reference-number check
- Highlighted text: "training images of 576"
- PROBLEM: Count check: TransReID (Table 1: 49,357 images) and CLIP-SENet ('training set with 576 identities and 37,778 images') use 37,778 training images; 37,778 + 11,579 = 49,357. 37,781 also appears in older descriptions.
- SUGGESTED FIX: Pick one count and use it consistently.

## 6. PDF page 3 | ORANGE unsupported claim
- Highlighted text: "No pure ViT-B method has been reported above 90%"
- PROBLEM: This framing ('we approach 90%') contradicts your own finding that TransReID and CLIP-ReID with your post-processing reach 91.12 / 91.80%.
- SUGGESTED FIX: Frame the gap as 'recipe vs post-processing effects are never separated', which is what the paper actually shows.

## 7. PDF page 3 | YELLOW AI-style/AI-draft
- Highlighted text: "The contributions of this work are as follows:"
- PROBLEM: Unit 04 (Contributions): about 75% copied from the AI draft.
- SUGGESTED FIX: Rewrite C1-C5 in your own words; keep the numbers.

## 8. PDF page 3 | ORANGE unsupported claim
- Highlighted text: "both slightly above ours,"
- PROBLEM: 1.15 and 1.83 pp are not 'slightly' above.
- SUGGESTED FIX: Say 'both above ours (by 1.15 and 1.83 pp)'.

## 9. PDF page 3 | YELLOW AI-style/AI-draft
- Highlighted text: "reuses that model’s checkpoint, we present it as a demonstration of feature complementarity, which a paired bootstrap test shows is significant over the best si"
- PROBLEM: The 'not peer reviewed' clause is fixed (CLIP-SENet is in IEEE T-ITS 2026). The rest of this sentence is still garbled: the 'which ...' clause sits between 'complementarity' and 'rather than'.
- SUGGESTED FIX: e.g. '...we present it as a demonstration of feature complementarity, not a decisive state of the art. A paired bootstrap test shows the gain over the best single stream is significant.' Also check that the T-ITS version still reports 92.9 / 98.7.

## 10. PDF page 3 | ORANGE unsupported claim
- Highlighted text: "supported by a CityFlowV2 MTMC port,"
- PROBLEM: CityFlowV2 is used as evidence here (and in 5.10 and 6.5) but is never described anywhere: no setup, no numbers, no table.
- SUGGESTED FIX: Either remove the CityFlowV2 claims, or add a short paragraph with the setup and IDF1 results.

## 11. PDF page 3 | PURPLE reference-number check
- Highlighted text: "(92.1% mAP"
- PROBLEM: Same as 92.09 elsewhere: the value is from the authors' GitHub README (with re-ranking), not from the ITSC paper (85.63 there).
- SUGGESTED FIX: Add the GitHub repository as a source.

## 12. PDF page 3 | PURPLE reference-number check
- Highlighted text: "No pure ViT-B method has been reported above 90%"
- PROBLEM: Literature check: CLIP-SENet (IEEE T-ITS 2026, arXiv 2502.16815), Table I lists 'CLIP-ReID [11]* AAAI 2023' at 91.7 mAP / 98.0 R1 on VeRi-776 (* = transformer; that paper uses re-ranking on VeRi-776). So a peer-reviewed paper already reports a pure ViT-B result above 90%.
- SUGGESTED FIX: Soften to 'no ViT-B paper reports above 90% in its own results', or mention CLIP-SENet's 91.7 for CLIP-ReID.

## 13. PDF page 4 | GREEN fixed/check-only
- Highlighted text: "They cover parts, multiple data sources"
- PROBLEM: Reference fixed to Yi et al. (Neurocomputing 2025). The content of this sentence was not checked against that survey.
- SUGGESTED FIX: Confirm the survey really covers parts, multi-source data and cross-domain adaptation.

## 14. PDF page 4 | YELLOW AI-style/AI-draft
- Highlighted text: "TransReID [1] (ICCV 2021) was the first pure Vision Transformer framework for object re-identification. It introduced the SIE and JPM modules. It gets 82.3% mAP"
- PROBLEM: Units 05-41 were 'rewritten' mainly by splitting sentences: average length dropped from 26 to 14 words, with very uniform short sentences. 'So ...' starts 34 sentences and 'This is ...' 28. That uniform rhythm is itself a recognisable machine pattern.
- SUGGESTED FIX: When rewriting, merge some short sentences, vary the length, and drop most 'So ...' / 'This confirms ...' openers.

## 15. PDF page 4 | PURPLE reference-number check
- Highlighted text: "92.09%"
- PROBLEM: Source note (the number itself is fine): 92.09 / 98.03 is reported in the authors' GitHub README (github.com/videturfortuna/vehicle_reid_itsc2023, 'teste.py ... --re_rank', 'With re-ranking: mAP= 92.09, CMC1= 98.03'). The cited ITSC paper (arXiv 2310.01129, Table IV) reports MBR-4B-LAI at 85.63 / 97.74 without re-ranking. CLIP-SENet's T-ITS Table I lists MBR at 91.9 / 98.2.
- SUGGESTED FIX: Keep 92.09, and cite the GitHub repository next to the paper (e.g. 'with re-ranking, from the authors' released code').

## 16. PDF page 4 | PURPLE reference-number check
- Highlighted text: "location-aware identity embeddings"
- PROBLEM: Description check: MBR4B paper (arXiv 2310.01129), Section III-C is titled 'Leveraging Additional Information (LAI)' and uses camera ID and viewpoint metadata. It does not describe 'location-aware identity embeddings'.
- SUGGESTED FIX: '... with LAI (Leveraging Additional Information), which adds camera and viewpoint metadata'.

## 17. PDF page 4 | PURPLE reference-number check
- Highlighted text: "s ResNet101-IBN-a local appearance"
- PROBLEM: Backbone check: CLIP-SENet T-ITS version (arXiv 2502.16815), 'Training details': 'we employ a ResNext101 with IBN structure as our CNN Backbone'. Its Table VI: ResNet101-IBN gives 91.9 / 98.2, ResNeXt101-IBN gives the headline 92.9 / 98.7. (Fine if your own v6 checkpoint is ResNet101-IBN-a, but the cited 92.9 is the ResNeXt101 model.)
- SUGGESTED FIX: Describe the published model as ResNeXt101-IBN, and say your Stream 2 uses ResNet101-IBN-a if that is the case.

## 18. PDF page 4 | PURPLE reference-number check
- Highlighted text: "Trains on VeRi-776, VehicleID and synthetic data together"
- PROBLEM: Description check: VehicleNet paper (arXiv 2004.06305), Sec. III-A: 'We involve four public datasets, i.e., CityFlow, VeRi-776, CompCar and VehicleID ... 434,440 training images of 31,805 classes'. No synthetic data.
- SUGGESTED FIX: 'Trains on CityFlow, VeRi-776, CompCars and VehicleID together'.

## 19. PDF page 4 | PURPLE reference-number check
- Highlighted text: "ResNet101-IBN-a with multi-head attention, trained on several domain"
- PROBLEM: Description check: Strong Baseline paper (arXiv 2104.10850), Sec. 3: MixStyle in a 'ResNeXt101 ibn a' backbone plus multi-head attention; the final model ensembles ResNet50-ibn-a, ResNeXt101-ibn-a and ResNet152. Its Table 5 also gives Rank-1 = 97.0 (Table 1 shows '--'). RPTM's Table 2 marks this result as re-ranked.
- SUGGESTED FIX: 'ResNeXt101-IBN-a ensemble with MixStyle and multi-head attention'; R1 97.0.

## 20. PDF page 4 | PURPLE reference-number check
- Highlighted text: "1The PROVID (53.42/81.56) and VAMI (50.13/77.03) figures are the values reported in the respective papers and reproduced throughout the survey literature [11, 1"
- PROBLEM: Citation check: Ye et al. (arXiv 2001.04193) is a person re-ID survey only (abstract) and would not list PROVID / VAMI vehicle results.
- SUGGESTED FIX: Cite only the vehicle survey (Yi et al.) here.

## 21. PDF page 4 | PURPLE reference-number check
- Highlighted text: "was the first pure Vision Transformer framework"
- PROBLEM: Claim check: the TransReID paper says it proposes 'a pure transformer-based object ReID framework'; it does not claim to be the first.
- SUGGESTED FIX: Drop 'first', or attribute it carefully.

## 22. PDF page 4 | PURPLE reference-number check
- Highlighted text: "84.5% mAP and 97.3% Rank-1 on VeRi-776"
- PROBLEM: Citation check: correct value, but it is cited to the OpenCodePapers mirror. The CLIP-ReID paper (arXiv 2211.13977), Table 3, row 'CLIP-ReID' (ViT), gives 84.5 / 97.3 directly.
- SUGGESTED FIX: Cite the CLIP-ReID paper [8].

## 23. PDF page 5 | ORANGE unsupported claim
- Highlighted text: "Supervised Contrastive Learning (SupCon) ["
- PROBLEM: A paragraph about a training loss sits inside the 'Re-ranking and post-processing' section.
- SUGGESTED FIX: Move it to the methodology (loss function) or a short 'metric learning' paragraph.

## 24. PDF page 5 | ORANGE unsupported claim
- Highlighted text: "statistically equivalent."
- PROBLEM: A gap smaller than one seed SD is not a statistical equivalence test.
- SUGGESTED FIX: Say 'the gap is within training noise, so we treat the two as equivalent'.

## 25. PDF page 5 | RED factual/inconsistency
- Highlighted text: "AQE costs almost nothing."
- PROBLEM: Contradicts Section 6.4, where the CPU AQE pass takes 138 s, longer than re-ranking (50 s).
- SUGGESTED FIX: Say 'GPU AQE is cheap', or explain the CPU timing in 6.4.

## 26. PDF page 5 | PURPLE reference-number check
- Highlighted text: ", no prior work reports above 90% m"
- PROBLEM: Same point: CLIP-SENet's Table I reports CLIP-ReID (ViT) at 91.7 / 98.0 on VeRi-776.
- SUGGESTED FIX: Rephrase as above.

## 27. PDF page 5 | PURPLE reference-number check
- Highlighted text: "of the same class in a mini-batch count as positives. This gives embedding spaces that are more uniform and more discriminative than triplet loss alone [11]. We"
- PROBLEM: Citation check: this is cited to Ye et al. (TPAMI). That survey was first posted on 13 Jan 2020 (arXiv 2001.04193); SupCon appeared in Apr 2020, so the survey cannot support a claim about SupCon.
- SUGGESTED FIX: Cite Khosla et al. alone, or drop the claim.

## 28. PDF page 6 | RED factual/inconsistency
- Highlighted text: "The deployed headline checkpoint"
- PROBLEM: Four different Stream-1 numbers are all attached to 'A5alpha / deployed': 89.97 (headline, 1536D), 89.63 (released checkpoint, 768D), 89.06 (ablation row, actually a from-scratch run) and 89.99 (Sec. 5.7/6.4, typo for 89.97).
- SUGGESTED FIX: Label 89.06 as 'a from-scratch ablation run of the A5alpha recipe' and say the released checkpoint scores 89.63 at 768D.

## 29. PDF page 7 | ORANGE unsupported claim
- Highlighted text: "statistically equivalent."
- PROBLEM: A gap smaller than one seed SD is not a statistical equivalence test.
- SUGGESTED FIX: Say 'the gap is within training noise, so we treat the two as equivalent'.

## 30. PDF page 7 | ORANGE unsupported claim
- Highlighted text: "The exact P×"
- PROBLEM: The P x K tuple 'was not logged', but Section 5.5 retrains three seeds 'under identical hyperparameters'. Which P x K did those runs use?
- SUGGESTED FIX: State the P x K used for the seed retrains, or say the seed runs used 12x8.

## 31. PDF page 7 | RED factual/inconsistency
- Highlighted text: "(88.75 ± 0.55 p"
- PROBLEM: 0.55 is the population SD (divide by n). For n = 3 seeds the usual sample SD is 0.68 (Rank-1: 0.09, not 0.07). The +-0.55 band is repeated in Sections 1.3, 3.2, 4.4, 5.4 and 6.5.
- SUGGESTED FIX: Report the sample SD (0.68 / 0.09) everywhere, or state 'population SD'. The 0.49 pp argument still holds.

## 32. PDF page 7 | PURPLE reference-number check
- Highlighted text: "CLIP-SENet uses a ResNet101-IBN-a backbone"
- PROBLEM: Same backbone point: the CLIP-SENet paper's headline model uses ResNeXt101-IBN (ResNet101-IBN variant: 91.9 / 98.2, their Table VI).
- SUGGESTED FIX: Separate 'the published CLIP-SENet' from 'our v6 checkpoint'.

## 33. PDF page 8 | RED factual/inconsistency
- Highlighted text: "Post-processing is applied to each stream separately, before fusion."
- PROBLEM: Contradicts 3.5: in the fusion pipeline only AQE is per-stream; re-ranking is applied once to the fused matrix.
- SUGGESTED FIX: e.g. 'This section gives each stream's standalone settings. In the fusion pipeline, AQE is applied per stream and k-reciprocal re-ranking once, to the fused matrix.'

## 34. PDF page 8 | PURPLE reference-number check
- Highlighted text: "Epochs"
- PROBLEM: Value check: the TransReID paper does not state an epoch count (no 'epoch' in the text). 120 is presumably from TransReID's released config.
- SUGGESTED FIX: Cite the config, or mark as 'from the released code'.

## 35. PDF page 9 | ORANGE unsupported claim
- Highlighted text: "we found no sign that feature-level concatenation overfits"
- PROBLEM: Contradicts the first paragraph, which justifies score-level fusion by the risk of overfitting.
- SUGGESTED FIX: Drop the overfitting argument from the first paragraph and keep the 'explicit weights' reason.

## 36. PDF page 10 | PURPLE reference-number check
- Highlighted text: "categories), vehicle type, colour and spatiotemporal metadata [6]. The standard split has 37 781 training images of 576 identities, 11 579 gallery images of 200"
- PROBLEM: Count check: TransReID (Table 1: 49,357 images) and CLIP-SENet ('training set with 576 identities and 37,778 images') use 37,778 training images; 37,778 + 11,579 = 49,357. 37,781 also appears in older descriptions.
- SUGGESTED FIX: Pick one count and use it consistently.

## 37. PDF page 10 | PURPLE reference-number check
- Highlighted text: "covering a 1.0km2 area over 24 hours. Each vehicle is annotated with identity, camera index, viewpoint (8 categories), vehicle type, colour and spatiotemporal m"
- PROBLEM: Source check: the VeRi page (github.com/JDAI-CV/VeRidataset) lists 'BBoxes, types, colors, and brands'; viewpoint labels come from later annotation work, not PROVID.
- SUGGESTED FIX: Cite the source of the viewpoint labels, or drop '(8 categories)'.

## 38. PDF page 10 | YELLOW AI-style/AI-draft
- Highlighted text: "Every number in this paper comes from deterministic evaluation of two frozen, SHA-256-pinned checkpoints. We want to be clear about what this guarantees. Infere"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 39. PDF page 11 | PURPLE reference-number check
- Highlighted text: "RPTM"
- PROBLEM: Post-processing mark: Table 6 marks RPTM as without post-processing. RPTM paper (arXiv 2110.07933), Table 2 caption: 'The * indicates the usage of re-ranking', and the row 'RPTM (ResNet-101)*' gives 88.00 / 97.30. The text also says 82.5% mAP 'w/o re-ranking'.
- SUGGESTED FIX: Mark RPTM as with post-processing (or use its non-re-ranked number).

## 40. PDF page 11 | PURPLE reference-number check
- Highlighted text: "92.09"
- PROBLEM: Source note (the number itself is fine): 92.09 / 98.03 is reported in the authors' GitHub README (github.com/videturfortuna/vehicle_reid_itsc2023, 'teste.py ... --re_rank', 'With re-ranking: mAP= 92.09, CMC1= 98.03'). The cited ITSC paper (arXiv 2310.01129, Table IV) reports MBR-4B-LAI at 85.63 / 97.74 without re-ranking. CLIP-SENet's T-ITS Table I lists MBR at 91.9 / 98.2.
- SUGGESTED FIX: Keep 92.09, and cite the GitHub repository next to the paper (e.g. 'with re-ranking, from the authors' released code').

## 41. PDF page 11 | PURPLE reference-number check
- Highlighted text: "(92.1% mAP"
- PROBLEM: Same as 92.09 elsewhere: the value is from the authors' GitHub README (with re-ranking), not from the ITSC paper (85.63 there).
- SUGGESTED FIX: Add the GitHub repository as a source.

## 42. PDF page 11 | PURPLE reference-number check
- Highlighted text: "ResNet101-IBN-a + TinyCLIP"
- PROBLEM: Table 6 backbone for CLIP-SENet (92.90 / 98.70): the paper's 92.9 model uses ResNeXt101-IBN + TinyCLIP (ViT-B/32).
- SUGGESTED FIX: 'ResNeXt101-IBN-a + TinyCLIP'.

## 43. PDF page 11 | PURPLE reference-number check
- Highlighted text: "VehicleNet"
- PROBLEM: Post-processing mark: VehicleNet's paper describes query expansion and re-ranking for its AI City Challenge pipeline, not for the VeRi-776 result (83.41 / 96.78). RPTM's Table 2 does mark VehicleNet as re-ranked, so sources disagree.
- SUGGESTED FIX: Check the VehicleNet paper / code and set the mark accordingly.

## 44. PDF page 11 | YELLOW AI-style/AI-draft
- Highlighted text: "This confirms"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 45. PDF page 12 | RED factual/inconsistency
- Highlighted text: "point in one place. It includes a validation-selected fusion row (Section 5.7) as the recommended tuning-free default. The headline fusion also reaches 84.14% m"
- PROBLEM: Not tuning-free: its post-processing parameters are tuned on the test split; only the fusion weight comes from a validation split.
- SUGGESTED FIX: e.g. 'a fusion row whose weight is selected on a validation split, which we recommend as the default'.

## 46. PDF page 12 | RED factual/inconsistency
- Highlighted text: "(TransReID* ViT-B/16, released by the TransReID authors"
- PROBLEM: Labelled ViT-B/16 here, but Table 7 lists TransReID* as DeiT-B/16 (82.3) and plain ViT-B as 80.6. The 'matches its published number' check depends on which checkpoint this is.
- SUGGESTED FIX: Name the exact checkpoint (DeiT-B/16 stride-12?) and the published number it should match.

## 47. PDF page 12 | PURPLE reference-number check
- Highlighted text: "TransReID (ViT-B)"
- PROBLEM: Value check: Table 7 gives 80.60 / 97.00. TransReID paper (arXiv 2102.04378), Table 6, ViT-B/16 block, row 'TransReID b' (camera+view): 80.6 mAP / 96.9 R1. The 97.0 belongs to row 'TransReID v' (79.6 / 97.0).
- SUGGESTED FIX: Use 80.6 / 96.9, or name the variant you mean.

## 48. PDF page 13 | ORANGE unsupported claim
- Highlighted text: "The same is probably true for much of the apparent progress after TransReID"
- PROBLEM: Generalises from two models (TransReID, CLIP-ReID) to 'much of the progress' on the benchmark.
- SUGGESTED FIX: Limit the claim to the two baselines you tested, or test more checkpoints.

## 49. PDF page 13 | PURPLE reference-number check
- Highlighted text: "so our extraction is faithful."
- PROBLEM: Value check: 82.3 is TransReID* with DeiT-B/16 (TransReID Table 6). The ViT-B/16* model is 82.0 / 97.1, which your 82.11 matches even more closely. Section 5.3 calls the checkpoint ViT-B/16, Table 7 calls TransReID* DeiT-B.
- SUGGESTED FIX: Confirm which official checkpoint was used and compare with its own published number.

## 50. PDF page 14 | RED factual/inconsistency
- Highlighted text: "centre, deployed)"
- PROBLEM: This row is a single from-scratch run (see footnote), not the released checkpoint, which scores 89.63 at this operating point.
- SUGGESTED FIX: Relabel 'deployed recipe, ablation run'.

## 51. PDF page 14 | BLUE presentation
- Highlighted text: "A1, un-tuned SGD control"
- PROBLEM: Blank table row after this line: the source uses '\\\\' (double row break).
- SUGGESTED FIX: Replace the double '\\\\' with a single '\\' (also after the TransReID-baseline and CLIP-SENet-base rows, and the two 'Ours' rows of Table 6).

## 52. PDF page 14 | BLUE presentation
- Highlighted text: "TransReID baseline (DeiT-B*)"
- PROBLEM: Blank table row after this line (double row break).
- SUGGESTED FIX: Use a single '\\'.

## 53. PDF page 14 | ORANGE unsupported claim
- Highlighted text: "property in practice. SupCon alone (A3) barely helps (+1.86 pp). But it combines well once CLIP and AdamW are in place. The deployed A5α recipe reaches 89.06% m"
- PROBLEM: No row supports this: there is no CLIP + AdamW run without SupCon to compare, and A5beta (SupCon) is below A5alpha.
- SUGGESTED FIX: Delete the sentence, or add the missing ablation row.

## 54. PDF page 14 | RED factual/inconsistency
- Highlighted text: "recipe reaches 89.06%"
- PROBLEM: 89.06 here is a from-scratch ablation run, not the released checkpoint (89.63 at the same operating point).
- SUGGESTED FIX: 'A single from-scratch run of the deployed A5alpha recipe reaches 89.06% ...'

## 55. PDF page 14 | RED factual/inconsistency
- Highlighted text: "(88.75 ± 0.55 p"
- PROBLEM: 0.55 is the population SD (divide by n). For n = 3 seeds the usual sample SD is 0.68 (Rank-1: 0.09, not 0.07). The +-0.55 band is repeated in Sections 1.3, 3.2, 4.4, 5.4 and 6.5.
- SUGGESTED FIX: Report the sample SD (0.68 / 0.09) everywhere, or state 'population SD'. The 0.49 pp argument still holds.

## 56. PDF page 14 | YELLOW AI-style/AI-draft
- Highlighted text: "This confirms"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 57. PDF page 15 | ORANGE unsupported claim
- Highlighted text: "statistically equivalent"
- PROBLEM: A gap smaller than one seed SD is not a statistical equivalence test.
- SUGGESTED FIX: Say 'the gap is within training noise, so we treat the two as equivalent'.

## 58. PDF page 16 | RED factual/inconsistency
- Highlighted text: "88.75 ± 0.55"
- PROBLEM: 0.55 is the population SD (divide by n). For n = 3 seeds the usual sample SD is 0.68 (Rank-1: 0.09, not 0.07). The +-0.55 band is repeated in Sections 1.3, 3.2, 4.4, 5.4 and 6.5.
- SUGGESTED FIX: Report the sample SD (0.68 / 0.09) everywhere, or state 'population SD'. The 0.49 pp argument still holds.

## 59. PDF page 16 | YELLOW AI-style/AI-draft
- Highlighted text: "This confirms"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 60. PDF page 17 | RED factual/inconsistency
- Highlighted text: "close to established defaults."
- PROBLEM: Not true: Zhong et al.'s defaults are k1=20, k2=6, lambda=0.3. Your k1=80 is four times the default.
- SUGGESTED FIX: Say the re-ranking was tuned, and lean on the flat sweep (88.3-90.1% across the grid) instead.

## 61. PDF page 17 | RED factual/inconsistency
- Highlighted text: "Second, the re-ranking and AQE settings are close to established defaults. The values k1=80,k2=15,λ=0.2 lie within the ranges recommended by Zhong et al. [3], a"
- PROBLEM: Zhong et al. use k1=20, k2=6, lambda=0.3; they do not recommend k1=80.
- SUGGESTED FIX: Drop this claim.

## 62. PDF page 17 | RED factual/inconsistency
- Highlighted text: ", literature-default post-processing)"
- PROBLEM: The post-processing here is the same test-tuned setting as the headline, not a literature default.
- SUGGESTED FIX: 'same post-processing as the headline'.

## 63. PDF page 17 | RED factual/inconsistency
- Highlighted text: "gets 89.99%,"
- PROBLEM: Typo: the deployed setting gives 89.97% (headline).
- SUGGESTED FIX: Change to 89.97% here, in 6.4 (89.92 vs 89.99) and in the CA-Jaccard paragraph.

## 64. PDF page 17 | ORANGE unsupported claim
- Highlighted text: "benefit more from graph-based"
- PROBLEM: AQE is a mean of the top-k neighbours, not graph-based smoothing.
- SUGGESTED FIX: 'neighbourhood averaging'.

## 65. PDF page 17 | YELLOW AI-style/AI-draft
- Highlighted text: "This confirms"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 66. PDF page 19 | RED factual/inconsistency
- Highlighted text: "(82.30%→"
- PROBLEM: Raw Stream-1 mAP is 82.22 everywhere else; 82.30 is TransReID's published number.
- SUGGESTED FIX: If it is a typo: '2.5 pp (82.22% -> 79.75%)'. If it comes from the transfer code, say so.

## 67. PDF page 19 | ORANGE unsupported claim
- Highlighted text: "This agrees with the CityFlowV2 result"
- PROBLEM: Undescribed CityFlowV2 result used as evidence. It also disagrees with 6.5 ('lowered by 1.8 pp' vs 'best-case change of about -1.8 pp').
- SUGGESTED FIX: Remove, or describe the experiment properly.

## 68. PDF page 19 | PURPLE reference-number check
- Highlighted text: "Disabling camera and view embeddings is standard practice"
- PROBLEM: Claim check: Ben Mabrouk et al. (arXiv 2606.01981) only say '*Cross-dataset evaluation does not use view and camera embeddings' for their own experiments; they do not call it standard practice.
- SUGGESTED FIX: '... as in [29]'.

## 69. PDF page 19 | PURPLE reference-number check
- Highlighted text: "VAPC (adapted)"
- PROBLEM: Value check: all SPGAN / UDAP / ECN / VAPC-DT / VAPC-DA rows match the VAPC arXiv version (2011.09099, Table I) exactly. The reference now points to the T-ITS 2022 version, which was not checked.
- SUGGESTED FIX: Optional: confirm against the T-ITS version.

## 70. PDF page 20 | RED factual/inconsistency
- Highlighted text: "(+4.3,"
- PROBLEM: Table 12 gives 35.9-31.7 = +4.2 and 30.5-26.7 = +3.8, not +4.3 / +3.7.
- SUGGESTED FIX: Use the table values, or say the deltas are from unrounded numbers.

## 71. PDF page 20 | RED factual/inconsistency
- Highlighted text: "which fits the"
- PROBLEM: Your own timings (50 s at 13,257 images, 254 s at 41,861, 519 s at 69,389) grow as about N^1.4, not N^2. '3.6x the gallery' divides query+gallery by the gallery alone; the image count grew 3.2x.
- SUGGESTED FIX: 'roughly five times the in-domain pass for 3.2x as many images'; state the measured ~N^1.4 scaling once in 6.4.

## 72. PDF page 20 | PURPLE reference-number check
- Highlighted text: "Supervised training on the 30,671-identity t"
- PROBLEM: Citation check: '79-89% mAP' fits Ben Mabrouk et al. (TransReID 79.5, CLIP-ReID 80.3 on VeRi-Wild) and CLIP-SENet (89.1). But Lou et al. 2019 (also cited here) is FDA-Net, which reports 35.1% (Table 12 of this paper).
- SUGGESTED FIX: Drop Lou et al. from this citation, or say '35-89%'.

## 73. PDF page 21 | ORANGE unsupported claim
- Highlighted text: "Visual inspection suggests"
- PROBLEM: Qualitative section with no figure. Table 13 states mechanisms that were never measured ('CLIP prior abstracts away lighting', 'SupCon anchor pulls clusters', '>60% occlusion', '<40x40 px'). Reads as generated text.
- SUGGESTED FIX: If you inspected failures: keep only the observed failure groups in 3-4 plain sentences and drop the table. If not: remove the section.

## 74. PDF page 21 | YELLOW AI-style/AI-draft
- Highlighted text: "in a more honest light."
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 75. PDF page 22 | RED factual/inconsistency
- Highlighted text: "AQE is a single similarity pass 2"
- PROBLEM: Called cheap, but the next sentences say the CPU AQE pass takes 138 s versus 50 s for re-ranking.
- SUGGESTED FIX: Distinguish GPU AQE (cheap) from the CPU timing.

## 76. PDF page 22 | RED factual/inconsistency
- Highlighted text: "the gallery, which fits"
- PROBLEM: 5x time for 3.2x images is about N^1.4, not O(N^2).
- SUGGESTED FIX: 'That is about 5x the in-domain pass for 3.2x as many images.'

## 77. PDF page 22 | RED factual/inconsistency
- Highlighted text: "This fits quadratic growth"
- PROBLEM: 50 / 254 / 519 s at 13,257 / 41,861 / 69,389 images is a steady ~N^1.4, not quadratic.
- SUGGESTED FIX: 'Time grows roughly as N^1.4 in this range; memory grows quadratically.'

## 78. PDF page 22 | YELLOW AI-style/AI-draft
- Highlighted text: "This confirms"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 79. PDF page 23 | RED factual/inconsistency
- Highlighted text: "(32 vs. 44 s)"
- PROBLEM: Dense in-domain re-ranking is 50 s in the previous paragraph but 44 s here.
- SUGGESTED FIX: Use one number, or say they come from different machines/runs.

## 80. PDF page 23 | PURPLE reference-number check
- Highlighted text: "the official CA-Jaccard implementation [37] (CVPR 2024) as an evaluation-time re-ranker on Stream-1. At the default evaluation settings of its authors (k1=30, k"
- PROBLEM: Value check: the CA-Jaccard paper (arXiv 2311.10605) states kintra=5 and kinter=20 (matches), but not k1=30, k2=6, lambda=0.3. Those presumably come from the authors' code.
- SUGGESTED FIX: Say 'the default settings of the authors' released code'.

## 81. PDF page 23 | YELLOW AI-style/AI-draft
- Highlighted text: "below our tuned standard k-reciprocal (89.99%). This is a comparison of defaults against tuned settings, and we say so. Under zero-shot transfer it does not get"
- PROBLEM: AI-style phrase. Over-disclosure ('we want to be clear', 'we say so', 'in a more honest light') and self-confirming wrap-ups ('This confirms ...') are typical of recent AI assistants.
- SUGGESTED FIX: Cut it, or say it plainly once.

## 82. PDF page 24 | RED factual/inconsistency
- Highlighted text: "AQE costs almost nothing,"
- PROBLEM: Contradicts Section 6.4, where the CPU AQE pass takes 138 s, longer than re-ranking (50 s).
- SUGGESTED FIX: Say 'GPU AQE is cheap', or explain the CPU timing in 6.4.

## 83. PDF page 24 | RED factual/inconsistency
- Highlighted text: "but not the quadratic growth in time."
- PROBLEM: Your sparse timings (32 s at 13,257 images to 372 s at 138,517) grow roughly linearly (~N^0.9-1.2).
- SUGGESTED FIX: '...removes the memory wall, and its measured time grows roughly linearly'.

## 84. PDF page 24 | ORANGE unsupported claim
- Highlighted text: "This agrees with the CityFlowV2 evidence,"
- PROBLEM: Undescribed CityFlowV2 experiment; 'best-case change of about -1.8 pp' conflicts with 'lowered by 1.8 pp' in 5.10.
- SUGGESTED FIX: Remove, or describe it properly.

## 85. PDF page 24 | ORANGE unsupported claim
- Highlighted text: "A separate best-Rank-1 operating point reaches 85.14% mAP and 98.33% Rank-1. This number comes from the post-processing pipeline, not from the recipe. At the ra"
- PROBLEM: Two sentences earlier 'our recipe' includes the post-processing pipeline. The term 'recipe' switches meaning, and the central argument depends on it.
- SUGGESTED FIX: Define 'recipe' once as training only (backbone, initialisation, optimiser, loss, augmentation) and use it consistently.

## 86. PDF page 24 | YELLOW AI-style/AI-draft
- Highlighted text: "Score-level fusion with a CLIP-SENet branch [4] reaches 93.32% mAP and 98.45% Rank-1. This is slightly the best published mAP on VeRi-776, above the previous be"
- PROBLEM: Ungrammatical.
- SUGGESTED FIX: 'This is the best published mAP on VeRi-776, by a narrow +0.42 pp.'

## 87. PDF page 24 | ORANGE unsupported claim
- Highlighted text: "under seen/unseen vehicle-type protocols instead of standard random-identity splits, and extension to nighttime surveillance and CityFlowV2. All code and checkp"
- PROBLEM: Lists CityFlowV2 as future work, but 1.3, 5.10 and 6.5 cite a CityFlowV2 result as evidence.
- SUGGESTED FIX: Make the two consistent.

## 88. PDF page 25 | GREEN fixed/check-only
- Highlighted text: "Use of large language models."
- PROBLEM: Good: keep this disclosure. It is your real protection; a detector score is not. Springer also asks for LLM use to be documented in the methods.
- SUGGESTED FIX: Make sure it matches what was actually done (drafting by Claude, then author rewriting).

## 89. PDF page 25 | GREEN fixed/check-only
- Highlighted text: "References"
- PROBLEM: Reference list corrected and verified: all 29 DOIs and 7 arXiv IDs resolve to the right paper and first author (commit 1e648d1).
- SUGGESTED FIX: Only remaining check: that the T-ITS version of CLIP-SENet still reports 92.9 / 98.7.

## 90. PDF page 27 | BLUE presentation
- Highlighted text: "Author Biographies"
- PROBLEM: Only 2 of the 5 author photos exist (Seif, Ahmed).
- SUGGESTED FIX: Add photos for M. A. Ali, A. A. Ali and A. Hamdi if the journal asks for them.

## 91. PDF page 27 | YELLOW AI-style/AI-draft
- Highlighted text: "He led this project from start to fini"
- PROBLEM: Bio repeats the author-contribution list almost word for word.
- SUGGESTED FIX: Keep the bio to background and interests (50-100 words). Also check 'received his B.Sc.' is true on the submission date.

## 92. PDF page 27 | YELLOW AI-style/AI-draft
- Highlighted text: "His undergraduate research addressed data augmentation"
- PROBLEM: About 62% copied from the AI draft, and written by Seif although the checklist says each author writes their own bio.
- SUGGESTED FIX: Have Mohamed write it.

## 93. PDF page 27 | YELLOW AI-style/AI-draft
- Highlighted text: "His work focuses on the engineering of reproducible evaluation pipelines"
- PROBLEM: Bio still marked AI-DRAFT (100% the AI text); inflated for an undergraduate.
- SUGGESTED FIX: Ali A. Ali should write his own bio.

## 94. PDF page 27 | YELLOW AI-style/AI-draft
- Highlighted text: "His undergraduate work focused on deep representation learning"
- PROBLEM: Bio still marked AI-DRAFT (100% the AI text).
- SUGGESTED FIX: Abdelrahman Hamdi should write his own bio.

## 95. PDF page 28 | YELLOW AI-style/AI-draft
- Highlighted text: "ment, Faculty of Engineering, Cairo University, Giza, Egypt. His research spans machine learning, computer architecture and high performance computing. He super"
- PROBLEM: Marked REWRITTEN, but 100% identical to the AI draft.
- SUGGESTED FIX: The supervisor should confirm or rewrite it.
