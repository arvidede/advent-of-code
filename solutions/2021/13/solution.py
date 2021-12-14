from sys import argv

flatten = lambda arr: [1 if non_zero else 0 for non_zero in sum(arr, [])]


def parse_dots(dots):
    coords = [tuple(map(int, dot.split(","))) for dot in dots]
    x_max, y_max = tuple(map(max, zip(*coords)))
    paper = [[0] * (x_max + 1) for _ in range(y_max + 1)]
    for x, y in coords:
        paper[y][x] = 1
    return paper


def parse_instruction(instruction):
    axis, line = instruction.replace("fold along ", "").split("=")
    return axis, int(line)


def fold(paper, instruction):
    axis, line = parse_instruction(instruction)
    if axis == "y":
        top, bottom = paper[:line], paper[(line + 1) :]
        bottom = [row for row in reversed(bottom)]
        offset = len(top) - len(bottom)
        for row in range(len(bottom)):
            for column in range(len(bottom[row])):
                top[row + offset][column] += bottom[row][column]
        paper = top
    else:
        for i, row in enumerate(paper):
            left, right = row[:line], list(reversed(row[(line + 1) :]))
            offset = len(left) - len(right)
            for column in range(len(right)):
                left[column + offset] += right[column]
            paper[i] = left
    return paper


def print_paper(paper):
    for row in paper:
        print(" ".join(["#" if point else "." for point in row]))


def __1__(dots, instructions, only_first=True):
    paper = parse_dots(dots)
    for instruction in instructions:
        paper = fold(paper, instruction)
        if only_first:
            break
    print_paper(paper)
    return sum(flatten(paper))


def __2__(dots, instructions):
    return __1__(dots, instructions, False)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    dots, instructions = [
        lines.splitlines() for lines in open(file).read().split("\n\n")
    ]
    print({"1": __1__, "2": __2__}[argv[1]](dots, instructions))


main()
