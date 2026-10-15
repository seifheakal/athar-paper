# Handoff: paper review state (15 Oct 2026)

Read this first when the user says "continue the handoff".

## How the user wants to work (important)
- **Change only what the user explicitly asks for.** Earlier, edits beyond the request (consistency fixes, table redesigns) were unwanted and were reverted. When in doubt, ask.
- **Show each change (before/after) and wait for approval before editing the paper.**
- Never "fix" a number just because a note says so; the review notes are findings to verify, not instructions.
- Commit only when asked; one clear commit per request. Push only when asked.

## What has been done (all on `main`)
| Commit | What |
|---|---|
| `1e648d1` | Reference list (units 43-44) corrected and verified: all 29 DOIs + 7 arXiv IDs resolve to the right paper/first author. 10 wrong author lists fixed; CLIP-SENet -> IEEE T-ITS 2026, VAPC -> IEEE T-ITS 2022, FastReID -> ACM MM 2023, DINOv2 -> TMLR 2024; pages/DOIs added. Related in-text fixes in units 05, 06, 08, 20 (Yi et al. survey name, Ye survey is person-only, Zhang et al. method description, venue labels). |
| `b550d11` + revert `ecd4587` | Consistency fixes: **reverted at the user's request**. Do not re-apply unless asked. |
| `7e9e2ac` | `main.tex`: removed the two visible guidance notes (ORCID "to be supplied", photo instruction); added an empty paragraph so Seif's wrapfigure photo still renders after the "Author Biographies" heading. |
| `0ee90e3` + revert `a146b72` | Tables 6/7 redesign: **reverted at the user's request** (it duplicated Table 9). |
| `016d6a1` | Unit 04: dropped "not peer reviewed" for CLIP-SENet (it is published in T-ITS now). |

Net change vs. the user's original text: references + related in-text citation fixes, guidance notes removed, unit 04 peer-review clause.

## Review material (repo root)
- `main_current.pdf`: current paper (built from the sources at `016d6a1`).
- `main_review_highlighted.pdf`: same paper with 101 colour-coded highlight notes (page 1 = summary page). Colours: RED factual/inconsistency, ORANGE unsupported claim, YELLOW AI-draft/AI-style, BLUE presentation, GREEN fixed/check-only, PURPLE reference-number check (each note names the source paper + table/section).
- `review_notes.md`: the 95 distinct notes as a numbered list.
- `review_prompt.md`: prompt the user runs in a separate account/session to verify every note independently; it should produce `review_report.md`.

**Next step the user planned:** run `review_prompt.md` in a fresh session, get `review_report.md`, then decide here which confirmed items to fix (show each change first).

## Key open findings (unverified by the user; see the notes for evidence)
- AI-writing: ~32% of 8-word sequences still verbatim from `original/main_ai_draft.tex`; abstract, intro (units 02-04), statements and bios 46-49 are mostly the draft; units 05-41 mainly sentence-split. 0/49 units reviewed per CHECKLIST.md.
- Internal: four Stream-1 numbers on one label (89.97 / 89.63 / 89.06 / 89.99, the user said 89.99 is a typo for 89.97); "close to defaults" (k1=80 vs Zhong default 20); "fits O(N^2)" vs measured ~N^1.4; seed SD is population (0.55) not sample (0.68); CityFlowV2 cited but never described; unit 33 qualitative claims without evidence; unit 29 82.30 vs 82.22 (source unknown); dense re-rank 50 s vs 44 s (unknown).
- Reference numbers (purple notes): Table 7 TransReID ViT-B R1 is 96.9 not 97.0; RPTM 88.0 is with re-ranking (Table 6 marks it without); MBR4B 92.09 is from the authors' GitHub README with re-ranking (paper itself: 85.63), so cite the repo too (the number is fine); MBR4B "LAI" = Leveraging Additional Information; CLIP-SENet's 92.9 model uses ResNeXt101-IBN (ResNet101-IBN variant 91.9/98.2); CLIP-SENet's T-ITS Table I lists CLIP-ReID (ViT) at 91.7 mAP, contradicting "no pure ViT-B above 90%"; VehicleNet / Strong Baseline descriptions; Ye survey cited for SupCon and vehicle numbers; 37,781 vs 37,778 training images.
- Rank-1 for the re-evaluated TransReID / CLIP-ReID checkpoints (91.12 / 91.80) is not recorded anywhere in the paper.

## How to rebuild
- Paper: `pdflatex main && pdflatex main` (MiKTeX). Build into a temp folder (`-output-directory`) to avoid overwriting `main.pdf` unless the user wants that. One known pre-existing overfull box in the VeRi-Wild table (unit 29).
- Highlighted PDF: `python review_tools/annotate.py main_current.pdf main_review_highlighted.pdf` (needs PyMuPDF). It reports any anchor text it cannot find; anchors must match the PDF text.
- `review_tools/stylo.py <repo>`: AI-draft overlap / sentence statistics vs `original/main_ai_draft.tex`.
- `review_tools/crossref.py [keys]`: Crossref metadata for each reference.
- `review_tools/findnums.py <paper>`: searches cited papers' text for numbers; it expects `review_tools/papers/<name>.txt`. The PDFs are not committed; re-download from arXiv (TransReID 2102.04378, CLIP-ReID 2211.13977, PVEN 2004.05021, CAL 2108.08728, VehicleNet 2004.06305, HPGN 2005.14684, Strong Baseline 2104.10850, RPTM 2110.07933, MBR4B 2310.01129, CLIP-SENet 2502.16815, VAPC 2011.09099, CA-Jaccard 2311.10605, Ben Mabrouk 2606.01981, ViT 2010.11929) and extract text with PyMuPDF.
