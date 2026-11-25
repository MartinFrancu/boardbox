# One Punch Man - Cards v2 (text)

Legend: `#` = health cell (monster) / hole (hero stencil), `.` = empty.

Hero card fields:
- Cost: money to hire.
- Attack: what the hero does when deployed (uses a player's turn).
- Support: happens at the end of the round if the hero is hired but didn't attack.

Monster card fields:
- Level · Toll (civilians killed each round it survives) · Fame (tokens when
  killed) · Health (cells to cross out).
- Terminal: if yes, killing it ends the encounter.
- Extra: special rule.

---------------------------------------------------------------- HEROES

### Mumen Rider
Cost: 1
Attack: stencil of current class or lower.
Support: rescue 1 civilian (A/S: 2).
```
C       B       A       S
##      ###     ###     ###
                #.#     ###
```

### Snek
Cost: 1
Attack: stencil of current class or lower. Ambitious: if this attack
kills the monster, Snek moves up 1 extra ladder slot.
Support: none.
```
C       B       A       S
##      ##      ##.     ###
        .#      .##     .##
```

### Zombieman
Cost: 2
Attack: stencil of current class or lower. Can attack **twice** per
round.
Support: none.
```
C       B       A       S
#       ##      ###     ####
```

### Puri-Puri Prisoner
Cost: 2
Attack: stencil of current class or lower.
Support: rescue 1 civilian.
```
C       B       A       S
##      #.#     #..#    #..#
#.      ###     #..#    #..#
                ####    #..#
                        ####
```

### Metal Bat
Cost: 2
Attack: stencil of current class or lower. If he attacked this same
monster in an earlier round, also cross out 1 more health cell anywhere.
Support: none.
```
C       B       A       S
##      ###     ###     ####
        .#.     ###     ####
```

### Fubuki
Cost: 2
Attack: stencil of current class or lower.
Support: +1 money.
```
C       B       A       S
##      ##      ###     ###
        ##      #..     ###
                ###     ###
```

### Drive Knight
Cost: 2
Attack: stencil of current class or lower. May mirror it.
Support: none.
```
C       B       A       S
#.      ##.     ##..    ##...
##      .##     .##.    .##..
                ..##    ..##.
                        ...##
```

### Tank-Top Master
Cost: 2
Attack: stencil of current class or lower.
Support: this round's toll -1.
```
C       B       A       S
##      .#.     .#.     .##.
        ###     ###     ####
                ###     ####
```

### King
Cost: 2
Attack: crosses nothing. Instead, **Saitama appears** right now: take him out
of the hero deck (or discard pile).
Support: none.

### Genos
Cost: 3
Attack: stencil of current class or lower.
Support: cross out 1 health cell anywhere.
```
C       B       A        S
###     ####    #####    ######
                         ######
```

### Child Emperor
Cost: 3
Attack: stencil of current class or lower.
Support: look at the top 3 hero cards and
put them back in any order (can delay Saitama).
```
C       B       A        S
#.#     #.#     #.#.#    #.#.#
        ...     .....    .#.#.
        #.#     #.#.#    #.#.#
                         .#.#.
```

### Flashy Flash
Cost: 3
Attack: stencil of current class or lower. Attacking with Flash
doesn't end your turn; take another action.
Support: none.
```
C       B       A        S
#       #.#     #.#.#    #.#.#
                         .#.#.
```

### Silver Fang
Cost: 4
Attack: stencil of current class or lower.
Support: once per encounter, move a hero
ranked below him up 1 ladder slot.
```
C       B       A       S
#.      #..     ##..    ###..
.#      .#.     .##.    .###.
        ..#     ..##    ..###
```

### Atomic Samurai
Cost: 4
Attack: stencil of current class or lower.
Support: none.
```
C       B       A        S
#.#     #.#     #...#    #.#.#
        .#.     .#.#.    .#.#.
        #.#     ..#..    #.#.#
                .#.#.    .#.#.
                #...#    #.#.#
```

### Tatsumaki
Cost: 5
Attack: stencil of current class or lower.
Support: this round's toll -1.
```
C       B       A       S
#.#     .#.     ###     ####
        ###     #.#     #..#
        .#.     ###     #..#
                        ####
```

### Saitama
Cost: not hireable.
Attack: none.
Support: none.
Appears: when drawn into the roster (draw a replacement, he takes no roster
spot) or summoned by King. Stays until the encounter ends.
While present: at the end of each round he kills every monster in play and
takes all their fame (he moves up the ladder).
Ladder: starts in the bottom slot.

---------------------------------------------------------------- MONSTERS

### Mosquito Girl
Wolf · Toll 1 · Fame 1 · Health 5
Terminal: no
Extra: none.
```
#....#
......
..#...
......
#....#
```

### Frog Man
Wolf · Toll 1 · Fame 1 · Health 4
Terminal: no
Extra: none.
```
.##.
.##.
```

### Crablante
Wolf · Toll 1 · Fame 1 · Health 6
Terminal: no
Extra: none.
```
#....#
.####.
```

### Subterranean King
Wolf · Toll 1 · Fame 1 · Health 5
Terminal: no
Extra: none.
```
..#..
.###.
..#..
```

### Hammerhead
Tiger · Toll 2 · Fame 2 · Health 9
Terminal: no
Extra: none.
```
.###..
######
```

### Vaccine Man
Tiger · Toll 2 · Fame 2 · Health 11
Terminal: no
Extra: none.
```
..##..
.####.
.####.
..#...
```

### Marugori
Tiger · Toll 2 · Fame 2 · Health 10
Terminal: no
Extra: none.
```
.####.
######
```

### Beast King
Tiger · Toll 2 · Fame 2 · Health 9
Terminal: no
Extra: none.
```
#.##.#
.####.
..#...
```

### Carnage Kabuto
Demon · Toll 3 · Fame 3 · Health 14
Terminal: no
Extra: from his 3rd round alive, toll is doubled.
```
..##..
.####.
######
#....#
```

### Ancient King
Demon · Toll 3 · Fame 3 · Health 14
Terminal: no
Extra: none.
```
######
#....#
######
```

### Melzargard
Demon · Toll 3 · Fame 3 · Health 12
Terminal: no
Extra: at the end of each round, un-cross 2 health cells.
```
#.#.#.
.#.#.#
#.#.#.
.#.#.#
```

### Gouketsu
Demon · Toll 3 · Fame 3 · Health 15
Terminal: no
Extra: none.
```
.####.
##..##
##..##
.###..
```

### Deep Sea King
Demon · Toll 3 · Fame 4 · Health 16
Terminal: yes
Extra: toll +1 for each round he survives.
```
..##..
.####.
######
.####.
```

### Elder Centipede
Dragon · Toll 4 · Fame 5 · Health 20
Terminal: yes
Extra: armored; stencils with fewer than 4 holes do nothing.
```
######
#.....
######
.....#
######
```

### Boros
Dragon · Toll 5 · Fame 6 · Health 24
Terminal: yes
Extra: at the end of each round, un-cross 3 health cells.
```
.####.
######
##..##
######
.####.
```

---------------------------------------------------------------- LADDER SHEET

16 slots, best (1) to worst (16):
```
S: 1  2
A: 3  4  5
B: 6  7  8  9  10
C: 11 12 13 14 15 16
```
