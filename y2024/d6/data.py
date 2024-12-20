from typing import List

sample = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

puzzle = """.....#......................................................#...................#.........................................#..#....
.......................#.......#...............................................#.................#...#.......#..............#.....
.........#.................................................................#.....................##...............................
.....#..#.............#.......................#..#....#............#.............................................#................
............#................##............................................#.##..................#.................#.....#...#....
....................................................................#..#.................#.....#................#....#.....#......
.#.........##.................##................#..............................................#..................................
...................#..................#.......#......#......................#..#...................#.........#...............#.#..
.......................#.#.........#...............#....................#........#.............#..................................
......#...........#........................................#........#.........#...............#.#.........#.......................
...#...........................................................#...........#............................#.........................
...........#............................#.#........#...#........#........................................................#........
.........#................................................#...#..#........#............#................#.........................
..#.....................................................................#...............#.........#....#.......#..................
.......................#....#..#............#.........#.............#...................##....................................#...
..................#...................................................................#.....................#...................#.
............................#..........................#.....#...........##.......................................................
........................#.............................#...............#..............................#.........................#..
.....................#..........#...#.....#....#..............#...........................................#...............#.#.....
...................................#.................................#......#..................#..................................
.#.....#.......##......#..................#...............................................#.........................#.........#...
.................#...............#..............................#............................................#......#.............
...#.........#................#...#....................#......................#.#......#.............#............................
.............#..........##....#...#................#.............#.............#............................................#.....
.....#............................................................................................................#...............
........................#..........................##........#........................................#........#..................
..........................#.....##.#.............#.........#..............................#..............................#........
..............#.....................#...............................................#..................................#..........
...#................................................#.........#.....................#..........................................#..
.##..............#..........#......................................................................#.........#........#.........#.
...##.#.....#........#..........................#.............................#..........#.#..#...................................
..................................#...#......#......#................#..#.....................................#...#...............
.........................................................................................#..................#......#..............
.................#....................#..#....#..............................#........##...#.......#...............#..............
...#.................#................#..................................#..................##....##.....#............#...........
..........#...#....................##......................#.....#...........#......#......#.............##....#...#........#.#...
............................#......#.........#..............................................................#........#............
.........................................#.........................................................#...............#.............#
.....#..........#..#........#................................................................................##......#............
.#................#.....................................................................................#.....#...................
..............#........#..................................#..............................##.......................................
........................#.....................#..............................#..................#.............................#.##
#...........................................................#..##........#........................................................
..............#...............#.........#...........^.....................................................#...#.........##..#.....
......................................................#.......................................#..............#...............#....
...#....#..................#....#.......................#.#..........#.......#.................#................................#.
#.........................................................................................................#.......................
..........................#......................................................................#.............#..................
................#...............................................................#........#........................................
..........#............#...............#.#........................................................................................
....#.....#............#.....##.........#......##.................#.......#................#...............................#...#..
................................................................................#...#.......................................#.....
.#........................................#.................................................................#.#...................
.......#....#...................................................................................#...........#..#.............#....
...#...#...............................................................................................................#..........
..#....................................#......#.................#.........................................................#.......
...........................................#......#.........#.##........##..#.........#..........................#....##.#....#...
.........................#...............#............................................................................#...........
................................................#................#..................#..#...........#.......................#.....#
..........................................................#..........#........................................#...................
..................#...................#................##.........#...........................#...................................
............................#.................................................................#...........#.#.....................
................#.......................#.........................................................................#....#..........
#..........#..............#.#............................................................................................#........
..........................................................................................#.......#.........................#....#
...........................................#.......#................................................................#...#.........
..#...................#........................................#..............#.......................#...........................
.......................#..............................#...........................#......#......................#........#........
.....#................................................................................#....#......................................
..#..................................#.........#....#............#....#..............#.............#......#.........#......#....#.
.......##.................................................................................................#.#....#................
............................................#.....#...................#...........#.........#.....................................
...............#.........................................#.............................#.........................#............#...
..............................................##..................................................#........................#......
..................................................................................................#.................#............#
......................#.......................#.........#......................................................................#..
..#...........................#...........................................................................#.....#........#........
..........#....................#...........................##................................................................#....
.........#........#...........................................#........##.........................................................
....#.............................#....................#.................#..........................#........................#....
.......................................#...#....#...............................................#.................................
............#............................................#..............................#..........#......#.......................
.#..............................#...........#........#...............................#.#......#..................................#
#................#..#.............................................................................................................
................................#................#............#....#.#..................##.....................#...............#.#
#....##................#...........#....#..#..........#.....................#..........................#.....................#....
............................................................................................#.....................................
.......................#................................................##..................................#.....................
....#.....#..#................................................................................................##..................
..........................#......#...#...#..........#...#................#.................................................#......
............................#....#.#.......#..........#............................................#..............................
......#...........#......................#..#.....................................................................................
.........................................#...................................................##...............#............#...##.
...................................#.#............................................................................................
......................#........##..................................................#..............................................
...................#......................................................#......#.............................#...........#......
......#................#................................................................................#..................#......
..#.........................#.....#..............#.........#...................#.......................................#..........
..................#..............................................#......#.#.......................................................
...........#.....................................................................#.......................#........................
.......#.........###.....................#........................................................................................
...............#...#..........#........................#....................#......#............#..................#..............
.............#.......#.............#....................................................#.....................................#...
.............................................................................#.#...............................#..#...............
.........##..........#..#.#.................................................................................#................#....
.#..................#.....................................#...................#.#..............#...........................#......
........#.....#...........................#..........................#.............................#...............#..............
#.........#.#.......................................................................................................#.............
..#...................................................................#............#...#.........#................................
..................#......#........#...........#......................#........#..#.......................................#...#..#.
.......................................................#.............#...........#............................#............#......
..............................................#....................................................................#..............
.............#....................#.......................#.............#..........#.........#.............#....#.......#.....#...
...#...................#...............#........#.............#.................#..........#........#................#............
...........#...............#.....................#.................................................#...#.....#.....#..............
....#......................................#......#..............................#...........#.....#..................#...........
#.........#...................#.........#............#............#..............#..........#...........#...#.#..##...............
...........................................................#..................#......#..................#...............#.........
...........#.......................#.........................................................#.......#..............#..........#..
.................................#.....#.....#..............................#..........#..............#............#..............
...............#.......................................................................##.........#...........................#...
....#...............#.........#.#...........#.......#.#..#....#...................................................................
.........#.............................................#.......................................................#..........##......
......................................#...............#.......#..#..#.#...................#....................#.#................
.................#..................................................................#..........................#.....#......#.#...
..#...........#..................#..............#.....#......#.................#..............##.......#...#.......#.......#......
......................................#.....................#..........#............................................##.#..........
#......#................#........................................................#....#....##..................#.................#
............##..............##..........#........##.....................................#..........#..............................
.#.##............#.................#...................#....#...#...............................................#................."""


def puzzle_as_list_of_list(p: str) -> List[List[str]]:
    return [list(x.strip()) for x in p.splitlines()]
