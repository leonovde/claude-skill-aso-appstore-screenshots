# Screenshot Design Specification

> The exact visual rules every generated App Store screenshot must follow.
> Referenced by: [03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md) · [04-QUALITY-CHECKLIST.md](04-QUALITY-CHECKLIST.md)

## Canvas Dimensions

App Store Connect requires **exact** pixel dimensions — it rejects anything else.

| Display | Portrait | Landscape |
|---------|----------|-----------|
| iPhone 6.5" | 1242 × 2688 px | 2688 × 1242 px |
| **iPhone 6.7" (default)** | **1290 × 2796 px** | 2796 × 1290 px |
| iPhone 6.9" | 1320 × 2868 px | 2868 × 1320 px |

**Default target: 1290 × 2796 px** (iPhone 6.7")

> **Aspect ratio note**: Apple's dimensions (~0.461 ratio) are narrower than standard 9:16 (0.5625). If your image generator outputs 9:16, you must **crop the sides** and resize to exact Apple dimensions. Crop equally from left and right edges, preserving the top edge.

## Layout Anatomy

```
┌──────────────────────────────┐
│         top padding          │  ← 200px from top
│                              │
│      ████ ACTION VERB ████   │  ← Line 1: biggest, boldest text
│       BENEFIT DESCRIPTOR     │  ← Line 2: smaller but still bold
│                              │
│     ┌────────────────────┐   │  ← Device frame starts ~720px from top
│     │  ┌──────────────┐  │   │
│     │  │              │  │   │
│     │  │  App Screen  │  │   │
│     │  │  (simulator  │  │   │
│     │  │  screenshot) │  │   │
│     │  │              │  │   │
│     │  │              │  │   │
│     └──┴──────────────┴──┘   │  ← Device bleeds off bottom edge
└──────────────────────────────┘
         1290 × 2796 px
```

## Typography

| Element | Size | Weight | Colour | Alignment |
|---------|------|--------|--------|-----------|
| **Action verb** (Line 1) | 256px → 150px auto-fit | Black / Heavy | White | Centre |
| **Benefit descriptor** (Line 2) | 124px fixed | Black / Heavy | White | Centre |

- **Font**: SF Pro Display Black (or any heavy/black sans-serif: Inter Black, Montserrat Black, etc.)
- **ALL CAPS** for both lines
- **Verb auto-sizing**: starts at 256px, shrinks in 4px steps down to 150px until it fits within 92% of canvas width (1186px)
- **Descriptor word-wrap**: wraps at 92% canvas width (1186px), 24px gap between wrapped lines
- **Gap between verb and descriptor**: 20px
- **Text starts at 200px** from the top of the canvas

### ⚠️ Horizontal Safe Zone (Critical)

All text **must** stay within the centre ~70% of canvas width. Leave ≥15% padding on each side. If generating at 9:16 and cropping to Apple's narrower ratio, **any text near the edges WILL be cut off**. Keep headlines short or break across lines rather than extending to edges.

## Device Frame

- **Modern iPhone mockup** (black frame, Dynamic Island)
- **Width**: ~80% of canvas (1030px on 1290px canvas)
- **Position**: centred horizontally, top at ~720px from canvas top
- **Bottom bleed**: the device intentionally extends past the bottom canvas edge — the phone is cropped, not fully visible. This creates a dynamic, modern feel.
- **Bezel**: 15px border between device edge and screen
- **Screen corner radius**: 62px rounded corners
- **Device corner radius**: 77px
- **Dynamic Island**: 130 × 38px, centred, 14px below screen top
- **Colours**: body RGB(30,30,30), inner bevel RGB(20,20,20), buttons RGB(25,25,25), Dynamic Island black

## Background

- **Solid bold brand colour** fills entire canvas — same colour on ALL screenshots in the set
- **No glows, gradients, radial patterns, or light effects** — keep it flat and bold
- Must be saturated and vibrant (stops the scroll in the App Store)
- High contrast with white text

## Breakout Elements (Optional)

Breakout elements make screenshots dynamic but must be used with restraint. **A clean screenshot with no breakout is better than a forced one.**

### Primary — Feature Zoom-Out (only when relevant)

- Only use when there is an **obvious, visually compelling UI panel** on the app screen that directly relates to the benefit headline
- Must be a **complete card/section/panel** — never individual buttons, icons, or small elements
- **Same vertical position and orientation** as on the app screen — NO rotation or angling
- **Scaled UP significantly** — much larger than on-screen size, extending beyond BOTH left and right edges of the device frame
- **Overlaps the phone bezel** on both sides, expanding to nearly full canvas width
- **Soft drop shadow** beneath it to create depth/floating effect
- Content must match the app — same colours, style, text. Do NOT invent new elements.

### Secondary — Supporting Elements (0-2, optional)

- Small creative additions (contextual icons, subtle cues, floating UI elements) that reinforce the benefit
- Must NOT compete with the primary breakout for attention
- Must be directly relevant to the benefit headline
- Less is more — every element must earn its place

### What to Avoid

- Random decorative elements unrelated to the benefit
- Excessive particles, sparkles, or effects
- Cluttered compositions — polished and intentional, not busy
- Any text other than the headline (no watermarks, no App Store chrome)

## Set-Wide Consistency Rules

When generating multiple screenshots for the same app:

1. **Same background colour** on every screenshot
2. **Same device frame rendering** — identical phone mockup, same reflections, shadows, size
3. **Same text treatment** — identical font, weight, size, positioning
4. **Same visual style** — if one has accent shapes, all have similar accent shapes
5. **Same level of polish** — when placed side-by-side, they look like a cohesive professional set
