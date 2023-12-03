from sys import argv


def has_symbol_neighbor(lines, col_start, col_end, row):
    for i in range(max(row - 1, 0), min(row + 2, len(lines))):
        for j in range(max(col_start - 1, 0), min(col_end + 2, len(lines[i]))):
            value = lines[i][j]
            if value != "." and not value.isdigit():
                return value, (i, j)
    return False


def __1__(lines: list[str]):
    total = 0
    for row, line in enumerate(lines):
        start = None
        for column, char in enumerate(line):
            if char.isdigit():
                if start is None:
                    start = column
            elif start is not None:
                if has_symbol_neighbor(lines, start, column - 1, row):
                    total += int(line[start:column])
                start = None

    return total


def __2__(lines):
    parts = {}
    for row, line in enumerate(lines):
        start = None
        for column, char in enumerate(line):
            if char.isdigit():
                if start is None:
                    start = column
            elif start is not None:
                has_symbol = has_symbol_neighbor(lines, start, column - 1, row)
                if has_symbol:
                    symbol, coord = has_symbol
                    if symbol == "*":
                        if coord not in parts:
                            parts[coord] = []
                        parts[coord].append(int(line[start:column]))
                start = None

    return sum(
        [gears[0] * gears[1] for gears in parts.values() if len(gears) == 2]
    )


def apply_padding(lines):
    columns = len(lines[0])
    return [
        "." * (columns + 2),
        *[f".{line}." for line in lines],
        "." * (columns + 2),
    ]


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return apply_padding(lines)


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
