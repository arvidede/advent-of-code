from sys import argv
from collections import deque


def parse_cave_system(lines):
    cave = {}
    for line in lines:
        start, end = line.split("-")
        if start not in cave:
            cave[start] = []
        if end not in cave:
            cave[end] = []
        cave[start].append(end)
        cave[end].append(start)
    return cave


def search_cave(
    cave,
    current_node,
    paths=[],
    path=[],
    visited=set(),
    has_visited_twice=False,
):
    if len(path) == 0:
        path = [current_node]

    if current_node == "end":
        paths.append(path)
        return paths

    if current_node in visited:
        if has_visited_twice:
            return paths
        has_visited_twice = True

    elif current_node.islower():
        visited.add(current_node)

    for neighbor in cave[current_node]:
        if neighbor != "start":
            search_cave(
                cave,
                neighbor,
                paths,
                [*path, neighbor],
                visited.copy(),
                has_visited_twice,
            )

    return paths


def __1__(lines, has_visited_twice=True):
    cave = parse_cave_system(lines)
    valid_paths = search_cave(
        cave, "start", has_visited_twice=has_visited_twice
    )
    return len(valid_paths)


def __2__(lines):
    return __1__(lines, has_visited_twice=False)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
