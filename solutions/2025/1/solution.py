from math import ceil
from sys import argv

NUM_DIGITS = 100


def __1__(lines):
    dial = 50
    num_zero = 0

    for line in lines:
        direction, steps = line[0], int(line[1:])
        mult = -1 if direction == "L" else 1
        dial = (dial + mult * steps) % NUM_DIGITS
        num_zero += dial == 0

    return num_zero


def __2__(lines):
    dial = 50
    num_zero = 0

    for line in lines:
        direction, steps = line[0], int(line[1:])
        mult = -1 if direction == "L" else 1

        for _ in range(steps):
            dial = (dial + mult) % NUM_DIGITS
            num_zero += dial == 0

    return num_zero


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
