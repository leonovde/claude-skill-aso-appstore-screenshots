# ASO Google Play Screenshots

A GitHub Copilot agent skill that generates high-converting Google Play Store screenshots for your Android app. It analyzes your codebase, identifies core benefits, and creates professional screenshot images using AI.

## What It Does

1. **Benefit Discovery** — Analyzes your app's codebase to identify the 3–5 core benefits that drive installs
2. **Screenshot Pairing** — Reviews your app screenshots, rates them, and pairs each with the best benefit
3. **Generation** — Creates polished Google Play screenshots using a two-stage process: deterministic scaffolding (compose.py) + AI enhancement (Nano Banana Pro via Gemini MCP)
4. **Feature Graphic** — Generates the required 1024×500 Feature Graphic for your Play Store listing
5. **Showcase** — Generates a preview image with up to 8 screenshots side-by-side

## Installation

### 1. Add the skill to your project

Copy the skill directory into your project's `.github/skills/` folder:

```bash
# From your app's project root
mkdir -p .github/skills
cp -r path/to/aso-googleplay-screenshots .github/skills/aso-googleplay-screenshots
```

Or for personal use across all projects, copy to your user-level Copilot skills directory:

```bash
mkdir -p ~/.copilot/skills
cp -r path/to/aso-googleplay-screenshots ~/.copilot/skills/aso-googleplay-screenshots
```

### 2. Install Python dependencies

```bash
pip install Pillow
```

### 3. Font requirement

The skill uses **Roboto Black** for headline text — Google's product font. Install it from [Google Fonts](https://fonts.google.com/specimen/Roboto). The skill will automatically find it if installed at a standard system font path, or fall back to another heavy sans-serif if Roboto is not available.

### 4. Set up Gemini MCP (for AI enhancement)

The generation phase requires [@houtini/gemini-mcp](https://www.npmjs.com/package/@houtini/gemini-mcp) to be configured as an MCP server:

```bash
npm install -g @houtini/gemini-mcp
```

Then add it to your MCP configuration (e.g., project `.mcp.json` or your editor's global MCP settings).

## Usage

From within your app's project directory, ask GitHub Copilot to use the skill:

```
Use the aso-googleplay-screenshots skill to generate Google Play Store screenshots for my app.
```

The skill will guide you through each phase interactively. Progress is saved to `.aso-state/` files in your project directory, so you can resume across conversations.

## How It Works

### Scaffold → Enhance Pipeline

Rather than generating screenshots from scratch (which produces inconsistent results), the skill uses a two-stage approach:

1. **compose.py** creates a deterministic scaffold with exact text positioning, Pixel device frame, and your app screenshot composited inside
2. **Nano Banana Pro** (via Gemini MCP) enhances the scaffold — adding a photorealistic device frame, breakout elements, callout annotations, and visual polish

This ensures consistent layout across all screenshots while letting AI handle the creative enhancement.

### Three-Act Narrative Structure

The skill generates 6–8 screenshots following a story arc:

- **Act 1 — Screenshot 1** ("Stop the Scroll"): Hero shot — single powerful headline, one impressive app screen
- **Act 2 — Screenshots 2–4** ("Build the Case"): Feature-led frames with callout annotation bubbles
- **Act 3 — Screenshots 5–8** ("Eliminate Doubt"): Reassurance — data depth, social proof, secondary use cases

### Google Play Native 9:16

Unlike Apple's App Store (which uses a narrower non-standard ratio), Google Play uses native 9:16. This means **no post-generation cropping is needed** — compose.py outputs 1080×1920 px directly, which is ready to upload to Google Play Console.

### Output

Screenshots are saved to a `screenshots/` directory in your project:

```
screenshots/
  01-benefit-slug/          ← working versions
    scaffold.png            ← deterministic compose.py output
    v1.png, v2.png, v3.png  ← AI-enhanced versions
  final/                    ← approved screenshots, ready to upload
    01-benefit-slug.png
    02-benefit-slug.png
    feature-graphic.png     ← 1024×500 Feature Graphic
  showcase.png              ← preview image with all screenshots
```

The `final/` folder contains Google Play-ready screenshots at 1080×1920 px and the Feature Graphic at 1024×500 px.

### State Files

Progress is persisted in `.aso-state/` at the project root:

```
.aso-state/
  benefits.md     ← confirmed benefits, target audience, brand colour
  pairings.md     ← screenshot assessments and benefit-to-screenshot pairings
  generation.md   ← generation status, approved versions, final file paths
```

## Files

| File | Purpose |
|------|---------|
| `.github/skills/aso-googleplay-screenshots/SKILL.md` | The skill prompt — defines the multi-phase workflow |
| `.github/skills/aso-googleplay-screenshots/compose.py` | Deterministic scaffold generator (Pillow-based); outputs 1080×1920 or 1024×500 Feature Graphic |
| `.github/skills/aso-googleplay-screenshots/generate_frame.py` | Generates the Pixel device frame template |
| `.github/skills/aso-googleplay-screenshots/showcase.py` | Generates the side-by-side showcase image (up to 8 screenshots) |
| `.github/skills/aso-googleplay-screenshots/assets/device_frame.png` | Pre-rendered Pixel device frame template |

## License

MIT
