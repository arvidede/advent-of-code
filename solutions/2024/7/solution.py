from functools import cache
from sys import argv


def test_equation(
    test_value,
    numbers,
    concat=False,
    acc=None,
):
    if len(numbers) == 0:
        return test_value == acc

    number = numbers.pop(0)

    if test_equation(test_value, numbers.copy(), concat, (acc or 1) * number):
        return True
    elif test_equation(test_value, numbers.copy(), concat, (acc or 0) + number):
        return True
    elif concat:
        if not acc:
            return False

        return test_equation(test_value, numbers.copy(), concat, int(f"{acc}{number}"))
    return False


def __1__(equations, concat=False):
    return sum(
        test_value
        for test_value, numbers in equations
        if test_equation(test_value, numbers, concat)
    )


def __2__(equations):
    return __1__(equations, concat=True)


def parse_line(line):
    test_value, numbers = line.split(": ")
    return (int(test_value), list(map(int, numbers.split(" "))))


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = [parse_line(line) for line in open(file).read().splitlines()]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
