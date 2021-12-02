from sys import argv


dir_map = {
    'forward': [1, 0],
    'down':  [0, 1],
    'up': [0, -1],
}


def parse_command(line: str):
    direction, distance = line.split(' ')
    distance = int(distance)
    dx, dy = dir_map[direction]
    return distance * dx, distance * dy


def __1__(lines):
    position = {'x': 0, 'y': 0}
    for line in lines:
        dx, dy = parse_command(line)
        position['x'] += dx
        position['y'] += dy

    return position['x'] * position['y']


def __2__(lines):
    position = {'x': 0, 'y': 0, 'aim': 0}
    for line in lines:
        dx, dy = parse_command(line)
        position['aim'] += dy
        position['x'] += dx
        position['y'] += dx * position['aim']

    return position['x'], position['y'], position['x'] * position['y']


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
