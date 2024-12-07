from collections import defaultdict
from sys import argv

GUARD = "^"
OBSTACLE = "#"
VISITED = "X"
EMPTY = "."

DIR_MAP = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}
ROTATION_MAP = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


def get_start_position(grid):
    for position, cell in grid.items():
        if cell == GUARD:
            return position


def step(guard, grid):
    x, y = guard
    direction = grid[guard]

    grid[guard] = VISITED

    dx, dy = DIR_MAP[direction]
    next_x, next_y = x + dx, y + dy

    if next_x < 0 or next_y < 0 or next_x >= grid["cols"] or next_y >= grid["rows"]:
        return guard, grid, True

    if grid[(next_x, next_y)] == OBSTACLE:
        grid[guard] = ROTATION_MAP[direction]
        return guard, grid, False

    grid[(next_x, next_y)] = direction

    return (next_x, next_y), grid, False


def creates_loop(grid, guard_position, object_position):
    grid[object_position] = OBSTACLE
    visited = defaultdict(set)

    done = False
    guard = guard_position

    while not done:
        guard, grid, done = step(guard, grid)
        if guard in visited and grid[guard] in visited[guard]:
            return True
        else:
            visited[guard].add(grid[guard])

    return False


def __1__(grid):
    guard = get_start_position(grid)
    done = False

    while not done:
        guard, grid, done = step(guard, grid)

    return sum(col == VISITED for col in grid.values())


def __2__(grid):

    guard = get_start_position(grid)

    return sum(
        creates_loop(grid.copy(), guard, position)
        for position in grid
        if grid[position] == EMPTY
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    grid = {
        (x, y): cell
        for y, line in enumerate(lines)
        for x, cell in enumerate(list(line))
    }

    grid["rows"] = len(lines)
    grid["cols"] = len(lines[0])

    return grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
