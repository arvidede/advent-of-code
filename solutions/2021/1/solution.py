from sys import argv


def __1__(lines):
    nums = list(map(int, lines))
    return sum([num > nums[i-1] for i, num in enumerate(nums)])


def __2__(lines):
    nums = list(map(int, lines))
    window = 3
    return sum([nums[i+window] > nums[i] for i in range(len(nums) - window)])


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
