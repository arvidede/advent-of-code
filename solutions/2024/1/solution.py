from collections import Counter
from sys import argv


def __1__(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def __2__(left, right):
    right_occurrences = Counter(right)
    return sum(l * right_occurrences.get(l, 0) for l in left)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = [
        list(map(int, line.split("   "))) for line in open(file).read().splitlines()
    ]
    return list(zip(*lines))


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
