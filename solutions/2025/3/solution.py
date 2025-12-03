from sys import argv


def argmax(items):
    return max(enumerate(items), key=lambda x: x[1])[0]


def find_maximum_joltage(bank, length=2):
    bank = list(map(int, bank))
    joltage = []
    remaining = length

    while remaining > 0:
        offset = 1 - remaining
        battery = argmax(bank[:offset] if offset < 0 else bank)
        joltage.append(str(bank[battery]))
        bank = bank[battery + 1 :]
        remaining -= 1

    return int("".join(joltage))


def __1__(lines):
    return sum(map(find_maximum_joltage, lines))


def __2__(lines):
    return sum(map(lambda line: find_maximum_joltage(line, 12), lines))


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
