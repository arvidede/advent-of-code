from sys import argv

PAPER = "@"
EMPTY = "."

NEIGHBOR_GRID = [
    (dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if not (dx == 0 and dy == 0)
]


def get_neighbors(grid, position):
    x, y = position
    return [(x + dx, y + dy) for dx, dy in NEIGHBOR_GRID if (x + dx, y + dy) in grid]


def can_access_position(grid, position):

    return (
        sum(grid[neighbor] == PAPER for neighbor in get_neighbors(grid, position)) < 4
    )


def __1__(grid):
    return sum(
        can_access_position(grid, position)
        for position in grid
        if grid[position] == PAPER
    )


def __2__(grid):

    removed = []
    accessed = True

    while accessed:
        paper = [p for p in grid if grid[p] == PAPER]
        accessed = False
        copy = grid.copy()

        for position in paper:
            if can_access_position(grid, position):
                copy[position] = EMPTY
                removed.append(position)
                accessed = True

        grid = copy

    return len(removed)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    grid = {(x, y): cell for y, line in enumerate(lines) for x, cell in enumerate(line)}

    return grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
