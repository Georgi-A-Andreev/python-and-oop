def generate_partitions(n, max_val=None):
    partitions = []

    if n == 0:
        partitions.append([])
        return partitions

    if max_val is None:
        max_val = n

    for i in range(1, min(max_val, n) + 1):
        sub_partitions = generate_partitions(n - i, i)
        for partition in sub_partitions:
            partitions.append([i] + partition)

    return partitions


def display_partitions(partitions):
    for partition in partitions[::-1]:
        print(' + '.join([str(x) for x in partition]))


n = int(input())
partitions = generate_partitions(n)
display_partitions(partitions)
