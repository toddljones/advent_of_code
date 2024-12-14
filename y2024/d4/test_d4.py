def test_s_as_list_of_lists():
    from y2024.d4.data import s_as_list_of_lists

    test_input = """MMMS
    MSAM"""

    expected_output = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]


def test_s_as_list_of_lists():
    from y2024.d4.data import s_as_list_of_lists

    test_input = """MMMS
    MSAM"""

    expected_output = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]

    output = s_as_list_of_lists(test_input)

    assert output == expected_output


def test_word_search_coord():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")

    assert word_search.coord(0, 0) == "M"
    assert word_search.coord(3, 0) == "S"
    assert word_search.coord(2, 1) == "A"
    assert word_search.coord(4, 0) is None
    assert word_search.coord(0, 2) is None


def test_map_all_occurrences():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")
    word_search.map_all_occurrences()

    expected_occurrences = [[(1, 1), (2, 1), (3, 1)]]

    assert word_search.occurrences == expected_occurrences


def test_check_all_directions():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")
    word_search.check_all_directions(1, 1)

    expected_occurrences = [[(1, 1), (2, 1), (3, 1)]]

    assert word_search.occurrences == expected_occurrences


def test_check_direction():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")
    word_search.check_direction(1, 1, (1, 0))

    expected_occurrences = [[(1, 1), (2, 1), (3, 1)]]

    assert word_search.occurrences == expected_occurrences


def test_count_occurrences():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")
    word_search.map_all_occurrences()

    assert word_search.count_occurrences() == 1


def test_coord():
    from y2024.d4.d4 import WordSearch

    grid = [
        ["M", "M", "M", "S"],
        ["M", "S", "A", "M"],
    ]
    word_search = WordSearch(grid, "SAM")

    assert word_search.coord(0, 0) == "M"
    assert word_search.coord(3, 0) == "S"
    assert word_search.coord(2, 1) == "A"
    assert word_search.coord(4, 0) is None
    assert word_search.coord(0, 2) is None
    assert word_search.coord(3, -1) is None


def test_p1_sample():
    from y2024.d4.d4 import WordSearch
    from y2024.d4.data import sample, s_as_list_of_lists

    expected_result = 18

    word_search = WordSearch(s_as_list_of_lists(sample), "XMAS")
    word_search.map_all_occurrences()
    result = word_search.count_occurrences()

    assert result == expected_result
