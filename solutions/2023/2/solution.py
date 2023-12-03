from functools import reduce
from sys import argv


def parse_game(line):
    id, line = line.split(": ")
    id = int(id.split(" ")[1])

    sets = [
        {
            color: int(amount)
            for amount, color in [cube.split(" ") for cube in s.split(", ")]
        }
        for s in line.split("; ")
    ]

    return id, sets


def is_valid_game(bag, game):
    for cubes in game:
        for color in bag:
            if color in cubes and cubes[color] > bag[color]:
                return False
    return True


def min_valid_game(game):
    bag = {}
    for cubes in game:
        for color in cubes:
            if (
                color in bag and cubes[color] > bag[color]
            ) or color not in bag:
                bag[color] = cubes[color]
    return bag


def multiply(bag):
    return reduce(lambda acc, color: acc * bag[color], bag.keys(), 1)


def __1__(lines):
    bag = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for line in lines:
        id, game = parse_game(line)
        if is_valid_game(bag, game):
            total += id

    return total


def __2__(lines):
    return sum(
        [multiply(min_valid_game(parse_game(line)[1])) for line in lines]
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
