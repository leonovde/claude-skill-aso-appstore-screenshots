# Quality Checklist

> Validate every generated screenshot before delivery.
> Rules from: [02-SCREENSHOT-SPEC.md](02-SCREENSHOT-SPEC.md) · Applied after: [03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md)

## Per-Screenshot Checks

Run through this for **every** generated screenshot:

### Dimensions
- [ ] Image is exactly **1290 × 2796 px** (or the target Apple size)
- [ ] Aspect ratio matches Apple's requirement (not standard 9:16)
- [ ] If cropped from wider source: sides trimmed equally, top edge preserved

### Typography
- [ ] Action verb is the **biggest, boldest** text on the image
- [ ] Benefit descriptor is visibly smaller than the verb but still bold
- [ ] Both lines are **white, uppercase, centre-aligned**
- [ ] Font is heavy/black weight sans-serif (not regular or bold — **black** weight)
- [ ] Text is **crisp and highly readable** (not blurred, artefacted, or partially obscured)
- [ ] Text is within the **centre 70% of canvas width** (generous side margins)
- [ ] Text wording matches the intended benefit exactly (no AI hallucination / rewording)
- [ ] Text sits in the **top ~20-25%** of the canvas with comfortable top padding

### Device Frame
- [ ] Shows a **realistic iPhone mockup** (black frame, Dynamic Island visible)
- [ ] Device is **centred horizontally**
- [ ] Bottom of phone **bleeds off the bottom edge** (intentionally cropped)
- [ ] The app screenshot is clearly visible on the phone screen
- [ ] App screenshot is **not distorted, stretched, or cropped incorrectly**
- [ ] Screen content matches the intended simulator screenshot

### Background
- [ ] **Solid brand colour** fills entire background
- [ ] **No** glows, gradients, radial patterns, or light effects
- [ ] Colour matches the specified hex code
- [ ] Background has **high contrast** with white text

### Breakout Elements (if present)
- [ ] Element is a **complete UI panel/card/section** (not a small button or icon)
- [ ] Same vertical position as on the app screen (not rotated or angled)
- [ ] **Scaled up** and extends beyond both edges of the device frame
- [ ] Soft drop shadow creates floating/depth effect
- [ ] Content matches the app (same colours, text, style — nothing invented)
- [ ] Element directly relates to the benefit headline

### Content Quality
- [ ] No watermarks
- [ ] No extra text beyond the headline
- [ ] No App Store UI chrome (status bar, nav bar, etc. from the App Store itself)
- [ ] No AI artefacts (extra fingers on hands, garbled text, strange reflections)
- [ ] Image looks **professionally designed** — would pass for agency work

---

## Set-Wide Consistency Checks

Run these after generating **all** screenshots in the set:

- [ ] **Same background colour** on every screenshot
- [ ] **Same device frame** — identical phone rendering, size, position, shadows across all
- [ ] **Same text style** — identical font, weight, size, positioning on every screenshot
- [ ] **Same overall aesthetic** — consistent polish level, accent style, visual language
- [ ] When viewed **side-by-side**, they look like a cohesive professional series
- [ ] Each screenshot shows a **different** benefit (no duplicate content)
- [ ] The **first screenshot** communicates the single most compelling reason to download

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
| Status bar clutter (low battery, carrier) | Clean status bar (9:41, full signal) |

---

## Quick Decision Flowchart

```
Generated image ready?
│
├─ Dimensions correct (1290×2796)?
│  ├─ No → Crop and resize first
│  └─ Yes ↓
│
├─ Text readable, correct, and within safe zone?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Device frame realistic and correctly positioned?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Background clean solid colour (no gradients)?
│  ├─ No → Regenerate
│  └─ Yes ↓
│
├─ Matches style template (for screenshots 2+)?
│  ├─ No → Regenerate with style template reference
│  └─ Yes ↓
│
└─ ✅ Ready for App Store Connect
```
