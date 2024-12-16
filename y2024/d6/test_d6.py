import pytest
from y2024.d6.data import sample, puzzle_as_list_of_list
from y2024.d6.d6 import GuardGallivant


@pytest.fixture
def sample_input():
    return puzzle_as_list_of_list(sample)


@pytest.fixture
def guard_gallivant(sample_input):
    return GuardGallivant(sample_input)


def test_puzzle_as_list_of_lists():
    from y2024.d6.data import puzzle_as_list_of_list

    input = """abc
    def"""

    expected = [["a", "b", "c"], ["d", "e", "f"]]

    output = puzzle_as_list_of_list(input)

    assert output == expected


def test_get_coord(guard_gallivant):
    assert guard_gallivant.get_coord(0, 1, "up") == "."
    assert guard_gallivant.get_coord(0, 1, "left") == None
    assert guard_gallivant.get_coord(0, 6, "right") == "#"


def test_log_visited(guard_gallivant):
    guard_gallivant.log_visited(0, 1)
    assert guard_gallivant.coords_visited == [[4, 6], [0, 1]]
    guard_gallivant.log_visited(0, 1)
    assert guard_gallivant.coords_visited == [[4, 6], [0, 1], [0, 1]]
    guard_gallivant.log_visited(1, 1)
    assert guard_gallivant.coords_visited == [[4, 6], [0, 1], [0, 1], [1, 1]]


def test_initial_coord(guard_gallivant):
    assert guard_gallivant.initial_coord() == [4, 6]


def test_gallivant(guard_gallivant):
    expected = [
        [4, 6],
        [4, 5],
        [4, 4],
        [4, 3],
        [4, 2],
        [4, 1],
        [5, 1],
        [6, 1],
        [7, 1],
        [8, 1],
        [8, 2],
        [8, 3],
        [8, 4],
        [8, 5],
        [8, 6],
        [7, 6],
        [6, 6],
        [5, 6],
        [4, 6],
        [3, 6],
        [2, 6],
        [2, 5],
        [2, 4],
        [3, 4],
        [4, 4],
        [5, 4],
        [6, 4],
        [6, 5],
        [6, 6],
        [6, 7],
        [6, 8],
        [5, 8],
        [4, 8],
        [3, 8],
        [2, 8],
        [1, 8],
        [1, 7],
        [2, 7],
        [3, 7],
        [4, 7],
        [5, 7],
        [6, 7],
        [7, 7],
        [7, 8],
        [7, 9],
    ]

    actual = guard_gallivant.gallivant()

    assert actual == expected
