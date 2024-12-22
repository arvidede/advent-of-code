import re
from functools import cache
from sys import argv

NUMERIC_KEYPAD = {
    "A": {
        "^": "3",
        "<": "0",
    },
    "0": {
        ">": "A",
        "^": "2",
    },
    "1": {
        ">": "2",
        "^": "4",
    },
    "2": {
        ">": "3",
        "v": "0",
        "<": "1",
        "^": "5",
    },
    "3": {
        "v": "A",
        "<": "2",
        "^": "6",
    },
    "4": {
        ">": "5",
        "v": "1",
        "^": "7",
    },
    "5": {
        ">": "6",
        "v": "2",
        "<": "4",
        "^": "8",
    },
    "6": {
        "v": "3",
        "<": "5",
        "^": "9",
    },
    "7": {
        ">": "8",
        "v": "4",
    },
    "8": {
        "v": "5",
        "<": "7",
        ">": "9",
    },
    "9": {
        "v": "6",
        "<": "8",
    },
}

DIRECTONAL_KEYPAD = {
    "A": {
        "v": ">",
        "<": "^",
    },
    "^": {
        "v": "v",
        ">": "A",
    },
    ">": {
        "^": "A",
        "<": "v",
    },
    "v": {
        ">": ">",
        "^": "^",
        "<": "<",
    },
    "<": {
        ">": "v",
    },
}

direction_priority = {
    "<": 1,
    "^": 2,
    "v": 3,
    ">": 4,
    "A": 5,
}


def bfs(start, end, graph):
    visited = set([start])
    queue = [(start, [])]

    while queue:
        node, path = queue.pop(0)

        if node == end:
            return "".join(path) + "A"

        for direction, neighbor in graph[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [direction]))


def generate_all_paths():
    paths = {}
    for a in NUMERIC_KEYPAD:
        for b in NUMERIC_KEYPAD:
            paths[(a, b)] = "".join(
                sorted(
                    list(bfs(a, b, NUMERIC_KEYPAD)),
                    key=lambda x: direction_priority[x],
                )
            )

    for a in DIRECTONAL_KEYPAD:
        for b in DIRECTONAL_KEYPAD:
            paths[(a, b)] = "".join(
                sorted(
                    list(bfs(a, b, DIRECTONAL_KEYPAD)),
                    key=lambda x: direction_priority[x],
                )
            )

    # Requires manual correction to account for invalid paths
    paths[("A", "1")] = "^<<A"
    paths[("A", "4")] = "^^<<A"
    paths[("A", "7")] = "^^^<<A"
    paths[("0", "1")] = "^<A"
    paths[("0", "4")] = "^^<A"
    paths[("0", "7")] = "^^^<A"
    paths[("1", "A")] = ">>vA"
    paths[("1", "0")] = ">vA"
    paths[("4", "A")] = ">>vvA"
    paths[("4", "0")] = ">vvA"
    paths[("7", "A")] = ">>vvvA"
    paths[("7", "0")] = ">vvvA"
    paths[("<", "^")] = ">^A"
    paths[("<", "A")] = ">>^A"
    paths[("A", "<")] = "v<<A"
    paths[("^", "<")] = "v<A"

    return paths


paths = generate_all_paths()

START = "A"


def find_path(code):
    return "".join(paths[(a, b)] for a, b in zip([START, *code[:-1]], code))


def complexity(code, sequence_length):
    return sequence_length * int(code[:-1])


@cache
def dive(code, depth):
    if depth == 1:
        return len(code)

    return sum(dive(find_path(c), depth - 1) for c in re.findall("([^A]*A)", code))


def __1__(codes):
    return sum(complexity(code, dive(code, 1 + 2 + 1)) for code in codes)


def __2__(codes):
    return sum(complexity(code, dive(code, 1 + 25 + 1)) for code in codes)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
