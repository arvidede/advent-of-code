import re
from sys import argv

INT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

DIGITS = re.compile("(?=(one|two|three|four|five|six|seven|eight|nine|\d))")


def get_first_last(line):
    digits = DIGITS.findall(line)
    return int(f"{INT_MAP[digits[0]]}{INT_MAP[digits[-1]]}")


def __1__(lines):
    return sum(map(get_first_last, lines))


def __2__(lines):
    return __1__(lines)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
