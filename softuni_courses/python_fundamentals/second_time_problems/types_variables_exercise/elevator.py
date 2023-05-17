
people = int(input())
capacity = int(input())

courses = people // capacity if people % capacity == 0 else people // capacity + 1

print(courses)
