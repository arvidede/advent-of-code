import re
from math import gcd
from sys import argv

COST = {"A": 3, "B": 1}


def f(a, b, price):
    # a_x * a + b_x * b = p_x
    # a_y * a + b_y * b = p_y

    a_x, a_y = a
    b_x, b_y = b
    p_x, p_y = price

    b_0 = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)
    a_0 = (p_x - b_0 * b_x) / a_x

    if int(a_0) != a_0 or int(b_0) != b_0:
        return 0

    return int(a_0) * COST["A"] + int(b_0) * COST["B"]


def __1__(lines):
    return sum(f(*line) for line in lines)


def __2__(lines):
    offset = 10000000000000
    lines = [(a, b, (price[0] + offset, price[1] + offset)) for a, b, price in lines]
    return __1__(lines)


def parse_line(line):
    a = tuple(map(int, re.search("Button A: X\+(\d+), Y\+(\d+)", line).groups()))
    b = tuple(map(int, re.search("Button B: X\+(\d+), Y\+(\d+)", line).groups()))
    prize = tuple(map(int, re.search("Prize: X=(\d+), Y=(\d+)", line).groups()))

    return a, b, prize


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().split("\n\n")
    return list(map(parse_line, lines))


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
