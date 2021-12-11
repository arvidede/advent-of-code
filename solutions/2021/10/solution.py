from sys import argv
from functools import reduce

tags = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}

POINTS_1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def __1__(lines, points=POINTS_1):
    illegal = []
    corrupt = [0] * len(lines)
    for i, line in enumerate(lines):
        open_stack = []
        for c in line:
            if c in tags:
                open_stack.append(c)
                continue
            expected = tags[open_stack.pop()]
            if c != expected:
                illegal.append(points[c])
                corrupt[i] = 1
    print(sum(illegal))
    return corrupt


def __2__(lines, points=POINTS_2):
    scoring = lambda acc, t: 5 * acc + points[tags[t]]
    corrupt = __1__(lines)
    incomplete = [line for i, line in enumerate(lines) if not corrupt[i]]
    score = []
    for line in incomplete:
        open_stack = []
        for c in line:
            if c in tags:
                open_stack.append(c)
                continue
            open_stack.pop()
        score.append(reduce(scoring, reversed(open_stack), 0))
    return sorted(score)[int((len(score) - 1) / 2)]


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
