from y2024.d1.data import puzzle_as_lists, _puzzle


def get_distance(l1: list, l2: list) -> int:
    _l1 = l1.copy()
    _l2 = l2.copy()
    _l1.sort()
    _l2.sort()
    distance = sum([abs(x - y) for x, y in zip(_l1, _l2)])
    return distance


def get_similarity(l1: list, l2: list) -> int:
    score = 0
    for i in l1:
        cnt = l2.count(i)
        score += i * cnt
    return score


def part1() -> None:
    l1, l2 = puzzle_as_lists(_puzzle)
    distance = get_distance(l1, l2)
    print(distance)


def part2() -> None:
    l1, l2 = puzzle_as_lists(_puzzle)
    similarity = get_similarity(l1, l2)
    print(similarity)


if __name__ == "__main__":
    part1()
    part2()
