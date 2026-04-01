# Benefit Discovery

> Extracts 3–5 high-converting benefit headlines from app information.
> Referenced by: [00-SYSTEM.md](00-SYSTEM.md) · Feeds into: [03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md)

## What You Need

Any combination of: app description, feature list, Google Play listing, README, screenshots, or the app itself. The more context, the better the benefits.

## How to Extract Benefits

### Step 1: Understand the App

From the provided information, determine:
- **Core functionality** — What does the app actually DO?
- **Target audience** — Who is this for? (age, interests, skill level)
- **Unique value** — What makes it different from competitors?
- **Problems solved** — What pain does it relieve?
- **#1 install reason** — Why would someone tap "Install"?

### Step 2: Draft 3–5 Benefit Headlines

Each benefit MUST follow this format:

```
[ACTION VERB]  +  [BENEFIT DESCRIPTOR]
   Line 1              Line 2
  (big text)        (smaller text)
```

**Action verb rules:**
- Single strong verb: TRACK, SEARCH, BUILD, BOOST, FIND, CREATE, SAVE, SORT, SHARE, LEARN, PLAY, TURN, ADD, etc.
- Can be 1-2 words max (e.g., "TURN YOURSELF" counts as the verb line)
- ALL CAPS, biggest text on the screenshot

**Benefit descriptor rules:**
- Completes the sentence started by the verb
- Focuses on what the USER gets, not what the app does technically
- Specific enough to be compelling — "TRADING CARD PRICES" not "YOUR COLLECTION"
- ALL CAPS, smaller than verb but still bold

### Step 3: Validate

For each benefit, ask:
- ✅ Does it start with a strong action verb?
- ✅ Is it specific (not generic)?
- ✅ Does it answer "why should I install this?"
- ✅ Can I pair it with a visually compelling screenshot?
- ✅ Is it different enough from the other benefits?

### Examples

| App Type | Benefit 1 | Benefit 2 | Benefit 3 |
|----------|-----------|-----------|-----------|
| Card price tracker | TRACK · TRADING CARD PRICES | SEARCH · ANY CARD INSTANTLY | BUILD · YOUR COLLECTION |
| Meditation app | FIND · YOUR CALM | TRACK · DAILY STREAKS | SLEEP · BETTER TONIGHT |
| Fitness app | CRUSH · YOUR WORKOUTS | TRACK · EVERY REP | BUILD · REAL STRENGTH |
| Bible app | SEARCH · ANY VERSE IN SECONDS | SAVE · YOUR FAVOURITES | READ · WITH DAILY PLANS |

## Screenshot Pairing

Once you have 3–5 benefits, pair each with the best app screenshot:

- **Relevance**: Does the screenshot directly demonstrate this benefit?
- **Visual impact**: Is the screen rich with content, colour, and activity?
- **Clarity**: Can a user understand it at Google Play thumbnail size?
- **Uniqueness**: Don't reuse the same screenshot for multiple benefits

**Never use**: empty states, placeholder data, settings pages, login screens, loading indicators, or screens with sparse content.

## Brand Colour Selection

If no brand colour is provided, determine one automatically:

1. Check the app's UI for accent/brand colours (material theme, colour constants)
2. Pick a colour that **complements** the screenshots (makes app screens pop, doesn't clash)
3. Must be **bold and saturated** — muted/pastel gets lost in Google Play
4. Avoid white/light grey (disappears) and colours too close to the app UI's dominant colour

## Feature Graphic Headline

Also plan a separate **Feature Graphic headline** (5–7 words) for the 1024×500 brand asset that appears at the top of the Google Play listing. This should be the single most compelling statement about the app — not the same wording as any individual screenshot headline, but a broader brand promise.

## Output

After this phase you should have:

```
App: [App Name]
Audience: [Target audience]

Benefits:
1. [VERB] · [DESCRIPTOR]  →  [screenshot-1.png]
2. [VERB] · [DESCRIPTOR]  →  [screenshot-2.png]
3. [VERB] · [DESCRIPTOR]  →  [screenshot-3.png]
4. [VERB] · [DESCRIPTOR]  →  [screenshot-4.png]  (optional)
5. [VERB] · [DESCRIPTOR]  →  [screenshot-5.png]  (optional)

Feature Graphic Headline: [5-7 word brand headline]

Brand Colour: [Name] (#HEXCODE)
```

→ Take these to **[03-GENERATION-PROMPT.md](03-GENERATION-PROMPT.md)** for image generation.
