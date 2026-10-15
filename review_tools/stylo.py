"""Stylometric pass over the paper units vs the original AI draft.

usage: python stylo.py <paper_dir>
"""
import re, sys, statistics as st
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1])

ENVS = r"(table\*?|figure\*?|equation\*?|tabular|wrapfigure|align\*?|thebibliography)"


def prose(tex: str) -> str:
    tex = re.sub(r"(?<!\\)%.*", "", tex)                      # comments
    tex = re.sub(r"\\begin\{" + ENVS + r"\}.*?\\end\{\1\}", " ", tex, flags=re.S)
    tex = re.sub(r"\\(cite|ref|label|eqref|url|includegraphics|footnotetext)\*?(\[[^\]]*\])?\{[^}]*\}", "", tex)
    tex = re.sub(r"\\footnote\{", " ", tex)
    tex = re.sub(r"\$[^$]*\$", " X ", tex)                    # inline math
    tex = re.sub(r"\\(textbf|emph|textit|texttt|subsection|subsubsection|section|paragraph)\*?\{", "", tex)
    tex = re.sub(r"\\item", " ", tex)
    tex = re.sub(r"\\[a-zA-Z]+\*?", " ", tex)                 # other commands
    tex = tex.replace("~", " ").replace("{", "").replace("}", "")
    tex = re.sub(r"\\.", " ", tex)
    return re.sub(r"\s+", " ", tex).strip()


ABBR = ["e.g.", "i.e.", "vs.", "et al.", "Fig.", "Sect.", "Eq.", "approx.", "rand.", "Gauss.", "Proc."]


def sentences(p: str):
    for a in ABBR:
        p = p.replace(a, a.replace(".", "<D>"))
    p = re.sub(r"(\d)\.(\d)", r"\1<D>\2", p)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", p)
    return [s.replace("<D>", ".").strip() for s in parts if len(s.split()) >= 2]


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", s.lower())


def ngrams(ws, n=5):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


TELLS = {
    # classic LLM vocabulary
    "classic": r"\b(notably|crucially|importantly|furthermore|moreover|comprehensive|robust(ly)?|rigorous(ly)?|holistic|delve|leverag\w*|underscore\w*|pivotal|crucial|landscape|seamless(ly)?|intricate|nuanced|showcase\w*|it is worth noting|in summary|plays? an? \w+ role|paramount|meticulous\w*|fully specified)\b",
    # negation / contrast pairs
    "contrast": r"\b(rather than|not only|merely|instead of|not as an?|not from|not a\b|, not )",
    # candour / over-disclosure register typical of recent assistants
    "candour": r"\b(honest\w*|to be clear|we want to be clear|state it openly|we say so|for transparency|genuine\w*|deliberately|we do not claim|faithful|concrete|first-order|statistically solid|in a more honest light)\b",
    # self-confirming wrap-ups
    "confirm": r"\b(this confirms|which confirms|this suggests|this supports|this shows|this fits|which fits)\b",
}


def stats(text):
    ss = sentences(text)
    lens = [len(words(s)) for s in ss]
    ws = words(text)
    openers = Counter(words(s)[0] for s in ss if words(s))
    out = dict(
        words=len(ws), sents=len(ss),
        mean=st.mean(lens) if lens else 0,
        sd=st.pstdev(lens) if len(lens) > 1 else 0,
        ttr=len(set(ws[:300])) / max(1, min(300, len(ws))),
        openers=openers,
        lens=lens,
    )
    out["cv"] = out["sd"] / out["mean"] if out["mean"] else 0
    for k, pat in TELLS.items():
        out[k] = len(re.findall(pat, text, flags=re.I))
    return out


draft_txt = prose((root / "original" / "main_ai_draft.tex").read_text(encoding="utf-8"))
draft_ws = words(draft_txt)
draft_grams = ngrams(draft_ws)

units = sorted((root / "sections").glob("*.tex"))
rows = []
all_text = []
for u in units:
    raw = u.read_text(encoding="utf-8")
    status = re.search(r"% Status: (\S+)", raw)
    if u.name.startswith(("43_", "44_")):
        continue
    p = prose(raw)
    all_text.append(p)
    s = stats(p)
    g = ngrams(words(p))
    s["overlap"] = len(g & draft_grams) / max(1, len(g))
    s["status"] = status.group(1) if status else "?"
    rows.append((u.stem, s))

print(f"{'unit':28} {'status':10} {'words':>5} {'sent':>4} {'mean':>5} {'sd':>5} {'cv':>4} {'5g-overlap':>10} cls con cand conf")
for name, s in rows:
    print(f"{name:28} {s['status']:10} {s['words']:5} {s['sents']:4} {s['mean']:5.1f} {s['sd']:5.1f} {s['cv']:4.2f} {s['overlap']:10.0%} {s['classic']:3} {s['contrast']:3} {s['candour']:4} {s['confirm']:4}")

cur = " ".join(all_text)
S, D = stats(cur), stats(draft_txt)
print("\n=== whole paper (prose only, no refs) vs original AI draft ===")
for k in ["words", "sents", "mean", "sd", "cv", "classic", "contrast", "candour", "confirm"]:
    a, b = S[k], D[k]
    if k in ("classic", "contrast", "candour", "confirm"):
        print(f"{k:8} current {a:5} ({1000*a/S['words']:.1f}/1k words)   draft {b:5} ({1000*b/D['words']:.1f}/1k words)")
    else:
        print(f"{k:8} current {a:8.2f}   draft {b:8.2f}")
cg = ngrams(words(cur))
print(f"5-gram overlap of current paper with draft: {len(cg & draft_grams)/len(cg):.0%}")
# 8-gram verbatim runs
c8, d8 = ngrams(words(cur), 8), ngrams(draft_ws, 8)
print(f"8-gram overlap (verbatim phrasing):        {len(c8 & d8)/len(c8):.0%}")

print("\nsentence length distribution (current): ", Counter(min(l // 5 * 5, 40) for l in S["lens"]).most_common())
print("sentence length distribution (draft):   ", Counter(min(l // 5 * 5, 40) for l in D["lens"]).most_common())
tot = sum(S["openers"].values())
print("\ntop sentence openers (current):", [(w, f"{c/tot:.0%}") for w, c in S["openers"].most_common(12)])
tot = sum(D["openers"].values())
print("top sentence openers (draft):  ", [(w, f"{c/tot:.0%}") for w, c in D["openers"].most_common(12)])

print("\n=== tell-phrase hits in current text ===")
for k, pat in TELLS.items():
    hits = Counter(m.group(0).lower() for m in re.finditer(pat, cur, flags=re.I))
    print(k, hits.most_common(25))

for phrase in ["This confirms", "So ", "This is ", "We also ", "But ", "It is ", "This gives", "pp"]:
    print(f"{phrase!r:14} {cur.count(phrase)}")
