count = int(input())
result = {}

for i in range(count):
    word = input()
    synonym = input()

    if word not in result:
        result[word] = [synonym]
    else:
        result[word].append(synonym)

for x, y in result.items():
    print(f"{x} - {', '.join(y)}")
