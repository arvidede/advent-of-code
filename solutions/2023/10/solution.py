from copy import deepcopy
from sys import argv

START = "S"

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Came from {direction} => Should go {direction}
pipe_map = {
    "|": {
        NORTH: SOUTH,
        SOUTH: NORTH,
    },
    "-": {
        EAST: WEST,
        WEST: EAST,
    },
    "L": {
        NORTH: EAST,
        EAST: NORTH,
    },
    "J": {
        NORTH: WEST,
        WEST: NORTH,
    },
    "7": {
        SOUTH: WEST,
        WEST: SOUTH,
    },
    "F": {
        SOUTH: EAST,
        EAST: SOUTH,
    },
}

opposite_map = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}


def get_next_position(current_position, direction):
    row, col = current_position
    if direction == NORTH:
        return (row - 1, col)

    if direction == EAST:
        return (row, col + 1)

    if direction == SOUTH:
        return (row + 1, col)

    if direction == WEST:
        return (row, col - 1)


def get_next_direction(direction, pipe):
    came_from = opposite_map[direction]
    return pipe_map[pipe][came_from]


def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == START:
                return (i, j)


def find_start_direction(grid, position):
    row, col = position

    if grid[row - 1][col] in ["|", "F", "7"]:
        return NORTH

    if grid[row][col + 1] in ["-", "J", "7"]:
        return EAST

    if grid[row + 1][col] in ["|", "J", "L"]:
        return SOUTH

    if grid[row][col - 1] in ["-", "F", "L"]:
        return WEST


def get_path(grid):
    position = start_position = find_start_position(grid)
    path = []

    while True:
        path.append(position)
        row, col = position
        pipe = grid[row][col]

        direction = (
            find_start_direction(grid, position)
            if pipe == START
            else get_next_direction(direction, pipe)
        )
        position = get_next_position(position, direction)

        if position == start_position:
            break

    return set(path)


def __1__(grid):
    return len(get_path(grid)) // 2


def get_start_type(grid, position):
    row, col = position
    north = grid[row - 1][col] in ["|", "7", "F"]
    east = grid[row][col + 1] in ["-", "7", "J"]
    south = grid[row + 1][col] in ["|", "J", "L"]
    west = grid[row][col - 1] in ["-", "F", "L"]

    if north and south:
        return "|"
    if east and west:
        return "-"
    if east and north:
        return "L"
    if east and south:
        return "F"
    if west and north:
        return "J"
    if west and south:
        return "7"


def paint(grid):
    for row in grid:
        print("".join(list(map(str, row))))


def __2__(grid):
    # Idea:
    # - cast rays from left to right
    # - if the ray has crossed an odd number of edges, it's outside the loop

    path = get_path(grid)

    pipe_grid = deepcopy(grid)
    count_grid = deepcopy(grid)

    start = find_start_position(grid)
    pipe_grid[start[0]][start[1]] = get_start_type(grid, start)

    for i, row in enumerate(count_grid):
        for j, _ in enumerate(row):
            if (i, j) not in path:
                count_grid[i][j] = 0
            else:
                count_grid[i][j] = "."

    for i, row in enumerate(count_grid):
        n_pipes = 0
        for j, _ in enumerate(row):
            if (i, j) in path:
                if pipe_grid[i][j] == "|":
                    n_pipes += 1
                if pipe_grid[i][j] == "L" or pipe_grid[i][j] == "7":
                    n_pipes += 0.5
                if pipe_grid[i][j] == "J" or pipe_grid[i][j] == "F":
                    n_pipes -= 0.5

                continue

            if n_pipes % 2 == 1:
                count_grid[i][j] = 1

    paint(count_grid)

    return sum(cell == 1 for row in count_grid for cell in row)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = list(map(list, open(file).read().splitlines()))
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
