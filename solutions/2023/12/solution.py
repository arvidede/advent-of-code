import re
from collections import Counter
from itertools import product
from sys import argv

BROKEN = "#"
OPERATIONAL = "."
UNKNOWN = "?"


def build_expression(groups):
    pattern = "\.*"
    last = len(groups) - 1
    for i, group in enumerate(groups):
        pattern += f"#{{{group}}}\."
        pattern += "*" if i == last else "+"

    return re.compile(pattern)


def is_valid_arrangement(arrangement, expression):
    return bool(expression.match(arrangement))


cache = {}


def get_valid_arrangements(line):
    springs, groups = line
    # springs = "?".join(springs for _ in range(5))
    # groups = ",".join(groups for _ in range(5))
    groups = list(map(int, groups.split(",")))
    unknown_springs = [i for i, s in enumerate(springs) if s == UNKNOWN]
    num_broken = sum(groups)
    num_known_broken = sum(s == BROKEN for s in springs)
    num_unknown_broken = num_broken - num_known_broken
    num_unknown = len(unknown_springs)
    expression = build_expression(groups)

    arrangements = []

    for arrangement in product([".", "#"], repeat=num_unknown):
        if Counter(arrangement)[BROKEN] != num_unknown_broken:
            continue

        spring_arrangement = list(springs)

        for i, spring_index in enumerate(unknown_springs):
            spring_arrangement[spring_index] = arrangement[i]

        spring_arrangement = "".join(spring_arrangement)

        if is_valid_arrangement(spring_arrangement, expression):
            arrangements.append(spring_arrangement)

    return arrangements


def __1__(lines):
    return sum(len(get_valid_arrangements(line)) for line in lines)


def __2__(lines):
    return len(set([l[0] for l in lines]))


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return [line.split(" ") for line in open(file).read().splitlines()]


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
