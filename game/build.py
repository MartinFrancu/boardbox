"""Regenerate everything derived from game/cards.json.

Usage: python3 game/build.py
Outputs: CARDS.md, app/index.html (from app/app.src.html).
Fails if RULES.md version differs from cards.json version.
"""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'game/cards.json').read_text())
V = data['version']

rules_v = re.search(r'^Version: (\S+)', (ROOT / 'RULES.md').read_text(), re.M)
if not rules_v or rules_v.group(1) != V:
    sys.exit(f"Version mismatch: cards.json {V}, RULES.md {rules_v and rules_v.group(1)}")

moves = {m['id']: m for m in data['moves']}
holes = lambda g: sum(r.count('#') for r in g)

# ---------------- CARDS.md
out = [f"# One Punch Man - Cards v{V}", "",
       "Generated from `game/cards.json` by `game/build.py` - don't edit by hand.", "",
       "Legend: `#` = health cell (monster) / hole (move stencil), `.` = empty.", "",
       "Hero card fields:",
       "- Cost: money to hire.",
       "- Moves: the hero's move for each class (C / B / A / S). Stencils are in the Moves section.",
       "- Attack: what the hero does when deployed (uses a player's turn).",
       "- Support: happens at the end of the round if the hero is hired but didn't attack.", "",
       "Monster card fields:",
       "- Level · Toll (civilians killed each round it survives) · Fame (tokens when killed) · Health (cells to cross out).",
       "- Terminal: if yes, killing it ends the encounter.",
       "- Extra: special rule.", "",
       "-" * 64 + " HEROES", ""]
for h in data['heroes']:
    mv = ' · '.join(f"{c} {moves[h['moves'][c]]['name']}" for c in 'CBAS') if h['moves'] else 'none.'
    out += [f"### {h['name']}", f"Cost: {h['cost']}", f"Moves: {mv}",
            f"Attack: {h['attack']}", f"Support: {h['support']}", ""]
s = data['saitama']
out += [f"### {s['name']}", "Cost: not hireable.", "Moves: none.", "Attack: none.", "Support: none."]
out += [t for t in s['text'] if not t.startswith('Not hireable')] + [""]
out += ["-" * 64 + " MOVES (stencils, shared between heroes)", ""]
for m in data['moves']:
    users = [f"{h['name']} {c}" for h in data['heroes'] if h['moves'] for c in 'CBAS' if h['moves'][c] == m['id']]
    out += [f"### {m['name']} - {holes(m['grid'])} holes", "Used by: " + ', '.join(users), "```", *m['grid'], "```", ""]
out += ["-" * 64 + " MONSTERS", ""]
for m in data['monsters']:
    out += [f"### {m['name']}",
            f"{m['level']} · Toll {m['toll']} · Fame {m['fame']} · Health {holes(m['grid'])}",
            f"Terminal: {'yes' if m['terminal'] else 'no'}",
            f"Extra: {m['extra'] or 'none.'}", "```", *m['grid'], "```", ""]
lad = data['setup']['ladder']; n = 0; rows = []
for c in 'SABC':
    rows.append(f"{c}: " + '  '.join(str(i) for i in range(n + 1, n + lad[c] + 1))); n += lad[c]
out += ["-" * 64 + " LADDER SHEET", "", f"{n} slots, best (1) to worst ({n}):", "```", *rows, "```", ""]
(ROOT / 'CARDS.md').write_text('\n'.join(out))

# ---------------- app
src = (ROOT / 'app/app.src.html').read_text()
assert '/*__CARDS__*/null' in src
(ROOT / 'app/index.html').write_text(src.replace('/*__CARDS__*/null', json.dumps(data, ensure_ascii=False)))
print(f"Built v{V}: CARDS.md, app/index.html")
