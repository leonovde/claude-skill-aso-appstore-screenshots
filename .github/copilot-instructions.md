# Copilot Instructions

This file provides guidance to GitHub Copilot when working with code in this repository.

## What This Is

A GitHub Copilot agent skill (`aso-googleplay-screenshots`) that guides users through creating high-converting Google Play Store screenshots for their Android app. It is invoked by asking Copilot to use the `aso-googleplay-screenshots` skill from within a user's app project.

## Architecture

Four files + one asset make up the skill:

- **SKILL.md** — The skill prompt. Defines a multi-phase workflow: Benefit Discovery → Screenshot Pairing → Generation → Feature Graphic. Uses local `.aso-state/` files to persist state across conversations so users can resume mid-workflow. Generation first creates a deterministic scaffold via compose.py, then sends it to Nano Banana Pro for AI enhancement.
- **compose.py** — A standalone Python compositing script (Pillow-based) that deterministically renders Google Play screenshots. Takes a background hex colour, action verb, benefit descriptor, and app screenshot path, then produces a pixel-perfect 1080×1920 PNG with headline text, Pixel device frame template, and the screenshot composited inside. Also supports `--feature-graphic` mode to generate the required 1024×500 Feature Graphic. The verb text auto-sizes to fit the canvas width.
- **generate_frame.py** — Generates the Pixel device frame template PNG (`assets/device_frame.png`). Run once to create or update the template. The template is an 860×1570 RGBA PNG with a black Pixel body, transparent screen cutout, small centred camera hole-punch (no Dynamic Island), and side buttons (power + volume, no silent switch).
- **showcase.py** — Generates a showcase image showing up to 8 final screenshots side-by-side with an optional GitHub link at the bottom. Used as the final step after all screenshots are approved.
- **assets/device_frame.png** — Pre-rendered Pixel device frame template used by compose.py. Using a template instead of drawing the frame at compose time ensures pixel-perfect consistency across all generated screenshots.

## Running compose.py

```bash
# Requires: pip install Pillow
# Requires: Roboto Black font (or any heavy sans-serif) — auto-detected from system paths

# Generate a phone screenshot (1080×1920):
python3 .github/skills/aso-googleplay-screenshots/compose.py \
  --bg "#E31837" \
  --verb "TRACK" \
  --desc "TRADING CARD PRICES" \
  --screenshot path/to/app-screenshot.png \
  --output output.png

# Generate a Feature Graphic (1024×500):
python3 .github/skills/aso-googleplay-screenshots/compose.py \
  --bg "#E31837" \
  --feature-graphic \
  --headline "TRACK EVERY CARD IN YOUR COLLECTION" \
  --output feature-graphic.png
```

## Key Design Decisions

- **Two-stage generation**: compose.py creates a deterministic scaffold first (text + frame + screenshot), then Nano Banana Pro enhances it. This avoids the inconsistencies of generating from scratch.
- **compose.py outputs native Google Play dimensions** (1080×1920 for phone portrait) — no post-processing crop needed. Google Play uses 9:16 natively, unlike Apple's narrower ratio.
- **Device frame is a Pixel phone template** (`assets/device_frame.png`) — not an iPhone. No Dynamic Island, no silent switch. Camera hole-punch centred at top. Regenerate with `python3 .github/skills/aso-googleplay-screenshots/generate_frame.py` if the frame design needs updating.
- **Device floats with breathing room**: The Pixel device frame is fully contained within the canvas with ~80px of breathing room below it. It does NOT bleed off the bottom edge (this was the iOS style).
- **Verb text auto-sizes** — shrinks from 200px down to 110px to fit multi-word verbs within the canvas width.
- **SKILL.md always generates 3 versions in parallel** for each benefit so the user can pick the best one.
- **No crop step** — unlike the App Store workflow, Google Play uses native 9:16 so the output from compose.py is ready for Nano Banana enhancement and then direct upload to Google Play Console.
- **Local state files are central to the workflow** — benefits, screenshot assessments, pairings, brand colour, and generation state are all persisted in `.aso-state/` so users can resume across conversations.
- **Three-act narrative**: The skill plans 6–8 screenshots as Act 1 (hero), Act 2 (features + callout annotations), Act 3 (reassurance). This follows Google Play's recommended approach for maximising conversion.
