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


def iterate_differences(differences, adjacent):
    if len(differences) == 0:
        return 1

    current = differences.pop()

    if current == 1:
        adjacent += 1
    else:
        adjacent = 0

    coef = 2 if adjacent > 1 else 1

    combo = coef * iterate_differences(differences, adjacent) - (adjacent > 3)
    print(current, combo)
    return combo
    # return coef * iterate_differences(differences, adjacent) - (adjacent > 3)


def __2__(adapters):
    offset = 3
    device_rating = max(adapters) + offset
    adapters = [0] + sorted(adapters) + [device_rating]
    differences = [a - b for a, b in zip(adapters[1:], adapters[:-1])]

    return iterate_differences(differences, 0)


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    lines = list(map(int, lines))
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
