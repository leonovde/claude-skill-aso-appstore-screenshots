# ASO App Store Screenshots

A GitHub Copilot agent skill that generates high-converting App Store screenshots for your iOS app. It analyzes your codebase, identifies core benefits, and creates professional screenshot images using AI.

## What It Does

1. **Benefit Discovery** — Analyzes your app's codebase to identify the 3-5 core benefits that drive downloads
2. **Screenshot Pairing** — Reviews your simulator screenshots, rates them, and pairs each with the best benefit
3. **Generation** — Creates polished App Store screenshots using a two-stage process: deterministic scaffolding (compose.py) + AI enhancement (Nano Banana Pro via Gemini MCP)
4. **Showcase** — Generates a preview image with all screenshots side-by-side

## Installation

### 1. Add the skill to your project

Copy the skill directory into your project's `.github/skills/` folder:

```bash
# From your app's project root
mkdir -p .github/skills
cp -r path/to/aso-appstore-screenshots .github/skills/aso-appstore-screenshots
```

Or for personal use across all projects, copy to your user-level Copilot skills directory:

```bash
mkdir -p ~/.copilot/skills
cp -r path/to/aso-appstore-screenshots ~/.copilot/skills/aso-appstore-screenshots
```

### 2. Install Python dependencies

```bash
pip install Pillow
```

### 3. Font requirement

The skill uses **SF Pro Display Black** for headline text. On macOS, install it from [Apple's developer fonts](https://developer.apple.com/fonts/). The expected path is:

```
/Library/Fonts/SF-Pro-Display-Black.otf
```

### 4. Set up Gemini MCP (for AI enhancement)

The generation phase requires [@houtini/gemini-mcp](https://www.npmjs.com/package/@houtini/gemini-mcp) to be configured as an MCP server:

```bash
npm install -g @houtini/gemini-mcp
```

Then add it to your MCP configuration (e.g., project `.mcp.json` or your editor's global MCP settings).

## Usage

From within your app's project directory, ask GitHub Copilot to use the skill:

```
Use the aso-appstore-screenshots skill to generate App Store screenshots for my app.
```

The skill will guide you through each phase interactively. Progress is saved to `.aso-state/` files in your project directory, so you can resume across conversations.

## How It Works

### Scaffold → Enhance Pipeline

Rather than generating screenshots from scratch (which produces inconsistent results), the skill uses a two-stage approach:

1. **compose.py** creates a deterministic scaffold with exact text positioning, device frame, and your simulator screenshot composited inside
2. **Nano Banana Pro** (via Gemini MCP) enhances the scaffold — adding a photorealistic device frame, breakout elements, and visual polish

This ensures consistent layout across all screenshots while letting AI handle the creative enhancement.

### Output

Screenshots are saved to a `screenshots/` directory in your project:

```
screenshots/
  01-benefit-slug/          ← working versions
    scaffold.png            ← deterministic compose.py output
    v1.png, v2.png, v3.png  ← AI-enhanced versions
    v1-resized.png, ...     ← cropped to App Store dimensions
  final/                    ← approved screenshots, ready to upload
    01-benefit-slug.png
    02-benefit-slug.png
  showcase.png              ← preview image with all screenshots
```

The `final/` folder contains App Store-ready screenshots at exact Apple dimensions (default: 1290×2796px for iPhone 6.7").

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
| `.github/skills/aso-appstore-screenshots/SKILL.md` | The skill prompt — defines the multi-phase workflow |
| `.github/skills/aso-appstore-screenshots/compose.py` | Deterministic scaffold generator (Pillow-based) |
| `.github/skills/aso-appstore-screenshots/generate_frame.py` | Generates the device frame template |
| `.github/skills/aso-appstore-screenshots/showcase.py` | Generates the side-by-side showcase image |
| `.github/skills/aso-appstore-screenshots/assets/device_frame.png` | Pre-rendered iPhone device frame template |

## License

MIT
