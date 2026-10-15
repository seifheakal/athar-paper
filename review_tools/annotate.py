"""Make a review copy of the paper: highlight each issue and attach a note with the problem and a suggested fix.

usage: python annotate.py <in.pdf> <out.pdf>
"""
import sys
import fitz

RED = (1.0, 0.45, 0.45)      # factual error / internal inconsistency
ORANGE = (1.0, 0.72, 0.30)   # unsupported or over-stated claim
YELLOW = (1.0, 0.95, 0.35)   # AI-style wording / mostly copied from the AI draft
BLUE = (0.55, 0.78, 1.0)     # presentation / submission checklist
GREEN = (0.55, 0.90, 0.55)   # already fixed, or check-only
PURPLE = (0.80, 0.66, 1.0)   # reference-number check: value or claim compared against the cited source

LEGEND = [(RED, "Factual error or internal inconsistency"),
          (ORANGE, "Claim not supported by the paper / over-stated"),
          (BLUE, "Presentation, wording or submission checklist"),
          (PURPLE, "Reference-number check: compared with the cited source (note says where to look)")]

# Page filters for anchors that also occur elsewhere: only pages containing this text are searched.
T1 = "CNN-era methods on VeRi-776"          # Table 1
T3 = "Training hyperparameters: Stream"     # Table 3
T6 = "State-of-the-art comparison on VeRi-776"  # Table 6
T7 = "Transformer-based methods on VeRi-776"    # Table 7
T12 = "Zero-shot VeRi-776"                  # Table 12

# (anchor, colour, problem, suggested fix, occurrence, page filter). Each note gives the source location so it can be re-checked.
REFCHECK = [
    ("TransReID (ViT-B)", PURPLE,
     "Value check: Table 7 gives 80.60 / 97.00. TransReID paper (arXiv 2102.04378), Table 6, ViT-B/16 block, row 'TransReID b' (camera+view): 80.6 mAP / 96.9 R1. The 97.0 belongs to row 'TransReID v' (79.6 / 97.0).",
     "Use 80.6 / 96.9, or name the variant you mean.", 1, T7),
    ("RPTM", PURPLE,
     "Post-processing mark: Table 6 marks RPTM as without post-processing. RPTM paper (arXiv 2110.07933), Table 2 caption: 'The * indicates the usage of re-ranking', and the row 'RPTM (ResNet-101)*' gives 88.00 / 97.30. The text also says 82.5% mAP 'w/o re-ranking'.",
     "Mark RPTM as with post-processing (or use its non-re-ranked number).", 1, T6),
    ("location-aware identity embeddings", PURPLE,
     "Description check: MBR4B paper (arXiv 2310.01129), Section III-C is titled 'Leveraging Additional Information (LAI)' and uses camera ID and viewpoint metadata. It does not describe 'location-aware identity embeddings'.",
     "'... with LAI (Leveraging Additional Information), which adds camera and viewpoint metadata'.", 1, None),
    ("ResNet101-IBN-a local appearance", PURPLE,
     "Backbone check: CLIP-SENet T-ITS version (arXiv 2502.16815), 'Training details': 'we employ a ResNext101 with IBN structure as our CNN Backbone'. Its Table VI: ResNet101-IBN gives 91.9 / 98.2, ResNeXt101-IBN gives the headline 92.9 / 98.7. (Fine if your own v6 checkpoint is ResNet101-IBN-a, but the cited 92.9 is the ResNeXt101 model.)",
     "Describe the published model as ResNeXt101-IBN, and say your Stream 2 uses ResNet101-IBN-a if that is the case.", 1, None),
    ("CLIP-SENet uses a ResNet101-IBN-a backbone", PURPLE,
     "Same backbone point: the CLIP-SENet paper's headline model uses ResNeXt101-IBN (ResNet101-IBN variant: 91.9 / 98.2, their Table VI).",
     "Separate 'the published CLIP-SENet' from 'our v6 checkpoint'.", 1, None),
    ("ResNet101-IBN-a + TinyCLIP", PURPLE,
     "Table 6 backbone for CLIP-SENet (92.90 / 98.70): the paper's 92.9 model uses ResNeXt101-IBN + TinyCLIP (ViT-B/32).",
     "'ResNeXt101-IBN-a + TinyCLIP'.", 1, T6),
    ("No pure ViT-B method has been reported above 90% mAP", PURPLE,
     "Literature check: CLIP-SENet (IEEE T-ITS 2026, arXiv 2502.16815), Table I lists 'CLIP-ReID [11]* AAAI 2023' at 91.7 mAP / 98.0 R1 on VeRi-776 (* = transformer; that paper uses re-ranking on VeRi-776). So a peer-reviewed paper already reports a pure ViT-B result above 90%.",
     "Soften to 'no ViT-B paper reports above 90% in its own results', or mention CLIP-SENet's 91.7 for CLIP-ReID.", 1, None),
    ("no prior work reports above 90%", PURPLE,
     "Same point: CLIP-SENet's Table I reports CLIP-ReID (ViT) at 91.7 / 98.0 on VeRi-776.",
     "Rephrase as above.", 1, None),
    ("Trains on VeRi-776, VehicleID and synthetic data together", PURPLE,
     "Description check: VehicleNet paper (arXiv 2004.06305), Sec. III-A: 'We involve four public datasets, i.e., CityFlow, VeRi-776, CompCar and VehicleID ... 434,440 training images of 31,805 classes'. No synthetic data.",
     "'Trains on CityFlow, VeRi-776, CompCars and VehicleID together'.", 1, T1),
    ("ResNet101-IBN-a with multi-head attention", PURPLE,
     "Description check: Strong Baseline paper (arXiv 2104.10850), Sec. 3: MixStyle in a 'ResNeXt101 ibn a' backbone plus multi-head attention; the final model ensembles ResNet50-ibn-a, ResNeXt101-ibn-a and ResNet152. Its Table 5 also gives Rank-1 = 97.0 (Table 1 shows '--'). RPTM's Table 2 marks this result as re-ranked.",
     "'ResNeXt101-IBN-a ensemble with MixStyle and multi-head attention'; R1 97.0.", 1, T1),
    ("Supervised training on the 30,671-identity", PURPLE,
     "Citation check: '79-89% mAP' fits Ben Mabrouk et al. (TransReID 79.5, CLIP-ReID 80.3 on VeRi-Wild) and CLIP-SENet (89.1). But Lou et al. 2019 (also cited here) is FDA-Net, which reports 35.1% (Table 12 of this paper).",
     "Drop Lou et al. from this citation, or say '35-89%'.", 1, None),
    ("more uniform and more discriminative than triplet loss alone", PURPLE,
     "Citation check: this is cited to Ye et al. (TPAMI). That survey was first posted on 13 Jan 2020 (arXiv 2001.04193); SupCon appeared in Apr 2020, so the survey cannot support a claim about SupCon.",
     "Cite Khosla et al. alone, or drop the claim.", 1, None),
    ("reproduced throughout the survey", PURPLE,
     "Citation check: Ye et al. (arXiv 2001.04193) is a person re-ID survey only (abstract) and would not list PROVID / VAMI vehicle results.",
     "Cite only the vehicle survey (Yi et al.) here.", 1, None),
    ("training images of 576", PURPLE,
     "Count check: TransReID (Table 1: 49,357 images) and CLIP-SENet ('training set with 576 identities and 37,778 images') use 37,778 training images; 37,778 + 11,579 = 49,357. 37,781 also appears in older descriptions.",
     "Pick one count and use it consistently.", 0, None),
    ("viewpoint (8 categories)", PURPLE,
     "Source check: the VeRi page (github.com/JDAI-CV/VeRidataset) lists 'BBoxes, types, colors, and brands'; viewpoint labels come from later annotation work, not PROVID.",
     "Cite the source of the viewpoint labels, or drop '(8 categories)'.", 1, None),
    ("Epochs", PURPLE,
     "Value check: the TransReID paper does not state an epoch count (no 'epoch' in the text). 120 is presumably from TransReID's released config.",
     "Cite the config, or mark as 'from the released code'.", 1, T3),
    ("was the first pure Vision Transformer framework", PURPLE,
     "Claim check: the TransReID paper says it proposes 'a pure transformer-based object ReID framework'; it does not claim to be the first.",
     "Drop 'first', or attribute it carefully.", 1, None),
    ("so our extraction is faithful", PURPLE,
     "Value check: 82.3 is TransReID* with DeiT-B/16 (TransReID Table 6). The ViT-B/16* model is 82.0 / 97.1, which your 82.11 matches even more closely. Section 5.3 calls the checkpoint ViT-B/16, Table 7 calls TransReID* DeiT-B.",
     "Confirm which official checkpoint was used and compare with its own published number.", 1, None),
    ("VehicleNet", PURPLE,
     "Post-processing mark: VehicleNet's paper describes query expansion and re-ranking for its AI City Challenge pipeline, not for the VeRi-776 result (83.41 / 96.78). RPTM's Table 2 does mark VehicleNet as re-ranked, so sources disagree.",
     "Check the VehicleNet paper / code and set the mark accordingly.", 1, T6),
    ("Disabling camera and view embeddings is standard practice", PURPLE,
     "Claim check: Ben Mabrouk et al. (arXiv 2606.01981) only say '*Cross-dataset evaluation does not use view and camera embeddings' for their own experiments; they do not call it standard practice.",
     "'... as in [29]'.", 1, None),
    ("At the default evaluation settings of its authors", PURPLE,
     "Value check: the CA-Jaccard paper (arXiv 2311.10605) states kintra=5 and kinter=20 (matches), but not k1=30, k2=6, lambda=0.3. Those presumably come from the authors' code.",
     "Say 'the default settings of the authors' released code'.", 1, None),
    ("84.5% mAP and 97.3% Rank-1 on VeRi-776", PURPLE,
     "Citation check: correct value, but it is cited to the OpenCodePapers mirror. The CLIP-ReID paper (arXiv 2211.13977), Table 3, row 'CLIP-ReID' (ViT), gives 84.5 / 97.3 directly.",
     "Cite the CLIP-ReID paper [8].", 1, None),
]

# (anchor text as it appears in the PDF, colour, problem, suggested fix, occurrence)  occurrence: 1-based, 0 = all
ISSUES = [
    # ---------- front matter ----------
    ("We use a specific recipe that we just build on", RED,
     "Broken sentence; it does not parse.",
     "e.g. 'Our pipeline combines CLIP-pretrained initialisation, AdamW with layer-wise learning-rate decay, a tuned metric objective and a three-step post-processing chain (...)'.", 1),

    # ---------- introduction ----------
    ("No pure ViT-B method has been reported above 90% mAP", ORANGE,
     "This framing ('we approach 90%') contradicts your own finding that TransReID and CLIP-ReID with your post-processing reach 91.12 / 91.80%.",
     "Frame the gap as 'recipe vs post-processing effects are never separated', which is what the paper actually shows.", 1),
    ("both slightly above ours", ORANGE,
     "1.15 and 1.83 pp are not 'slightly' above.",
     "Say 'both above ours (by 1.15 and 1.83 pp)'.", 1),
    ("which a paired bootstrap test shows is significant", BLUE,
     "Garbled sentence: the 'which ...' clause sits between 'complementarity' and 'rather than'.",
     "e.g. '...we present it as a demonstration of feature complementarity, not a decisive state of the art. A paired bootstrap test shows the gain over the best single stream is significant.'", 1),
    ("supported by a CityFlowV2 MTMC port", ORANGE,
     "CityFlowV2 is used as evidence here (and in 5.10 and 6.5) but is never described anywhere: no setup, no numbers, no table.",
     "Either remove the CityFlowV2 claims, or add a short paragraph with the setup and IDF1 results.", 1),

    # ---------- related work ----------
    ("They cover parts, multiple data sources", PURPLE,
     "Content check: the content of this sentence was not checked against the Yi et al. survey.",
     "Confirm the survey really covers parts, multi-source data and cross-domain adaptation.", 1),
    ("Supervised Contrastive Learning (SupCon)", ORANGE,
     "A paragraph about a training loss sits inside the 'Re-ranking and post-processing' section.",
     "Move it to the methodology (loss function) or a short 'metric learning' paragraph.", 1),
    ("statistically equivalent", ORANGE,
     "A gap smaller than one seed SD is not a statistical equivalence test.",
     "Say 'the gap is within training noise, so we treat the two as equivalent'.", 0),
    ("AQE costs almost nothing", RED,
     "Contradicts Section 6.4, where the CPU AQE pass takes 138 s, longer than re-ranking (50 s).",
     "Say 'GPU AQE is cheap', or explain the CPU timing in 6.4.", 0),

    # ---------- methodology ----------
    ("The deployed headline checkpoint", RED,
     "Four different Stream-1 numbers are all attached to 'A5alpha / deployed': 89.97 (headline, 1536D), 89.63 (released checkpoint, 768D), 89.06 (ablation row, actually a from-scratch run) and 89.99 (Sec. 5.7/6.4, typo for 89.97).",
     "Label 89.06 as 'a from-scratch ablation run of the A5alpha recipe' and say the released checkpoint scores 89.63 at 768D.", 1),
    ("Post-processing is applied to each stream separately, before fusion.", RED,
     "Contradicts 3.5: in the fusion pipeline only AQE is per-stream; re-ranking is applied once to the fused matrix.",
     "e.g. 'This section gives each stream's standalone settings. In the fusion pipeline, AQE is applied per stream and k-reciprocal re-ranking once, to the fused matrix.'", 1),
    ("The exact P", ORANGE,
     "The P x K tuple 'was not logged', but Section 5.5 retrains three seeds 'under identical hyperparameters'. Which P x K did those runs use?",
     "State the P x K used for the seed retrains, or say the seed runs used 12x8.", 1),
    ("we found no sign that feature-level concatenation overfits", ORANGE,
     "Contradicts the first paragraph, which justifies score-level fusion by the risk of overfitting.",
     "Drop the overfitting argument from the first paragraph and keep the 'explicit weights' reason.", 1),

    # ---------- results ----------
    ("tuning-free default", RED,
     "Not tuning-free: its post-processing parameters are tuned on the test split; only the fusion weight comes from a validation split.",
     "e.g. 'a fusion row whose weight is selected on a validation split, which we recommend as the default'.", 1),
    ("(TransReID* ViT-B/16, released by the TransReID authors", RED,
     "Labelled ViT-B/16 here, but Table 7 lists TransReID* as DeiT-B/16 (82.3) and plain ViT-B as 80.6. The 'matches its published number' check depends on which checkpoint this is.",
     "Name the exact checkpoint (DeiT-B/16 stride-12?) and the published number it should match.", 1),
    ("The same is probably true for much of the apparent progress after TransReID", ORANGE,
     "Generalises from two models (TransReID, CLIP-ReID) to 'much of the progress' on the benchmark.",
     "Limit the claim to the two baselines you tested, or test more checkpoints.", 0),
    ("centre, deployed)", RED,
     "This row is a single from-scratch run (see footnote), not the released checkpoint, which scores 89.63 at this operating point.",
     "Relabel 'deployed recipe, ablation run'.", 1),
    ("A1, un-tuned SGD control", BLUE,
     "Blank table row after this line: the source uses '\\\\\\\\' (double row break).",
     "Replace the double '\\\\\\\\' with a single '\\\\' (also after the TransReID-baseline and CLIP-SENet-base rows, and the two 'Ours' rows of Table 6).", 1),
    ("TransReID baseline (DeiT-B*)", BLUE, "Blank table row after this line (double row break).", "Use a single '\\\\'.", 1),
    ("CLIP-SENet v6, base cosine", BLUE, "Blank table row after this line (double row break).", "Use a single '\\\\'.", 1),
    ("But it combines well once CLIP and AdamW are in place.", ORANGE,
     "No row supports this: there is no CLIP + AdamW run without SupCon to compare, and A5beta (SupCon) is below A5alpha.",
     "Delete the sentence, or add the missing ablation row.", 1),
    ("recipe reaches 89.06%", RED,
     "89.06 here is a from-scratch ablation run, not the released checkpoint (89.63 at the same operating point).",
     "'A single from-scratch run of the deployed A5alpha recipe reaches 89.06% ...'", 1),
    ("88.75 ± 0.55", RED,
     "0.55 is the population SD (divide by n). For n = 3 seeds the usual sample SD is 0.68 (Rank-1: 0.09, not 0.07). The +-0.55 band is repeated in Sections 1.3, 3.2, 4.4, 5.4 and 6.5.",
     "Report the sample SD (0.68 / 0.09) everywhere, or state 'population SD'. The 0.49 pp argument still holds.", 0),
    ("close to established defaults", RED,
     "Not true: Zhong et al.'s defaults are k1=20, k2=6, lambda=0.3. Your k1=80 is four times the default.",
     "Say the re-ranking was tuned, and lean on the flat sweep (88.3-90.1% across the grid) instead.", 1),
    ("lie within the ranges recommended by Zhong", RED,
     "Zhong et al. use k1=20, k2=6, lambda=0.3; they do not recommend k1=80.",
     "Drop this claim.", 1),
    ("literature-default post-processing", RED,
     "The post-processing here is the same test-tuned setting as the headline, not a literature default.",
     "'same post-processing as the headline'.", 1),
    ("gets 89.99%", RED, "Typo: the deployed setting gives 89.97% (headline).", "Change to 89.97% here, in 6.4 (89.92 vs 89.99) and in the CA-Jaccard paragraph.", 1),
    ("benefit more from graph-based", ORANGE, "AQE is a mean of the top-k neighbours, not graph-based smoothing.", "'neighbourhood averaging'.", 1),
    ("(82.30%", RED,
     "Raw Stream-1 mAP is 82.22 everywhere else; 82.30 is TransReID's published number.",
     "If it is a typo: '2.5 pp (82.22% -> 79.75%)'. If it comes from the transfer code, say so.", 1),
    ("This agrees with the CityFlowV2 result", ORANGE,
     "Undescribed CityFlowV2 result used as evidence. It also disagrees with 6.5 ('lowered by 1.8 pp' vs 'best-case change of about -1.8 pp').",
     "Remove, or describe the experiment properly.", 1),
    ("+4.3", RED, "Table 12 gives 35.9-31.7 = +4.2 and 30.5-26.7 = +3.8, not +4.3 / +3.7.", "Use the table values, or say the deltas are from unrounded numbers.", 1),
    ("which fits the", RED,
     "Your own timings (50 s at 13,257 images, 254 s at 41,861, 519 s at 69,389) grow as about N^1.4, not N^2. '3.6x the gallery' divides query+gallery by the gallery alone; the image count grew 3.2x.",
     "'roughly five times the in-domain pass for 3.2x as many images'; state the measured ~N^1.4 scaling once in 6.4.", 1),
    ("Visual inspection suggests", ORANGE,
     "Qualitative section with no figure. Table 13 states mechanisms that were never measured ('CLIP prior abstracts away lighting', 'SupCon anchor pulls clusters', '>60% occlusion', '<40x40 px').",
     "If you inspected failures: keep only the observed failure groups in 3-4 plain sentences and drop the table. If not: remove the section.", 1),

    # ---------- discussion ----------
    ("AQE is a single similarity pass", RED,
     "Called cheap, but the next sentences say the CPU AQE pass takes 138 s versus 50 s for re-ranking.",
     "Distinguish GPU AQE (cheap) from the CPU timing.", 1),
    ("the gallery, which fits", RED,
     "5x time for 3.2x images is about N^1.4, not O(N^2).",
     "'That is about 5x the in-domain pass for 3.2x as many images.'", 1),
    ("This fits quadratic growth", RED,
     "50 / 254 / 519 s at 13,257 / 41,861 / 69,389 images is a steady ~N^1.4, not quadratic.",
     "'Time grows roughly as N^1.4 in this range; memory grows quadratically.'", 1),
    ("(32 vs. 44 s)", RED, "Dense in-domain re-ranking is 50 s in the previous paragraph but 44 s here.", "Use one number, or say they come from different machines/runs.", 1),
    ("but not the quadratic growth in time", RED,
     "Your sparse timings (32 s at 13,257 images to 372 s at 138,517) grow roughly linearly (~N^0.9-1.2).",
     "'...removes the memory wall, and its measured time grows roughly linearly'.", 1),
    ("This agrees with the CityFlowV2 evidence", ORANGE,
     "Undescribed CityFlowV2 experiment; 'best-case change of about -1.8 pp' conflicts with 'lowered by 1.8 pp' in 5.10.",
     "Remove, or describe it properly.", 1),

    # ---------- conclusion ----------
    ("This number comes from the post-processing pipeline, not from the recipe", ORANGE,
     "Two sentences earlier 'our recipe' includes the post-processing pipeline. The term 'recipe' switches meaning, and the central argument depends on it.",
     "Define 'recipe' once as training only (backbone, initialisation, optimiser, loss, augmentation) and use it consistently.", 1),
    ("This is slightly the best published mAP", BLUE, "Ungrammatical.", "'This is the best published mAP on VeRi-776, by a narrow +0.42 pp.'", 1),
    ("and extension to nighttime surveillance and CityFlowV2", ORANGE,
     "Lists CityFlowV2 as future work, but 1.3, 5.10 and 6.5 cite a CityFlowV2 result as evidence.",
     "Make the two consistent.", 1),

    # ---------- back matter ----------
    ("Author Biographies", BLUE,
     "Only 2 of the 5 author photos exist (Seif, Ahmed).",
     "Add photos for M. A. Ali, A. A. Ali and A. Hamdi if the journal asks for them.", 1),
    ("He led this project from start to finish", BLUE,
     "Bio repeats the author-contribution list almost word for word.",
     "Keep the bio to background and interests (50-100 words). Also check 'received his B.Sc.' is true on the submission date.", 1),
]

# Triage: notes checked and NOT counted as real problems (opinion, rounding, minor citation style, or sources disagree).
# They are not highlighted; they are listed on the summary page instead. Key = (anchor, colour).
DROP = {
    ("No pure ViT-B method has been reported above 90% mAP", ORANGE): "framing opinion (the factual part is kept as a purple note)",
    ("both slightly above ours", ORANGE): "wording ('slightly' for 1.15 / 1.83 pp)",
    ("They cover parts, multiple data sources", PURPLE): "not checked, no evidence of an error",
    ("Supervised Contrastive Learning (SupCon)", ORANGE): "section placement (structure opinion)",
    ("statistically equivalent", ORANGE): "wording ('within training noise' would be more careful)",
    ("we found no sign that feature-level concatenation overfits", ORANGE): "minor logic between two paragraphs",
    ("(TransReID* ViT-B/16, released by the TransReID authors", RED): "merged into the purple note at 'so our extraction is faithful'",
    ("The same is probably true for much of the apparent progress after TransReID", ORANGE): "hedged claim ('probably')",
    ("88.75 ± 0.55", RED): "population vs sample SD: a convention, the argument holds either way",
    ("benefit more from graph-based", ORANGE): "terminology for AQE",
    ("+4.3", RED): "rounding: unrounded values (e.g. 35.93) give +4.3 / +3.7",
    ("AQE is a single similarity pass", RED): "duplicate of the 'AQE costs almost nothing' note",
    ("This number comes from the post-processing pipeline, not from the recipe", ORANGE): "terminology ('recipe') clarity",
    ("He led this project from start to finish", BLUE): "bio style",
    ("training images of 576", PURPLE): "37,781 and 37,778 both appear in the literature",
    ("viewpoint (8 categories)", PURPLE): "minor citation of the viewpoint labels",
    ("Epochs", PURPLE): "120 epochs is from TransReID's released config, not the paper (minor)",
    ("was the first pure Vision Transformer framework", PURPLE): "'first' is commonly accepted",
    ("VehicleNet", PURPLE): "post-processing mark: sources disagree",
    ("Disabling camera and view embeddings is standard practice", PURPLE): "mild overstatement of the citation",
    ("At the default evaluation settings of its authors", PURPLE): "defaults come from the authors' code (minor)",
    ("84.5% mAP and 97.3% Rank-1 on VeRi-776", PURPLE): "value correct; only the citation could be the primary paper",
}

# AI-style phrase pass: switched off (the user does not want AI-draft / AI-style highlights)
PHRASES = []
PHRASE_NOTE = ("", "")


def matches(page, anchor):
    """search_for returns one quad per line; group the line pieces of each match together."""
    want = len(anchor.replace(" ", "")) * 0.85
    groups, cur, got = [], [], 0
    for q in page.search_for(anchor, quads=True):
        cur.append(q)
        got += len(page.get_textbox(q.rect).replace(" ", "").replace("\n", ""))
        if got >= want:
            groups.append(cur)
            cur, got = [], 0
    if cur:
        groups.append(cur)
    return groups


def add(page, quads, colour, problem, fix):
    annot = page.add_highlight_annot(quads)
    annot.set_colors(stroke=colour)
    annot.set_info(title="Review", content=f"PROBLEM: {problem}\n\nSUGGESTED FIX: {fix}")
    annot.update()


def main(src, dst):
    doc = fitz.open(src)
    missing, count = [], 0
    for item in ISSUES + REFCHECK:
        anchor, colour, problem, fix, occ = item[:5]
        ctx = item[5] if len(item) > 5 else None
        if (anchor, colour) in DROP:
            continue
        hits = []
        for page in doc:
            if ctx and ctx not in page.get_text():
                continue
            hits += [(page, g) for g in matches(page, anchor)]
        if not hits:
            missing.append(anchor)
            continue
        chosen = hits if occ == 0 else hits[occ - 1:occ]
        for page, q in chosen:
            add(page, q, colour, problem, fix)
            count += 1
    for ph in PHRASES:
        for page in doc:
            for g in matches(page, ph):
                add(page, g, YELLOW, *PHRASE_NOTE)
                count += 1

    # summary page in front
    p = doc.new_page(0, width=doc[1].rect.width, height=doc[1].rect.height)
    y = 60
    p.insert_text((50, y), "Review copy: highlighted problems and suggested fixes", fontsize=15, fontname="hebo")
    y += 22
    p.insert_text((50, y), "Hover over / click any highlight to read its note (problem + suggested fix).", fontsize=10)
    y += 26
    for colour, label in LEGEND:
        p.draw_rect(fitz.Rect(50, y - 9, 66, y + 2), color=None, fill=colour)
        p.insert_text((74, y), label, fontsize=10)
        y += 17
    y += 12
    body = (
        "Only open, real problems are highlighted. Resolved items (reference list, guidance notes, 'not peer reviewed',\n"
        "MBR4B 92.09 source: now cited to the authors' GitHub repository) and AI-draft / AI-style notes were removed.\n\n"
        "Highest-priority open items\n"
        "1. Four different Stream-1 numbers (89.97 / 89.63 / 89.06 / 89.99) attached to the same label.\n"
        "2. 'Close to defaults' (k1=80 vs default 20) and 'fits O(N^2)' (measured ~N^1.4) are false by the paper's own numbers.\n"
        "3. CityFlowV2 is cited as evidence three times but never described.\n"
        "4. Qualitative section (5.11) asserts mechanisms with no figure or measurement.\n"
        "5. Three author photos are missing (M. A. Ali, A. A. Ali, A. Hamdi).\n\n"
        "Reference-number check (purple notes)\n"
        "About 80 numbers and claims taken from cited papers were compared with the papers themselves (arXiv PDFs,\n"
        "dataset pages, the MBR4B GitHub README). Most match. Each purple note names the source paper, the table or\n"
        "section, and the exact value found there, so every note can be re-checked independently. They are findings\n"
        "to verify, not changes: nothing in the paper was changed because of them.\n\n"
        "Checked and not counted as real problems (not highlighted)\n"
        + "".join(f"- '{a[:58]}': {why}\n" for (a, _), why in DROP.items())
    )
    p.insert_textbox(fitz.Rect(50, y, p.rect.width - 40, p.rect.height - 30), body, fontsize=8.6, lineheight=1.3)

    doc.save(dst, garbage=3, deflate=True)
    print(f"annotations: {count}")
    print("NOT FOUND:", missing)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
