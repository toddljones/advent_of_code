from typing import List
from y2024.d2.data import get_reports, puzzle


def check_all_increasing_or_decreasing(l: list[int]) -> bool:
    safe = all(l[i] < l[i + 1] for i in range(len(l) - 1)) or all(
        l[i] > l[i + 1] for i in range(len(l) - 1)
    )
    return safe


def check_gradual_increasing_or_decreasing(l: list[int]) -> bool:
    safe = all(abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))
    return safe


def count_safe_reports(reports: List[List[int]]) -> int:
    return sum(check_report(report) for report in reports)


def count_safe_reports_with_tolerance(reports: List[List[int]]) -> int:
    safe = 0
    for report in reports:
        if check_report(report):
            safe += 1
        else:
            # pop one element at a time and check if the report is safe
            l_report = len(report)
            for i in range(l_report):
                if check_report(report[:i] + report[i + 1 :]):
                    safe += 1
                    break
    return safe


def check_report(report: List[int]) -> bool:
    return check_all_increasing_or_decreasing(
        report
    ) and check_gradual_increasing_or_decreasing(report)


def part1() -> None:
    reports = get_reports(puzzle)
    print(count_safe_reports(reports))


def part2() -> None:
    reports = get_reports(puzzle)
    print(count_safe_reports_with_tolerance(reports))


if __name__ == "__main__":
    part1()
    part2()
