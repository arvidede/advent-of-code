from collections import defaultdict
from sys import argv

EMPTY = "."


def checksum(blocks):
    return sum(i * int(block) for i, block in enumerate(blocks) if block != EMPTY)


def __1__(line):
    free_space = list(map(int, line[1::2]))
    files = [(str(id), int(block_size)) for id, block_size in enumerate(line[::2])]
    blocks = []

    while len(free_space) > 0:
        id, block_size = files.pop(0)
        blocks += [id] * block_size
        blocks += [EMPTY] * free_space.pop(0)

    id, block_size = files.pop(0)
    blocks += [id] * block_size

    file_blocks = [(i, block) for i, block in enumerate(blocks) if block != EMPTY]

    for block_index, block in enumerate(blocks):
        if block == EMPTY:
            last_block_index, last_block = file_blocks.pop()

            if block_index >= last_block_index:
                break

            blocks[block_index] = last_block
            blocks[last_block_index] = EMPTY

    return checksum(blocks)


FILE = "F"
SPACE = "S"


def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def shuffle(line):

    blocks = [
        {
            "type": FILE if i % 2 == 0 else SPACE,
            "size": int(block_size),
            "id": str(i // 2),
        }
        for i, block_size in enumerate(line)
    ]

    files = [(i, block) for i, block in enumerate(blocks) if block["type"] == FILE]
    spaces = [(i, block) for i, block in enumerate(blocks) if block["type"] == SPACE]
    draft = defaultdict(list)

    for file_idx, file in reversed(files):
        for space_idx, space in spaces:
            if space_idx >= file_idx:
                break

            if space["size"] >= file["size"]:
                space["size"] = space["size"] - file["size"]

                draft[space_idx].append(file)
                blocks[file_idx] = {"type": SPACE, "size": file["size"]}
                break

    for to, files in draft.items():
        space = blocks[to]

        if space["size"] > 0:
            files.append(space)

        blocks[to] = files

    return list(flatten(blocks))


def __2__(line):
    blocks = []

    for block in shuffle(line):
        if block["type"] == SPACE:
            blocks += [EMPTY] * block["size"]
            continue

        blocks += [block["id"]] * block["size"]

    return checksum(blocks)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    return list(open(file).read())


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
