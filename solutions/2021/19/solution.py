import re
import timeit
from sys import argv

RANGE = 1000

d = lambda p1, p2: sum((a - b) ** 2 for a, b in zip(p1, p2))


def subtract(A, B):
    return [a - b for (a, b) in zip(A, B)]


def multiply(A, B):
    [sum(starmap(mul, zip(first, col))) for col in zip(*second)]


def rotate_x(beacon, direction):
    [x, y, z] = beacon
    return [x, direction * z, -direction * y]


def rotate_y(beacon, direction):
    [x, y, z] = beacon
    return [-direction * z, y, direction * x]


def rotate_z(beacon, direction):
    [x, y, z] = beacon
    return [direction * y, -direction * x, z]


rotations = [
    rotate_x(beacon, direction),
    rotate_y(beacon, direction),
    rotate_z(beacon, direction),
]


def get_rotation_matrix(scanner1, scanner2):
    # v = scanner1 x scanner2 (rotation axis)
    # s = ||v|| (sin Ø)
    # c = a • b (cos Ø)
    pass


def get_translation(scanner1, scanner2):
    return subtract(scanner1[0], scanner2[0])


def find_relative_scanner_position(scanner1, scanner2):
    rotation = get_rotation_matrix(scanner1, scanner2)
    translation = subtract(scanner1[0], scanner2[0])  # Assuming ordered input
    return


def generate_distance_scanner_map(scanners):
    beacon_distances = {}
    for scanner, beacons in enumerate(scanners):
        for i, p1 in enumerate(beacons):
            for p2 in beacons[i:]:
                beacon_distance = d(p1, p2)
                if beacon_distance in beacon_distances:
                    beacon_distances[beacon_distance].add(scanner)
                elif beacon_distance > 0:
                    beacon_distances[beacon_distance] = set([scanner])
    return [
        scanners for scanners in beacon_distances.values() if len(scanners) > 1
    ]


def get_adjacent_scanners(scanners):
    distance_map = generate_distance_scanner_map(scanners)
    adjacent_scanners = {}

    for scanner in range(len(scanners)):
        neighbors = {}
        for connection in distance_map:
            if scanner in connection:
                for neighbor in connection:
                    if neighbor == scanner:
                        continue
                    if neighbor in neighbors:
                        neighbors[neighbor] += 1
                        continue
                    neighbors[neighbor] = 1

        adjacent_scanners[scanner] = [
            neighbor
            for neighbor, num_common in neighbors.items()
            if num_common >= 66  # 12 choose 2
        ]
    return adjacent_scanners


def __1__(scanners):
    adjacent_scanners = get_adjacent_scanners(scanners)

    return adjacent_scanners


def __2__(lines):
    return 2


def parse_scanner_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    scanners = [
        [
            list(map(int, point.split(",")))
            for point in line.split("\n")
            if point
        ]
        for line in re.split("--- scanner \d+ ---\\n", open(file).read())
        if line != ""
    ]
    return scanners


def main():
    start = timeit.default_timer()
    scanners = parse_scanner_input()
    print({"1": __1__, "2": __2__}[argv[1]](scanners))
    stop = timeit.default_timer()
    print("Finished in: %.2fms" % (start * 1000))


main()
