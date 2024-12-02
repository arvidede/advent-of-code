from sys import argv


def check_safety(levels):
    diff = [a - b for a, b in zip(levels[:-1], levels[1:])]
    return set(diff) <= {1, 2, 3} or set(diff) <= {-1, -2, -3}


def __1__(lines):
    return sum(check_safety(list(map(int, line.split(" ")))) for line in lines)


def __2__(lines):
    safe = []
    for line in lines:
        levels = list(map(int, line.split(" ")))

        safe.append(
            any(
                check_safety(levels[:i] + levels[(i + 1) :]) for i in range(len(levels))
            )
        )
    return sum(safe)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
