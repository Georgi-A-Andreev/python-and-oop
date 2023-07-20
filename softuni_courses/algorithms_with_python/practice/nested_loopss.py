n = int(input())

vector = [0] * n


def gen1n(idx, n, vector):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return
    for i in range(1, n + 1):
        vector[idx] = i
        gen1n(idx + 1, n, vector)


gen1n(0, n, vector)
