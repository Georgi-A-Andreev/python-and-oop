nums = [float(x) for x in input().split()]

occurrences = {}

for el in nums:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1

for k, v in occurrences.items():
    print(f'{k} - {v} times')
