from sys import argv

MARKER_LEN = 4
MESSAGE_LEN = 14


def __1__(line, num_bits=MARKER_LEN):
    for i in range(num_bits, len(line) + 1):
        if len(set(line[(i - num_bits) : i])) == num_bits:
            return i


def __2__(line):
    return __1__(line, MESSAGE_LEN)


def test(question):
    with open(f"validation{question}.txt", "r") as f:
        lines = f.readlines()

        if question == 1:
            for case, answer in enumerate([5, 6, 10, 11]):
                assert __1__(lines[case]) == answer

        if question == 2:
            for case, answer in enumerate([19, 23, 23, 29, 26]):
                assert __2__(lines[case]) == answer


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    line = open(file).readline().replace("\n", "")
    return line


def main():
    test(argv[1])
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
