from sys import argv
from collections import Counter


def parse_rules(rules):
    return {
        key: value for key, value in [rule.split(" -> ") for rule in rules]
    }


def __1__(polymer, rules, steps=10):
    rules = parse_rules(rules)
    frequencies = Counter()
    char_frequencies = Counter(polymer)

    for i in range(len(polymer) - 1):
        frequencies[polymer[i : (i + 2)]] += 1

    for step in range(steps):
        step_frequency = Counter()
        for pair, frequency in frequencies.items():
            step_frequency[pair[0] + rules[pair]] += frequency
            step_frequency[rules[pair] + pair[1]] += frequency
            char_frequencies[rules[pair]] += frequency
        frequencies = step_frequency
    return max(char_frequencies.values()) - min(char_frequencies.values())


def __2__(polymer, rules):
    return __1__(polymer, rules, 40)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    template, rules = open(file).read().split("\n\n")
    print({"1": __1__, "2": __2__}[argv[1]](template, rules.splitlines()))


main()
