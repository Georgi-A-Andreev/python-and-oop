line = input().split()
counter = 0

while True:
    text = input()

    if text == 'end':
        break

    counter += 1

    idx1, idx2 = [int(i) for i in text.split()]

    if idx1 == idx2 or idx1 < 0 or idx2 < 0 or idx1 >= len(line) or idx2 >= len(line):
        line.insert(len(line) // 2, f"-{counter}a")
        line.insert(len(line) // 2, f"-{counter}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if line[idx1] == line[idx2]:
        item = line[idx1]
        line.remove(item)
        line.remove(item)
        print(f"Congrats! You have found matching elements - {item}!")
    else:
        print("Try again!")

    if not line:
        print(f"You have won in {counter} turns!")
        break

if line:
    print(f'''Sorry you lose :(
{' '.join(line)}
''')
