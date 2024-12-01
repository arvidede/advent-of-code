from sys import argv
import re


def build_valve_tree(lines):
    tree = {}
    flow_rate = {}

    for line in lines:
        sections = line.split(";")
        valve = sections[0][6:8]
        flow = int(sections[0].split("=")[1])
        flow_rate[valve] = flow
        paths = re.findall("[A-Z]{2}", sections[1])
        tree[valve] = paths

    return tree, flow_rate


TIME = 30

open_valve = lambda valve: f"{valve}-o"

move = lambda A, B: f"{A}{B}"


def generate_paths(node, path, tree, seen):
    for neighbor in tree.get(node):
        if move(node, neighbor) in seen:
            continue
        seen.add(move(node, neighbor))
        paths = generate_paths(neighbor, path, tree, seen.copy())


def __1__(lines):
    tree, flow_rates = build_valve_tree(lines)
    start = "AA"
    paths = generate_paths(start, [], tree, set())
    return paths


def __2__(lines):
    return 2


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
