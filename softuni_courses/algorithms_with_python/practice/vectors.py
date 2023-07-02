n = int(input())
vector = [0] * n


def lexi(idx, vector):
    if idx < 0 or idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(0, 2):
        vector[idx] = num
        lexi(idx + 1, vector)


lexi(0, vector)
