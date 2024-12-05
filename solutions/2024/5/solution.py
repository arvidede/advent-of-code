from collections import defaultdict
from sys import argv


def is_valid(update, rules):
    for i, before in enumerate(update):
        for after in update[(i + 1) :]:

            if not after in rules[before]:
                return False
    return True


def order(update: list[int], rules):
    ordered = update.copy()

    for i_before, before in enumerate(update):
        for i_after in range(i_before + 1, len(update)):
            after = update[i_after]

            if not after in rules[before]:
                ordered[i_before], ordered[i_after] = after, before
                return order(ordered, rules)

    return ordered


def middle(numbers: list[int]):
    return numbers[len(numbers) // 2]


def __1__(rules, updates):
    return sum([middle(update) for update in updates if is_valid(update, rules)])


def __2__(rules, updates):
    return sum(
        [
            middle(order(update, rules))
            for update in updates
            if not is_valid(update, rules)
        ]
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    rules, updates = open(file).read().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]

    rule_map = defaultdict[int, set](set)

    for before, after in rules:
        if before in rule_map:
            rule_map[before].add(after)
        else:
            rule_map[before] = set([after])

    return rule_map, updates


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
