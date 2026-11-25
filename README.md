# Sum up 24 November's world news in one image

Entry for the make.fun bounty
**“Sum up 24 November's world news in one image”**
<https://make.fun/bounty/news-image-20261124>

- $100 reward, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each,
  11th–50th $1.20 each). $100 USDC in escrow on Solana.
- Ends **Thu 26 Nov 2026, 00:00 UTC** (03:30 Tehran).
- An AI judge that can see images compares entries two at a time and picks
  the one that best sums up the day's world news; entries rank by win rate.
  The judge has no news feed — the image itself must carry the news.

## What it does

`main.py` is a self-contained Python 3 program (Pillow only, no network,
no randomness, no current time). It draws a newspaper-style front page and
writes one image:

- `output/entry.png` — 1024 × 1024 PNG, ~135 KB (limit: 1 MiB, 1024 × 1024)
- also `/output/entry.png` when that directory is writable (the path the
  bounty runner expects)

The image sums up **Tuesday 24 November 2026** in 7 stories:

| # | Story |
|---|-------|
| 1 | **Nvidia brings back Jensen Huang as CEO** — board reinstates him unanimously days after his resignation; shares jump ~30%; Trump says he persuaded the board. |
| 2 | **Ukraine hits a Russian warship in Libya** — naval drones strike at a base in Libya; Kyiv calls it self-defence. |
| 3 | **Russian strike kills 2 in Zaporizhzhia** — overnight attack on an apartment block; about 40 wounded, including four children. |
| 4 | **Tensions rise over the U.S. naval blockade** — Vance and Rubio meet Qatar's PM; Iran vows to confront the blockade; three tankers hit mines in Hormuz. |
| 5 | **Israeli strike kills Hamas security chief** — Naeem Abu Nahel, director of Hamas' internal security, killed with six others, medics say. |
| 6 | **COP31 ends with no deal in Antalya** — first climate summit since 2009 to fail; split over fossil fuels and finance; UN chief António Guterres "deeply disappointed". (Talks closed Sun 22 Nov; reported 24 Nov.) |
| 7 | **Bus crash kills 13 in Ras Al Khaimah, UAE** — bus carrying 41 hits a broken-down truck on Al Watan Road; 14 injured; toll rose from 11 to 13. |

## News sources (all reported 24 Nov 2026)

- Just Security, “Early Edition: November 24, 2026” —
  <https://www.justsecurity.org/165763/early-edition-november-24-2026/>
  (stories 2–5, incl. AP reporting on the Qatar meetings and Gaza)
- UN News, “COP31 ends without climate pact…” —
  <https://news.un.org/en/story/2026/11/1168855> and Reuters, “COP31 was a flop.
  What now?” — <https://www.reuters.com/sustainability/cop31-was-flop-what-now-2026-11-24/>
- Reuters / Khaleej Times / Gulf News via Gulf Business, “Death toll rises to 13
  in Ras Al Khaimah bus-truck collision” —
  <https://gulfbusiness.com/en/2026/uae/uae-11-killed-in-bus-truck-collision-in-ras-al-khaimah-ministry-of-interior-confirms/>
- CWEB Daily Shocker News Headlines, 24 Nov 2026 (Nvidia reinstatement,
  markets rebound, Libya strike, Zaporizhzhia toll) and Medium / All Voices
  News, “Global and U.S. Strategic News Brief: November 24, 2026” —
  <https://medium.com/all-voices-news/global-and-u-s-strategic-news-brief-november-24-2026-d22ad6d00284>

No story was invented: every headline and figure above appears in at least
one of these sources, and the two single-source items (COP31, UAE crash)
were corroborated by a second search round (Smithsonian / UN News / Reuters
for COP31; Reuters, Khaleej Times, Gulf News, Indian Consulate in Dubai
for the UAE crash).

## How to run

```bash
python3 main.py
# writes output/entry.png (and /output/entry.png if writable)
```

Requires Python 3 with Pillow (`pip install pillow`). Uses only the
DejaVu fonts shipped with the system (`/usr/share/fonts/truetype/dejavu`),
falling back to Pillow's default font if they are absent.

## Verification (done 25 Nov 2026, ~06:30 Tehran)

- Ran `python3 main.py` twice: both runs wrote byte-identical PNGs
  (`cmp` clean). SHA-256:
  `b349a873868a4ad1fd38e2c1ebb15d8e8f67466acad1b02bba9a65b2d204703d`
- Output checked: 1024 × 1024 PNG, 134,533 bytes (< 1 MiB limit).
- Image visually inspected: masthead, lead story, all 7 numbered cards and
  the source footer are legible, with no overlapping or clipped text.

## What is still missing to submit (NOT done)

- **GitHub repo:** create a public repo owned by @kalidefi, created after the
  competition opened, under an OSI-approved license (MIT `LICENSE` included
  here), with `main.py` in its root.
- **Agent transcripts:** upload the transcripts of the sessions that built
  this entry with the submission.
- **Linking:** GitHub and X must be linked on make.fun (as of 24 Nov they
  were not linked for this account).
- **Submission + wallet signature:** submit via make.fun before the deadline
  (Thu 26 Nov 2026, 00:00 UTC / 03:30 Tehran) and sign with the linked
  Solana wallet (BvNG…R8hv). No submission, signature, posting, funding,
  or account linking was done while building this entry.
