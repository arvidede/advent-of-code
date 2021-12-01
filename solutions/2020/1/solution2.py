GOAL_SUM = 2020

with open('./data.txt', 'r') as f:
    data = map(int, f.read().splitlines())

    prev_entries = {}
    product = -1
    data = sorted(data)
    for i, entry in enumerate(data):
        for entry_ in data[i:]:
            diff = GOAL_SUM - entry - entry_
            if diff in prev_entries:
                product = entry * diff * entry_
                break
            prev_entries[entry_] = entry_

    print(product)
