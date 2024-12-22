from collections import Counter
from sys import argv


def split(stone):
    stone_str = f"{stone}"
    mid = len(stone_str) // 2
    return int(stone_str[:mid]), int(stone_str[mid:])


def is_even(num):
    return len(f"{num}") % 2 == 0


cache = {}


def blink(stone, n_blinks):
    if n_blinks == 0:
        return 1

    if (stone, n_blinks) in cache:
        return cache[(stone, n_blinks)]

    if stone == 0:
        size = blink(1, n_blinks - 1)
    elif is_even(stone):
        left, right = split(stone)
        size = blink(left, n_blinks - 1) + blink(right, n_blinks - 1)
    else:
        size = blink(stone * 2024, n_blinks - 1)

    cache[(stone, n_blinks)] = size

    return size


def __1__(stones, n_blinks=25):
    return sum(blink(stone, n_blinks) for stone in stones)


def __2__(stones):
    return __1__(stones, 75)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = list(map(int, open(file).read().split(" ")))
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
