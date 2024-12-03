import pytest


def item_priority(i):
    if ord(i) >= ord("a"):
        return ord(i) - ord("a") + 1
    else:
        return ord(i) - ord("A") + 26 + 1


def chunk_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


class Rucksacks:
    def __init__(self):
        self.rucksacks = []

    def add(self, rucksack):
        self.rucksacks.append(rucksack)

    def get_sum_dupes_priority(self):
        priority_of_dupes = []
        for rucksack in self.rucksacks:
            priority_of_dupes.append(rucksack.priority_of_dupe())
        return sum(priority_of_dupes)

    def get_sum_group_priorities(self):
        # divide into groups and calculate priorities
        priorities = []
        for group in chunk_list(self.rucksacks, 3):
            # get unique items for each rucksack in current group
            uniques = []
            for rucksack in group:
                uniques.extend(rucksack.get_uniques())
            # find the item that occurs 3 times
            badge = [x for x in set(uniques) if uniques.count(x) == 3][0]
            priorities.append(item_priority(badge))
        return sum(priorities)


class Rucksack:
    def __init__(self, content) -> None:
        self.items = content

    def get_dupe(self):
        """
        rucksack contains 2 compartments
        need to first convert the compartments into sets, then see if an item is in both
        """
        compartment1 = list(set(self.items[0 : int(len(self.items) / 2)]))
        compartment2 = list(set(self.items[int(len(self.items) / 2) :]))
        combined = compartment1 + compartment2
        dupes = [x for x in combined if combined.count(x) > 1]
        return dupes[0]

    def priority_of_dupe(self):
        dupe = self.get_dupe()
        return item_priority(dupe)

    def get_uniques(self):
        return list(set(self.items))


@pytest.mark.parametrize(
    "test_input,expected_value",
    [
        ("a", 1),
        ("b", 2),
        ("p", 16),
        ("s", 19),
        ("t", 20),
        ("v", 22),
        ("z", 26),
        ("A", 27),
        ("L", 38),
        ("P", 42),
        ("Z", 52),
    ],
)
def test_item_priority(test_input, expected_value):
    test_output = item_priority(test_input)
    assert test_output == expected_value


def test_get_sum_priority_of_dupes():
    sum_dupes = get_sum_priority_of_dupes("2022/d3.test")
    assert sum_dupes == 157


def test_rucksack_dupe_priority():
    content = "vJrwpWtwJgWrhcsFMMfFFhFp"
    rucksack = Rucksack(content=content)
    assert rucksack.get_dupe() == "p"
    test_output = rucksack.priority_of_dupe()
    assert test_output == 16


def get_sum_priority_of_dupes(path):
    rucksacks = Rucksacks()
    contents = open(path).read().splitlines()
    for content in contents:
        rucksack = Rucksack(content)
        rucksacks.add(rucksack)
    return rucksacks.get_sum_dupes_priority()


def test_get_sum_priority_of_groups():
    sum_groups = get_sum_priority_of_groups("2022/d3.test")
    assert sum_groups == 70


def get_sum_priority_of_groups(path):
    rucksacks = Rucksacks()
    contents = open(path).read().splitlines()
    for content in contents:
        rucksack = Rucksack(content)
        rucksacks.add(rucksack)
    return rucksacks.get_sum_group_priorities()


if __name__ == "__main__":
    test_get_sum_priority_of_dupes()
    sum_priority_of_dupes = get_sum_priority_of_dupes("2022/d3.prod")
    print("sum_priority_of_dupes", sum_priority_of_dupes)
    sum_priority_of_groups = get_sum_priority_of_groups("2022/d3.prod")
    print("sum_priority_of_groups", sum_priority_of_groups)
