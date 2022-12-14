from sys import argv

get_candidates = lambda s: [
    (s[0] + 1, s[1]),
    (s[0] + 1, s[1] - 1),
    (s[0] + 1, s[1] + 1),
]

overflowing = (
    lambda s, grid: s[0] >= len(grid) or s[1] < 0 or s[1] >= len(grid[0])
)


def move_sand(sand, grid):
    prev = sand
    for candidate in get_candidates(sand):

        if overflowing(candidate, grid):
            return sand, grid, True, True

        if not grid[candidate[0]][candidate[1]]:
            grid[prev[0]][prev[1]] = 0
            grid[candidate[0]][candidate[1]] = 1
            return candidate, grid, False, False

    return sand, grid, True, False


def __1__(grid, start):
    sand = start
    resting = []

    overflow = False
    while not overflow:

        rest = False
        while not rest:
            sand, grid, rest, overflow = move_sand(sand, grid)

        if sand == start:
            resting.append(sand)
            break

        if not overflow:
            resting.append(sand)
            sand = start

    return len(resting)


def __2__(grid, start):
    for col in range(len(grid[-1])):
        grid[-1][col] = 1

    return __1__(grid, start)


xrange = lambda a, b: range(a, b + 1) if a < b else range(b, a + 1)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    paths = [
        [list(map(int, coord.split(","))) for coord in line.split(" -> ")]
        for line in lines
    ]
    padding = 1000
    bottom = max(y for path in paths for (_, y) in path)
    left = min(x for path in paths for (x, _) in path) - padding
    right = max(x for path in paths for (x, _) in path) + padding
    width = right - left + 1
    height = bottom + 3

    grid = [[0 for _ in range(width)] for _ in range(height)]

    # interpolation
    for path in paths:
        prev_j, prev_i = path[0]
        for j, i in path[1:]:
            for row in xrange(prev_i, i):
                for col in xrange(prev_j, j):
                    grid[row][col - left] = 1
            prev_j, prev_i = j, i

    sand = (0, 500 - left)
    grid[sand[0]][sand[1]] = 1
    return grid, sand


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
