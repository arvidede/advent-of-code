import textwrap
from sys import argv


def __1__(lines):
    def is_invalid(id):
        id_str = str(id)
        half = len(id_str) // 2
        return id_str[:half] == id_str[half:]

    return sum(
        id for start, end in lines for id in range(start, end + 1) if is_invalid(id)
    )


def __2__(lines):
    def is_invalid(id):
        id_str = str(id)
        half = len(id_str) // 2

        for i in range(half, 0, -1):
            id_pattern = id_str[:i]
            if all(chunk == id_pattern for chunk in textwrap.wrap(id_str, i)):
                return True

        return False

    return sum(
        id for start, end in lines for id in range(start, end + 1) if is_invalid(id)
    )


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().split(",")
    return [(int(id) for id in line.split("-")) for line in lines]


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
