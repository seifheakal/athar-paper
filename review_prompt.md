# Prompt for an independent review session

Put these three files in an empty folder, open Claude Code there, and paste everything below the line as the first message:

- `main_review_highlighted.pdf` (the paper with highlighted notes; page 1 is a summary page)
- `review_notes.md` (the same notes as a plain list)
- `main_current.pdf` (the clean paper, no notes)

---

I am submitting a research paper (vehicle re-identification, VeRi-776, to The Visual Computer). A previous AI session reviewed it and left notes. I do not trust those notes blindly. Your job is to check every note independently and tell me which ones are real.

Files in this folder:
- `main_current.pdf`: the paper as it will be submitted.
- `main_review_highlighted.pdf`: the same paper with colour-coded highlights. Each highlight has a note ("PROBLEM: ... SUGGESTED FIX: ..."). Page 1 is a summary page added by the previous session; paper page N is PDF page N+1.
- `review_notes.md`: all notes as a numbered list (page, colour category, highlighted text, note).

Colour categories: RED = factual error or internal inconsistency, ORANGE = claim not supported, YELLOW = AI-draft wording / AI-style pattern, BLUE = presentation, GREEN = already fixed or check-only, PURPLE = a number or claim compared with a cited source (the note says which paper, table or section to look at).

What to do, for every numbered note in `review_notes.md`:
1. Find the highlighted passage in `main_current.pdf` and read its context (the whole paragraph, table or caption).
2. Check the claim in the note yourself:
   - For PURPLE notes and anything about a cited paper: open the primary source (the arXiv PDF, the publisher page, or the GitHub README named in the note) and find the exact table, row or sentence. Quote it.
   - For RED / ORANGE notes about the paper's own numbers: check them against the other places in the paper where the same number appears, and redo any arithmetic.
   - For YELLOW notes: you cannot check the "% copied from the AI draft" figures (the draft is not included), so say "not verifiable here" for those, and only judge whether the wording itself reads as AI-generated.
   - For BLUE notes: check the PDF.
3. Give a verdict: CONFIRMED, PARTLY RIGHT, WRONG (the note is mistaken), or CANNOT VERIFY (say why, e.g. paywalled).
4. Give the evidence: the quote, the page/table/row, and the URL you used.
5. Say what I should do: KEEP AS IS, SMALL FIX (say exactly what), or NEEDS AUTHOR DATA (something only the authors can answer, e.g. which checkpoint was used).

Rules:
- Do not edit the PDFs or create a new version of the paper. Only report.
- Do not rely on memory for any number or author list. If you cannot open the source, say CANNOT VERIFY instead of guessing.
- A number that is reported somewhere official (for example in the authors' GitHub README) is not wrong just because it is not in the paper; in that case the only question is whether the citation points to the right place. Say that clearly instead of calling the number wrong.
- Separate facts (a number in a table) from opinions (style, "reads as AI").
- Be short. One block per note.

Output: write `review_report.md` with
- a table: note number | PDF page | verdict | one-line reason,
- then one block per note with the evidence and recommended action,
- then a final section "What actually needs fixing before submission", ordered by importance, listing only CONFIRMED or PARTLY RIGHT items, with the exact change for each.

Useful tip for reading the annotations directly (Python, PyMuPDF):

```python
import fitz
doc = fitz.open("main_review_highlighted.pdf")
for page in doc:
    for a in page.annots():
        print(page.number + 1, page.get_textbox(a.rect).strip()[:80], "||", a.info["content"])
```
