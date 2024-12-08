from y2024.d1.d1 import get_distance, get_similarity
from y2024.d1.data import puzzle_as_lists, _sample
from typing import Tuple, List

sample_l1 = [3, 4, 2, 1, 3, 3]
sample_l2 = [4, 3, 5, 3, 9, 3]


def test_get_distance():
    assert get_distance(sample_l1, sample_l2) == 11


def test_puzzle_as_lists():
    l1, l2 = puzzle_as_lists(_sample)
    assert l1 == sample_l1
    assert l2 == sample_l2


def test_get_distance_with_empty_lists():
    assert get_distance([], []) == 0


def test_get_distance_with_identical_lists():
    identical_list = [1, 2, 3, 4, 5]
    assert get_distance(identical_list, identical_list) == 0


def test_get_similarity():
    assert get_similarity(sample_l1, sample_l2) == 31
