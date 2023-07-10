budged = int(input())

while True:
    command = input()

    if command == 'End':
        print("You bought everything needed.")
        break

    command = int(command)
    if budged - command < 0:
        print("You went in overdraft!")
        break

    budged -= command
