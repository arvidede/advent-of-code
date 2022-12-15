from sys import argv
import re

X, Y = 0, 1
START, END = 0, 1
d = lambda p1, p2: abs(p1[X] - p2[X]) + abs(p1[Y] - p2[Y])
lmap = lambda f, l: list(map(f, l))


def get_row_sensor_outline(sensor, radius, row):
    # b
    # |
    # --- a
    # radius = a + b
    x, y = sensor
    b = y - row if y > row else row - y
    a = radius - b
    start = x - a
    end = x + a
    return start, end


def overlapping(lineA, lineB):
    if lineA[END] >= lineB[START] and lineA[START] <= lineB[START]:
        return True
    if lineB[END] >= lineA[START] and lineB[START] <= lineA[START]:
        return True
    return False


def concatenate(lineA, lineB):
    return (min(lineA[START], lineB[START]), max(lineA[END], lineB[END]))


def concatenate_outlines(outlines):
    outlines = sorted(outlines, key=lambda line: line[START])
    lineA = outlines[0]
    concatenated = [lineA]
    for lineB in outlines[1:]:
        if overlapping(lineA, lineB):
            lineA = concatenate(lineA, lineB)
            concatenated[-1] = lineA
        else:
            lineA = lineB
            concatenated.append(lineA)

    return concatenated


sum_lines = lambda lines: sum(line[END] - line[START] for line in lines)


def __1__(coordinates):
    target_row = 2000000
    outlines = []
    for sensor, beacon in coordinates:
        radius = d(sensor, beacon)
        if sensor[Y] - radius <= target_row <= sensor[Y] + radius:
            outlines.append(get_row_sensor_outline(sensor, radius, target_row))

    return sum_lines(concatenate_outlines(outlines))


def __2__(coordinates):
    n_rows = 4000000
    for row in range(n_rows):
        outlines = []
        for sensor, beacon in coordinates:
            radius = d(sensor, beacon)
            if sensor[Y] - radius <= row <= sensor[Y] + radius:
                outlines.append(get_row_sensor_outline(sensor, radius, row))

        lines = concatenate_outlines(outlines)
        if len(lines) > 1:
            x = lines[0][END] + 1
            return x * n_rows + row


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    coordinates = lmap(
        lambda line: lmap(
            lambda s: lmap(int, re.findall("=(-?\d+)", s)),
            line.split(":"),
        ),
        lines,
    )

    return coordinates


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
