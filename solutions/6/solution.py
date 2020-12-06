from sys import argv
from functools import reduce


def __1__(groups):
    return sum([len(set(group.replace('\n', ''))) for group in groups])


def __2__(groups):
    return sum([len(reduce(lambda rest, p: rest & set(p), group.split(
        '\n'), set(group.replace('\n', '')))) for group in groups])


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().split('\n\n')
    print(lines)
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
