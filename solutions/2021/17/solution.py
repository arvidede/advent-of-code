from sys import argv
import re
from collections import Counter


def move_probe(position, velocity):
    dx, dy = velocity
    position = (position[0] + dx, position[1] + dy)
    velocity = (dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0, dy - 1)
    return (position, velocity)


def within_x(position, target_area):
    return position[0] >= target_area[0] and position[0] <= target_area[1]


def within_y(position, target_area):
    return position[1] >= target_area[2] and position[1] <= target_area[3]


def probe_in_target_area(position, target_area):
    return within_x(position, target_area) and within_y(position, target_area)


# Ape strong
def __1__(target_area):
    history = []
    x_min, x_max, y_min, y_max = target_area
    for dx in range(x_max + 1):
        for dy in range(y_min, 1000):
            position, velocity = (0, 0), (dx, dy)
            max_y = position[1]
            increasing = False
            while True:
                max_y = max(max_y, position[1])
                position, velocity = move_probe(position, velocity)

                if probe_in_target_area(position, target_area):
                    history.append(((dx, dy), max_y))

                if increasing and velocity[1] <= 0:
                    if position[1] != max_y:
                        break
                    increasing = False

                if position[0] > x_max:
                    break

                if position[1] < y_min:
                    break

                if velocity[0] == 0 and not within_x(position, target_area):
                    break

    return max(history, key=lambda x: x[1]), len(history)


f_x = lambda c, t, dt: c + max(dt - t, 0)
f_y = lambda c, t, dt: c + dt - t


def find_x_within_area(target_area):
    valid = []
    x_min, x_max = target_area
    for dx in range(1, x_max + 1):
        x_t = 0
        t = 0
        while x_t <= x_max:
            x_t = f_x(x_t, t, dx)

            if t > x_max:
                break

            if x_t >= x_min and x_t <= x_max:
                valid.append((dx, t))

            t += 1
    return list(zip(*valid))


def find_y_within_area(target_area, t_max):
    valid = []
    y_min, y_max = target_area
    for dy in range(y_min, 10000):
        if dy == 0:
            continue
        y_t = 0
        t = 0
        while y_t >= y_min and t <= t_max:
            y_t = f_y(y_t, t, dy)
            if y_t >= y_min and y_t <= y_max:
                valid.append((dy, t))
            t += 1
    return list(zip(*valid))


def find_init_velocity(target_area):
    dx, dx_t = find_x_within_area(target_area[:2])
    dy, dy_t = find_y_within_area(target_area[2:], max(dx_t))
    x_ts, y_ts = Counter(dx_t), Counter(dy_t)

    return sum(x_ts[t] * y_ts[t] for t in x_ts)


def __2__(target_area):
    return find_init_velocity(target_area)


def parse_target_area(line):
    # x_min, x_max, y_min, y_max
    return list(map(int, re.findall(r"-?\d+", line)))


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    target_area = parse_target_area(open(file).readline())
    print({"1": __1__, "2": __2__}[argv[1]](target_area))


main()
