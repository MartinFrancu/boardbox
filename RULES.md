# One Punch Man - Rules (draft)

Status: first draft. Parts marked **[Q#]** are still undecided. Each one has my
suggestion, and the suggestion is used until you decide otherwise.

## 1. Theme & goal
Players are executives of the Hero Association. Monsters attack the city;
you deploy heroes to kill them. You want to:
- keep civilians alive,
- build up your heroes' fame and rank,
- **not lean on Saitama**: he kills anything in one punch, but nobody gets the fame.

**[Q1] Co-op or competitive?**
Suggestion: **semi-co-op**. Everyone loses if too many civilians die. Each
executive manages their own heroes. At the end, the executive whose heroes
have the most fame wins.

**[Q2] How does the game end?**
Suggestion: after the monster deck (~8 monsters) is used up. Everyone loses
early if the city drops below X civilians.

## 2. Components (pen & paper)

### World board
- One sheet with ~6 districts, each with a row of civilian boxes (e.g. 8).
- Districts that border each other are marked as neighbours.
- A dead civilian = cross out a box with a pencil.

### Monster card
- A picture with a grid printed over it (e.g. 8×8).
- Some grid cells are marked as **health cells**. Cross them all out and the
  monster dies.
- To reuse the card, put it in a clear plastic sleeve and mark it with a
  dry-erase marker (or a pencil on tracing paper laid on top).
- The card also lists:
  - **Threat** (strength 1–5).
  - **Area effect**, typically "each round: kill 2 civilians in its district,
    1 in each neighbour".
  - **Fame**: points awarded when it dies (see [Q5]).
  - **Extra rules** (optional), e.g. "regenerates 2 cells per round".

### Hero card
- Name, picture, **cost**, and **rank** (C → B → A → S).
- **Attack pattern**: a small shape of cells (e.g. 4 cells in an L).
  Rank-dependent: each rank has its own, usually bigger, pattern printed on the
  card. Use the pattern for the hero's current rank.
- Pen & paper: the pattern is a **cardboard stencil with holes**. Lay it on the
  monster grid and mark through the holes. Alternative: the shape is drawn on
  the card and you copy it by hand.

**[Q3] Placement rules for the attack pattern?**
Suggestion: you may rotate it but not mirror it. It must lie fully inside the
monster's grid. Holes that land on empty or already-crossed cells are wasted.

### Trackers
- **Money** per executive (or shared, depending on Q1): a row of boxes / a
  tally on paper.
- **Fame & rank** per hero: a fame track on the hero card (e.g. 0–10 with
  rank-up marks at 3 / 6 / 10).

## 3. Round structure
1. **Monster appears**: if no monster is on the board, draw one from the
   monster deck. Roll a d6 to pick the district it lands in.
2. **Hero offer**: refill a market of 3 face-up hero cards from the hero deck.
3. **Executive turns**: in turn order, each executive takes **one** action:
   - **Hire**: pay a hero's cost and take them from the market.
   - **Deploy**: send one of your ready heroes to attack (apply their pattern
     to the monster). The hero is now *exhausted* until the next round.
   - **Pass**.
4. **Monster acts**: if the monster is still alive, apply its area effect
   (cross out civilians).
5. **Cleanup**: exhausted heroes become ready again.

**[Q4] Can a hero attack every round?**
Suggestion: yes (the "redeploy" you mentioned). Hiring is the main money sink,
so heroes are reusable.

## 4. Killing a monster
When the last health cell is crossed out:
- **Fame** goes to the heroes who hit it (see Q5) and moves their rank tracks.
- **Donations**: gain money = the surviving civilians in the attacked district.
- The monster card is discarded (wipe the sleeve).

**[Q5] How is fame split?**
Suggestion: some health cells are marked with a ★. Each ★ a hero crosses out =
+1 fame for that hero. Landing the killing blow = +2 fame.

## 5. Saitama
- Always available. Costs nothing. Can be deployed as an action.
- Kills any monster instantly (cross out the whole grid).
- **Nobody gets fame** for that monster, and you get **no donations** (people
  credit someone else / don't notice him).

**[Q6] What stops players from using Saitama every time?**
Suggestion: on top of the lost fame, he is unreliable. When deployed, roll a
d6. On 1–3 he's lost / at the supermarket and arrives at the end of the next
round, so the monster acts once more first.

## 6. Open questions not yet placed
- **[Q7] Multiple monsters at once?** Suggestion: one at a time for the first
  playtest.
- **[Q8] Civilians on the monster grid?** Suggestion: some grid cells show
  civilians. If a hero's pattern covers one, that civilian dies (cross out one
  in the district). Clumsy, strong heroes become risky.
