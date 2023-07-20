line = [int(x) for x in input().split()]


def reverse_and_print_line(idx, line):
    if idx == len(line):
        return
    reverse_and_print_line(idx + 1, line)
    print(line[idx], end=' ')


reverse_and_print_line(0, line)
