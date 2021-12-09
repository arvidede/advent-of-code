from sys import argv
from itertools import product
from functools import reduce


def is_low_point(grid, i, j):
    rows, cols = len(grid), len(grid[0])
    point = int(grid[i][j])
    if j + 1 < cols and point >= int(grid[i][j + 1]):
        return False
    if j - 1 >= 0 and point >= int(grid[i][j - 1]):
        return False
    if i + 1 < rows and point >= int(grid[i + 1][j]):
        return False
    if i - 1 >= 0 and point >= int(grid[i - 1][j]):
        return False
    return True


def find_low_points(grid):
    rows, cols = len(grid), len(grid[0])
    return [
        (i, j)
        for i, j in list(product(range(rows), range(cols)))
        if is_low_point(grid, i, j)
    ]


def get_neighbors(grid, point):
    i, j = point
    return [
        (a, b)
        for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and int(grid[a][b]) < 9
    ]


def search(visited, grid, point):
    if point not in visited:
        visited.add(point)
        for neighbour in get_neighbors(grid, point):
            search(visited, grid, neighbour)
    return len(visited)


def __1__(lines):
    return sum([int(lines[i][j]) + 1 for i, j in find_low_points(lines)])


def __2__(grid):
    basins = [search(set(), grid, point) for point in find_low_points(grid)]
    top_basins = sorted(basins)[::-1][:3]
    return reduce(lambda a, b: a * b, top_basins)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
