import re
from math import prod
from sys import argv

OPERATOR_MAP = {"*": prod, "+": sum}


def __1__():
    lines = parse_input(1)
    result = 0
    for line in lines.copy():
        operator = line.pop()
        result += OPERATOR_MAP[operator](map(int, line))

    return result


def transpose(lines):
    return list(map(list, zip(*lines)))


def __2__():
    lines = parse_input(2)

    result = 0
    for line in lines.copy():
        operator = line.pop()
        numbers = map(
            lambda x: re.sub(r"0+$", "", "".join(x)),
            transpose(line),
        )
        result += OPERATOR_MAP[operator](map(int, numbers))

    return result


def parse_input(step):

    def parse_number(number):
        if step == 1 or any(operator in number for operator in OPERATOR_MAP.keys()):
            return number.replace(" ", "")

        return number.replace(" ", "0")

    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    column_lengths = []

    for line in lines[:-1]:
        numbers = re.split("\s+", line.strip())

        if not column_lengths:
            column_lengths = [0] * len(numbers)

        for column, number in enumerate(numbers):
            column_lengths[column] = max(len(number), column_lengths[column])

    numbers = []
    for line in lines:
        cursor = 0
        row = []

        for column in column_lengths:
            next = cursor + column
            row.append(parse_number(line[cursor:next]))
            cursor = next + 1

        numbers.append(row)

    return transpose(numbers)


def main():
    print({"1": __1__, "2": __2__}[argv[1]]())


main()
