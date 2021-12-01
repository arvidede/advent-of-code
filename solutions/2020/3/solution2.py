from functools import reduce

with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

    policies = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    num_trees = [0] * len(policies)

    for l_idx, line in enumerate(lines):
        for p_idx, policy in enumerate(policies):
            if l_idx % policy[1] == 0:
                col = (policy[0] * round(l_idx / policy[1])) % len(line)
                num_trees[p_idx] += (line[col] == '#')

    print(reduce(lambda a, b: a*b, num_trees), num_trees)
