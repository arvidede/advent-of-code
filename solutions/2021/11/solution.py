from sys import argv

COLUMNS = 10
ROWS = 10

if_not_first = lambda i, col: i if col > 0 else -1
if_not_last = lambda i, col: i if col < COLUMNS - 1 else -1


def get_neighbors(cell, rows=ROWS, cols=COLUMNS):
    row, col = cell // cols, cell % cols
    return [
        i
        for i in [
            if_not_first(cell - cols - 1, col),
            cell - cols,
            if_not_last(cell - cols + 1, col),
            if_not_first(cell - 1, col),
            if_not_last(cell + 1, col),
            if_not_first(cell + cols - 1, col),
            cell + cols,
            if_not_last(cell + cols + 1, col),
        ]
        if 0 <= i < rows * cols
    ]


def flash(cells, flashed):
    will_flash = False
    for i, cell in enumerate(cells):
        if cell > 9 and i not in flashed:
            flashed.add(i)
            for neighbor in get_neighbors(i):
                cells[neighbor] += 1
                if cells[neighbor] > 9 and neighbor not in flashed:
                    will_flash = True
    if will_flash:
        return flash(cells, flashed)
    return cells, flashed


def __1__(lines):
    num_flashes = 0
    cells = [int(c) + 1 for line in lines for c in line]
    for step in range(100):
        cells, flashed = flash(cells, set())
        num_flashes += len(flashed)
        cells = [1 if c > 9 else c + 1 for c in cells]
    return num_flashes


def __2__(lines):
    cells = [int(c) + 1 for line in lines for c in line]
    num_cells, step, flashed = len(cells), 0, set()
    while len(flashed) != num_cells:
        cells, flashed = flash(cells, set())
        cells = [1 if c > 9 else c + 1 for c in cells]
        step += 1
    return step


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
