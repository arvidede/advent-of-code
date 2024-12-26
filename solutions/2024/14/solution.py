from math import prod
from sys import argv

WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7


def step(robots):
    for robot, (p, v) in enumerate(robots.copy()):
        px, py = p
        vx, vy = v
        px = (px + vx) % WIDTH
        py = (py + vy) % HEIGHT
        p = (px, py)
        robots[robot] = (p, v)

    return robots


def count(robots):
    quadrants = {
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 0,
    }

    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2

    for p, _ in robots:
        x, y = p

        if x == mid_x or y == mid_y:
            continue

        qx = min(x // mid_x, 1)
        qy = min(y // mid_y, 1)

        quadrants[(qx, qy)] += 1

    return quadrants.values()


def __1__(robots, steps=100):
    for _ in range(steps):
        robots = step(robots)

    return prod(count(robots))


# This was just dumb luck
def is_tree(robots):
    return len(robots) == len(set(p for p, _ in robots))


def paint(robots):
    grid = [list("." * WIDTH) for _ in range(HEIGHT)]

    for (x, y), _ in robots:
        grid[y][x] = "#"

    for row in grid:
        print("".join(row))


def __2__(robots):
    t = 0
    while not is_tree(robots):
        robots = step(robots)
        t += 1

    paint(robots)
    return t


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()

    robots = []

    for line in lines:
        p, v = line.split(" ")
        p = tuple(map(int, p.replace("p=", "").split(",")))
        v = tuple(map(int, v.replace("v=", "").split(",")))
        robots.append((p, v))

    return robots


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
