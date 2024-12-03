class Pair:
    def __init__(self, pair):
        self.pair = pair
        self.derive_ranges()
        self.overlaps = self.check_overlap(self.r1, self.r2)

    def derive_ranges(self):
        self.r1 = dict(
            lbound=int(self.pair.split(",")[0].split("-")[0]),
            ubound=int(self.pair.split(",")[0].split("-")[1]),
        )

        self.r2 = dict(
            lbound=int(self.pair.split(",")[1].split("-")[0]),
            ubound=int(self.pair.split(",")[1].split("-")[1]),
        )

    @staticmethod
    def check_overlap(r1, r2):
        for a, b in ((r1, r2), (r2, r1)):
            if a["lbound"] >= b["lbound"] and a["ubound"] <= b["ubound"]:
                return True
        return False


def count_overlapping_pairs(path):
    inputs = open(path).read().splitlines()
    overlapping_pairs = 0
    for input in inputs:
        pair = Pair(input)
        if pair.overlaps:
            overlapping_pairs += 1
    return overlapping_pairs


def test_count_overlapping_pairs():
    path = "2022/d4.test"
    assert count_overlapping_pairs(path) == 2


if __name__ == "__main__":
    overlapping_pairs = count_overlapping_pairs("2022/d4.prod")
    print("overlapping_pairs", overlapping_pairs)
