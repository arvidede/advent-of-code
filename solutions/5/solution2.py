from sys import argv

file = argv[1] if len(argv) > 1 else 'data.txt'

with open(file) as f:
    lines = f.read() \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('L', '0') \
        .replace('R', '1') \
        .splitlines()


def binary_partition(lower, upper, is_upper):
    if len(is_upper) == 1:
        return upper if int(is_upper) else lower
    mid = lower + (upper - lower) // 2
    return binary_partition(lower if not int(is_upper[0]) else mid + 1,
                            upper if int(is_upper[0]) else mid,
                            is_upper[1:])

def partition_seat(seat):
    return binary_partition(0, 127, seat[:-3]), binary_partition(0, 7, seat[-3:])

ids = sorted([row * 8 + col for line in lines for row, col in [partition_seat(line)]])

for a,b in zip(ids[:-1], ids[1:]):
    if b - a > 1:
        print(a + 1)
        break