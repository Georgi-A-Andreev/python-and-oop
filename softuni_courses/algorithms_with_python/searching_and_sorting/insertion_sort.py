    line = [int(x) for x in input().split()]


    def insertion_sort(line):
        for idx in range(1, len(line)):

            while line[idx] <= line[idx - 1] and idx >= 1:
                line[idx], line[idx - 1] = line[idx - 1], line[idx]
                idx -= 1

        return ' '.join(str(x) for x in line)


    print(insertion_sort(line))
