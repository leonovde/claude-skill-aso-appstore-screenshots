# Screenshot Design Specification

> The exact visual rules every generated Google Play Store screenshot must follow.
> Referenced by: [03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md) · [04-QUALITY-CHECKLIST.md](04-QUALITY-CHECKLIST.md)

## Canvas Dimensions

Google Play uses native **9:16 aspect ratio** — no post-processing crop is needed.

| Format | Dimensions | Notes |
|--------|-----------|-------|
| **Phone portrait (default)** | **1080 × 1920 px** | Standard 9:16 |
| Phone landscape | 1920 × 1080 px | 16:9 |
| Feature Graphic | 1024 × 500 px | Required for every listing |
| 7-inch tablet | 1024 × 600 px | Optional |
| 10-inch tablet | 1280 × 800 px | Optional |

**Default target: 1080 × 1920 px** (phone portrait)

> **No crop step needed**: compose.py outputs exactly 1080×1920. Unlike Apple's narrower ratio, Google Play uses native 9:16 so images are ready to upload immediately.

Minimum: 320px on the shortest side. Maximum: 3840px on the longest side.
Format: JPG or 24-bit PNG — **no alpha/transparency channel**.
Minimum 2 screenshots, recommended 6–8. All must share the same orientation.

## Layout Anatomy

```
┌──────────────────────────────┐
│         top padding          │  ← 60px from top
│                              │
│      ████ ACTION VERB ████   │  ← Line 1: biggest, boldest text
│       BENEFIT DESCRIPTOR     │  ← Line 2: smaller but still bold
│                              │  ← Headline zone: top ~15% (~288px)
│     ┌────────────────────┐   │
│     │ ○ (camera hole)    │   │  ← Pixel device frame starts at ~290px
│     │  ┌──────────────┐  │   │
│     │  │              │  │   │
│     │  │  App Screen  │  │   │
│     │  │  (emulator   │  │   │
│     │  │  screenshot) │  │   │
│     │  │              │  │   │
│     │  └──────────────┘  │   │
│     └────────────────────┘   │  ← Device bottom: ~80px from canvas bottom
│         breathing room       │  ← Device floats — does NOT bleed off edge
└──────────────────────────────┘
         1080 × 1920 px
```

**Key difference from iOS**: The device frame floats with breathing room on all sides. It does NOT bleed off the bottom edge. This is the correct Google Play aesthetic.

## Typography

| Element | Size | Weight | Colour | Alignment |
|---------|------|--------|--------|-----------|
| **Action verb** (Line 1) | 200px → 110px auto-fit | Black / Heavy | White | Centre |
| **Benefit descriptor** (Line 2) | 90px fixed | Black / Heavy | White | Centre |

- **Font**: Roboto Black (Google's product font) or any heavy/black sans-serif (Inter Black, Montserrat Black, etc.)
- **ALL CAPS** for both lines
- **Verb auto-sizing**: starts at 200px, shrinks in 4px steps down to 110px until it fits within 88% of canvas width (950px)
- **Descriptor word-wrap**: wraps at 88% canvas width (950px), 18px gap between wrapped lines
- **Gap between verb and descriptor**: 16px
- **Text starts at 60px** from the top of the canvas (top ~15% zone)

## Device Frame

- **Pixel phone mockup** (black frame, small centred camera hole-punch at top — NOT a Dynamic Island or notch)
- **Width**: ~80% of canvas (860px on 1080px canvas)
- **Height**: fully contained within canvas (~1570px frame height)
- **Position**: centred horizontally, top at ~290px from canvas top
- **Bottom clearance**: ~80px breathing room between device bottom and canvas bottom
- **Device floats**: visible breathing room on all four sides — NO bottom bleed
- **Bezel**: 14px border between device edge and screen
- **Screen corner radius**: 50px rounded corners
- **Device corner radius**: 60px
- **Camera hole-punch**: 18px radius circle, centred horizontally, 22px below screen top
- **Colours**: body RGB(30,30,30), inner bevel RGB(20,20,20), buttons RGB(25,25,25), camera black
- **No silent switch** — Android/Pixel devices do not have one

## Background

- **Solid bold brand colour** fills entire canvas — same colour on ALL screenshots in the set
- Subtle same-hue gradient is acceptable (e.g., slightly darker at bottom) but keep it restrained
- **No harsh glows, radial patterns, or strong light effects** — keep it clean and bold
- Must be saturated and vibrant (stops the scroll in Google Play)
- High contrast with white text

## Callout Annotations (Act 2 Screenshots)

For screenshots 2–4 ("Build the Case"), add 2–3 annotation callout bubbles:

- **Shape**: pill/rounded-rectangle label
- **Size**: fits 2–5 words comfortably
- **Arrow/line**: short pointer from the pill to the specific UI element it describes
- **Colour**: app's accent colour, OR white pill with dark text, OR dark pill with white text — pick one style and use it consistently
- **Position**: overlaid on the app screen in the device frame; never overlapping the headline
- **Content**: concise label (e.g., "Real-time prices", "One-tap scan", "Offline mode")
- **Max per frame**: 3 callouts

## Feature Graphic

Required for every Google Play listing. Displayed at the top of the store page.

| Attribute | Value |
|-----------|-------|
| Dimensions | 1024 × 500 px (exactly) |
| Format | JPG or 24-bit PNG, no alpha |
| Content | App icon + bold headline (5–7 words) + background colour |
| No UI screenshots | Brand/marketing asset only |
| Video thumbnail | Doubles as thumbnail if a promo video exists |

## Set-Wide Consistency Rules

When generating multiple screenshots for the same app:

1. **Same background colour** (or same gradient style) on every screenshot
2. **Same device frame rendering** — identical Pixel mockup, same reflections, shadows, size
3. **Same text treatment** — identical font, weight, size, positioning
4. **Same callout style** — if using annotation bubbles, same pill style and colour across Act 2 frames
5. **Same visual style** — consistent polish level when placed side-by-side
6. **Same device model** — do not mix Pixel models across the set
7. **Same orientation** — all portrait or all landscape (cannot mix)
