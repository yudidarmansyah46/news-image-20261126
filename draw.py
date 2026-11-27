"""Draw the front page for Thursday 26 November 2026.

A Pillow program for the news-image-20261126 bounty. It paints a
newspaper front page, THE WORLD TODAY, with the day's lead story
(a fuel tanker fire on Cairo's Ring Road) and six more stories
from around the world, and saves it as entry.png: 1024 by 1024
pixels, RGB, under 1 MiB.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
PAPER = (248, 243, 230)
CARD = (255, 253, 246)
INK = (24, 24, 24)
RED = (176, 32, 32)
NAVY = (30, 58, 96)
GREY = (100, 94, 82)
SKY = (38, 44, 66)
ORANGE = (238, 118, 34)
GOLD = (244, 178, 62)

FONTS = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONTS + name, size)


def wrap(draw, text, face, width):
    """Break text into lines that fit width in pixels."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if draw.textlength(trial, font=face) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_fire_scene(d, x0, y0, x1, y1):
    """Night scene: a burning tanker on a highway, flames and smoke."""
    d.rectangle([x0, y0, x1, y1], fill=SKY)
    d.ellipse([x1 - 52, y0 + 8, x1 - 16, y0 + 44], fill=(226, 214, 180))
    # distant skyline
    for bx, bw, bh in ((x0 + 12, 34, 46), (x0 + 52, 26, 64),
                       (x0 + 84, 40, 38), (x0 + 130, 24, 56)):
        d.rectangle([bx, y1 - 96 - bh, bx + bw, y1 - 96], fill=(52, 58, 84))
    # road
    d.rectangle([x0, y1 - 96, x1, y1], fill=(44, 44, 48))
    d.rectangle([x0, y1 - 52, x1, y1 - 48], fill=(240, 210, 90))
    # tanker truck silhouette, kept inside the panel
    tx, ty = x0 + 26, y1 - 120
    d.rectangle([tx, ty, tx + 150, ty + 42], fill=(200, 200, 196))
    d.rectangle([tx + 150, ty + 12, tx + 186, ty + 42], fill=(176, 32, 32))
    d.ellipse([tx + 18, ty + 42, tx + 44, ty + 68], fill=(16, 16, 16))
    d.ellipse([tx + 118, ty + 42, tx + 144, ty + 68], fill=(16, 16, 16))
    d.ellipse([tx + 158, ty + 42, tx + 182, ty + 68], fill=(16, 16, 16))
    # flames rising from the tank, all inside the panel
    for cx, cy, r, col in ((tx + 45, ty - 24, 26, ORANGE),
                           (tx + 82, ty - 38, 32, (244, 84, 20)),
                           (tx + 118, ty - 22, 22, GOLD),
                           (tx + 82, ty - 20, 15, (255, 226, 120))):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    # smoke puffs, small and inside the panel
    for sx, sy, r in ((tx + 40, ty - 58, 10), (tx + 82, ty - 66, 12),
                      (tx + 118, ty - 56, 9)):
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(120, 118, 112))
    # charred car at the edge
    d.rectangle([x1 - 78, y1 - 128, x1 - 18, y1 - 100], fill=(20, 20, 22))
    d.rectangle([x1, y0, x1, y1], fill=INK)
    d.rectangle([x0, y0, x1, y1], outline=INK, width=2)


def draw_card(d, px, py, pw, ph, number, tag, head, body):
    d.rectangle([px, py, px + pw, py + ph], fill=CARD, outline=INK, width=1)
    d.rectangle([px, py, px + 5, py + ph], fill=RED)
    d.ellipse([px + 18, py + 14, px + 52, py + 48], fill=NAVY)
    d.text((px + 35, py + 31), str(number),
           font=font("DejaVuSans-Bold.ttf", 20), fill=(255, 255, 255),
           anchor="mm")
    tx = px + 64
    d.text((tx, py + 15), tag, font=font("DejaVuSans-Bold.ttf", 13),
           fill=RED)
    head_lines = wrap(d, head, font("DejaVuSerif-Bold.ttf", 19), pw - 80)
    hy = py + 36
    for line in head_lines[:2]:
        d.text((tx, hy), line, font=font("DejaVuSerif-Bold.ttf", 19),
               fill=INK)
        hy += 23
    body_lines = wrap(d, body, font("DejaVuSans.ttf", 14), pw - 80)
    by = hy + 3
    for line in body_lines[:2]:
        d.text((tx, by), line, font=font("DejaVuSans.ttf", 14),
               fill=(44, 44, 44))
        by += 18


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)

    d.rectangle([12, 12, W - 13, H - 13], outline=INK, width=3)
    d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

    # Masthead
    d.text((W // 2, 92), "THE WORLD TODAY",
           font=font("DejaVuSerif-Bold.ttf", 72), fill=INK, anchor="mm")
    d.line([34, 136, W - 34, 136], fill=INK, width=3)
    d.text((W // 2, 158), "THURSDAY, 26 NOVEMBER 2026",
           font=font("DejaVuSans-Bold.ttf", 28), fill=RED, anchor="mm")
    d.text((W // 2, 182), "ONE DAY'S WORLD NEWS IN ONE PAGE",
           font=font("DejaVuSans.ttf", 15), fill=GREY, anchor="mm")
    d.line([34, 196, W - 34, 196], fill=INK, width=2)

    # Lead story
    d.text((34, 212), "LEAD STORY  —  CAIRO, EGYPT",
           font=font("DejaVuSans-Bold.ttf", 17), fill=RED)
    headline = ["TANKER FIRE KILLS 31", "ON CAIRO RING ROAD"]
    y = 238
    for line in headline:
        d.text((34, y), line, font=font("DejaVuSerif-Bold.ttf", 44),
               fill=INK)
        y += 52
    deck = ("A fuel tanker overturns and explodes in Giza, "
            "engulfing cars in flames. At least 31 people are "
            "killed and 21 injured in the overnight blaze.")
    deck_lines = wrap(d, deck, font("DejaVuSans.ttf", 20), 600)
    y = 350
    for line in deck_lines:
        d.text((34, y), line, font=font("DejaVuSans.ttf", 20), fill=INK)
        y += 27
    draw_fire_scene(d, 668, 238, 990, 438)
    d.text((829, 448), "Flames from the tanker on the Ring Road",
           font=font("DejaVuSans.ttf", 13), fill=GREY, anchor="mm")
    d.line([34, 478, W - 34, 478], fill=INK, width=2)

    # Six numbered stories
    stories = [
        ("THE GULF",
         "Two tankers hit mines in Hormuz",
         "Iran's Guard says two tankers, one a supertanker "
         "with over 2m barrels, hit sea mines near Khasab."),
        ("UKRAINE",
         "Missiles hit Kyiv mall, 7 hurt",
         "Ballistic missiles strike a shopping centre in Kyiv; "
         "113 drones fly overnight across Ukraine."),
        ("UNITED STATES",
         "Trump tariffs hit 14 economies",
         "The US proposes new tariffs on 14 trading partners, "
         "China capped at 20%, after a probe."),
        ("GAZA",
         "Israeli strikes kill 9 in Gaza",
         "Strikes in Deir al-Balah kill nine, including a Hamas "
         "deputy education minister, on a third night."),
        ("INDONESIA",
         "Mine flood kills 13 in Bogor",
         "An illegal gold mine floods 100 metres down after "
         "heavy rain; 13 miners dead, 13 missing."),
        ("UNITED KINGDOM",
         "Migration falls to 77,000",
         "Net migration drops to its lowest since 1997 outside "
         "the pandemic, in the year to June 2026."),
    ]
    cw, ch = 464, 128
    ox, oy = 34, 492
    for i, (tag, head, body) in enumerate(stories):
        px = ox + (i % 2) * (cw + 16)
        py = oy + (i // 2) * (ch + 6)
        draw_card(d, px, py, cw, ch, i + 1, tag, head, body)

    # Also today
    ay = oy + 3 * ch + 2 * 6 + 14
    d.line([34, ay, W - 34, ay], fill=INK, width=2)
    d.text((34, ay + 10), "ALSO TODAY",
           font=font("DejaVuSans-Bold.ttf", 15), fill=RED)
    also = ("Macy's Thanksgiving parade put off to Saturday by a "
            "storm, a first in 100 years  •  Drone attack in Kuwait "
            "kills two Italian technicians  •  Bangkok refinery blast "
            "injures nine  •  China unveils a 2030 plan for 6G networks")
    also_lines = wrap(d, also, font("DejaVuSans.ttf", 15), W - 68)
    yy = ay + 34
    for line in also_lines:
        d.text((34, yy), line, font=font("DejaVuSans.ttf", 15), fill=INK)
        yy += 21
    d.text((W // 2, H - 30),
           "All stories reported on Thursday 26 November 2026",
           font=font("DejaVuSans.ttf", 13), fill=GREY, anchor="mm")

    page.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", page.size, page.mode)


if __name__ == "__main__":
    main()
