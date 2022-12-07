from sys import argv
from math import inf


class File:
    def __init__(self, name, size):
        self.size_ = int(size)
        self.name = name

    def size(self):
        return self.size_

    def __str__(self, n):
        return f"{'  ' * n}- {self.name} (file, size={self.size_})"


class Dir:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.children = {}
        self.size_ = None

    def mkdir(self, name):
        self.children[name] = Dir(name, self)

    def touch(self, name, size):
        self.children[name] = File(name, size)

    def size(self):
        if self.size_ is None:
            self.size_ = sum(
                [entry.size() for entry in self.children.values()]
            )
        return self.size_

    def cd(self, path):
        if path == "..":
            return self.parent
        return self.children.get(path)

    def __str__(self, n=1):
        prefix = "  " * n
        children = (f"{prefix}\n").join(
            t.__str__(n + 1) for t in self.children.values()
        )
        return f"{prefix}- {self.name} (dir)\n{children}"


def flatten(tree, nodes=[]):
    if len(nodes) == 0:
        nodes.append(tree.size())
    for child in tree.children.values():
        if isinstance(child, Dir):
            nodes.append(child.size())
            flatten(child, nodes)

    return nodes


def create_dir_tree(commands) -> Dir:
    root = Dir("/", None)
    current_dir = root
    for command in commands:
        args = command.split(" ")

        if command == "$ ls":
            continue

        if command.startswith("$ cd"):
            current_dir = current_dir.cd(args[2])
            continue

        if command.startswith("dir"):
            current_dir.mkdir(args[1])
            continue

        size, file = args
        current_dir.touch(file, size)

    return root


def __1__(lines):
    tree = create_dir_tree(lines)
    return sum(list(filter(lambda x: x <= 100000, flatten(tree))))


def __2__(lines):
    MEMORY = 70000000
    MIN_AVAILABLE = 30000000
    tree = create_dir_tree(lines)
    available = MEMORY - tree.size()
    required = MIN_AVAILABLE - available

    return list(filter(lambda x: x >= required, sorted(flatten(tree))))[0]


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()[1:]
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
