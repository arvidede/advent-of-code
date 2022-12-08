from sys import argv

t = lambda X: list(map(list, zip(*X)))


def __1__(lines):
    by_row = lines
    by_col = t(lines)
    num_rows = len(by_row)
    num_cols = len(by_col)
    num_edge = 2 * num_rows + 2 * num_cols - 4
    num_visible = num_edge

    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            left, right = by_row[i][:j], by_row[i][(j + 1) :]
            up, down = by_col[j][:i], by_col[j][(i + 1) :]
            tree = by_row[i][j]
            if (
                tree > max(up)
                or tree > max(down)
                or tree > max(left)
                or tree > max(right)
            ):
                num_visible += 1

    return num_visible


def viewing_distance(baseline, trees):
    for n, tree in enumerate(trees):
        if tree >= baseline:
            return n + 1
    return len(trees)


def __2__(lines):
    by_row = lines
    by_col = t(lines)
    num_rows = len(by_row)
    num_cols = len(by_col)
    max_view = 0

    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):

            left, right = by_row[i][:j][::-1], by_row[i][(j + 1) :]
            up, down = by_col[j][:i][::-1], by_col[j][(i + 1) :]
            tree = by_row[i][j]

            view = 1
            view *= viewing_distance(tree, up)
            view *= viewing_distance(tree, down)
            view *= viewing_distance(tree, left)
            view *= viewing_distance(tree, right)

            max_view = max(max_view, view)

    return max_view


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return list(map(lambda line: list(map(int, line)), lines))


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
