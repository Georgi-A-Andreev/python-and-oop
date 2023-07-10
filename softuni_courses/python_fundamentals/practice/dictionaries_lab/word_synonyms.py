n = int(input())
result = {}

for _ in range(n):
    word = input()
    word2 = input()

    if word not in result:
        result[word] = []
    result[word].append(word2)

for k, v in result.items():
    print(f'{k} - {", ".join(v)}')
