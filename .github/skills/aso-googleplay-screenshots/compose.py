#!/usr/bin/env python3
"""
Google Play Screenshot Composer
Composites headline text, device frame template, and app screenshot
into a pixel-perfect 1080×1920 Google Play portrait image.

The device frame floats with breathing room on all sides — it does NOT
bleed off the bottom edge (Google Play uses native 9:16, no crop needed).
"""

import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

# ── Canvas ──────────────────────────────────────────────────────────
CANVAS_W = 1080
CANVAS_H = 1920

# ── Device template constants (must match generate_frame.py) ───────
DEVICE_W = 860
BEZEL = 14
SCREEN_W = DEVICE_W - 2 * BEZEL    # 832
SCREEN_CORNER_R = 50

# ── Layout zones (Google Play three-zone layout) ────────────────────
# Headline: top ~15% (~288px), Screenshot: centre ~70%, Bottom: ~15%
HEADLINE_TOP = 60           # headline text starts here
DEVICE_TOP = 290            # device frame top (leaves ~15% for headline)
DEVICE_BOTTOM_MARGIN = 80   # breathing room below device before canvas bottom

# ── Typography ──────────────────────────────────────────────────────
VERB_SIZE_MAX = 200
VERB_SIZE_MIN = 110
DESC_SIZE = 90
VERB_DESC_GAP = 16
DESC_LINE_GAP = 18
MAX_TEXT_W = int(CANVAS_W * 0.88)
MAX_VERB_W = int(CANVAS_W * 0.88)

# Prefer Roboto Black (Android/Google font); fall back to common alternatives
_FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/roboto/hinted/RobotoCondensed-Bold.ttf",
    "/usr/share/fonts/truetype/roboto/Roboto-Black.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Roboto-Black.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]

def _resolve_font():
    for path in _FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None

FONT_PATH = _resolve_font()
FRAME_PATH = os.path.join(os.path.dirname(__file__), "assets", "device_frame.png")


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def word_wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = f"{cur} {w}".strip()
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_font(text, max_w, size_max, size_min):
    """Return the largest font size where text fits within max_w."""
    dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    for size in range(size_max, size_min - 1, -4):
        if FONT_PATH:
            font = ImageFont.truetype(FONT_PATH, size)
        else:
            font = ImageFont.load_default()
        bbox = dummy.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_w:
            return font
    if FONT_PATH:
        return ImageFont.truetype(FONT_PATH, size_min)
    return ImageFont.load_default()


def draw_centered(draw, y, text, font, max_w=None):
    lines = word_wrap(draw, text, font, max_w) if max_w else [text]
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        h = bbox[3] - bbox[1]
        draw.text((CANVAS_W // 2, y - bbox[1]), line, fill="white", font=font, anchor="mt")
        y += h + DESC_LINE_GAP
    return y


def compose(bg_hex, verb, desc, screenshot_path, output_path):
    bg = hex_to_rgb(bg_hex)

    # ── 1. Canvas ───────────────────────────────────────────────────
    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), (*bg, 255))
    draw = ImageDraw.Draw(canvas)

    # ── 2. Headline text (top ~15% zone) ────────────────────────────
    if FONT_PATH:
        verb_font = fit_font(verb.upper(), MAX_VERB_W, VERB_SIZE_MAX, VERB_SIZE_MIN)
        desc_font = ImageFont.truetype(FONT_PATH, DESC_SIZE)
    else:
        verb_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()

    y = HEADLINE_TOP
    y = draw_centered(draw, y, verb.upper(), verb_font)
    y += VERB_DESC_GAP
    draw_centered(draw, y, desc.upper(), desc_font, max_w=MAX_TEXT_W)

    # ── 3. Device frame position (floating with breathing room) ──────
    device_x = (CANVAS_W - DEVICE_W) // 2
    device_y = DEVICE_TOP
    screen_x = device_x + BEZEL
    screen_y = device_y + BEZEL

    # ── 4. Screenshot into screen area ──────────────────────────────
    shot = Image.open(screenshot_path).convert("RGBA")

    scale = SCREEN_W / shot.width
    sc_w = SCREEN_W
    sc_h = int(shot.height * scale)
    shot = shot.resize((sc_w, sc_h), Image.LANCZOS)

    # Screen height: fills from screen_y to device bottom with breathing room
    device_h_available = CANVAS_H - DEVICE_BOTTOM_MARGIN - device_y
    screen_h = device_h_available - 2 * BEZEL

    # Screen mask (rounded rect) — fully contained within canvas
    scr_mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(scr_mask).rounded_rectangle(
        [screen_x, screen_y, screen_x + SCREEN_W, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=255,
    )

    scr_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(scr_layer).rounded_rectangle(
        [screen_x, screen_y, screen_x + SCREEN_W, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=(0, 0, 0, 255),
    )
    scr_layer.paste(shot, (screen_x, screen_y))
    scr_layer.putalpha(scr_mask)

    canvas = Image.alpha_composite(canvas, scr_layer)

    # ── 5. Device frame template ────────────────────────────────────
    frame_template = Image.open(FRAME_PATH).convert("RGBA")

    frame_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    frame_layer.paste(frame_template, (device_x, device_y))
    canvas = Image.alpha_composite(canvas, frame_layer)

    # ── 6. Save (no alpha — Google Play requires JPG or 24-bit PNG) ──
    canvas.convert("RGB").save(output_path, "PNG")
    print(f"✓ {output_path} ({CANVAS_W}×{CANVAS_H})")


def compose_feature_graphic(bg_hex, headline, output_path):
    """Generate a 1024×500 Feature Graphic (required by Google Play)."""
    FG_W, FG_H = 1024, 500
    bg = hex_to_rgb(bg_hex)
    canvas = Image.new("RGBA", (FG_W, FG_H), (*bg, 255))
    draw = ImageDraw.Draw(canvas)

    if FONT_PATH:
        font_size = 90
        font = ImageFont.truetype(FONT_PATH, font_size)
        # Auto-shrink if too wide
        max_w = int(FG_W * 0.88)
        while font_size > 40:
            bbox = draw.textbbox((0, 0), headline.upper(), font=font)
            if (bbox[2] - bbox[0]) <= max_w:
                break
            font_size -= 4
            font = ImageFont.truetype(FONT_PATH, font_size)
    else:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), headline.upper(), font=font)
    text_h = bbox[3] - bbox[1]
    y = (FG_H - text_h) // 2 - bbox[1]
    draw.text((FG_W // 2, y), headline.upper(), fill="white", font=font, anchor="mt")

    canvas.convert("RGB").save(output_path, "PNG")
    print(f"✓ {output_path} ({FG_W}×{FG_H}) [Feature Graphic]")


def main():
    p = argparse.ArgumentParser(description="Compose Google Play screenshot or Feature Graphic")
    p.add_argument("--bg", required=True, help="Background hex colour (#E31837)")
    p.add_argument("--verb", help="Action verb (TRACK)")
    p.add_argument("--desc", help="Benefit descriptor (TRADING CARD PRICES)")
    p.add_argument("--screenshot", help="App screenshot path")
    p.add_argument("--output", required=True, help="Output file path")
    p.add_argument("--feature-graphic", action="store_true",
                   help="Generate 1024×500 Feature Graphic instead of screenshot")
    p.add_argument("--headline", help="Headline for Feature Graphic (5-7 words)")
    args = p.parse_args()

    if args.feature_graphic:
        if not args.headline:
            p.error("--headline is required when using --feature-graphic")
        compose_feature_graphic(args.bg, args.headline, args.output)
    else:
        if not args.verb or not args.desc or not args.screenshot:
            p.error("--verb, --desc, and --screenshot are required for screenshot mode")
        compose(args.bg, args.verb, args.desc, args.screenshot, args.output)


if __name__ == "__main__":
    main()
