from sys import argv


def diff(elements):
    return [elements[i + 1] - elements[i] for i in range(len(elements) - 1)]


def get_element_at(elements, position=-1):
    if not any(elements):
        return elements[position]

    k = 1 if position == -1 else -1
    return elements[position] + k * get_element_at(diff(elements), position)


def __1__(lines):
    return sum(get_element_at(line, -1) for line in lines)


def __2__(lines):
    return sum(get_element_at(line, 0) for line in lines)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = [
        list(map(int, line.split())) for line in open(file).read().splitlines()
    ]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
