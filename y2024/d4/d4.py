from typing import List

from y2024.d4.data import puzzle, s_as_list_of_lists


class WordSearch:
    """
    - find all occurrences of word
    - word can occur in any direction
    - directions include diagonal
    """

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
        "up_left": (-1, -1),
        "up_right": (1, -1),
        "down_left": (-1, 1),
        "down_right": (1, 1),
    }

    def __init__(self, grid: List[List[str]], word: str):
        self.grid = grid
        self.word = word.upper()
        self.occurrences: List[List[int]] = []

    def grid_to_upper(self):
        return [[cell.upper() for cell in row] for row in self]

    def coord(self, x: int, y: int):
        coord = None
        if x < 0 or y < 0:
            return coord
        try:
            coord = self.grid[y][x]
        except IndexError:
            coord = None
        return coord

    def map_all_occurrences(self):
        """
        start by finding all the first letters
        then, every time you hit a first letter, call
        another function that will check all directions
        to see if word is present. this function will save
        the results in the self.occurrences list of lists
        """
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == self.word[0]:
                    self.check_all_directions(x, y)

    def check_all_directions(self, x: int, y: int):
        for direction in self.directions.values():
            self.check_direction(x, y, direction)

    def check_direction(self, x: int, y: int, direction: tuple):
        """
        - retrieve the letters for the direction
        - use the length of the word to determine how many iterations to check
        - if you run out of real estate, stop
        - once you have the full letters, check if it's the word
        - if it is, save the coordinates
        - save the full coords of the words to occurrences
        """
        dx = direction[0]
        dy = direction[1]
        letters = []
        word_coords = []
        l_word = len(self.word)
        for i in range(l_word):
            coord = self.coord(x, y)
            if coord is None:
                break
            letters.append(coord)
            word_coords.append((x, y))
            x += dx
            y += dy
        if "".join(letters) == self.word:
            self.occurrences.append(word_coords)

    def count_occurrences(self):
        return len(self.occurrences)


def p1():
    grid = s_as_list_of_lists(puzzle)
    word_search = WordSearch(grid, "XMAS")
    word_search.map_all_occurrences()
    return word_search.count_occurrences()


if __name__ == "__main__":
    print(p1())
