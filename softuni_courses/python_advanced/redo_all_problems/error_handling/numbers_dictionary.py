numbers_dictionary = {}
while True:
    line = input()

    if line == 'Search':
        break
    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print("The variable number must be an integer")


while True:
    line = input()
    if line == "Remove":
        break
    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary" )

while True:
    line = input()

    if line == "End":
        break
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
