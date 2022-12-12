from sys import argv
from collections import deque

valid_height = lambda a, b: a - b < 2

get_neighbors = lambda p: [
    (p[0] - 1, p[1]),  # up
    (p[0], p[1] + 1),  # right
    (p[0] + 1, p[1]),  # down
    (p[0], p[1] - 1),  # left
]


def within_bounds(pos, grid):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def bfs(start, stop, grid):
    visited = set([])
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        current_height = grid[current[0]][current[1]]

        for neighbor in get_neighbors(current):

            if neighbor in visited:
                continue

            if not within_bounds(neighbor, grid):
                continue

            neighbor_height = grid[neighbor[0]][neighbor[1]]

            if not valid_height(current_height, neighbor_height):
                continue

            if stop(neighbor):
                return path + [neighbor]

            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))


def __1__(start, end, grid):
    stop = lambda p: p == start
    return len(bfs(end, stop, grid))


def __2__(start, end, grid):
    stop = lambda p: grid[p[0]][p[1]] == ord("a")
    return len(bfs(end, stop, grid))


def get_start_end_pos(grid):
    S = ord("S")
    E = ord("E")
    start, end = None, None
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if start is None and col == S:
                start = (i, j)
                continue

            if end is None and col == E:
                end = (i, j)
    return start, end


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    grid = [[ord(c) for c in line] for line in lines]
    start, end = get_start_end_pos(grid)
    grid[start[0]][start[1]] = ord("a")
    grid[end[0]][end[1]] = ord("z")
    return start, end, grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
