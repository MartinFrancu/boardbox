# One Punch Man - Cards v0.2

Generated from `game/cards.json` by `game/build.py` - don't edit by hand.

Legend: `#` = health cell (monster) / hole (move stencil), `.` = empty.
Monster grids include 1 empty border cell(s) on every side.

Hero card fields:
- Cost: money to hire.
- Moves: the hero's move for each class (C / B / A / S). Stencils are in the Moves section.
- Attack: what the hero does when deployed (uses a player's turn).
- Support: happens at the end of the round if the hero is hired but didn't attack.

Monster card fields:
- Level · Toll (civilians killed each round it survives) · Fame (tokens when killed) · Health (cells to cross out).
- Terminal: if yes, killing it ends the encounter.
- Extra: special rule.

---------------------------------------------------------------- HEROES

### Mumen Rider
Cost: 1
Moves: C One-Two · B Combo · A Arch · S Double Fist
Attack: one move of current class or lower.
Support: rescue 1 civilian (A/S: 2).

### Snek
Cost: 1
Moves: C One-Two · B Hook · A Zigzag · S Charge
Attack: one move of current class or lower. Ambitious: if this attack kills the monster, Snek moves up 1 extra ladder slot.
Support: none.

### Zombieman
Cost: 2
Moves: C Jab · B One-Two · A Combo · S Barrage
Attack: one move of current class or lower. Can attack twice per round.
Support: none.

### Puri-Puri Prisoner
Cost: 2
Moves: C Hook · B Arch · A Bear Hug · S Grand Hug
Attack: one move of current class or lower.
Support: rescue 1 civilian.

### Metal Bat
Cost: 2
Moves: C One-Two · B Hammer · A Double Fist · S Wall
Attack: one move of current class or lower. If he attacked this same monster in an earlier round, also cross out 1 more health cell anywhere.
Support: none.

### Fubuki
Cost: 2
Moves: C One-Two · B Block · A Gate · S Crush
Attack: one move of current class or lower.
Support: +1 money.

### Drive Knight
Cost: 2
Moves: C Hook · B Zigzag · A Cascade · S Long Cascade
Attack: one move of current class or lower. May mirror it.
Support: none.

### Tank-Top Master
Cost: 2
Moves: C One-Two · B Hammer · A Tank Press · S Avalanche
Attack: one move of current class or lower.
Support: this round's toll -1.

### King
Cost: 2
Moves: none.
Attack: crosses nothing. Instead, Saitama appears right now: take him out of the hero deck (or discard pile).
Support: none.

### Genos
Cost: 3
Moves: C Combo · B Barrage · A Beam · S Mega Beam
Attack: one move of current class or lower.
Support: cross out 1 health cell anywhere.

### Child Emperor
Cost: 3
Moves: C Twin Strike · B Four Corners · A Gadget Spread · S Missile Rain
Attack: one move of current class or lower.
Support: look at the top 3 hero cards and put them back in any order (can delay Saitama).

### Flashy Flash
Cost: 3
Moves: C Jab · B Twin Strike · A Flicker · S Lightning Step
Attack: one move of current class or lower. Attacking with Flash doesn't end your turn; take another action.
Support: none.

### Silver Fang
Cost: 4
Moves: C Slip · B Flowing Strike · A Cascade · S Torrent
Attack: one move of current class or lower.
Support: once per encounter, move a hero ranked below him up 1 ladder slot.

### Atomic Samurai
Cost: 4
Moves: C Twin Strike · B Cross Cut · A Big X · S Blade Storm
Attack: one move of current class or lower.
Support: none.

### Tatsumaki
Cost: 5
Moves: C Twin Strike · B Burst · A Ring · S Psychic Ring
Attack: one move of current class or lower.
Support: this round's toll -1.

### Saitama
Cost: not hireable.
Moves: none.
Attack: none.
Support: none.
Appears: when drawn into the roster (draw a replacement, he takes no roster spot) or summoned by King. Stays until the encounter ends.
While present: at the end of each round he kills every monster in play and takes all their fame (he moves up the ladder).
Ladder: starts in the bottom slot.

---------------------------------------------------------------- MOVES (stencils, shared between heroes)

### Jab - 1 holes
Used by: Zombieman C, Flashy Flash C
```
#
```

### One-Two - 2 holes
Used by: Mumen Rider C, Snek C, Zombieman B, Metal Bat C, Fubuki C, Tank-Top Master C
```
##
```

### Slip - 2 holes
Used by: Silver Fang C
```
#.
.#
```

### Twin Strike - 2 holes
Used by: Child Emperor C, Flashy Flash B, Atomic Samurai C, Tatsumaki C
```
#.#
```

### Combo - 3 holes
Used by: Mumen Rider B, Zombieman A, Genos C
```
###
```

### Flicker - 3 holes
Used by: Flashy Flash A
```
#.#.#
```

### Flowing Strike - 3 holes
Used by: Silver Fang B
```
#..
.#.
..#
```

### Hook - 3 holes
Used by: Snek B, Puri-Puri Prisoner C, Drive Knight C
```
##
.#
```

### Barrage - 4 holes
Used by: Zombieman S, Genos B
```
####
```

### Block - 4 holes
Used by: Fubuki B
```
##
##
```

### Four Corners - 4 holes
Used by: Child Emperor B
```
#.#
...
#.#
```

### Hammer - 4 holes
Used by: Metal Bat B, Tank-Top Master B
```
###
.#.
```

### Zigzag - 4 holes
Used by: Snek A, Drive Knight B
```
##.
.##
```

### Arch - 5 holes
Used by: Mumen Rider A, Puri-Puri Prisoner B
```
###
#.#
```

### Beam - 5 holes
Used by: Genos A
```
#####
```

### Burst - 5 holes
Used by: Tatsumaki B
```
.#.
###
.#.
```

### Charge - 5 holes
Used by: Snek S
```
###
.##
```

### Cross Cut - 5 holes
Used by: Atomic Samurai B
```
#.#
.#.
#.#
```

### Lightning Step - 5 holes
Used by: Flashy Flash S
```
#.#.#
.#.#.
```

### Cascade - 6 holes
Used by: Drive Knight A, Silver Fang A
```
##..
.##.
..##
```

### Double Fist - 6 holes
Used by: Mumen Rider S, Metal Bat A
```
###
###
```

### Gadget Spread - 6 holes
Used by: Child Emperor A
```
#.#.#
.....
#.#.#
```

### Gate - 7 holes
Used by: Fubuki A
```
###
#..
###
```

### Tank Press - 7 holes
Used by: Tank-Top Master A
```
.#.
###
###
```

### Bear Hug - 8 holes
Used by: Puri-Puri Prisoner A
```
#..#
#..#
####
```

### Long Cascade - 8 holes
Used by: Drive Knight S
```
##...
.##..
..##.
...##
```

### Ring - 8 holes
Used by: Tatsumaki A
```
###
#.#
###
```

### Wall - 8 holes
Used by: Metal Bat S
```
####
####
```

### Big X - 9 holes
Used by: Atomic Samurai A
```
#...#
.#.#.
..#..
.#.#.
#...#
```

### Crush - 9 holes
Used by: Fubuki S
```
###
###
###
```

### Torrent - 9 holes
Used by: Silver Fang S
```
###..
.###.
..###
```

### Avalanche - 10 holes
Used by: Tank-Top Master S
```
.##.
####
####
```

### Grand Hug - 10 holes
Used by: Puri-Puri Prisoner S
```
#..#
#..#
#..#
####
```

### Missile Rain - 10 holes
Used by: Child Emperor S
```
#.#.#
.#.#.
#.#.#
.#.#.
```

### Mega Beam - 12 holes
Used by: Genos S
```
######
######
```

### Psychic Ring - 12 holes
Used by: Tatsumaki S
```
####
#..#
#..#
####
```

### Blade Storm - 13 holes
Used by: Atomic Samurai S
```
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#
```

---------------------------------------------------------------- MONSTERS

### Mosquito Girl
Wolf · Toll 1 · Fame 1 · Health 5
Terminal: no
Extra: none.
```
........
.#....#.
........
...#....
........
.#....#.
........
```

### Frog Man
Wolf · Toll 1 · Fame 1 · Health 4
Terminal: no
Extra: none.
```
......
..##..
..##..
......
```

### Crablante
Wolf · Toll 1 · Fame 1 · Health 6
Terminal: no
Extra: none.
```
........
.#....#.
..####..
........
```

### Subterranean King
Wolf · Toll 1 · Fame 1 · Health 5
Terminal: no
Extra: none.
```
.......
...#...
..###..
...#...
.......
```

### Hammerhead
Tiger · Toll 2 · Fame 2 · Health 9
Terminal: no
Extra: none.
```
........
..###...
.######.
........
```

### Vaccine Man
Tiger · Toll 2 · Fame 2 · Health 11
Terminal: no
Extra: none.
```
........
...##...
..####..
..####..
...#....
........
```

### Marugori
Tiger · Toll 2 · Fame 2 · Health 10
Terminal: no
Extra: none.
```
........
..####..
.######.
........
```

### Beast King
Tiger · Toll 2 · Fame 2 · Health 9
Terminal: no
Extra: none.
```
........
.#.##.#.
..####..
...#....
........
```

### Carnage Kabuto
Demon · Toll 3 · Fame 3 · Health 14
Terminal: no
Extra: from his 3rd round alive, toll is doubled.
```
........
...##...
..####..
.######.
.#....#.
........
```

### Ancient King
Demon · Toll 3 · Fame 3 · Health 14
Terminal: no
Extra: none.
```
........
.######.
.#....#.
.######.
........
```

### Melzargard
Demon · Toll 3 · Fame 3 · Health 12
Terminal: no
Extra: at the end of each round, un-cross 2 health cells.
```
........
.#.#.#..
..#.#.#.
.#.#.#..
..#.#.#.
........
```

### Gouketsu
Demon · Toll 3 · Fame 3 · Health 15
Terminal: no
Extra: none.
```
........
..####..
.##..##.
.##..##.
..###...
........
```

### Deep Sea King
Demon · Toll 3 · Fame 4 · Health 16
Terminal: yes
Extra: toll +1 for each round he survives.
```
........
...##...
..####..
.######.
..####..
........
```

### Elder Centipede
Dragon · Toll 4 · Fame 5 · Health 20
Terminal: yes
Extra: armored; stencils with fewer than 4 holes do nothing.
```
........
.######.
.#......
.######.
......#.
.######.
........
```

### Boros
Dragon · Toll 5 · Fame 6 · Health 24
Terminal: yes
Extra: at the end of each round, un-cross 3 health cells.
```
........
..####..
.######.
.##..##.
.######.
..####..
........
```

---------------------------------------------------------------- LADDER SHEET

16 slots, best (1) to worst (16):
```
S: 1  2
A: 3  4  5
B: 6  7  8  9  10
C: 11  12  13  14  15  16
```
