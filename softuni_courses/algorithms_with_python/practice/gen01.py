n = int(input())
vector = [0] * n


def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for i in range(2):
        vector[idx] = i
        gen01(idx + 1, vector)


gen01(0, vector)
