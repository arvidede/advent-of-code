from sys import argv


def parse_instructions(instructions):
    return [(i[0], int(i[1:])) for i in instructions]


def rotate(position, direction, rotation):
    # N = 0, E = 1, S = 2, W = 3
    rotation = int(rotation / 90)
    position['direction'] = (position['direction'] +
                             dir_map[direction] * rotation) % 4
    return position


def rotate_waypoint(position, direction, rotation):
    rotation = (dir_map[direction] * int(rotation / 90)) % 4

    if rotation == 1:
        prev_y = position['dy']
        position['dy'] = position['dx']
        position['dx'] = -prev_y
    if rotation == 2:
        position['dy'] *= -1
        position['dx'] *= -1
    if rotation == 3:
        prev_x = position['dx']
        position['dx'] = position['dy']
        position['dy'] = -prev_x

    return position


def move(position, direction, distance):
    if direction == 'F':
        action = dir_map[position['direction']]
    else:
        action = dir_map[direction]
    position[action[0]] += distance * action[1]
    return position


def move_towards_waypoint(boat_position, wp_position, factor):
    boat_position['dx'] += factor * wp_position['dx']
    boat_position['dy'] += factor * wp_position['dy']
    return boat_position


dir_map = {
    'R': 1,
    'L': -1,
    'N': ('dy', -1),
    'E': ('dx', 1),
    'S': ('dy', 1),
    'W': ('dx', -1),
    0: ('dy', -1),
    1: ('dx', 1),
    2: ('dy', 1),
    3: ('dx', -1),
}


def __1__(lines):
    action_map = {
        'L': rotate,
        'R': rotate,
        'N': move,
        'S': move,
        'E': move,
        'W': move,
        'F': move,
    }

    instructions = parse_instructions(lines)
    position = {'dx': 0, 'dy': 0, 'direction': 1}

    for action, value in instructions:
        position = action_map[action](position, action, value)

    return abs(position['dx']) + abs(position['dy'])


def __2__(lines):
    action_map = {
        'L': rotate_waypoint,
        'R': rotate_waypoint,
        'N': move,
        'S': move,
        'E': move,
        'W': move,
    }

    instructions = parse_instructions(lines)
    boat_position = {'dx': 0, 'dy': 0}
    wp_position = {'dx': 10, 'dy': -1}

    for action, value in instructions:
        if action == 'F':
            boat_position = move_towards_waypoint(
                boat_position, wp_position, value)
        else:
            wp_position = action_map[action](wp_position, action, value)

    return abs(boat_position['dx']) + abs(boat_position['dy'])


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
