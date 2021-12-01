from sys import argv
from functools import reduce


def index_replace(s, idx, new):
    return s[:idx] + new + s[idx+1:]


def binary_combinations(address, key='X'):
    if address.count(key) > 0:
        idx = address.index(key)
        false = index_replace(address, idx, '0')
        true = index_replace(address, idx, '1')
        if true.count(key) > 0:
            return binary_combinations(false) + binary_combinations(true)
        return [false, true]
    return []


def bitmask(value, mask, floating=False):
    if floating:
        return binary_combinations("".join([a if b == '0' else b if b == 'X' else '1' for a, b in zip(value, mask)]))
    return "".join([a if b == 'X' else b for a, b in zip(value, mask)])


def __1__(instructions, address_bits=36):
    mem = {}
    mask = 'X' * address_bits
    for instruction in instructions:
        if 'mask' in instruction:
            mask = instruction[-address_bits:]
            continue
        address, value = instruction.split('] = ')
        address = address.split('[')[1]
        value = format(int(value), '036b')
        mem[address] = bitmask(value, mask)

    return reduce(lambda a, b: a + int(b, 2), mem.values(), 0)


def __2__(instructions, address_bits=36):
    mem = {}
    mask = '0' * address_bits
    for instruction in instructions:
        if 'mask' in instruction:
            mask = instruction[-address_bits:]
            continue
        address, value = instruction.split('] = ')
        address = format(int(address.split('[')[1]), '036b')

        for masked_address in bitmask(address, mask, floating=True):
            mem[masked_address] = int(value)

    print(mem)
    return sum(mem.values())


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
