from sys import argv
from math import inf
from collections import deque


def get_neighbors(grid, node):
    i, j = node
    return [
        (a, b)
        for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if 0 <= a < len(grid) and 0 <= b < len(grid[0])
    ]


def dijkstra(grid, start=(0, 0), end=(-1, -1)):
    graph = [[inf] * len(row) for row in grid]

    graph[start[1]][start[0]] = 0
    queue = deque([start])

    while queue:
        current_node = queue.pop()
        current_row, current_col = current_node
        for neighbor in get_neighbors(grid, current_node):
            row, col = neighbor
            prev_cost = graph[row][col]
            new_cost = graph[current_row][current_col] + grid[row][col]
            if new_cost < prev_cost:
                queue.appendleft(neighbor)
                graph[row][col] = new_cost

    return graph[end[0]][end[1]]


def parse_grid(lines):
    return [list(map(int, line)) for line in lines]


def parse_full_grid(lines, multiply=5):
    tile = parse_grid(lines)
    n_rows = len(tile) * multiply
    n_cols = len(tile[0]) * multiply
    grid = [
        [
            (
                (
                    tile[i % len(tile)][j % len(tile[0])]
                    + (i // len(tile))
                    + (j // len(tile[0]))
                    - 1
                )
                % 9
            )
            + 1
            for j in range(n_cols)
        ]
        for i in range(n_rows)
    ]
    return grid


def __1__(lines):
    grid = parse_grid(lines)
    return dijkstra(grid)


def __2__(lines):
    grid = parse_full_grid(lines)
    return dijkstra(grid)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
