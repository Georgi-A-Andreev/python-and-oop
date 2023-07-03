line = input().split(' ')


def reverse_line(idx, line):
    if idx >= len(line):
        return
    reverse_line(idx + 1, line)
    print(line[idx], end=' ')


reverse_line(0, line)
