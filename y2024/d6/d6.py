from y2024.d6.data import puzzle, puzzle_as_list_of_list
from typing import Dict, List
import copy
from tqdm import tqdm


class GuardGallivant:

    move: Dict[str, List[int]] = {
        "up": [0, -1],
        "down": [0, 1],
        "left": [-1, 0],
        "right": [1, 0],
        None: [0, 0],
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
        self.inital_heading = self.heading
        self.max_x_index = len(puzzle[0]) - 1
        self.max_y_index = len(puzzle) - 1
        self.coords_visited: List[List[int]] = []
        self.initial_coord: List[int] = self.get_initial_coord()
        self.current_coord: List[int] = self.initial_coord
        self.infinite_loop_obstacle_coords: List[List[int]] = []
        self.log_visited(*self.current_coord)

    def get_initial_coord(self) -> List[int]:
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
                continue
            if next_coord == None:
                return self.coords_visited

        return None

    def place_obstacles(self):
        """
        - place obstacles in all coords
        - test to see if a infinite loop is encountered
        - log the coord to infinite_loop_obstacle_coords
        -- this code sucks, really needs to track if it's overlapping where
           it has already been, but i'm being lazy and will just let the inefficent
           code run, as it only has to run once
        """
        # save a copy of the beginning state
        puzzle_copy = copy.deepcopy(self.puzzle)
        coord_copy = copy.deepcopy(self.initial_coord)
        heading_copy = self.heading
        for x in tqdm(range(self.max_x_index + 1)):
            for y in tqdm(range(self.max_y_index + 1)):
                self.puzzle = copy.deepcopy(puzzle_copy)
                self.current_coord = copy.deepcopy(coord_copy)
                self.heading = heading_copy
                if self.get_coord(x, y, None) in ["."]:
                    self.puzzle[y][x] = "#"
                    if not self.gallivant():
                        self.infinite_loop_obstacle_coords.append([x, y])
        return len(set(tuple(coord) for coord in self.infinite_loop_obstacle_coords))


def p1():
    puzzle_list = puzzle_as_list_of_list(puzzle)
    guard_gallivant = GuardGallivant(puzzle_list)
    coords_visited = guard_gallivant.gallivant()
    return len(set(tuple(coord) for coord in coords_visited))


def p2():
    puzzle_list = puzzle_as_list_of_list(puzzle)
    guard_gallivant = GuardGallivant(puzzle_list)
    cnt_infinite_loop_coords = guard_gallivant.place_obstacles()
    return cnt_infinite_loop_coords


if __name__ == "__main__":
    print(p1())
    print(p2())
