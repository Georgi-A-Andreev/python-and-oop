positives_list = []
negatives_list = []

for _ in range(int(input())):
    num = int(input())
    if num >= 0:
        positives_list.append(num)
    else:
        negatives_list.append(num)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")
