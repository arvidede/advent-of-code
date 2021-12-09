from sys import argv


def parse_input(lines):
    return [
        [column.split(" ") for column in line.split(" | ")] for line in lines
    ]


sort_str = lambda a: "".join(sorted(a))
subtract = lambda a, b: sort_str(a.translate({ord(x): "" for x in b}))
add = lambda a, b: sort_str("".join(set(a + b)))
find = lambda condition, items: next(item for item in items if condition(item))

# I must have misunderstood something. This is ridiculous
def deduce(signal):
    segment_map = {}
    signal = sorted(signal, key=len)

    one = sort_str(signal[0])
    seven = sort_str(signal[1])
    four = sort_str(signal[2])
    eight = sort_str(signal[-1])
    six = sort_str(find(lambda x: len(add(x, one)) != len(x), signal[6:9]))
    nine = sort_str(find(lambda x: len(add(x, four)) == len(x), signal[6:9]))
    zero = sort_str(
        find(lambda x: sort_str(x) not in [six, nine], signal[6:9])
    )

    a = subtract(seven, one)
    c = subtract(eight, six)
    d = subtract(eight, zero)
    f = subtract(one, c)
    b = subtract(subtract(four, one), d)
    e = subtract(eight, nine)
    g = subtract(subtract(subtract(zero, seven), b), e)

    two = sort_str(f"{a}{c}{d}{e}{g}")
    three = sort_str(f"{a}{c}{d}{f}{g}")
    five = sort_str(f"{a}{b}{d}{f}{g}")

    segment_map[zero] = 0
    segment_map[one] = 1
    segment_map[two] = 2
    segment_map[three] = 3
    segment_map[four] = 4
    segment_map[five] = 5
    segment_map[six] = 6
    segment_map[seven] = 7
    segment_map[eight] = 8
    segment_map[nine] = 9

    return segment_map


def __1__(lines):
    find = set([2, 3, 4, 7])
    found = sum(
        [
            len(digit) in find
            for signal, output in parse_input(lines)
            for digit in output
        ]
    )

    return found


def __2__(lines):
    total = 0
    signals, outputs = zip(*parse_input(lines))
    for i, signal in enumerate(signals):
        segment_map = deduce(signal)
        total += int(
            "".join(
                f"{segment_map.get(sort_str(digit), '')}"
                for digit in outputs[i]
            )
        )
    return total


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
