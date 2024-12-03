import re
from sys import argv


def __1__(line):

    return sum(
        int(a) * int(b)
        for a, b in [op.split(",") for op in re.findall(r"mul\((\d+,\d+)\)", line)]
    )


def __2__(line):
    score = 0
    enabled = True

    for do, dont, op in re.findall(r"(do\(\))|(don't\(\))|mul\((\d+,\d+)\)", line):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            a, b = op.split(",")
            score += int(a) * int(b)

    return score


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return open(file).read()


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
