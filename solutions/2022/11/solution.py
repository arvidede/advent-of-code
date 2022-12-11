from sys import argv
from collections import deque
from functools import reduce


def __1__(monkeys, gcm, rounds=20, divider=3):
    for r in range(rounds):
        for idx, monkey in enumerate(monkeys):
            for item in monkey.get("items"):
                op = monkey.get("op")
                new = (op(item) % gcm) // divider
                get_receiver = monkey.get("receiver")
                receiver = get_receiver(new)
                monkeys[receiver]["items"].append(new)
                monkey["inspected"] += 1
            monkey.get("items").clear()
    inspected = list(sorted(monkey["inspected"] for monkey in monkeys))
    return inspected[-2] * inspected[-1]


def __2__(monkeys, gcm):
    return __1__(monkeys, gcm, 10000, 1)


def get_op(line):
    def op(item):
        var = {"old": item}
        exec(f"old={line}", globals(), var)
        return var["old"]

    return op


is_divisible = lambda num, divider: (num) % divider == 0

mult = lambda x: reduce(lambda a, b: a * b, x)


def parse_input():
    factors = []

    def parse_monkey(monkey: str):
        rows = monkey.splitlines()
        items = deque(map(int, rows[1].split("items: ")[1].split(",")))
        op = get_op(rows[2].split("new = ")[1])
        receivers = [int(rows[5].split(" ")[-1]), int(rows[4].split(" ")[-1])]
        divider = int(rows[3].split(" ")[-1])
        factors.append(divider)
        receiver = lambda x: receivers[int(is_divisible(x, divider))]
        return {"items": items, "op": op, "receiver": receiver, "inspected": 0}

    file = argv[2] if len(argv) > 2 else "data.txt"
    monkeys = list(map(parse_monkey, open(file).read().split("\n\n")))
    gcm = mult(factors)

    return monkeys, gcm


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
