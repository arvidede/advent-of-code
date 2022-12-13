from sys import argv
from ast import literal_eval
from functools import cmp_to_key
from math import prod

is_int = lambda x: isinstance(x, int)
is_list = lambda x: isinstance(x, list)


def in_order(left, right, inc=1):
    n_left, n_right = len(left), len(right)

    if n_left == 0 and n_left < n_right:
        return True

    if n_right == 0 and n_left > n_right:
        return False

    for idx in range(min(n_left, n_right)):
        l, r = left[idx], right[idx]
        if is_int(l) and is_int(r):
            if l < r:
                return True
            if l > r:
                return False

        if is_list(l) and is_list(r):
            is_in_order = in_order(l, r, inc + 1)
            if is_in_order is not None:
                return is_in_order
        elif is_list(l) or is_list(r):
            is_in_order = (
                in_order(l, [r], inc + 1)
                if is_list(l)
                else in_order([l], r, inc + 1)
            )
            if is_in_order is not None:
                return is_in_order

        if idx == n_left - 1 and n_left < n_right:
            return True

        if idx == n_right - 1 and n_left > n_right:
            return False
    return None


def __1__(pairs):
    return sum(
        [
            i + 1
            for i, (left, right) in enumerate(pairs)
            if in_order(left, right)
        ]
    )


def flatten(pairs):
    return [packet for pair in pairs for packet in pair]


def __2__(pairs):
    dividers = [[[2]], [[6]]]
    packets = flatten(pairs) + dividers
    compare_packets = lambda left, right: -1 if in_order(left, right) else 1
    sorted_packets = sorted(packets, key=cmp_to_key(compare_packets))
    return prod(i + 1 for i, p in enumerate(sorted_packets) if p in dividers)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return [
        list(map(literal_eval, pair.splitlines()))
        for pair in open(file).read().split("\n\n")
    ]


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
