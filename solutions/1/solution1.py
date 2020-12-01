GOAL_SUM = 2020

with open('./data.txt', 'r') as f:
    data = map(int, f.read().splitlines())

    prev_entries = {}
    product = -1
    for entry in data:
        diff = GOAL_SUM - entry
        if diff in prev_entries:
            product = entry * diff
            break
        prev_entries[entry] = entry

    print(product)
