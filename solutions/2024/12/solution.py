from collections import defaultdict
from itertools import combinations
from sys import argv


def get_neighbors(position):
    x, y = position
    return [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]


def bfs(position, grid, visited):
    queue = [position]
    visited_before = visited.copy()
    visited = visited.copy()

    visited.add(position)

    while queue:
        node = queue.pop(0)
        for neighbor in get_neighbors(node):

            if neighbor not in grid or grid[neighbor] != grid[node]:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited - visited_before


def explore(grid):
    remaining = set(grid.keys()) - set(["cols", "rows"])
    visited = set()
    regions = []

    while remaining:
        position = remaining.pop()
        region = bfs(position, grid, visited)
        regions.append(list(region))
        remaining -= region
        visited |= region

    return regions


def area(region):
    return len(region)


def perimiter(region):
    return len(
        [
            neighbor
            for position in region
            for neighbor in get_neighbors(position)
            if neighbor not in region
        ]
    )


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def sides(region, grid):
    sides = 0
    for node in region:
        x, y = node
        plant_type = grid[node]

        up = grid[(x, y - 1)] != plant_type
        down = grid[(x, y + 1)] != plant_type
        left = grid[(x - 1, y)] != plant_type
        right = grid[(x + 1, y)] != plant_type

        # Outer corner
        if up and left:
            sides += 1

        if up and right:
            sides += 1

        if down and left:
            sides += 1

        if down and right:
            sides += 1

        # Inner corner
        up_left = grid[(x - 1, y - 1)] != plant_type
        down_left = grid[(x - 1, y + 1)] != plant_type
        up_right = grid[(x + 1, y - 1)] != plant_type
        down_right = grid[(x + 1, y + 1)] != plant_type

        if down_right and not right and not down:
            sides += 1

        if down_left and not left and not down:
            sides += 1

        if up_right and not right and not up:
            sides += 1

        if up_left and not left and not up:
            sides += 1

    return sides


def __1__(grid):
    return sum(area(region) * perimiter(region) for region in explore(grid))


# Invalid
# 959698 high


def __2__(grid):

    return sum(area(region) * sides(region, grid) for region in explore(grid))


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    grid = defaultdict(str)

    rows = -1
    cols = -1
    for y, row in enumerate(lines):
        rows = max(rows, y)
        for x, cell in enumerate(row):
            cols = max(cols, x)
            grid[(x, y)] = cell

    grid["cols"] = cols + 1
    grid["rows"] = rows + 1

    return grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
