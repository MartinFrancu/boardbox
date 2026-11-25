# One Punch Man - Rules (draft v2, simplest version)

Co-op, sandboxy. All players win or lose together.
**[S]** = my suggestion filling a gap. It stands until you change it.
**[Q#]** = still need your answer.

## Goal
Get through the whole monster deck with civilians still alive.
You lose if civilians reach 0.

## Components (pen & paper)
- **Civilians track**: one row of 30 boxes. A death = cross out a box. [S]
- **Money**: shared, tally marks on paper. Start with 5. [S]
- **Monster deck**: each monster card has
  - a picture with a grid overlay. Some cells are **health cells**; cross them
    all out to kill it. Use a plastic sleeve + dry-erase marker.
  - **Toll**: civilians it kills at the end of each round it survives.
  - **Fame**: how many fame tokens it drops when killed.
  - **Terminal** or not: a terminal monster ends the encounter when killed.
- **Hero deck**: each hero card has a name, a picture, and an attack pattern
  per class (C / B / A / S). Patterns are cardboard stencils with holes.
- **Saitama card**: shuffled into the hero deck (see Saitama).
- **Ladder** sheet: numbered slots, ranked best (1) to worst. Slots are grouped
  into classes, e.g. S: 1–3, A: 4–7, B: 8–12, C: 13–20 [S].
  Each hero has a token on the ladder.

## Setup
- Shuffle the monster deck. Shuffle the hero deck, Saitama included.
- Place every hero's token on the ladder in random order. [S, see Q3]

## Structure
- **Game** = encounters, until the monster deck is empty.
- **Encounter** = a chain of monsters, ending when a terminal monster dies.
- **Round** = the steps below, repeated within an encounter.

## Round
1. **Monster**: if no monster is in play, draw the next one.
2. **Roster**: discard the unhired heroes from last round's roster, then draw
   3 new heroes from the hero deck. [S]
   If Saitama is drawn, he **appears** (see Saitama).
3. **Deploy**: players take turns around the table. On your turn either
   - **hire** a hero from the roster: pay their cost [S, see Q2], then they
     attack; or
   - **reuse** an already-hired hero who hasn't acted this round (free); or
   - **pass**.

   Each hero acts at most once per round. The round's deploy step ends when
   everyone passes in a row.
4. **Attack**: lay the hero's stencil (for their current class) anywhere on the
   monster grid. You may rotate it but not mirror it. It must fit inside the
   grid. Cross out the health cells under the holes.
5. **Monster dies?** When all its health cells are crossed:
   - Its fame tokens are given out; the players decide together how.
     1 fame token = the hero moves **up one slot** on the ladder and swaps with
     the hero above. Crossing into a new class = new attack pattern (and cost).
   - Non-terminal: the next monster is drawn at the start of next round.
   - Terminal: the encounter ends (see End of encounter).
6. **Toll**: if a monster is still alive at the end of the round, cross out
   civilians equal to its toll.
7. **Saitama**: if he has appeared, he kills the monster now. Its fame tokens
   are lost.

## Saitama
- He is a card in the hero deck. When drawn, he appears and stays until the
  encounter ends.
- At the end of each round, he kills every monster in play. Fame from those
  monsters is lost.
- **So the players want to score fame before he shows up.**

## End of encounter
- **Payday**: gain 1 money per 3 living civilians. [S]
- **Regrowth**: add back 2 civilians (un-cross 2 boxes). [S]
- Hired heroes return to the hero deck. Reshuffle the deck with Saitama in it. [S]

## Q (need your answer)
- **[Q1]** "heroes have different actions, can also **save a monster**". Did you
  mean *save a civilian*? Suggestion: a hero can either **attack** or **rescue**
  (un-cross 1 civilian). Some heroes have special actions on their card.
- **[Q2]** Hiring cost: fixed per hero, or set by class? Suggestion: by class
  (C=1, B=2, A=3, S=5). Ranking up makes a hero stronger but pricier.
- **[Q3]** Ladder: are all heroes on it from the start, or only hired ones?
  Suggestion: all of them from the start, in random order.
- **[Q4]** Saitama trigger: is a card in the hero deck OK? An alternative is a
  timer, e.g. he arrives in round 4 of each encounter.
