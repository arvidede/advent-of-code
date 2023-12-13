import re
from math import lcm
from sys import argv


def solve(instructions, nodes, start_node, end_node):
    current_node = start_node
    current_instruction = 0
    path = []
    n_instructions = len(instructions)

    while current_node != end_node:
        instruction = instructions[current_instruction % n_instructions]
        path.append(current_node)
        current_node = nodes[current_node][instruction]
        current_instruction += 1

    return path


def __1__(instructions, nodes):
    return len(solve(instructions, nodes, "AAA", "ZZZ"))


def __2__(instructions, nodes):
    start_end = [
        ("LQA", "FBZ"),
        ("SGA", "QNZ"),
        ("AAA", "ZZZ"),
        ("BJA", "QXZ"),
        ("SVA", "LHZ"),
        ("GFA", "BRZ"),
    ]

    return lcm(
        *(
            len(solve(instructions, nodes, start_node, end_node))
            for start_node, end_node in start_end
        )
    )


def parse_node_link(node):
    return re.match("(\w{3}) = \((\w{3}), (\w{3})\)", node).groups()


def build_map(links):
    return {root: (left, right) for root, left, right in links}


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    instructions, nodes = open(file).read().split("\n\n")
    instructions = list(
        map(int, list(instructions.replace("L", "0").replace("R", "1")))
    )
    node_map = build_map((map(parse_node_link, nodes.splitlines())))
    return instructions, node_map


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
