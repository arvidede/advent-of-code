from sys import argv


def parse_lines(lines):
    return [
        list(
            int(c) for coords in line.split(" -> ") for c in coords.split(",")
        )
        for line in lines
    ]


def _range(n):
    return range(n + 1) if n > 0 else reversed(range(n, 1))


def __1__(lines, diagonal=False):
    lines = parse_lines(lines)
    vents = {}
    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2:
            for i in _range(x2 - x1):
                for j in _range(y2 - y1):
                    coord = f"{x1 + i},{y1 + j}"
                    if coord in vents:
                        vents[coord] += 1
                    else:
                        vents[coord] = 1
        elif diagonal:
            for i, j in zip(_range(x2 - x1), _range(y2 - y1)):
                coord = f"{x1 + i},{y1 + j}"
                if coord in vents:
                    vents[coord] += 1
                else:
                    vents[coord] = 1

    return len(list(filter(lambda l: l > 1, vents.values())))


def __2__(lines):
    return __1__(lines, diagonal=True)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
