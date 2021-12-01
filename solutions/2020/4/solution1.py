from functools import reduce
from sys import argv

with open('data.txt', 'r') as f:
    required_keys = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']
    lines = f.read().split('\n\n')
    valid_passports = 0
    for line in lines:
        valid_passports += reduce(lambda rest, key: rest and key in line, required_keys, True)

    print(valid_passports)

# Alt, one line
print(sum([reduce(lambda r, k: r and k in l, ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid'], True) for l in open('data.txt').read().split('\n\n')]))
