from math import ceil, floor, sqrt
from sys import argv


def get_winning_combinations(times, records):
    # d = v * t
    # t = total_time - charging_time
    # v = charging_time
    # d = charging_time * (total_time - charging_time)
    # d = record <=> record = charging_time * total_time - charging_time^2
    # 0 = charging_time^2 - total_time * charging_time + record
    # charging_time = total_time / 2 ± sqrt((total_time / 2)^2 - record)

    wins = 1
    for total_time, record in zip(times, records):
        sq_discriminant = sqrt((total_time / 2) ** 2 - record)
        charging_time_lower = floor(total_time / 2 - sq_discriminant)
        charging_time_upper = ceil(total_time / 2 + sq_discriminant) - 1

        wins *= charging_time_upper - charging_time_lower

    return wins


def __1__(lines):
    times = map(int, lines[0].split(":")[1].split())
    records = map(int, lines[1].split(":")[1].split())
    return get_winning_combinations(times, records)


def __2__(lines):
    times = [int(lines[0].split(":")[1].replace(" ", ""))]
    records = [int(lines[1].split(":")[1].replace(" ", ""))]
    return get_winning_combinations(times, records)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return open(file).read().splitlines()


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
