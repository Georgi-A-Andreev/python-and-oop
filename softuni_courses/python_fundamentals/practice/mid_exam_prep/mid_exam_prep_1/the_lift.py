people_waiting = int(input())
lift = [int(i) for i in input().split()]

while True:
    if people_waiting == 0:
        break

    for i in range(len(lift)):
        if lift[i] < 4:
            lift[i] += 1
            people_waiting -= 1
            break
    else:
        break

if people_waiting > 0:
    print(f'''There isn't enough space! {people_waiting} people in a queue!
{' '.join(str(x) for x in lift)}
''')

elif people_waiting == 0 and lift[-1] == 4:
    print(' '.join(str(x) for x in lift))

else:
    print(f'''The lift has empty spots!
{' '.join(str(x) for x in lift)}
''')
