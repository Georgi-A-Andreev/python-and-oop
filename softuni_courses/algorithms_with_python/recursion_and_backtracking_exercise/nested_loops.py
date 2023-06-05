def simulate_nested_loops(field, idx):
    if idx == len(field):
        print(' '.join(str(x) for x in field))
        return

    for i in range(1, len(field) + 1):
        field[idx] = i
        simulate_nested_loops(field, idx + 1)


n = int(input())
field = [1] * n
simulate_nested_loops(field, 0)
