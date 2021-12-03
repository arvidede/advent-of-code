from sys import argv
from math import floor


def transpose(rows):
    return list(map(list, zip(*rows)))


def ones_complement(n):
    return n.replace("1", ".").replace("0", "1").replace(".", "0")


DEFAULT_CRITERIA = lambda x: int(x + 0.5)
CO2_CRITERIA = lambda x: 2 + ~DEFAULT_CRITERIA(x)


def most_frequent_by_column(rows, criteria=DEFAULT_CRITERIA):
    num_rows = len(rows)
    columns = transpose(rows)
    return "".join(
        [str(criteria(sum(map(int, column)) / num_rows)) for column in columns]
    )


def find_by_criteria(rows, criteria):
    n_bits = len(rows[0])
    for bit in range(n_bits):
        freq = most_frequent_by_column(rows, criteria)
        rows = list(filter(lambda x: x[bit] == freq[bit], rows))
        if len(rows) == 1:
            return int(rows[0], 2)


def __1__(rows):
    gamma_bin = most_frequent_by_column(rows)
    epsilon_bin = ones_complement(gamma_bin)
    return int(gamma_bin, 2) * int(epsilon_bin, 2)


def __2__(rows):
    oxygen = find_by_criteria(rows.copy(), DEFAULT_CRITERIA)
    co2 = find_by_criteria(rows.copy(), CO2_CRITERIA)
    return oxygen * co2


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    rows = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](rows))


main()
