# Quality Checklist

> Validate every generated screenshot before delivery.
> Rules from: [02-SCREENSHOT-SPEC.md](02-SCREENSHOT-SPEC.md) · Applied after: [03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md)

## Per-Screenshot Checks

Run through this for **every** generated screenshot:

### Dimensions
- [ ] Image is exactly **1080 × 1920 px** (or another valid Google Play size, e.g. 720×1280, 1440×2560)
- [ ] Aspect ratio is **9:16** (portrait) or 16:9 (landscape) — not Apple's narrower ratio
- [ ] Format is JPG or 24-bit PNG — **no alpha/transparency channel**

### Typography
- [ ] Action verb is the **biggest, boldest** text on the image
- [ ] Benefit descriptor is visibly smaller than the verb but still bold
- [ ] Both lines are **white, uppercase, centre-aligned**
- [ ] Font is heavy/black weight sans-serif (Roboto Black or equivalent — **black** weight, not just bold)
- [ ] Text is **crisp and highly readable** (not blurred, artefacted, or partially obscured)
- [ ] Text wording matches the intended benefit exactly (no AI hallucination / rewording)
- [ ] Text sits in the **top ~15%** of the canvas (approximately top 288px of a 1920px canvas)

### Device Frame
- [ ] Shows a **realistic Pixel phone mockup** (black frame, small centred camera hole-punch — NOT a Dynamic Island)
- [ ] Device is **centred horizontally**
- [ ] Device **floats with breathing room on all sides** — the bottom of the phone is NOT bleeding off the canvas edge
- [ ] Visible breathing room (~80px) between device bottom and canvas bottom
- [ ] The app screenshot is clearly visible on the phone screen
- [ ] App screenshot is **not distorted, stretched, or cropped incorrectly**
- [ ] Screen content matches the intended app screenshot
- [ ] **No Dynamic Island** — this is a Pixel/Android device, not an iPhone

### Background
- [ ] **Solid brand colour** (or subtle same-hue gradient) fills entire background
- [ ] **No** harsh glows, radial patterns, or strong light effects
- [ ] Colour matches the specified hex code
- [ ] Background has **high contrast** with white text

### Callout Annotations (Act 2 screenshots only)
- [ ] 2–3 pill-shaped annotation bubbles present
- [ ] Each callout has an arrow/line pointing at a specific UI element
- [ ] Callouts do NOT overlap the headline text
- [ ] Callout style is consistent across all Act 2 frames (same pill shape, same colour scheme)
- [ ] Callout text is concise (2–5 words each)
- [ ] Callouts describe real UI elements visible in the app screenshot (nothing invented)

### Content Quality
- [ ] No watermarks
- [ ] No extra text beyond the headline (and callouts for Act 2)
- [ ] No Google Play UI chrome (Play Store navigation, install button, etc.)
- [ ] No AI artefacts (garbled text, strange reflections, malformed UI elements)
- [ ] Image looks **professionally designed** — would pass for agency work
- [ ] Status bar (if visible on app screen): clean Android status bar (neutral time, full signal, full battery)

---

## Feature Graphic Checks

Run these for the **Feature Graphic** (1024×500):

- [ ] Dimensions are exactly **1024 × 500 px**
- [ ] Format is JPG or 24-bit PNG — **no alpha/transparency**
- [ ] App icon is visible and prominent
- [ ] Headline is 5–7 words, white, uppercase, heavy/black weight
- [ ] Background matches the screenshot set brand colour
- [ ] **No UI screenshots** in the Feature Graphic — brand/marketing asset only
- [ ] Headline is readable at thumbnail size (as displayed in search results)
- [ ] Typography style matches the screenshot set

---

## Set-Wide Consistency Checks

Run these after generating **all** screenshots in the set:

- [ ] **Same background colour** (or same gradient style) on every screenshot
- [ ] **Same device frame** — identical Pixel rendering, size, position, shadows across all
- [ ] **Same text style** — identical font, weight, size, positioning on every screenshot
- [ ] **Same callout style** — if used, same pill shape and colour across all Act 2 frames
- [ ] **Same overall aesthetic** — consistent polish level, accent style, visual language
- [ ] When viewed **side-by-side**, they look like a cohesive professional series
- [ ] Each screenshot shows a **different** benefit (no duplicate content)
- [ ] The **first screenshot** communicates the single most compelling reason to install
- [ ] Minimum **2 screenshots** uploaded; recommended **6–8**
- [ ] All screenshots share the **same orientation** (all portrait or all landscape — cannot mix)

---

## Screenshot Content Rules

These are hard rules — reject any screenshot that violates them:

| ❌ Never Use | ✅ Always Use |
|-------------|-------------|
| Empty states / "no results" | Screens full of content and activity |
| Placeholder / test data | Realistic, compelling content |
| Settings or preferences pages | Core feature screens |
| Login / signup screens | The app at its best |
| Loading indicators | Fully loaded states |
| Debug UI / console output | Clean production UI |
| Inconsistent dark/light mode | Consistent appearance mode |
| Status bar clutter (low battery, error icons) | Clean Android status bar (neutral time, full signal/battery) |
| iOS Dynamic Island or iPhone-specific UI | Pixel/Android device frame only |

---

## Quick Decision Flowchart

```
Generated image ready?
│
├─ Dimensions correct (1080×1920, no alpha)?
│  ├─ No → Regenerate at correct size
│  └─ Yes ↓
│
├─ Text readable, correct, and within top 15% zone?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Pixel device frame realistic and floating (no bottom bleed)?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Background clean (no harsh glows or radial patterns)?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Callouts present and correct (Act 2 only)?
│  ├─ No → Regenerate with callout instructions
│  └─ Yes ↓
│
├─ Feature Graphic validated (1024×500, no alpha, icon visible)?
│  ├─ No → Regenerate Feature Graphic
│  └─ Yes ↓
│
├─ Matches style template (for screenshots 2+)?
│  ├─ No → Regenerate with style template reference
│  └─ Yes ↓
│
└─ ✅ Ready for Google Play Console
```
