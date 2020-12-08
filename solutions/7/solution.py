from sys import argv
from functools import reduce


def parse_bag(line, with_count=False):
    bag, rest = line.split('contain')
    bag = bag[:-6]
    content = []
    if rest.strip() != 'no other bags.':
        if with_count:
            content = [' '.join(bag.strip().split(' ')[0:3])
                       for bag in rest.split(',')]
            content = flatten([int(bag[0:1])*[bag[2:]] for bag in content])
        else:
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


def recursion(graph, key):
    return [[recursion(graph, bag), key] if len(graph[key]) > 0 else [bag, key] for bag in graph[key]]


def __2__(lines, key='shiny gold'):
    graph = {}
    for line in lines:
        bag, content = parse_bag(line, with_count=True)
        graph[bag] = content
    return len(flatten(recursion(graph, key)))


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
