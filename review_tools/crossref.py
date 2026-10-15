"""Look up each reference title on Crossref and print authoritative metadata."""
import json, sys, urllib.parse, urllib.request, time

TITLES = {
    "he2021transreid": "TransReID: Transformer-based Object Re-Identification",
    "radford2021clip": "Learning Transferable Visual Models From Natural Language Supervision",
    "zhong2017rerank": "Re-ranking Person Re-identification with k-reciprocal Encoding",
    "liu2016veri": "Large-scale vehicle re-identification in urban surveillance videos",
    "liu2018provid": "PROVID: Progressive and Multimodal Vehicle Reidentification for Large-Scale Urban Surveillance",
    "dosovitskiy2021vit": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
    "li2023clipreid": "CLIP-ReID: Exploiting Vision-Language Model for Image Re-identification without Concrete Text Labels",
    "shen2022hpgn": "Exploring Spatial Significance via Hybrid Pyramidal Graph Network for Vehicle Re-Identification",
    "luo2023mbr4b": "Strength in Diversity: Multi-Branch Representation Learning for Vehicle Re-Identification",
    "ye2022survey": "Deep Learning for Person Re-Identification: A Survey and Outlook",
    "li2024vehiclereidsurvey": "Advances in vehicle re-identification techniques: A survey",
    "zhou2018vami": "Viewpoint-Aware Attentive Multi-view Inference for Vehicle Re-identification",
    "meng2020pven": "Parsing-Based View-Aware Embedding Network for Vehicle Re-Identification",
    "rao2021cal": "Counterfactual Attention Learning for Fine-Grained Visual Categorization and Re-identification",
    "zheng2020vehiclenet": "VehicleNet: Learning Robust Visual Representation for Vehicle Re-Identification",
    "cybercore2021strong": "A Strong Baseline for Vehicle Re-Identification",
    "khorramshahi2023selfsupervision": "Robust and Scalable Vehicle Re-Identification via Self-Supervision",
    "loshchilov2019adamw": "Decoupled Weight Decay Regularization",
    "holla2024msfft": "MSFFT: Multi-Scale Feature Fusion Transformer for cross platform vehicle re-identification",
    "kuang2025mikecoco": "Unity in Diversity: Multi-expert Knowledge Confrontation and Collaboration for Generalizable Vehicle Re-identification",
    "ghosh2023rptm": "Relation Preserving Triplet Mining for Stabilising the Triplet Loss in Re-identification Systems",
    "wang2020fastreid": "FastReID: A Pytorch Toolbox for General Instance Re-identification",
    "deng2018spgan": "Image-Image Domain Adaptation with Preserved Self-Similarity and Domain-Dissimilarity for Person Re-identification",
    "zhong2019ecn": "Invariance Matters: Exemplar Memory for Domain Adaptive Person Re-Identification",
    "song2020udap": "Unsupervised domain adaptive re-identification: Theory and practice",
    "zheng2020vapc": "Viewpoint-aware Progressive Clustering for Unsupervised Vehicle Re-identification",
    "benmabrouk2026genlimits": "Generalization Limits in Vehicle Re-Identification",
    "zhang2022vehiclererank": "Re-ranking vehicle re-identification with orientation-guide query expansion",
    "moral2023syntheticrerank": "Enhancing vehicle re-identification via synthetic training datasets and re-ranking based on video-clips information",
    "arandjelovic2012aqe": "Three things everyone should know to improve object retrieval",
    "khosla2020supcon": "Supervised Contrastive Learning",
    "pan2018ibn": "Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net",
    "lou2019veriwild": "VERI-Wild: A Large Dataset and a New Method for Vehicle Re-Identification in the Wild",
    "oquab2023dinov2": "DINOv2: Learning Robust Visual Features without Supervision",
    "clipsenet_pub": "CLIP-SENet: CLIP-based Semantic Enhancement Network for Vehicle Re-identification",
    "chen2024cajaccard": "CA-Jaccard: Camera-aware Jaccard Distance for Person Re-identification",
}

keys = sys.argv[1:] or list(TITLES)
for key in keys:
    title = TITLES[key]
    q = urllib.parse.urlencode({"query.bibliographic": title, "rows": 3,
                                "select": "DOI,title,author,container-title,volume,issue,page,article-number,published,type"})
    req = urllib.request.Request("https://api.crossref.org/works?" + q,
                                 headers={"User-Agent": "ref-check/0.1"})
    try:
        items = json.load(urllib.request.urlopen(req, timeout=30))["message"]["items"]
    except Exception as e:
        print(f"== {key}: ERROR {e}")
        continue
    print(f"== {key}")
    for it in items:
        t = (it.get("title") or [""])[0]
        if not t:
            continue
        auth = ", ".join(f"{a.get('family','')} {a.get('given','')}".strip() for a in it.get("author", []))
        yr = it.get("published", {}).get("date-parts", [[None]])[0][0]
        print(f"   [{it.get('type')}] {t}")
        print(f"      authors: {auth}")
        print(f"      in: {(it.get('container-title') or [''])[0]} vol={it.get('volume')} iss={it.get('issue')} "
              f"pp={it.get('page')} art={it.get('article-number')} year={yr} doi={it.get('DOI')}")
    time.sleep(2.5)
