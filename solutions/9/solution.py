from sys import argv
from collections import deque
import random


def __1__(lines, preamble=25):
    previous = deque(lines[0:preamble], maxlen=preamble)
    lines = lines[preamble:]

    for line in lines:
        for i, entry in enumerate(previous):
            if previous.count(line - entry) > 0:
                break
            if i == preamble - 1:
                return line
        previous.append(line)
    return False


# If it looks stupid, but it works, it's not stupid
def __2__(lines):
    invalid_number = __1__(lines)

    def random_interval(min_=0, max_=len(lines)):
        start = random.randint(0, len(lines)-2)
        end = random.randint(start + 1, len(lines)-1)
        return start, end

    start, end = random_interval()
    while sum(lines[start:end]) != invalid_number:
        start, end = random_interval()

    return min(lines[start:end]) + max(lines[start:end])


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    lines = list(map(int, lines))
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
