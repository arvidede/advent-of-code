from sys import argv


def get_priority(item):
    ascii_num = ord(item)
    offset = 96 if ascii_num >= 97 else 38
    return ascii_num - offset


def __1__(lines):
    priority = 0
    for line in lines:
        half = len(line) // 2
        left, right = set(line[:half]), set(line[half:])
        item = left.intersection(right).pop()
        priority += get_priority(item)

    return priority


def __2__(lines):
    priority = 0
    for (a, b, c) in zip(*(iter(lines),) * 3):
        item = set(a).intersection(set(b)).intersection(set(c)).pop()
        priority += get_priority(item)

    return priority


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
