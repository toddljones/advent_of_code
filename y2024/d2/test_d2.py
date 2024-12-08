from data import get_reports, sample

sample_reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def test_get_reports():
    assert get_reports(sample) == sample_reports


def test_check_all_increasing_or_decreasing():
    from d2 import check_all_increasing_or_decreasing

    assert check_all_increasing_or_decreasing([1, 2, 3, 4, 5])
    assert check_all_increasing_or_decreasing([5, 4, 3, 2, 1])
    assert not check_all_increasing_or_decreasing([1, 2, 3, 4, 1])
    assert not check_all_increasing_or_decreasing([1, 2, 3, 3, 4])


def test_check_gradual_increasing_or_decreasing():
    from d2 import check_gradual_increasing_or_decreasing

    assert check_gradual_increasing_or_decreasing([1, 2, 3, 4, 5])
    assert check_gradual_increasing_or_decreasing([5, 4, 3, 2, 1])
    assert check_gradual_increasing_or_decreasing([1, 2, 3, 4, 1])
    assert check_gradual_increasing_or_decreasing([1, 2, 3, 3, 4])
    assert not check_gradual_increasing_or_decreasing([1, 2, 3, 7, 8])
    assert not check_gradual_increasing_or_decreasing([9, 8, 7, 3, 2])


def test_count_safe_reports():
    from d2 import count_safe_reports

    assert count_safe_reports(sample_reports) == 2


def test_count_safe_reports_with_tolerance():
    from d2 import count_safe_reports_with_tolerance

    assert count_safe_reports_with_tolerance(sample_reports) == 4
