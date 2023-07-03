n = int(input())
vector = [0] * n


def gen01(vector, idx):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for el in range(2):
        vector[idx] = el
        gen01(vector, idx + 1)


gen01(vector, 0)