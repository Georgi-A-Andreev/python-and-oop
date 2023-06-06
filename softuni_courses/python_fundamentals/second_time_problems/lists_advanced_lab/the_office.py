happiness = [int(i) for i in input().split()]
improvement_factor = int(input())

happiness_with_factor = [i * improvement_factor for i in happiness]

average = sum(i for i in happiness_with_factor) / len(happiness_with_factor)

current = [i for i in happiness_with_factor if i > average]

if len(current) >= len(happiness_with_factor) // 2:
    print(f"Score: {len(current)}/{len(happiness_with_factor)}. Employees are happy!")
else:
    print(f"Score: {len(current)}/{len(happiness_with_factor)}. Employees are not happy!")
