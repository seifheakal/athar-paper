"""Print the context around each searched term in each cited paper's text."""
import re, sys
from pathlib import Path

D = Path(__file__).parent / "papers"
CHECKS = {
    "transreid": ["82.3", "97.1", "80.6", "96.9", "0.008", "momentum", "256", "120 epoch", "batch size", "16 identities",
                  "VAMI", "PVEN", "50.1", "53.4", "SIE", "JPM", "k = 4", "groups"],
    "clipreid": ["84.5", "97.3", "VeRi"],
    "pven": ["79.5", "95.6", "VAMI", "50.13", "53.42", "PROVID"],
    "cal": ["74.3", "95.4", "VeRi"],
    "vehiclenet": ["83.41", "96.78", "re-rank", "synthetic", "VehicleID"],
    "hpgn": ["80.18", "96.72", "VAMI", "PROVID"],
    "strong": ["87.1", "VeRi", "IBN", "101", "attention"],
    "rptm": ["88.0", "97.3", "VeRi"],
    "clipsenet": ["92.9", "98.7", "512", "TinyCLIP", "89.1", "97.9", "85.2", "79.5", "95.4", "re-rank", "320"],
    "vapc": ["VeRi-Wild", "SPGAN", "UDAP", "ECN", "24.1", "30.0", "34.7", "37.7", "39.7", "Direct", "13,164", "13164"],
    "cajaccard": ["k1", "λ", "intra", "inter", "default"],
    "vit": ["86M", "304M", "307M", "17.6"],
}

only = sys.argv[1:] or CHECKS
for paper in only:
    text = re.sub(r"\s+", " ", (D / f"{paper}.txt").read_text(encoding="utf-8"))
    print(f"\n######## {paper} ########")
    for term in CHECKS[paper]:
        hits = [m.start() for m in re.finditer(re.escape(term), text)]
        print(f"-- '{term}': {len(hits)} hits")
        for h in hits[:3]:
            print("     ..." + text[max(0, h - 130):h + 110] + "...")
