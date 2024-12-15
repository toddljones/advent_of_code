from y2024.d5.data import puzzle, parse_rules_and_pages


class PrintQueue:
    def __init__(self, rules, pages):
        self.rules = rules
        self.pages = pages
        self.ordered_pages = []

    @staticmethod
    def middle_page(pages):
        return pages[len(pages) // 2]

    def map_ordered_pages(self):
        for page in self.pages:
            if self.page_is_ordered(page):
                self.ordered_pages.append(page)

    def page_is_ordered(self, page):
        for rule in self.rules:
            # get the 2 page numbers of the rule
            r0 = rule[0]
            r1 = rule[1]
            if r0 not in page or r1 not in page:
                continue
            if page.index(r0) > page.index(r1):
                return False
        return True

    def sum_middles_of_ordered_pages(self):
        self.map_ordered_pages()
        return sum(self.middle_page(page) for page in self.ordered_pages)


def p1():
    rules, pages = parse_rules_and_pages(puzzle)
    queue = PrintQueue(rules, pages)
    sum_middles = queue.sum_middles_of_ordered_pages()
    return sum_middles


if __name__ == "__main__":
    print(p1())
