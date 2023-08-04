n = int(input())

vector = [1] * n


def print_vec01(vector, idx):
    if idx == len(vector):
        print(*vector, sep=' ')
        return
    for num in range(1, len(vector) + 1):
        vector[idx] = num
        print_vec01(vector, idx + 1)


print_vec01(vector, 0)