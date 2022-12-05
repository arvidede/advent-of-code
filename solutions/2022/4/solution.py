from sys import argv


def contains(pair):
    startA, endA, startB, endB = pair
    return (startA <= startB and endA >= endB) or (
        startB <= startA and endB >= endA
    )


def overlap(pair):
    startA, endA, startB, endB = pair
    return (endA >= startB and startA <= startB) or (
        endB >= startA and startB <= startA
    )


def __1__(pairs, condition=contains):
    return len(
        list(
            filter(
                condition,
                [
                    [
                        int(pos)
                        for elf in pair.split(",")
                        for pos in elf.split("-")
                    ]
                    for pair in pairs
                ],
            )
        )
    )


def __2__(lines):
    return __1__(lines, overlap)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
