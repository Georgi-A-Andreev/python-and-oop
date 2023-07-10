def loading_bar(n):
    result = ['.'] * 10

    for i in range(n // 10):
        result[i] = '%'
    if n == 100:
        return f"100% Complete!\n[{''.join(result)}]"

    return f"{n}% [{''.join(result)}]\nStill loading..."


n = int(input())
print(loading_bar(n))
