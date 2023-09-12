stack = []

commands = int(input())
for _ in range(commands):
    query = input()

    if query == '4':
        if stack:
            print(min(stack))

    elif query == '3':
        if stack:
            print(max(stack))

    elif query == '2':
        if stack:
            stack.pop()

    else:
        stack.append(int(query.split()[1]))

print(', '.join(str(x) for x in stack[::-1]))
