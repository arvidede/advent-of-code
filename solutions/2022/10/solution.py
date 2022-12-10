from sys import argv


op = lambda line: 0 if line == "noop" else int(line.split(" ")[1])


def __1__(lines):
    X, cycle, signal_strength, nth_cycle = 1, 0, 0, 20
    for line in lines:
        V = op(line)
        cycle += 2 if V else 1

        if any(map(lambda c: c == nth_cycle, range(cycle - 2, cycle + 1))):
            signal_strength += nth_cycle * X
            nth_cycle += 40

        X += V
    return signal_strength


def __2__(lines):
    CRT = [list("." * 40) for _ in range(6)]

    X, cycle = 1, 0
    for line in lines:
        V = op(line)
        remaining = 2 if V else 1
        while remaining:
            for offset in range(-1, 2):
                if X + offset == cycle % 40:
                    row = cycle // 40
                    CRT[row][X + offset] = "#"
            cycle += 1
            remaining -= 1
        X += V
    return "\n".join("".join(row) for row in CRT)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
