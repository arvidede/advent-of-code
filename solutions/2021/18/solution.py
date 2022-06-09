from sys import argv
from collections.abc import Iterable
from functools import reduce
from ast import literal_eval
import re
from copy import deepcopy

DEL = "X"


def get_item_to_explode(items, depth=0):
    if depth == 4:
        return items, DEL

    changed = False
    for i, item in enumerate(items):
        if isinstance(item, list):
            changed, items[i] = get_item_to_explode(item, depth + 1)
            if changed:
                break
    return changed, items


def explode(number):
    item, number = get_item_to_explode(number)
    if item is not False:
        left, right = item
        number_str = str(number)
        left_idx = re.search(r"\d{1,3}(?=\D+X)", number_str)
        right_idx = re.search(r"\d{1,3}(?=\D+X)", number_str[::-1])
        if left_idx is not None:
            idx_start = left_idx.start()
            idx_end = left_idx.end()
            new = int(number_str[idx_start:idx_end]) + left
            number_str = f"{number_str[:idx_start]}{new}{number_str[idx_end:]}"
        if right_idx is not None:
            idx_start = right_idx.start()
            idx_end = right_idx.end()
            number_str = number_str[::-1]
            new = f"{int(number_str[idx_start:idx_end][::-1]) + right}"[::-1]
            number_str = f"{number_str[:idx_start]}{new}{number_str[idx_end:]}"
            number_str = number_str[::-1]
        return True, literal_eval(
            number_str.replace(DEL, "0").replace("'", "")
        )

    return False, number


def split(number):
    changed = False
    for i, item in enumerate(number):
        if isinstance(item, int) and item >= 10:
            left = item // 2
            number[i] = [left, item - left]
            return True, number
        if isinstance(item, list):
            changed, number[i] = split(item)
            if changed:
                break
    return changed, number


def reduce_number(left, right):
    number = [deepcopy(left), deepcopy(right)]
    action = True
    while action:
        changed, number = explode(number)
        if changed:
            continue
        action, number = split(number)

    return number


def magnitude(number):
    if isinstance(number, list):
        left, right = number
        if isinstance(left, list):
            left = magnitude(left)
        if isinstance(right, list):
            right = magnitude(right)
        return 3 * left + 2 * right
    return number


def __1__(lines):
    number = reduce(reduce_number, lines)
    return number, magnitude(number)


def __2__(lines):
    history = []
    for i, left in enumerate(deepcopy(lines)):
        for j, right in enumerate(deepcopy(lines)):
            if i != j:
                history.append(magnitude(reduce_number(left, right)))
    return max(history)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    lines = list(map(literal_eval, lines))
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
