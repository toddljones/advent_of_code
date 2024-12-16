from y2024.d6.data import puzzle, puzzle_as_list_of_list
from typing import Dict, List


class GuardGallivant:

    move: Dict[str, List[int]] = {
        "up": [0, -1],
        "down": [0, 1],
        "left": [-1, 0],
        "right": [1, 0],
    }

    next_direction: Dict[str, str] = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up",
    }

    spaces: Dict[str, str] = {
        ".": "empty",
        "#": "wall",
        None: "wall",
    }

    def __init__(self, puzzle: List[List[str]]):
        self.puzzle = puzzle
        self.heading = "up"
        self.max_x_index = len(puzzle[0]) - 1
        self.max_y_index = len(puzzle) - 1
        self.coords_visited: List[List[int]] = []
        self.current_coord: List[int] = self.initial_coord()
        self.log_visited(*self.current_coord)

    def initial_coord(self) -> List[int]:
        for y, row in enumerate(self.puzzle):
            for x, coord in enumerate(row):
                if coord == "^":
                    return [x, y]

    def get_coord(self, x: int, y: int, direction: str) -> str:
        mx, my = self.move[direction]
        next_x = x + mx
        next_y = y + my
        if (
            next_x < 0
            or next_x > self.max_x_index
            or next_y < 0
            or next_y > self.max_y_index
        ):
            return None
        coord = self.puzzle[next_y][next_x]
        if coord == "^":
            coord = "."
        return coord

    def log_visited(self, x: int, y: int):
        self.coords_visited.append([x, y])

    def gallivant(self):
        for i in range(10000):
            x, y = self.current_coord
            next_coord = self.get_coord(*self.current_coord, self.heading)
            if next_coord == "#":
                self.heading = self.next_direction[self.heading]
                continue
            if next_coord == ".":
                next_x = x + self.move[self.heading][0]
                next_y = y + self.move[self.heading][1]
                self.current_coord = [next_x, next_y]
                self.log_visited(next_x, next_y)
            if next_coord == None:
                return self.coords_visited

        return None


def p1():
    puzzle_list = puzzle_as_list_of_list(puzzle)
    guard_gallivant = GuardGallivant(puzzle_list)
    coords_visited = guard_gallivant.gallivant()
    return len(set(tuple(coord) for coord in coords_visited))


if __name__ == "__main__":
    print(p1())
