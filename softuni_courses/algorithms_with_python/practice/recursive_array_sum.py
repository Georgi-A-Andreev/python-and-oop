line = [int(x) for x in input().split()]


def recursive_sum(line, idx):
    if idx == len(line) - 1:
        return line[idx]

    return line[idx] + recursive_sum(line, idx + 1)


print(recursive_sum(line, 0))