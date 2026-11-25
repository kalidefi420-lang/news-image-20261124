#!/usr/bin/env python3
"""
Sum up 24 November 2026's world news in one image.
Entry for make.fun bounty: https://make.fun/bounty/news-image-20261124

Writes a deterministic 1024x1024 PNG to /output/entry.png (the path the
bounty runner expects) and also to output/entry.png next to this script,
so the result can be inspected locally. No network access, no randomness,
no current time: both runs produce identical bytes.

Run:  python3 main.py
Requires: Pillow (PIL). Standard library otherwise.
"""
import hashlib
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# --- palette ---
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (16, 42, 67)
TEAL = (0, 110, 110)
AMBER = (176, 110, 0)
GREEN = (34, 120, 60)
PURPLE = (90, 60, 140)
SLATE = (70, 80, 90)
CARD = (255, 255, 255)
LINE = (200, 192, 175)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    p = os.path.join(FONT_DIR, name)
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    return ImageFont.load_default()


F_TITLE = font("DejaVuSerif-Bold.ttf", 46)
F_SUB = font("DejaVuSans-Bold.ttf", 20)
F_TAG = font("DejaVuSans-Bold.ttf", 17)
F_HEAD = font("DejaVuSans-Bold.ttf", 24)
F_HEAD_SM = font("DejaVuSans-Bold.ttf", 22)
F_BODY = font("DejaVuSans.ttf", 19)
F_BODY_SM = font("DejaVuSans.ttf", 18)
F_FOOT = font("DejaVuSans.ttf", 15)
F_NUM = font("DejaVuSans-Bold.ttf", 26)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_card(draw, x, y, w, h, num, colour, tag, headline, body, head_font=F_HEAD):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                           outline=LINE, width=1)
    # number badge
    cx, cy, r = x + 30, y + 30, 17
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour)
    tw = draw.textlength(str(num), font=F_NUM)
    draw.text((cx - tw / 2, cy - 14), str(num), font=F_NUM, fill=(255, 255, 255))
    draw.text((x + 56, y + 18), tag, font=F_TAG, fill=colour)
    lines = wrap(draw, headline, head_font, w - 32)
    ly = y + 52
    for ln in lines[:2]:
        draw.text((x + 16, ly), ln, font=head_font, fill=INK)
        ly += 28
    blines = wrap(draw, body, F_BODY_SM, w - 32)
    for ln in blines[:3]:
        draw.text((x + 16, ly + 4), ln, font=F_BODY_SM, fill=(50, 50, 50))
        ly += 23


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 118], fill=INK)
    d.text((32, 14), "THE WORLD IN ONE DAY", font=F_SUB, fill=(255, 210, 90))
    d.text((32, 48), "24 NOVEMBER 2026", font=F_TITLE, fill=(255, 255, 255))
    d.text((800, 30), "TUESDAY", font=F_SUB, fill=(255, 255, 255))
    d.text((800, 58), "WORLD NEWS", font=F_SUB, fill=(200, 200, 200))
    d.rectangle([0, 118, W, 124], fill=RED)

    # ---- lead story: Nvidia (dark panel) ----
    d.rounded_rectangle([24, 140, 1000, 348], radius=12, fill=NAVY)
    d.text((48, 156), "1  •  LEAD STORY — MARKETS / TECH", font=F_TAG, fill=(120, 220, 130))
    d.text((48, 182), "NVIDIA BRINGS BACK", font=font("DejaVuSans-Bold.ttf", 40), fill=(255, 255, 255))
    d.text((48, 226), "JENSEN HUANG AS CEO", font=font("DejaVuSans-Bold.ttf", 40), fill=(255, 255, 255))
    d.text((48, 278), "Board reinstates him unanimously, days after his",
           font=F_BODY, fill=(220, 230, 240))
    d.text((48, 300), "resignation; shares jump about 30%.",
           font=F_BODY, fill=(220, 230, 240))
    d.text((48, 322), "Trump says he persuaded the board.",
           font=F_BODY, fill=(220, 230, 240))
    # right-hand stat box
    d.rounded_rectangle([700, 168, 976, 324], radius=10, fill=(255, 255, 255))
    d.text((724, 184), "SHARES", font=F_TAG, fill=GREEN)
    d.text((724, 206), "+~30%", font=font("DejaVuSans-Bold.ttf", 52), fill=GREEN)
    d.text((724, 268), "after the board vote;\nmarkets rebound.",
           font=F_BODY_SM, fill=(50, 50, 50))

    # ---- six more stories, 2 columns x 3 rows ----
    stories = [
        (2, RED, "WAR IN UKRAINE",
         "Ukraine hits Russian warship in Libya",
         "Naval drones strike a Russian warship at a base in Libya. Kyiv calls it self-defence."),
        (3, AMBER, "WAR IN UKRAINE",
         "Russian strike kills 2 in Zaporizhzhia",
         "Overnight attack hits an apartment block; about 40 wounded, including four children."),
        (4, TEAL, "IRAN / U.S.",
         "Tensions rise over U.S. naval blockade",
         "Vance and Rubio meet Qatar's PM; Iran vows to confront the blockade as tankers hit mines in Hormuz."),
        (5, PURPLE, "GAZA",
         "Israeli strike kills Hamas security chief",
         "Naeem Abu Nahel, director of Hamas' internal security, killed with six others, medics say."),
        (6, GREEN, "CLIMATE — COP31",
         "COP31 ends with no deal in Antalya",
         "First climate summit since 2009 to fail: split over fossil fuels and finance. UN chief 'deeply disappointed'."),
        (7, SLATE, "UAE",
         "Bus crash kills 13 in Ras Al Khaimah",
         "Bus carrying 41 hits a broken-down truck on Al Watan Road; 14 injured. Toll rose from 11 to 13."),
    ]
    cw, ch, gx, gy = 476, 188, 24, 16
    x0, y0 = 24, 364
    for i, (num, colour, tag, head, body) in enumerate(stories):
        x = x0 + (i % 2) * (cw + gx)
        y = y0 + (i // 2) * (ch + gy)
        draw_card(d, x, y, cw, ch, num, colour, tag, head, body,
                  head_font=F_HEAD_SM)

    # ---- footer ----
    fy = 972
    d.line([24, fy - 8, 1000, fy - 8], fill=LINE, width=1)
    d.text((24, fy + 2),
           "Sources (all reported 24 Nov 2026): Just Security Early Edition; UN News & Reuters (COP31);",
           font=F_FOOT, fill=(90, 90, 90))
    d.text((24, fy + 22),
           "Reuters / Khaleej Times / Gulf News (UAE crash); AP via Just Security; CWEB daily brief.",
           font=F_FOOT, fill=(90, 90, 90))
    return img


def main():
    img = build()
    here = Path(__file__).resolve().parent
    targets = [Path("/output/entry.png"), here / "output" / "entry.png"]
    written = []
    for t in targets:
        try:
            t.parent.mkdir(parents=True, exist_ok=True)
            img.save(t, format="PNG", optimize=True)
            written.append(t)
        except OSError as e:
            print(f"warning: could not write {t}: {e}", file=sys.stderr)
    if not written:
        sys.exit("failed to write any output image")
    data = written[0].read_bytes()
    print(f"wrote {written[0]} ({len(data)} bytes, {W}x{H})")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    for t in written[1:]:
        print(f"also wrote {t}")


if __name__ == "__main__":
    main()
