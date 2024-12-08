from sys import argv
from collections import defaultdict

EMPTY = "."
ANTINODE = "#"

cols = lambda grid: max(grid.keys(), key=lambda x: x[0])[0] + 1
rows = lambda grid: max(grid.keys(), key=lambda x: x[1])[1] + 1


def paint(grid):
    grid_by_row = [[EMPTY] * cols(grid) for _ in range(rows(grid))]

    for (x, y), cell in grid.items():
        grid_by_row[y][x] = cell

    for row in grid_by_row:
        print("".join(row))


def group_antennas(grid):
    antennas = defaultdict(list)
    for location, type in grid.items():
        if type != EMPTY:
            antennas[type].append(location)
    return antennas


def in_grid(node, grid):
    x, y = node
    n_cols = cols(grid)
    n_rows = rows(grid)

    return x >= 0 and x < n_cols and y >= 0 and y < n_rows


def extrapolate_antinodes(origin, dx, dy, grid):
    antinodes = set()
    node = (origin[0] + dx, origin[1] + dy)
    period = 2
    while in_grid(node, grid):
        antinodes.add(node)
        node = (origin[0] + dx * period, origin[1] + dy * period)
        period += 1

    return antinodes


def calculate_antinodes(grid, resonation=False):
    antinodes = set()

    for nodes in group_antennas(grid).values():
        for i, node_a in enumerate(nodes):
            for node_b in nodes[(i + 1) :]:
                dx, dy = node_b[0] - node_a[0], node_b[1] - node_a[1]

                if resonation:
                    antinodes.update(extrapolate_antinodes(node_a, dx, dy, grid))
                    antinodes.update(extrapolate_antinodes(node_b, -dx, -dy, grid))
                else:
                    antinodes.add((node_a[0] - dx, node_a[1] - dy))
                    antinodes.add((node_b[0] + dx, node_b[1] + dy))

    antinodes = [(x, y) for x, y in antinodes if in_grid((x, y), grid)]

    return antinodes


def __1__(grid, resonation=False):
    antinodes = calculate_antinodes(grid, resonation)

    for node in antinodes:
        if grid[node] == EMPTY:
            grid[node] = ANTINODE

    paint(grid)

    return len(antinodes)


def __2__(grid):
    return __1__(grid, resonation=True)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return {
        (x, y): cell
        for y, line in enumerate(open(file).read().splitlines())
        for x, cell in enumerate(line)
    }


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
