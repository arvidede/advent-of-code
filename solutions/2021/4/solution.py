from sys import argv
from typing import List


def parse_boards(lines, grid_size=5):
    draws = list(map(int, lines[0].split(",")))
    lines = list(filter(lambda x: x, lines))
    board_rows = [
        [
            list(map(int, filter(lambda x: x, row.split(" "))))
            for row in lines[i : i + grid_size]
        ]
        for i in range(1, len(lines), grid_size)
    ]
    boards = [
        list(map(set, rows)) + [set(column) for column in zip(*rows)]
        for rows in board_rows
    ]

    return draws, boards


def mark_board(draw, board: List[set]):
    won = False
    for numbers in board:
        if draw in numbers:
            numbers.remove(draw)
        if len(numbers) == 0:
            won = True
    return board, won


def __1__(lines):
    draws, boards = parse_boards(lines)
    for draw in draws:
        for i, board in enumerate(boards):
            board, won = mark_board(draw, board)
            boards[i] = board
            if won:
                return draw * sum(list(set().union(*board)))


def __2__(lines):
    draws, boards = parse_boards(lines)
    wins = set()
    for draw in draws:
        for i, board in enumerate(boards):
            board, won = mark_board(draw, board)
            boards[i] = board
            if won:
                wins.add(i)
                if len(wins) == len(boards):
                    return draw * sum(list(set().union(*board)))


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
