from itertools import combinations
from sys import argv


def get_distance(universe, a, b, delta):
    start = a if a <= b else b
    end = b if a <= b else a

    distance = 0
    for i in range(start, end):
        distance += 1

        if len(set(universe[i])) == 1:
            distance += delta

    return distance


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def get_distances(universe, galaxies, delta=1):
    universe_transpose = transpose(universe)
    distance = {}
    for g1, g2 in combinations(galaxies, 2):
        vertical = get_distance(universe, g1[0], g2[0], delta)
        horisontal = get_distance(universe_transpose, g1[1], g2[1], delta)
        distance[(g1, g2)] = int(vertical + horisontal)

    return distance


def get_galaxies(lines):
    return [
        (i, j)
        for i, row in enumerate(lines)
        for j, value in enumerate(row)
        if value == "#"
    ]


def __1__(universe):
    galaxies = get_galaxies(universe)
    return sum(get_distances(universe, galaxies).values())


def __2__(universe):
    galaxies = get_galaxies(universe)
    return sum(get_distances(universe, galaxies, 1e6 - 1).values())


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
