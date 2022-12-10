from sys import argv

X, Y = 0, 1

dir_map = {
    "L": [X, -1],
    "R": [X, 1],
    "U": [Y, 1],
    "D": [Y, -1],
}

sign = lambda x: -1 if x < 0 else 1 if x > 0 else 0


def paint(knots, direction, distance, origo=[0, 0]):
    rows, cols = 30, 30
    grid = [["." for j in range(cols)] for i in range(rows)]

    for n, knot in enumerate(knots[::-1]):
        n = len(knots) - n - 1
        marker = "H" if n == 0 else str(n)
        grid[knot[1] + origo[0]][knot[0] + origo[1]] = marker

    for row in grid[::-1]:
        print("".join(row))

    print("\n")
    print(direction, distance)
    print("\n\n")


def __1__(lines):
    head, tail = [0, 0], (0, 0)
    visited = set()

    for line in lines:
        direction, distance = line
        idx, mult = dir_map[direction]
        while distance > 0:
            head[idx] += mult
            dx, dy = head[X] - tail[X], head[Y] - tail[Y]

            if abs(dx) > 1:
                tail = (head[X] - mult, head[Y])
            if abs(dy) > 1:
                tail = (head[X], head[Y] - mult)

            visited.add(tail)
            distance -= 1

    return len(visited)


def __2__(lines):
    n_knots = 10
    knots = [[0, 0] for k in range(n_knots)]
    visited = set([(0, 0)])

    for line in lines:
        direction, distance = line
        head_idx, head_mult = dir_map[direction]
        while distance > 0:
            idx, mult = head_idx, head_mult
            knots[0][idx] += mult

            for knot in range(0, len(knots) - 1):
                head, tail = knots[knot], knots[knot + 1]
                dx, dy = head[X] - tail[X], head[Y] - tail[Y]

                if abs(dx) > 1 or abs(dy) > 1:
                    tail[X] = head[X] - sign(dx) * (abs(dx) > 1)
                    tail[Y] = head[Y] - sign(dy) * (abs(dy) > 1)

                if knot == n_knots - 2:
                    visited.add(tuple(tail))

            distance -= 1

    return len(visited)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    lines = [(line[0], int(line[2:])) for line in lines]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
