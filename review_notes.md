# Review notes exported from main_review_highlighted.pdf

Page numbers are PDF pages of main_review_highlighted.pdf (page 1 is the added summary page; paper page N = PDF page N+1).
Notes repeated on consecutive lines of one phrase are merged. Only open, real problems are listed;
the summary page lists the notes that were checked and dropped.

## 1. PDF page 2 | RED factual/inconsistency
- Highlighted text: "This paper revisits the ViT-Base/16 pipeline on VeRi-776 and separates recipe effects from post-processing effects. We use a specific recipe that we just build "
- PROBLEM: Broken sentence; it does not parse.
- SUGGESTED FIX: e.g. 'Our pipeline combines CLIP-pretrained initialisation, AdamW with layer-wise learning-rate decay, a tuned metric objective and a three-step post-processing chain (...)'.

## 2. PDF page 3 | BLUE presentation/wording
- Highlighted text: "reuses that model’s checkpoint, we present it as a demonstration of feature complementarity, which a paired bootstrap test shows is significant over the best si"
- PROBLEM: Garbled sentence: the 'which ...' clause sits between 'complementarity' and 'rather than'.
- SUGGESTED FIX: e.g. '...we present it as a demonstration of feature complementarity, not a decisive state of the art. A paired bootstrap test shows the gain over the best single stream is significant.'

## 3. PDF page 3 | ORANGE unsupported claim
- Highlighted text: "supported by a CityFlowV2 MTMC port,"
- PROBLEM: CityFlowV2 is used as evidence here (and in 5.10 and 6.5) but is never described anywhere: no setup, no numbers, no table.
- SUGGESTED FIX: Either remove the CityFlowV2 claims, or add a short paragraph with the setup and IDF1 results.

## 4. PDF page 3 | PURPLE reference-number check
- Highlighted text: "No pure ViT-B method has been reported above 90%"
- PROBLEM: Literature check: CLIP-SENet (IEEE T-ITS 2026, arXiv 2502.16815), Table I lists 'CLIP-ReID [11]* AAAI 2023' at 91.7 mAP / 98.0 R1 on VeRi-776 (* = transformer; that paper uses re-ranking on VeRi-776). So a peer-reviewed paper already reports a pure ViT-B result above 90%.
- SUGGESTED FIX: Soften to 'no ViT-B paper reports above 90% in its own results', or mention CLIP-SENet's 91.7 for CLIP-ReID.

## 5. PDF page 4 | PURPLE reference-number check
- Highlighted text: "location-aware identity embeddings"
- PROBLEM: Description check: MBR4B paper (arXiv 2310.01129), Section III-C is titled 'Leveraging Additional Information (LAI)' and uses camera ID and viewpoint metadata. It does not describe 'location-aware identity embeddings'.
- SUGGESTED FIX: '... with LAI (Leveraging Additional Information), which adds camera and viewpoint metadata'.

## 6. PDF page 4 | PURPLE reference-number check
- Highlighted text: "s ResNet101-IBN-a local appearance"
- PROBLEM: Backbone check: CLIP-SENet T-ITS version (arXiv 2502.16815), 'Training details': 'we employ a ResNext101 with IBN structure as our CNN Backbone'. Its Table VI: ResNet101-IBN gives 91.9 / 98.2, ResNeXt101-IBN gives the headline 92.9 / 98.7. (Fine if your own v6 checkpoint is ResNet101-IBN-a, but the cited 92.9 is the ResNeXt101 model.)
- SUGGESTED FIX: Describe the published model as ResNeXt101-IBN, and say your Stream 2 uses ResNet101-IBN-a if that is the case.

## 7. PDF page 4 | PURPLE reference-number check
- Highlighted text: "Trains on VeRi-776, VehicleID and synthetic data together"
- PROBLEM: Description check: VehicleNet paper (arXiv 2004.06305), Sec. III-A: 'We involve four public datasets, i.e., CityFlow, VeRi-776, CompCar and VehicleID ... 434,440 training images of 31,805 classes'. No synthetic data.
- SUGGESTED FIX: 'Trains on CityFlow, VeRi-776, CompCars and VehicleID together'.

## 8. PDF page 4 | PURPLE reference-number check
- Highlighted text: "ResNet101-IBN-a with multi-head attention, trained on several domain"
- PROBLEM: Description check: Strong Baseline paper (arXiv 2104.10850), Sec. 3: MixStyle in a 'ResNeXt101 ibn a' backbone plus multi-head attention; the final model ensembles ResNet50-ibn-a, ResNeXt101-ibn-a and ResNet152. Its Table 5 also gives Rank-1 = 97.0 (Table 1 shows '--'). RPTM's Table 2 marks this result as re-ranked.
- SUGGESTED FIX: 'ResNeXt101-IBN-a ensemble with MixStyle and multi-head attention'; R1 97.0.

## 9. PDF page 4 | PURPLE reference-number check
- Highlighted text: "1The PROVID (53.42/81.56) and VAMI (50.13/77.03) figures are the values reported in the respective papers and reproduced throughout the survey literature [11, 1"
- PROBLEM: Citation check: Ye et al. (arXiv 2001.04193) is a person re-ID survey only (abstract) and would not list PROVID / VAMI vehicle results.
- SUGGESTED FIX: Cite only the vehicle survey (Yi et al.) here.

## 10. PDF page 5 | RED factual/inconsistency
- Highlighted text: "AQE costs almost nothing."
- PROBLEM: Contradicts Section 6.4, where the CPU AQE pass takes 138 s, longer than re-ranking (50 s).
- SUGGESTED FIX: Say 'GPU AQE is cheap', or explain the CPU timing in 6.4.

## 11. PDF page 5 | PURPLE reference-number check
- Highlighted text: ", no prior work reports above 90% m"
- PROBLEM: Same point: CLIP-SENet's Table I reports CLIP-ReID (ViT) at 91.7 / 98.0 on VeRi-776.
- SUGGESTED FIX: Rephrase as above.

## 12. PDF page 5 | PURPLE reference-number check
- Highlighted text: "of the same class in a mini-batch count as positives. This gives embedding spaces that are more uniform and more discriminative than triplet loss alone [11]. We"
- PROBLEM: Citation check: this is cited to Ye et al. (TPAMI). That survey was first posted on 13 Jan 2020 (arXiv 2001.04193); SupCon appeared in Apr 2020, so the survey cannot support a claim about SupCon.
- SUGGESTED FIX: Cite Khosla et al. alone, or drop the claim.

## 13. PDF page 6 | RED factual/inconsistency
- Highlighted text: "The deployed headline checkpoint"
- PROBLEM: Four different Stream-1 numbers are all attached to 'A5alpha / deployed': 89.97 (headline, 1536D), 89.63 (released checkpoint, 768D), 89.06 (ablation row, actually a from-scratch run) and 89.99 (Sec. 5.7/6.4, typo for 89.97).
- SUGGESTED FIX: Label 89.06 as 'a from-scratch ablation run of the A5alpha recipe' and say the released checkpoint scores 89.63 at 768D.

## 14. PDF page 7 | ORANGE unsupported claim
- Highlighted text: "The exact P×"
- PROBLEM: The P x K tuple 'was not logged', but Section 5.5 retrains three seeds 'under identical hyperparameters'. Which P x K did those runs use?
- SUGGESTED FIX: State the P x K used for the seed retrains, or say the seed runs used 12x8.

## 15. PDF page 7 | PURPLE reference-number check
- Highlighted text: "CLIP-SENet uses a ResNet101-IBN-a backbone"
- PROBLEM: Same backbone point: the CLIP-SENet paper's headline model uses ResNeXt101-IBN (ResNet101-IBN variant: 91.9 / 98.2, their Table VI).
- SUGGESTED FIX: Separate 'the published CLIP-SENet' from 'our v6 checkpoint'.

## 16. PDF page 8 | RED factual/inconsistency
- Highlighted text: "Post-processing is applied to each stream separately, before fusion."
- PROBLEM: Contradicts 3.5: in the fusion pipeline only AQE is per-stream; re-ranking is applied once to the fused matrix.
- SUGGESTED FIX: e.g. 'This section gives each stream's standalone settings. In the fusion pipeline, AQE is applied per stream and k-reciprocal re-ranking once, to the fused matrix.'

## 17. PDF page 11 | PURPLE reference-number check
- Highlighted text: "RPTM"
- PROBLEM: Post-processing mark: Table 6 marks RPTM as without post-processing. RPTM paper (arXiv 2110.07933), Table 2 caption: 'The * indicates the usage of re-ranking', and the row 'RPTM (ResNet-101)*' gives 88.00 / 97.30. The text also says 82.5% mAP 'w/o re-ranking'.
- SUGGESTED FIX: Mark RPTM as with post-processing (or use its non-re-ranked number).

## 18. PDF page 11 | PURPLE reference-number check
- Highlighted text: "ResNet101-IBN-a + TinyCLIP"
- PROBLEM: Table 6 backbone for CLIP-SENet (92.90 / 98.70): the paper's 92.9 model uses ResNeXt101-IBN + TinyCLIP (ViT-B/32).
- SUGGESTED FIX: 'ResNeXt101-IBN-a + TinyCLIP'.

## 19. PDF page 12 | RED factual/inconsistency
- Highlighted text: "point in one place. It includes a validation-selected fusion row (Section 5.7) as the recommended tuning-free default. The headline fusion also reaches 84.14% m"
- PROBLEM: Not tuning-free: its post-processing parameters are tuned on the test split; only the fusion weight comes from a validation split.
- SUGGESTED FIX: e.g. 'a fusion row whose weight is selected on a validation split, which we recommend as the default'.

## 20. PDF page 12 | PURPLE reference-number check
- Highlighted text: "TransReID (ViT-B)"
- PROBLEM: Value check: Table 7 gives 80.60 / 97.00. TransReID paper (arXiv 2102.04378), Table 6, ViT-B/16 block, row 'TransReID b' (camera+view): 80.6 mAP / 96.9 R1. The 97.0 belongs to row 'TransReID v' (79.6 / 97.0).
- SUGGESTED FIX: Use 80.6 / 96.9, or name the variant you mean.

## 21. PDF page 13 | PURPLE reference-number check
- Highlighted text: "so our extraction is faithful."
- PROBLEM: Value check: 82.3 is TransReID* with DeiT-B/16 (TransReID Table 6). The ViT-B/16* model is 82.0 / 97.1, which your 82.11 matches even more closely. Section 5.3 calls the checkpoint ViT-B/16, Table 7 calls TransReID* DeiT-B.
- SUGGESTED FIX: Confirm which official checkpoint was used and compare with its own published number.

## 22. PDF page 14 | RED factual/inconsistency
- Highlighted text: "centre, deployed)"
- PROBLEM: This row is a single from-scratch run (see footnote), not the released checkpoint, which scores 89.63 at this operating point.
- SUGGESTED FIX: Relabel 'deployed recipe, ablation run'.

## 23. PDF page 14 | BLUE presentation/wording
- Highlighted text: "A1, un-tuned SGD control"
- PROBLEM: Blank table row after this line: the source uses '\\\\' (double row break).
- SUGGESTED FIX: Replace the double '\\\\' with a single '\\' (also after the TransReID-baseline and CLIP-SENet-base rows, and the two 'Ours' rows of Table 6).

## 24. PDF page 14 | BLUE presentation/wording
- Highlighted text: "TransReID baseline (DeiT-B*)"
- PROBLEM: Blank table row after this line (double row break).
- SUGGESTED FIX: Use a single '\\'.

## 25. PDF page 14 | ORANGE unsupported claim
- Highlighted text: "property in practice. SupCon alone (A3) barely helps (+1.86 pp). But it combines well once CLIP and AdamW are in place. The deployed A5α recipe reaches 89.06% m"
- PROBLEM: No row supports this: there is no CLIP + AdamW run without SupCon to compare, and A5beta (SupCon) is below A5alpha.
- SUGGESTED FIX: Delete the sentence, or add the missing ablation row.

## 26. PDF page 14 | RED factual/inconsistency
- Highlighted text: "recipe reaches 89.06%"
- PROBLEM: 89.06 here is a from-scratch ablation run, not the released checkpoint (89.63 at the same operating point).
- SUGGESTED FIX: 'A single from-scratch run of the deployed A5alpha recipe reaches 89.06% ...'

## 27. PDF page 17 | RED factual/inconsistency
- Highlighted text: "close to established defaults."
- PROBLEM: Not true: Zhong et al.'s defaults are k1=20, k2=6, lambda=0.3. Your k1=80 is four times the default.
- SUGGESTED FIX: Say the re-ranking was tuned, and lean on the flat sweep (88.3-90.1% across the grid) instead.

## 28. PDF page 17 | RED factual/inconsistency
- Highlighted text: "Second, the re-ranking and AQE settings are close to established defaults. The values k1=80,k2=15,λ=0.2 lie within the ranges recommended by Zhong et al. [3], a"
- PROBLEM: Zhong et al. use k1=20, k2=6, lambda=0.3; they do not recommend k1=80.
- SUGGESTED FIX: Drop this claim.

## 29. PDF page 17 | RED factual/inconsistency
- Highlighted text: ", literature-default post-processing)"
- PROBLEM: The post-processing here is the same test-tuned setting as the headline, not a literature default.
- SUGGESTED FIX: 'same post-processing as the headline'.

## 30. PDF page 17 | RED factual/inconsistency
- Highlighted text: "gets 89.99%,"
- PROBLEM: Typo: the deployed setting gives 89.97% (headline).
- SUGGESTED FIX: Change to 89.97% here, in 6.4 (89.92 vs 89.99) and in the CA-Jaccard paragraph.

## 31. PDF page 19 | RED factual/inconsistency
- Highlighted text: "(82.30%→"
- PROBLEM: Raw Stream-1 mAP is 82.22 everywhere else; 82.30 is TransReID's published number.
- SUGGESTED FIX: If it is a typo: '2.5 pp (82.22% -> 79.75%)'. If it comes from the transfer code, say so.

## 32. PDF page 19 | ORANGE unsupported claim
- Highlighted text: "This agrees with the CityFlowV2 result"
- PROBLEM: Undescribed CityFlowV2 result used as evidence. It also disagrees with 6.5 ('lowered by 1.8 pp' vs 'best-case change of about -1.8 pp').
- SUGGESTED FIX: Remove, or describe the experiment properly.

## 33. PDF page 20 | RED factual/inconsistency
- Highlighted text: "which fits the"
- PROBLEM: Your own timings (50 s at 13,257 images, 254 s at 41,861, 519 s at 69,389) grow as about N^1.4, not N^2. '3.6x the gallery' divides query+gallery by the gallery alone; the image count grew 3.2x.
- SUGGESTED FIX: 'roughly five times the in-domain pass for 3.2x as many images'; state the measured ~N^1.4 scaling once in 6.4.

## 34. PDF page 20 | PURPLE reference-number check
- Highlighted text: "Supervised training on the 30,671-identity t"
- PROBLEM: Citation check: '79-89% mAP' fits Ben Mabrouk et al. (TransReID 79.5, CLIP-ReID 80.3 on VeRi-Wild) and CLIP-SENet (89.1). But Lou et al. 2019 (also cited here) is FDA-Net, which reports 35.1% (Table 12 of this paper).
- SUGGESTED FIX: Drop Lou et al. from this citation, or say '35-89%'.

## 35. PDF page 21 | ORANGE unsupported claim
- Highlighted text: "Visual inspection suggests"
- PROBLEM: Qualitative section with no figure. Table 13 states mechanisms that were never measured ('CLIP prior abstracts away lighting', 'SupCon anchor pulls clusters', '>60% occlusion', '<40x40 px').
- SUGGESTED FIX: If you inspected failures: keep only the observed failure groups in 3-4 plain sentences and drop the table. If not: remove the section.

## 36. PDF page 22 | RED factual/inconsistency
- Highlighted text: "the gallery, which fits"
- PROBLEM: 5x time for 3.2x images is about N^1.4, not O(N^2).
- SUGGESTED FIX: 'That is about 5x the in-domain pass for 3.2x as many images.'

## 37. PDF page 22 | RED factual/inconsistency
- Highlighted text: "This fits quadratic growth"
- PROBLEM: 50 / 254 / 519 s at 13,257 / 41,861 / 69,389 images is a steady ~N^1.4, not quadratic.
- SUGGESTED FIX: 'Time grows roughly as N^1.4 in this range; memory grows quadratically.'

## 38. PDF page 23 | RED factual/inconsistency
- Highlighted text: "(32 vs. 44 s)"
- PROBLEM: Dense in-domain re-ranking is 50 s in the previous paragraph but 44 s here.
- SUGGESTED FIX: Use one number, or say they come from different machines/runs.

## 39. PDF page 24 | RED factual/inconsistency
- Highlighted text: "AQE costs almost nothing,"
- PROBLEM: Contradicts Section 6.4, where the CPU AQE pass takes 138 s, longer than re-ranking (50 s).
- SUGGESTED FIX: Say 'GPU AQE is cheap', or explain the CPU timing in 6.4.

## 40. PDF page 24 | RED factual/inconsistency
- Highlighted text: "but not the quadratic growth in time."
- PROBLEM: Your sparse timings (32 s at 13,257 images to 372 s at 138,517) grow roughly linearly (~N^0.9-1.2).
- SUGGESTED FIX: '...removes the memory wall, and its measured time grows roughly linearly'.

## 41. PDF page 24 | ORANGE unsupported claim
- Highlighted text: "This agrees with the CityFlowV2 evidence,"
- PROBLEM: Undescribed CityFlowV2 experiment; 'best-case change of about -1.8 pp' conflicts with 'lowered by 1.8 pp' in 5.10.
- SUGGESTED FIX: Remove, or describe it properly.

## 42. PDF page 24 | BLUE presentation/wording
- Highlighted text: "Score-level fusion with a CLIP-SENet branch [4] reaches 93.32% mAP and 98.45% Rank-1. This is slightly the best published mAP on VeRi-776, above the previous be"
- PROBLEM: Ungrammatical.
- SUGGESTED FIX: 'This is the best published mAP on VeRi-776, by a narrow +0.42 pp.'

## 43. PDF page 24 | ORANGE unsupported claim
- Highlighted text: "under seen/unseen vehicle-type protocols instead of standard random-identity splits, and extension to nighttime surveillance and CityFlowV2. All code and checkp"
- PROBLEM: Lists CityFlowV2 as future work, but 1.3, 5.10 and 6.5 cite a CityFlowV2 result as evidence.
- SUGGESTED FIX: Make the two consistent.

## 44. PDF page 27 | BLUE presentation/wording
- Highlighted text: "Author Biographies"
- PROBLEM: Only 2 of the 5 author photos exist (Seif, Ahmed).
- SUGGESTED FIX: Add photos for M. A. Ali, A. A. Ali and A. Hamdi if the journal asks for them.
