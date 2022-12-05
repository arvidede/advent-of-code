from sys import argv
import re


def __1__(stacks, moves):
    for n, source, to in moves:
        for i in range(n):
            crate = stacks[source - 1].pop()
            stacks[to - 1].append(crate)

    return "".join([stack[-1] for stack in stacks])


def __2__(stacks, moves):
    for n, source, to in moves:
        stack = stacks[source - 1]
        stacks[source - 1] = stack[:-n]
        stacks[to - 1] += stack[-n:]

    return "".join([stack[-1] for stack in stacks])


def parse_stacks(raw_stacks):
    raw_stacks = raw_stacks.splitlines()
    raw_stacks, header = raw_stacks[:-1], raw_stacks[-1]
    columns = int(header.split("   ")[-1])
    stacks = [[] for c in range(columns)]
    for row in raw_stacks[::-1]:
        for col, crate in enumerate(re.findall("....|...$", row)):
            if crate[1] != " ":
                stacks[col].append(crate[1])

    return stacks


def parse_moves(moves):
    return [
        [int(m) for m in re.findall("\d+", move)]
        for move in moves.splitlines()
    ]


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    stacks, moves = open(file).read().split("\n\n")
    return parse_stacks(stacks), parse_moves(moves)


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
