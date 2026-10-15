"""Export the highlight notes of the review PDF to a markdown list.

usage: python export_notes.py <review.pdf> <out.md>
"""
import sys
import fitz

CATS = {(1.0, 0.45, 0.45): "RED factual/inconsistency", (1.0, 0.72, 0.3): "ORANGE unsupported claim",
        (0.55, 0.78, 1.0): "BLUE presentation/wording", (0.8, 0.66, 1.0): "PURPLE reference-number check"}


def category(c):
    return CATS[min(CATS, key=lambda k: sum((a - b) ** 2 for a, b in zip(k, c)))]


doc = fitz.open(sys.argv[1])
out = ["# Review notes exported from main_review_highlighted.pdf", "",
       "Page numbers are PDF pages of main_review_highlighted.pdf (page 1 is the added summary page; paper page N = PDF page N+1).",
       "Notes repeated on consecutive lines of one phrase are merged. Only open, real problems are listed;",
       "the summary page lists the notes that were checked and dropped.", ""]
seen, n, per = set(), 0, {}
for page in doc:
    for a in page.annots():
        note = a.info.get("content", "")
        if (page.number, note) in seen:
            continue
        seen.add((page.number, note))
        n += 1
        cat = category(a.colors["stroke"])
        per[cat] = per.get(cat, 0) + 1
        text = " ".join(page.get_textbox(a.rect).split())[:160]
        out += [f"## {n}. PDF page {page.number + 1} | {cat}", f"- Highlighted text: \"{text}\"",
                "- " + note.replace("\n\n", "\n- "), ""]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
print("notes exported:", n, per)
