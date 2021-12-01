print(sum([(l[i*3 % len(l)] == '#') for i, l in enumerate(open('data.txt').read().splitlines())]))
