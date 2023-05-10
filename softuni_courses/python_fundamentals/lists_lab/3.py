n = int(input())
positive = []
negative = []

for i in range(n):
    x = int(input())
    if x >= 0:
        positive.append(x)
    else:
        negative.append(x)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')
