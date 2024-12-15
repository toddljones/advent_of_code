from y2024.d5.data import puzzle, parse_rules_and_pages
from typing import List, Tuple


class PrintQueue:
    def __init__(self, rules: List[Tuple[int, int]], pages: List[List[int]]) -> None:
        self.rules = rules
        self.pages = pages
        self.ordered_pages: List[List[int]] = []
        self.misordered_pages: List[List[int]] = []

    @staticmethod
    def middle_page(pages) -> int:
        return pages[len(pages) // 2]

    def map_ordered_pages(self) -> None:
        for page in self.pages:
            if self.page_is_ordered(page):
                self.ordered_pages.append(page)
            else:
                self.misordered_pages.append(page)

    def page_is_ordered(self, page) -> bool:
        for rule in self.rules:
            # get the 2 page numbers of the rule
            r0 = rule[0]
            r1 = rule[1]
            if r0 not in page or r1 not in page:
                continue
            if page.index(r0) > page.index(r1):
                return False
        return True

    def sum_middles_of_ordered_pages(self) -> int:
        self.map_ordered_pages()
        return sum(self.middle_page(page) for page in self.ordered_pages)

    def correct_page_order(self, page):
        for rule in self.rules:
            # get the 2 page numbers of the rule
            r0 = rule[0]
            r1 = rule[1]
            if r0 not in page or r1 not in page:
                continue
            if page.index(r0) > page.index(r1):
                # delete the r0 item and move it before the r1 item
                page.remove(r0)
                page.insert(page.index(r1), r0)
        return page

    def reorder_misordered_pages(self):
        for page in self.misordered_pages:
            while not self.page_is_ordered(page):
                page = self.correct_page_order(page)

    def sum_middles_of_reordered_misordered_pages(self):
        self.map_ordered_pages()
        self.reorder_misordered_pages()
        return sum(self.middle_page(page) for page in self.misordered_pages)


def p1():
    rules, pages = parse_rules_and_pages(puzzle)
    queue = PrintQueue(rules, pages)
    sum_middles = queue.sum_middles_of_ordered_pages()
    return sum_middles


def p2():
    rules, pages = parse_rules_and_pages(puzzle)
    queue = PrintQueue(rules, pages)
    sum_middles = queue.sum_middles_of_reordered_misordered_pages()
    return sum_middles


if __name__ == "__main__":
    print(p1())
    print(p2())
