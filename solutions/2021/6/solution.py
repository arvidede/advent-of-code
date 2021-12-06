from sys import argv
from collections import Counter

RESET_TIMER, INITIAL_TIMER = 6, 8


def __1__(lines, num_days=80):
    fish_count = {idx: 0 for idx in range(INITIAL_TIMER + 1)} | dict(
        Counter(list(map(int, lines)))
    )
    fish_keys = sorted(fish_count)

    for day in range(num_days):
        resets = fish_count[0]
        for key in fish_keys[:-1]:
            fish_count[key] = fish_count[key + 1]
        fish_count[RESET_TIMER] += resets
        fish_count[INITIAL_TIMER] = resets
    return sum(fish_count.values())


def __2__(lines):
    return __1__(lines, 256)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().split(",")
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
