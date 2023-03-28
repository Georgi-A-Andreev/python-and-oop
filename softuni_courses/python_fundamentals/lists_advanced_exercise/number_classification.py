positive, negative, even, odd = [], [], [], []

n = [int(x) for x in input().split(", ")]

[positive.append(str(x)) if x >= 0 else negative.append(str(x)) for x in n]
[even.append(str(x)) if x % 2 == 0 else odd.append(str(x)) for x in n]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
