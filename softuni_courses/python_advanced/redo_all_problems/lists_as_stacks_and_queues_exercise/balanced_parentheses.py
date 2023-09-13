line = list(input())
stack = []

balanced = True
for el in line:
    if not stack and el in '}])':
        balanced = False
        break
    if stack:
        if el == ')':
            if stack.pop() == '(':
                continue
            else:
                balanced = False
                break
        elif el == ']':
            if stack.pop() == '[':
                continue
            else:
                balanced = False
                break
        elif el == '}':
            if stack.pop() == '{':
                continue
            else:
                balanced = False
                break
        else:
            stack.append(el)
    else:
        stack.append(el)

if balanced:
    print('YES')
else:
    print('NO')
