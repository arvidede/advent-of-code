from collections import defaultdict
from sys import argv

START = 0
END = 9


def get_starting_positions(grid):
    return [position for position, height in grid.items() if height == START]


def get_neighbors(grid, position):
    x, y = position
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))

    if y > 0:
        neighbors.append((x, y - 1))

    if x < grid["cols"] - 1:
        neighbors.append((x + 1, y))

    if y < grid["rows"] - 1:
        neighbors.append((x, y + 1))

    return neighbors


def bfs(grid, position, path, visited, paths):
    visited.add(position)

    if grid[position] == END:
        return paths.append(path)

    for neighbor in get_neighbors(grid, position):
        if neighbor in visited:
            continue

        if grid[neighbor] - grid[position] == 1:
            bfs(grid, neighbor, path + [neighbor], visited.copy(), paths)

    return paths


def __1__(grid):
    return sum(
        len(
            set(path[-1] for path in bfs(grid, position, [position], set(position), []))
        )
        for position in get_starting_positions(grid)
    )


def __2__(grid):
    return sum(
        len(bfs(grid, position, [position], set(position), []))
        for position in get_starting_positions(grid)
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    grid = defaultdict(int)

    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            grid[(x, y)] = int(cell) if cell != "." else -1

    cols = max(grid.keys(), key=lambda p: p[0])[0] + 1
    rows = max(grid.keys(), key=lambda p: p[1])[1] + 1

    grid["rows"] = rows
    grid["cols"] = cols

    return grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
