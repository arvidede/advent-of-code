from sys import argv
from functools import reduce


def increment_differences(acc, adapter):
    acc[str(adapter - acc['prev'])] += 1
    acc['prev'] = adapter
    return acc


def __1__(adapters):
    adapters = sorted(adapters) + [max(adapters) + 3]
    differences = reduce(increment_differences, adapters, {
                         '1': 0, '2': 0, '3': 0, 'prev': 0})
    return differences['1'] * differences['3']


def __2__(adapters):
    offset = 3
    device_rating = max(adapters) + offset
    adapters = [0] + sorted(adapters) + [device_rating]
    differences = [str(a - b) for a, b in zip(adapters[1:], adapters[:-1])]
    repeating_ones = "".join(differences).split('3')

    combinations = (7 ** repeating_ones.count('1111')) \
        * (4 ** repeating_ones.count('111')) \
        * (2 ** repeating_ones.count('11'))

    return combinations


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    lines = list(map(int, lines))
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
