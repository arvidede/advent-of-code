from sys import argv
from functools import reduce
from copy import deepcopy


class Area():
    def __init__(self, grid):
        self.grid = self.padding(grid)
        self.next = deepcopy(self.grid)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def update(self):
        did_not_change = self.grid == self.next
        self.grid = deepcopy(self.next)
        return did_not_change

    def num_adjacent_seats(self, i, j):
        return self.seat_is_occupied(i-1, j) + \
            self.seat_is_occupied(i+1, j) + \
            self.seat_is_occupied(i, j-1) + \
            self.seat_is_occupied(i, j+1) + \
            self.seat_is_occupied(i-1, j-1) + \
            self.seat_is_occupied(i-1, j+1) + \
            self.seat_is_occupied(i+1, j-1) + \
            self.seat_is_occupied(i+1, j+1)

    # This is ridiculous
    def num_first_seats(self, i, j):
        # Up
        y = i - 1
        up = False
        while y > 0:
            if self.grid[y][j] == '#':
                up = True
                break
            if self.grid[y][j] == 'L':
                break
            y -= 1

        # Down
        y = i + 1
        down = False
        while y < self.height:
            if self.grid[y][j] == '#':
                down = True
                break
            if self.grid[y][j] == 'L':
                break
            y += 1

        # Left
        x = j - 1
        left = False
        while x > 0:
            if self.grid[i][x] == '#':
                left = True
                break
            if self.grid[i][x] == 'L':
                break
            x -= 1

        # Right
        x = j + 1
        right = False
        while x < self.width:
            if self.grid[i][x] == '#':
                right = True
                break
            if self.grid[i][x] == 'L':
                break
            x += 1

        # Top left
        y = i - 1
        x = j - 1
        up_left = False
        while y > 0 and x > 0:
            if self.grid[y][x] == '#':
                up_left = True
                break
            if self.grid[y][x] == 'L':
                break
            y -= 1
            x -= 1

        # Top right
        y = i - 1
        x = j + 1
        up_right = False
        while y > 0 and x < self.width:
            if self.grid[y][x] == '#':
                up_right = True
                break
            if self.grid[y][x] == 'L':
                break
            y -= 1
            x += 1

        # Bottom left
        y = i + 1
        x = j - 1
        down_left = False
        while y < self.height and x > 0:
            if self.grid[y][x] == '#':
                down_left = True
                break
            if self.grid[y][x] == 'L':
                break
            y += 1
            x -= 1

        # Bottom right
        y = i + 1
        x = j + 1
        down_right = False
        while y < self.height and x < self.width:
            if self.grid[y][x] == '#':
                down_right = True
                break
            if self.grid[y][x] == 'L':
                break
            y += 1
            x += 1

        return sum([up, down, left, right, up_left, up_right, down_left, down_right])

    def seat_is_occupied(self, i, j):
        return self.grid[i][j] == '#'

    def seat_is_empty(self, i, j):
        return self.grid[i][j] == 'L'

    def num_occupied_seats(self):
        return reduce(lambda a, b: a + b.count('#'), self.grid, 0)

    def padding(self, grid):
        width = len(grid[0]) + 2
        return [['.'] * width] + [['.'] + row + ['.'] for row in grid] + [['.'] * width]

    def iterate(self, max_adjacent=4, adjacent=True):
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                num_adjacent_seats = self.num_adjacent_seats(
                    i, j) if adjacent else self.num_first_seats(i, j)
                if self.seat_is_empty(i, j) and num_adjacent_seats == 0:
                    self.next[i][j] = '#'
                if self.seat_is_occupied(i, j) and num_adjacent_seats >= max_adjacent:
                    self.next[i][j] = 'L'


def __1__(lines):
    area = Area(lines)
    while True:
        area.iterate()
        if area.update():
            break
    return area.num_occupied_seats()


def __2__(lines):
    area = Area(lines)
    while True:
        area.iterate(max_adjacent=5, adjacent=False)
        if area.update():
            break
    return area.num_occupied_seats()


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = [list(line.replace('L', '#'))
             for line in open(file).read().splitlines()]
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
