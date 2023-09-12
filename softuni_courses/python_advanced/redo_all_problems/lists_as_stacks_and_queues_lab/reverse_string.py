def reverse_string(string, stack):
    for c in string:
        stack.append(c)

    while stack:
        print(stack.pop(), end='')


string = input()
reverse_string(string, [])
