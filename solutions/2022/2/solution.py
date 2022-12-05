from sys import argv

outcomes = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6,
}
moves = {
    "AX": "Z",
    "AY": "X",
    "AZ": "Y",
    "BX": "X",
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X",
}


def __1__(lines):
    return sum(outcomes[line] for line in lines)


def __2__(lines):
    return __1__([f"{line[0]}{moves[line]}" for line in lines])


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = [line.replace(" ", "") for line in open(file).read().splitlines()]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
