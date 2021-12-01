from sys import argv
from collections import deque


def diff(turns):
    return turns[1] - turns[0]


def __1__(numbers, n_turns=2020):
    mem = {}
    prev_mem = {}
    last = -1
    for turn in range(1, n_turns+1):
        if turn <= len(numbers):  # Assuming all starting numbers are different
            last = numbers[turn-1]
            mem[last] = deque([turn], maxlen=2)
        else:
            if last in mem:
                if len(mem[last]) < 2:
                    last = 0
                else:
                    last = diff(mem[last])

                if last in mem:
                    mem[last].append(turn)
                else:
                    mem[last] = deque([turn], maxlen=2)
            else:
                mem[last] = deque([turn], maxlen=2)
                last = 0
    return last


def __2__(numbers):
    return __1__(numbers, n_turns=30000000)


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = list(map(int, open(file).read().split(',')))
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
