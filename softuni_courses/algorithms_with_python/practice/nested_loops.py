n = int(input())
line = [1] * n


def simulate_loop(idx, n, line):
    if idx >= len(line):
        print(*line, sep=' ')
        return
    for num in range(1, n + 1):
        line[idx] = num
        simulate_loop(idx + 1, n, line)


simulate_loop(0, n, line)
