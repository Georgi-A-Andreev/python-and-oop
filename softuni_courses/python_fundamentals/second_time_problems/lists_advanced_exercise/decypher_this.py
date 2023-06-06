message = [list(i) for i in input().split()]
counter = -1

for i in message:
    counter += 1
    num = ''
    for j in range(len(i)):
        if i[j].isdigit():
            num += i[j]
        else:
            break
    message[counter][0] = chr(int(num))
    message[counter] = [i for i in message[counter] if not i.isdigit()]
    message[counter][1], message[counter][-1] = message[counter][-1], message[counter][1]

for i in range(len(message)):
    message[i] = ''.join(message[i])

print(' '.join(message))
