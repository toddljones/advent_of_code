def test_parse_rules_and_pages():
    from y2024.d5.data import parse_rules_and_pages

    input = """47|53
    97|13
    
    75,47,61
    97,61,53"""

    expected = (
        [(47, 53), (97, 13)],
        [[75, 47, 61], [97, 61, 53]],
    )

    output = parse_rules_and_pages(input)

    assert output == expected


def test_middle_page():
    from y2024.d5.d5 import PrintQueue

    pages = [1, 2, 3, 4, 5]

    expected = 3

    output = PrintQueue.middle_page(pages)

    assert output == expected


def test_page_is_ordered():
    from y2024.d5.d5 import PrintQueue

    rules = [(47, 53), (97, 13)]
    pages = [[75, 47, 61, 53]]

    expected = True

    output = PrintQueue(rules, pages).page_is_ordered(pages[0])

    assert output == expected


def test_sum_middles_of_ordered_pages():
    from y2024.d5.d5 import PrintQueue
    from y2024.d5.data import sample, parse_rules_and_pages

    rules, pages = parse_rules_and_pages(sample)

    expected = 143

    output = PrintQueue(rules, pages).sum_middles_of_ordered_pages()

    assert output == expected


def test_correct_page_order():
    from y2024.d5.d5 import PrintQueue

    rules = [(47, 53), (97, 13)]
    pages = [[75, 53, 47, 61]]

    expected = [75, 47, 53, 61]

    output = PrintQueue(rules, pages).correct_page_order(pages[0])

    assert output == expected


def test_reorder_misordered_pages():
    from y2024.d5.d5 import PrintQueue
    from y2024.d5.data import sample, parse_rules_and_pages

    pages = [
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]

    rules, _ = parse_rules_and_pages(sample)

    queue = PrintQueue(rules, pages)
    queue.map_ordered_pages()
    queue.reorder_misordered_pages()

    expected = [
        [97, 75, 47, 61, 53],
        [61, 29, 13],
        [97, 75, 47, 29, 13],
    ]

    output = queue.misordered_pages

    assert output == expected


def test_sum_middles_of_reordered_misordered_pages():
    from y2024.d5.d5 import PrintQueue
    from y2024.d5.data import sample, parse_rules_and_pages

    rules, pages = parse_rules_and_pages(sample)

    expected = 123

    output = PrintQueue(rules, pages).sum_middles_of_reordered_misordered_pages()

    assert output == expected
