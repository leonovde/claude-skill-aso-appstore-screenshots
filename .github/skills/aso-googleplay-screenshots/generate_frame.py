#!/usr/bin/env python3
"""
Generate Pixel phone device frame template PNG for Google Play screenshots.
Output: assets/device_frame.png — standalone device image (not positioned on canvas).
compose.py positions this dynamically based on the layout zones.

Design: current-generation Pixel-style phone —
  - Clean rounded corners (no Dynamic Island)
  - Small centred camera hole-punch at top of screen
  - Power button (right side) and volume buttons (left side only — no silent switch)
  - Device floats fully within the canvas (no bottom bleed)
"""

from PIL import Image, ImageDraw, ImageChops

# ── Device dimensions ───────────────────────────────────────────────
# Width sized to ~80% of 1080 canvas
DEVICE_W = 860
DEVICE_H = 1570          # fully contained; canvas handles remaining space
DEVICE_CORNER_R = 60
BEZEL = 14
SCREEN_CORNER_R = 50

# Camera hole-punch (top centre of screen — Android style)
CAM_R = 18               # radius of camera circle
CAM_TOP_OFFSET = 22      # distance from screen top to camera centre

SCREEN_W = DEVICE_W - 2 * BEZEL
SCREEN_H = DEVICE_H - 2 * BEZEL


def generate():
    frame = Image.new("RGBA", (DEVICE_W, DEVICE_H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame)

    # ── Device body ─────────────────────────────────────────────────
    fd.rounded_rectangle(
        [0, 0, DEVICE_W - 1, DEVICE_H - 1],
        radius=DEVICE_CORNER_R,
        fill=(30, 30, 30, 255),
    )
    fd.rounded_rectangle(
        [1, 1, DEVICE_W - 2, DEVICE_H - 2],
        radius=DEVICE_CORNER_R - 1,
        fill=(20, 20, 20, 255),
    )

    # ── Screen cutout (transparent) ─────────────────────────────────
    screen_x = BEZEL
    screen_y = BEZEL

    cutout = Image.new("L", (DEVICE_W, DEVICE_H), 255)
    ImageDraw.Draw(cutout).rounded_rectangle(
        [screen_x, screen_y, screen_x + SCREEN_W, screen_y + SCREEN_H],
        radius=SCREEN_CORNER_R,
        fill=0,
    )
    frame.putalpha(ImageChops.multiply(frame.getchannel("A"), cutout))

    # ── Camera hole-punch (centred, top of screen) ───────────────────
    cam_cx = DEVICE_W // 2
    cam_cy = screen_y + CAM_TOP_OFFSET
    ImageDraw.Draw(frame).ellipse(
        [cam_cx - CAM_R, cam_cy - CAM_R, cam_cx + CAM_R, cam_cy + CAM_R],
        fill=(0, 0, 0, 255),
    )

    # ── Side buttons (Pixel-style — no silent switch) ────────────────
    btn_color = (25, 25, 25, 255)
    fd2 = ImageDraw.Draw(frame)

    # Power button (right side)
    fd2.rounded_rectangle(
        [DEVICE_W, 280, DEVICE_W + 4, 420],
        radius=2, fill=btn_color,
    )
    # Volume up (left side)
    fd2.rounded_rectangle(
        [-4, 230, 0, 340],
        radius=2, fill=btn_color,
    )
    # Volume down (left side)
    fd2.rounded_rectangle(
        [-4, 360, 0, 470],
        radius=2, fill=btn_color,
    )
    # No silent switch — Android/Pixel does not have one

    out = "assets/device_frame.png"
    frame.save(out, "PNG")
    print(f"✓ {out} ({DEVICE_W}×{DEVICE_H})")
    print(f"  BEZEL={BEZEL}, SCREEN_W={SCREEN_W}, SCREEN_H={SCREEN_H}")
    print(f"  SCREEN_CORNER_R={SCREEN_CORNER_R}")
    print(f"  Camera hole-punch: centre ({DEVICE_W // 2}, {BEZEL + CAM_TOP_OFFSET}), r={CAM_R}")


if __name__ == "__main__":
    generate()
