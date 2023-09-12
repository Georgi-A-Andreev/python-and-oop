expression = input()

stack = []

for idx, symbol in enumerate(expression):
    if symbol == '(':
        stack.append(idx)
    elif symbol == ')':
        print(expression[stack.pop():idx + 1])
