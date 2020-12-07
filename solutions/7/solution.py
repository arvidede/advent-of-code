from sys import argv
from functools import reduce


def parse_bag(line):
    bag, rest = line.split('contain')
    bag = bag[:-6]
    content = []
    if rest.strip() != 'no other bags.':
        content = [' '.join(bag.strip().split(' ')[1:3])
                   for bag in rest.split(',')]
    return bag, content


def backtrack(graph, key):
    if len(graph[key]) == 0:
        return key
    return [[backtrack(graph, bag), key] for bag in graph[key]]


def flatten(L):
    return [L] if not isinstance(L, list) else [x for X in L for x in flatten(X)]


def __1__(lines, key='shiny gold'):
    graph = {}
    for line in lines:
        bag, content = parse_bag(line)
        for c_bag in content:
            if bag not in graph:
                graph[bag] = set()
            if c_bag not in graph:
                graph[c_bag] = set([bag])
                continue
            graph[c_bag].add(bag)

    return len(set(filter(lambda x: x != key, flatten(backtrack(graph, key)))))


def __2__(lines):
    return 2


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
