from sys import argv
import re

file = argv[1] if len(argv) > 1 else 'data.txt'

validation = {
    'byr': lambda value: bool(re.fullmatch(r"\d{4}$", value)) and (1920 <= int(value) <= 2002),
    'iyr': lambda value: bool(re.fullmatch(r"\d{4}$", value)) and (2010 <= int(value) <= 2020),
    'eyr': lambda value: bool(re.fullmatch(r"\d{4}$", value)) and (2020 <= int(value) <= 2030),
    'hgt': lambda value: bool(re.fullmatch(r"\d{2,3}(in|cm)$", value)) and ((150 <= int(value[:-2]) <= 193) if value[-2:] == 'cm' else (59 <= int(value[:-2]) <= 76)),
    'hcl': lambda value: bool(re.fullmatch(r"#[a-f0-9]{6}$", value)),
    'ecl': lambda value: bool(re.fullmatch(r"(amb|blu|brn|gry|grn|hzl|oth)", value)),
    'pid': lambda value: bool(re.fullmatch(r"\d{9}$", value)),
    'cid': lambda value: True
}

with open(file) as f:
    valid_passports = 0
    for passport in f.read().split('\n\n'):
        required_fields = {
            'byr': False,
            'iyr': False,
            'eyr': False,
            'hgt': False,
            'hcl': False,
            'ecl': False,
            'pid': False,
            'cid': True
        }
        for field in passport.replace('\n', ' ').split(' '):
            key, value = field.split(':')
            required_fields[key] = validation[key](value)

        valid_passports += all(required_fields.values())

    print(valid_passports)
