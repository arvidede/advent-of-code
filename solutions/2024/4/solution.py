from collections import Counter, defaultdict
from sys import argv


def get_start_positions(grid: defaultdict[tuple[int, int], str], key="X"):
    return [position for position, letter in grid.items() if letter == key]


def p_range(start, end, keyword):
    if end == start:
        return [start] * len(keyword)
    elif start > end:
        return range(start, end, -1)

    return range(start, end)


def get_search_range(position, keyword):
    start_i, end_i, start_j, end_j = position
    return zip(p_range(start_i, end_i, keyword), p_range(start_j, end_j, keyword))


def is_keyword(position, grid, keyword):
    return keyword == "".join(grid[p] for p in get_search_range(position, keyword))


# Ape strong
def get_search_grid(start_position, keyword, diagonal_only):
    i, j = start_position
    grid = [
        # right
        (i, i, j, j + len(keyword)),
        # left
        (i, i, j, j - len(keyword)),
        # up
        (i, i - len(keyword), j, j),
        # down
        (i, i + len(keyword), j, j),
        # up-left
        (i, i - len(keyword), j, j - len(keyword)),
        # up-right
        (i, i - len(keyword), j, j + len(keyword)),
        # down-left
        (i, i + len(keyword), j, j - len(keyword)),
        # down-right
        (i, i + len(keyword), j, j + len(keyword)),
    ]

    if diagonal_only:
        return grid[4:]

    return grid


def search(start_position, grid, keyword, diagonal_only=False):
    return [
        position
        for position in get_search_grid(start_position, keyword, diagonal_only)
        if is_keyword(position, grid, keyword)
    ]


def __1__(grid):
    keyword = "XMAS"
    return sum(
        len(search(start_position, grid, keyword))
        for start_position in get_start_positions(grid)
    )


def __2__(grid):
    keyword = "MAS"
    return len(
        [
            position
            for position, occurrences in Counter(
                [
                    position
                    for start_position in get_start_positions(grid, keyword[0])
                    for keyword_range in search(
                        start_position, grid, keyword, diagonal_only=True
                    )
                    for position in get_search_range(keyword_range, keyword)
                    if grid[position] == "A"
                ]
            ).items()
            if occurrences > 1
        ]
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    grid = defaultdict(str)

    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            grid[(i, j)] = char

    return grid


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
