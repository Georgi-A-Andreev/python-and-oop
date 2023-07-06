line = [int(x) for x in input().split()]


def selection_sort(line):

    for idx in range(len(line)):
        min_idx = idx
        for j in range(idx, len(line)):
            if line[j] < line[min_idx]:
                min_idx = j

        line[idx], line[min_idx] = line[min_idx], line[idx]

    return ' '.join(str(x) for x in line)


print(selection_sort(line))