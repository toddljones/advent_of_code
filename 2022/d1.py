class Elves:
    def __init__(self):
        self.elves = []

    def add_elves(self, calorie_list):
        elf = Elf()
        for calories in calorie_list:
            if calories == "":
                self.elves.append(elf)
                elf = Elf()
                continue
            elf.add_snack(calories)
        self.elves.append(elf)

    def max_calories(self):
        return self.compute_max_calories(self.elves)

    def top_three(self):
        elves = self.elves.copy()
        top_three = []
        for i in range(3):
            top_three.append(self.compute_max_calories(elves, pop_elf=True))
        return sum(top_three)

    @staticmethod
    def compute_max_calories(elves, pop_elf=False):
        max_index = 0
        max_calories = 0
        for i, elf in enumerate(elves):
            if elf.sum_calories() > max_calories:
                max_calories = elf.sum_calories()
                max_index = i
        if pop_elf:
            elves.pop(max_index)
        return max_calories
    



class Elf:
    def __init__(self):
        self.snacks = []

    def add_snack(self, calories):
        self.snacks.append(int(calories))

    def sum_calories(self):
        return sum(self.snacks)


def generate_calorie_list(file_path):
    return open(file_path).read().splitlines()


def test_most_caloric_elf():
    elves = Elves()
    calorie_list = generate_calorie_list("2022/d1.test")
    elves.add_elves(calorie_list)
    max_calories = elves.max_calories()
    assert max_calories == 24000


def test_top_three():
    elves = Elves()
    calorie_list = generate_calorie_list("2022/d1.test")
    elves.add_elves(calorie_list)
    top_three = elves.top_three()
    assert top_three == 45000


if __name__ == "__main__":
    elves = Elves()
    elves.add_elves(generate_calorie_list("2022/d1.prod"))
    max_calories = elves.max_calories()
    print("max_calories", max_calories)
    top_three = elves.top_three()
    print("top_three", top_three)
