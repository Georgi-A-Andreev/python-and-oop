n = int(input())

vector = [0] * n


def gen(idx, n, vector):
    if idx == n:
        print(vector)
        return

    for i in range(2):
        vector[idx] = i
        gen(idx + 1, n, vector)


gen(0, n, vector)