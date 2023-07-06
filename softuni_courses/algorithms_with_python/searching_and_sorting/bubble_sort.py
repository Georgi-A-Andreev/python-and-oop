line = [int(x) for x in input().split()]


def bubble_sort(line):
    for idx in range(len(line)):

        for j in range(1, len(line) - idx):
            if line[j] < line[j - 1]:
                line[j], line[j - 1] = line[j - 1], line[j]

    return ' '.join(str(x) for x in line)


print(bubble_sort(line))
