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


max_id = 0
for line in lines:
    row = binary_partition(0, 127, line[:-3])
    col = binary_partition(0, 7, line[-3:])
    if row * 8 + col > max_id:
        max_id = row * 8 + col

print(max_id)
