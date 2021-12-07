from sys import argv
from collections import Counter
from math import sqrt


def gss(f, a, b, tol=1e-5):
    gr = (sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return f((b + a) / 2)


def minimize_cost(lines, distance):
    positions = list(map(int, lines))
    a = min(positions)
    b = max(positions)
    f = lambda x: sum(distance(x, p) for p in positions)
    return gss(f, a, b)


def __1__(lines):
    distance = lambda a, b: abs(round(a) - b)
    return minimize_cost(lines, distance)


def __2__(lines):
    distance = lambda a, b: sum(range(1, abs(round(a) - b) + 1))
    return minimize_cost(lines, distance)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().split(",")
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
