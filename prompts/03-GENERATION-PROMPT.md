# Image Generation Prompt Templates

> Copy-paste these prompts into your image generator (Nano Banana Pro, DALL·E, Midjourney, etc.).
> Requires: outputs from [01-BENEFIT-DISCOVERY.md](01-BENEFIT-DISCOVERY.md) · Rules from [02-SCREENSHOT-SPEC.md](02-SCREENSHOT-SPEC.md) · Validate with [04-QUALITY-CHECKLIST.md](04-QUALITY-CHECKLIST.md)

---

## Before You Generate

Fill in these variables from your benefit discovery:

```
BRAND_COLOUR  = #______        (e.g., #E31837)
VERB_1        = ____________   (e.g., TRACK)
DESC_1        = ____________   (e.g., TRADING CARD PRICES)
SCREENSHOT_1  = [attached]     (simulator screenshot for benefit 1)
VERB_2        = ____________
DESC_2        = ____________
SCREENSHOT_2  = [attached]
VERB_3        = ____________
DESC_3        = ____________
SCREENSHOT_3  = [attached]
```

---

## Prompt Template A — First Screenshot

Use this for the **first** screenshot in your set. Attach the simulator screenshot as the input image.

> **Tip**: Generate 3 versions and pick the best one. The chosen version becomes the **style template** for screenshots 2 and 3.

```
Create a professional, high-converting App Store screenshot with these exact specifications:

LAYOUT:
- Canvas: portrait orientation, 9:16 aspect ratio (will be cropped to 1290×2796px)
- Solid background colour: {BRAND_COLOUR} — flat, bold, no gradients or glows
- All text centred within the middle 70% of the canvas width (leave generous side margins)

HEADLINE TEXT (top area, ~top 25% of canvas):
- Line 1 (ACTION VERB): "{VERB_1}" — this is the BIGGEST, boldest text. White, uppercase, heavy/black weight sans-serif font. Centred.
- Line 2 (BENEFIT): "{DESC_1}" — noticeably smaller than line 1 but still bold. White, uppercase, same font family. Centred.
- Comfortable padding from top edge (~200px equivalent at 1290px width)

DEVICE:
- A photorealistic iPhone 15 Pro mockup (black frame, Dynamic Island) — sleek, modern, with accurate proportions, reflections, and subtle shadows
- The phone displays the attached app screenshot on its screen
- Device is centred horizontally, positioned so it overlaps or sits just below the headline text area
- The bottom of the phone bleeds off the bottom edge of the canvas — intentionally cropped for a dynamic feel
- Device width is roughly 80% of the canvas width

BREAKOUT ELEMENTS (optional):
{BREAKOUT_INSTRUCTIONS}

CRITICAL RULES:
- Background must be a clean, solid {BRAND_COLOUR}. NO glows, gradients, radial patterns, or light effects.
- All text must stay well within the centre 70% of the canvas (sides will be cropped)
- The result should look like it was designed by a professional App Store screenshot agency
- No watermarks, no extra text, no app store UI chrome
```

**For `{BREAKOUT_INSTRUCTIONS}`, choose one:**

*If a relevant UI panel is obvious:*
```
- The [panel name] card/section from the app screen pops out from the device frame. It stays at the same vertical position and orientation as on screen (NOT rotated). It is SCALED UP significantly — much larger than on-screen size — extending dramatically beyond BOTH left and right edges of the device frame, overlapping the phone bezel on both sides, expanding to nearly the full canvas width. A soft drop shadow beneath it creates a floating effect. The panel uses the exact same colours/content as the app.
- Optionally 1-2 small supporting elements (contextual icons, subtle cues) that reinforce the "{VERB_1} {DESC_1}" message, without competing with the primary breakout.
```

*If no relevant panel exists:*
```
- No breakout elements — the app screen speaks for itself. Keep the composition clean.
- Optionally 1-2 small supporting creative elements that reinforce the "{VERB_1} {DESC_1}" message (professional designer-style additions, not from the app UI).
```

---

## Prompt Template B — Subsequent Screenshots (2nd, 3rd, etc.)

Use this for **every screenshot after the first**. Attach **two images**:
1. The simulator screenshot for this benefit
2. The first approved screenshot (your **style template**)

```
Create the next screenshot in an App Store screenshot SET. It must look like it belongs to the same series as the style reference.

TWO REFERENCE IMAGES:
- FIRST image: The APP SCREENSHOT to display on the phone screen. This defines WHAT this screenshot shows.
- SECOND image: The STYLE TEMPLATE — an already-approved screenshot from the same set. Match its visual style EXACTLY.

HEADLINE TEXT:
- Line 1 (ACTION VERB): "{VERB_N}" — biggest, boldest text. White, uppercase, heavy/black sans-serif. Centred.
- Line 2 (BENEFIT): "{DESC_N}" — smaller than line 1, same font. White, uppercase, centred.
- Same text positioning as the style template

MATCH THE STYLE TEMPLATE EXACTLY:
- Same photorealistic iPhone device frame rendering — identical phone mockup, same size, position, shadows, reflections, edge treatment
- Same text treatment (font, weight, crispness, visual weight)
- Same background: clean, solid {BRAND_COLOUR}. No glows, gradients, or light effects.
- Same overall level of polish and aesthetic
- When placed side-by-side with the style template in the App Store, they must look like a cohesive professional set

DEVICE:
- Display this benefit's app screenshot on the phone screen
- Phone centred horizontally, bottom bleeds off canvas edge
- Device width ~80% of canvas

BREAKOUT ELEMENTS (optional):
{BREAKOUT_INSTRUCTIONS}

CRITICAL RULES:
- The device frame MUST match the style template EXACTLY — do NOT reinvent it
- Background must be a clean, solid {BRAND_COLOUR} — flat and bold
- All text within the centre 70% of canvas width
- No watermarks, no extra text, no app store UI chrome
```

---

## Prompt Template C — Iteration / Refinement

Use when the user wants changes to an already-generated screenshot. Attach **three images**:
1. The simulator screenshot (layout reference)
2. The first approved screenshot (style template)
3. The version the user liked best (creative direction)

```
Refine this App Store screenshot based on these three references:

- FIRST image: APP SCREENSHOT — defines the screen content to show on the phone
- SECOND image: STYLE TEMPLATE — the first approved screenshot in the set. Device frame, text treatment, and visual style MUST match this exactly.
- THIRD image: APPROVED DIRECTION — the version the user liked best. Match its creative approach, breakout elements, and secondary elements.

Generate a new version that keeps:
- Screen content from the app screenshot
- Device frame and visual style from the style template
- Creative direction from the approved version

WITH THESE CHANGES:
{USER_REQUESTED_CHANGES}

Maintain set-wide consistency. Background: solid {BRAND_COLOUR}, no gradients. All text in centre 70%.
No watermarks, no extra text, no app store UI chrome.
```

---

## Post-Generation: Crop to App Store Dimensions

**Every generated image must be cropped/resized to exact Apple dimensions before use.**

If your generator outputs 9:16 (e.g., 2160×3840), crop and resize:

1. Calculate crop width: `crop_w = height × (1290 / 2796)`
2. Calculate horizontal offset: `offset_x = (width - crop_w) / 2`
3. Crop from centre (trim sides equally, preserve top edge)
4. Resize to exactly **1290 × 2796 px**

Other target sizes:
- iPhone 6.5": resize to 1242 × 2688 px
- iPhone 6.9": resize to 1320 × 2868 px

→ Validate the result with **[04-QUALITY-CHECKLIST.md](04-QUALITY-CHECKLIST.md)**
