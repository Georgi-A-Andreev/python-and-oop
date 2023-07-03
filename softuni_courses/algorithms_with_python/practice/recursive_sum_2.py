line = [int(x) for x in input().split()]


def recursive_sum(idx, line):
    if idx >= len(line) - 1:
        return line[idx]

    return line[idx] + recursive_sum(idx + 1, line)


print(recursive_sum(0, line))
