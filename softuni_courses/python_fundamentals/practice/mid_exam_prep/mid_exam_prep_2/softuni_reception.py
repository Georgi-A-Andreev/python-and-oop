
one = int(input())
two = int(input())
three = int(input())

students = int(input())

together = one + two + three
counter = 0

while True:
    if students <= 0:
        break
    counter += 1
    students -= together

    if counter % 4 == 0:
        counter += 1

print(f'Time needed: {counter}h.')

