with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
    col_index = 0
    num_trees = 0
    for line in lines:
        num_trees += (line[col_index % len(line)] == '#')
        col_index += 3

    print(num_trees)
