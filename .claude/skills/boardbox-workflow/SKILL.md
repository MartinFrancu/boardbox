---
name: boardbox-workflow
description: How to work in the boardbox repo - a sandbox for rapid board game concept exploration. Use at the start of any task in this repo, when starting a new game concept, when deciding what goes to master, or when a game concept matures and the workflow should get more rigorous.
---

# Boardbox workflow

Boardbox is a sandbox for exploring board game ideas fast.

## Branches

- **One branch per game concept**, named after the game in kebab-case
  (e.g. `one-punch-man`).
- **Work only on the current game's branch.** Never commit game work to `master`.
- **`master` holds only shared, reusable stuff**: tools, templates, helpers or
  conventions that would speed up testing of *other* games.
- Promoting something to `master` happens only when the user agrees it is
  generally useful. Then: commit it on `master` and merge `master` into the game
  branches that want it.
- If unsure which branch you are on or should be on, ask.

## Maturity stages

Every game starts in stage 1. Move up only when the user says so.

### 1. Prototype (default)
Goal: test whether an idea is fun or interesting, as fast as possible.
- Anything goes: throwaway scripts, single-file HTML, hardcoded values,
  markdown notes, sketches.
- No tests, no structure, no polish. Speed over quality.
- Prefer cutting a feature over building it properly.

### 2. Playtest
Goal: the concept holds up; make it reliable enough to play repeatedly.
- Keep rules in one written, up-to-date rules doc.
- Clean up the code that is actually used; delete dead experiments.
- Add tests for rule logic that keeps breaking.

### 3. Robust
Goal: the game is worth keeping and building on.
- Clear project structure, tests for core rules, documented decisions.
- Changes are reviewed before committing.
- Look for parts worth promoting to `master`.

## Files on each game branch

### `README.md` - where we are (keep it short, ~10 lines)
```
# <Game name>
Stage: 1 - prototype
Now: <what we are working on right now, 1-2 lines>
Pitch: <the game in 1-2 sentences>
```
Update `Stage` and `Now` whenever they change.

### `IDEAS.md` - idea log
Every idea the user brings up gets logged here, even passing ones.
```
## Open
- <idea> (<date>)
## Done
- <idea> (<date>)
## Dismissed
- <idea> - <why, one line> (<date>)
```
- Never delete ideas; move them between sections.
- **This is a record, not a to-do list.** Always do what the user asks now.
  Don't steer work toward open ideas or remind the user of them unless asked.

## Habits
- Commit often with short messages; push the game branch.
