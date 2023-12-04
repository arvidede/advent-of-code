import re
from sys import argv


def get_matching(lines):
    return [len(winning.intersection(sample)) for winning, sample in lines]


def __1__(lines: list[tuple[set, set]]):
    return sum(
        bool(matching) * 2 ** (matching - 1)
        for matching in get_matching(lines)
    )


def __2__(lines: list[tuple[set, set]]):
    matching = get_matching(lines)
    cards = [1] * len(matching)

    for current, copies in enumerate(matching):
        next = current + 1
        last = current + copies + 1
        for card in range(next, last):
            cards[card] += cards[current]

    return sum(cards)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return [
        tuple(
            set(re.findall("\d{1,2}", numbers))
            for numbers in line.split(": ")[1].split(" | ")
        )
        for line in open(file).read().splitlines()
    ]


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
