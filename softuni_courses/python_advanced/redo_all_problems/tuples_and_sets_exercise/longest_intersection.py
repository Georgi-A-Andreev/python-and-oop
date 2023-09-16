lines = int(input())

intersection = []

for _ in range(lines):
    first_seq, second_seq = input().split('-')
    first = [int(x) for x in first_seq.split(',')]
    second = [int(x) for x in second_seq.split(',')]

    inter = set(range(first[0], first[1] + 1)).intersection(set(range(second[0], second[1] + 1)))
    if len(inter) > len(intersection):
        intersection = inter

print(f'Longest intersection is [{", ".join(str(x) for x in intersection)}] with length {len(intersection)}')
