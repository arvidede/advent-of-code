from sys import argv


def parse_instruction(line):
    line = line.split(' ')
    return line[0], int(line[1])


def replace_pair(v1, v2, line):
    copy = line
    if v1 in copy:
        line = line.replace(v1, v2)
    if v2 in copy:
        line = line.replace(v2, v1)
    return line


def __1__(instructions, visits=False):
    acc = 0
    index = 0
    visits = [0] * len(instructions)
    visits[index] = 1

    while visits[index] < 2:
        code, argument = parse_instruction(instructions[index])

        if code == 'acc':
            acc += argument
        if code == 'jmp':
            index += argument
        if code == 'nop' or code == 'acc':
            index += 1

        if index > len(visits) - 1:
            break

        visits[index] += 1

    return acc, index > len(visits) - 1


# I pray no google recruiter ever sees this
def __2__(instructions_):

    acc = 0
    original_instructions = instructions_
    visits = [0] * len(instructions_)

    for i, instruction in enumerate(original_instructions):
        if 'acc' in instruction:
            continue
        instructions = original_instructions.copy()
        instructions[i] = replace_pair('jmp', 'nop', instructions[i])
        acc, terminated = __1__(instructions, visits=False)
        if terminated:
            break
    return acc


def main():
    file = argv[2] if len(argv) > 2 else 'data.txt'
    lines = open(file).read().splitlines()
    print({"1": __1__, "2": __2__}[argv[1]](lines))


main()
