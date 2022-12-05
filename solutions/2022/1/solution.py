from sys import argv


def __1__(lines):
    return max(sum(elf) for elf in lines)


def __2__(lines):
    return sum(sorted(sum(elf) for elf in lines)[-3:])


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = [
        [int(line) for line in elf.split("\n") if line]
        for elf in open(file).read().split("\n\n")
    ]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
