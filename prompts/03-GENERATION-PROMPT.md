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
SCREENSHOT_1  = [attached]     (app screenshot for benefit 1)
VERB_2        = ____________
DESC_2        = ____________
SCREENSHOT_2  = [attached]
VERB_3        = ____________
DESC_3        = ____________
SCREENSHOT_3  = [attached]
```

---

## Prompt Template A — Act 1: "Stop the Scroll" (Screenshot 1)

Use this for the **first** screenshot in your set. Attach the app screenshot as the input image.

> **Tip**: Generate 3 versions and pick the best one. The chosen version becomes the **style template** for all subsequent screenshots.

```
Create a professional, high-converting Google Play Store screenshot with these exact specifications:

LAYOUT:
- Canvas: portrait orientation, 9:16 aspect ratio (1080×1920 px target — no crop needed)
- Solid background colour: {BRAND_COLOUR} — flat, bold; subtle same-hue gradient is OK but keep it restrained
- All text centred within the middle 88% of the canvas width

HEADLINE TEXT (top ~15% of canvas, approximately top 288px):
- Line 1 (ACTION VERB): "{VERB_1}" — this is the BIGGEST, boldest text. White, uppercase, heavy/black weight sans-serif font. Centred.
- Line 2 (BENEFIT): "{DESC_1}" — noticeably smaller than line 1 but still bold. White, uppercase, same font family. Centred.
- Comfortable padding from top edge (~60px equivalent)

DEVICE:
- A photorealistic Pixel phone mockup (black frame, small centred camera hole-punch at top — NOT a Dynamic Island or notch). The phone should look like a real Android device with accurate proportions, reflections, and subtle shadows.
- The phone displays the attached app screenshot on its screen
- Device is centred horizontally, positioned below the headline text area
- CRITICAL: The device must float with breathing room on all sides — the bottom of the phone must NOT bleed off the canvas edge. Leave approximately 80px of breathing room below the device. This is the correct Google Play style, not iOS style.
- Device width is roughly 80% of the canvas width

BREAKOUT ELEMENTS (optional):
{BREAKOUT_INSTRUCTIONS}

CRITICAL RULES:
- Background must be a clean, solid {BRAND_COLOUR} (subtle same-hue gradient OK). NO harsh glows, radial patterns, or strong light effects.
- The device MUST float fully within the canvas — visible breathing room below the device
- The result should look like it was designed by a professional Google Play screenshot agency
- No watermarks, no extra text, no Google Play UI chrome
- Output: 1080×1920 px (or 9:16 aspect ratio) — no cropping needed after generation
```

**For `{BREAKOUT_INSTRUCTIONS}`, choose one:**

*If a relevant UI panel is obvious:*
```
- The [panel name] card/section from the app screen pops out from the device frame. It stays at the same vertical position and orientation as on screen (NOT rotated). It is SCALED UP significantly — much larger than on-screen size — extending dramatically beyond BOTH left and right edges of the device frame, overlapping the phone bezel on both sides. A soft drop shadow beneath it creates a floating effect. The panel uses the exact same colours/content as the app.
- Optionally 1-2 small supporting elements (contextual icons, subtle cues) that reinforce the "{VERB_1} {DESC_1}" message, without competing with the primary breakout.
```

*If no relevant panel exists:*
```
- No breakout elements — the app screen speaks for itself. Keep the composition clean.
- Optionally 1-2 small supporting creative elements that reinforce the "{VERB_1} {DESC_1}" message (professional designer-style additions, not from the app UI).
```

---

## Prompt Template B — Act 2: "Build the Case" (Screenshots 2–4, with Callouts)

Use this for screenshots 2–4. Attach **two images**:
1. The app screenshot for this benefit
2. The first approved screenshot (your **style template**)

```
Create the next screenshot in a Google Play Store screenshot SET. It must look like it belongs to the same series as the style reference.

TWO REFERENCE IMAGES:
- FIRST image: The APP SCREENSHOT to display on the phone screen.
- SECOND image: The STYLE TEMPLATE — an already-approved screenshot from the same set. Match its visual style EXACTLY.

HEADLINE TEXT:
- Line 1 (ACTION VERB): "{VERB_N}" — biggest, boldest text. White, uppercase, heavy/black sans-serif. Centred.
- Line 2 (BENEFIT): "{DESC_N}" — smaller than line 1, same font. White, uppercase, centred.
- Same text positioning as the style template

CALLOUT ANNOTATIONS (Act 2 — Build the Case):
Add 2–3 pill-shaped annotation callout bubbles pointing at specific UI elements on the app screen:
- Each callout is a pill/rounded-rectangle label containing 2–5 words
- A short arrow/line points precisely at the relevant UI element on the phone screen
- Use {ACCENT_COLOUR} pill colour OR white pill with dark text — pick one and be consistent
- Callouts must NOT overlap the headline text
- Highlight: [CALLOUT_1], [CALLOUT_2], [CALLOUT_3]

MATCH THE STYLE TEMPLATE EXACTLY:
- Same photorealistic Pixel device frame rendering — identical phone mockup, same size, position, shadows, reflections
- Same text treatment (font, weight, crispness, visual weight)
- Same background: {BRAND_COLOUR} (subtle gradient OK). No harsh glows or radial patterns.
- Same overall level of polish and aesthetic

DEVICE:
- Display this benefit's app screenshot on the phone screen
- Phone centred horizontally, floating with breathing room on all sides
- Bottom of device must NOT bleed off canvas edge (~80px clearance)
- Device width ~80% of canvas

BREAKOUT ELEMENTS (optional):
{BREAKOUT_INSTRUCTIONS}

CRITICAL RULES:
- The device frame MUST match the style template EXACTLY — do NOT reinvent it
- Background must be a clean, solid {BRAND_COLOUR} — no harsh light effects
- Device floats — visible breathing room below the device, bottom does NOT bleed
- No watermarks, no extra text, no Google Play UI chrome
```

---

## Prompt Template C — Act 3: "Eliminate Doubt" (Screenshots 5–8)

Use this for reassurance screenshots. Attach the app screenshot and style template.

```
Create an Act 3 reassurance screenshot for a Google Play Store screenshot SET.

TWO REFERENCE IMAGES:
- FIRST image: The APP SCREENSHOT to display on the phone screen.
- SECOND image: The STYLE TEMPLATE — match visual style EXACTLY.

ACT 3 PURPOSE — ELIMINATE DOUBT:
This screenshot should reassure potential users. Choose ONE focus:
- Complex data or analytics view that proves depth/power
- Social proof (review count, user count, rating)
- Secondary use case (shows the app is useful in more scenarios)
- CTA frame (optional final screenshot with "tap Install" message)

HEADLINE TEXT:
- Line 1 (ACTION VERB): "{VERB_N}" — same size/weight/position as style template
- Line 2 (BENEFIT): "{DESC_N}" — same size/weight/position as style template

MATCH THE STYLE TEMPLATE EXACTLY (same device frame, same font treatment, same background).

DEVICE: Pixel phone, floating with breathing room on all sides, bottom NOT bleeding off canvas edge.

No watermarks, no extra text, no Google Play UI chrome.
```

---

## Prompt Template D — Iteration / Refinement

Use when the user wants changes to an already-generated screenshot. Attach **three images**:
1. The app screenshot (layout reference)
2. The first approved screenshot (style template)
3. The version the user liked best (creative direction)

```
Refine this Google Play Store screenshot based on these three references:

- FIRST image: APP SCREENSHOT — defines the screen content to show on the phone
- SECOND image: STYLE TEMPLATE — the first approved screenshot in the set. Device frame, text treatment, and visual style MUST match this exactly.
- THIRD image: APPROVED DIRECTION — the version the user liked best. Match its creative approach, breakout elements, and secondary elements.

Generate a new version that keeps:
- Screen content from the app screenshot
- Device frame and visual style from the style template
- Creative direction from the approved version

WITH THESE CHANGES:
{USER_REQUESTED_CHANGES}

Maintain set-wide consistency. Background: solid {BRAND_COLOUR} (subtle gradient OK). Device floats with breathing room — bottom does NOT bleed off edge. No watermarks, no extra text, no Google Play UI chrome.
```

---

## Feature Graphic Template

Use this to generate the 1024×500 Feature Graphic (required for every Google Play listing).

```
Create a professional Google Play Feature Graphic at exactly 1024×500 px.

CONTENT:
- App icon (large, prominent — centred or slightly left of centre)
- Bold headline: "{FEATURE_GRAPHIC_HEADLINE}" — white, uppercase, heavy/black weight sans-serif. 5–7 words.
- Background: solid {BRAND_COLOUR} — same as the screenshot set

RULES:
- Output must be exactly 1024×500 px (landscape orientation)
- NO app UI screenshots — this is a brand/marketing asset only
- No alpha/transparency — save as JPG or 24-bit PNG
- Typography must match the screenshot set style (same font weight and treatment)
- This doubles as the video thumbnail if a promo video exists
- No watermarks, no extra text

This will be displayed prominently at the top of the Google Play Store listing.
```

---

## No Post-Generation Crop Needed

Unlike Apple's App Store, Google Play uses native 9:16 — no cropping or resizing is required after generation.

If your generator outputs exactly 1080×1920, your images are ready to upload directly.

Other accepted sizes (same 9:16 ratio):
- 720 × 1280 px
- 1440 × 2560 px
- Any resolution up to 3840px on the longest side

→ Validate the result with **[04-QUALITY-CHECKLIST.md](04-QUALITY-CHECKLIST.md)**
