numbers = [int(i) for i in input().split(', ')]
count_of_beggars = int(input())

beggar_list = [0] * count_of_beggars

for i in range(len(numbers)):
    beggar_list[i % count_of_beggars] += numbers[i]

print(beggar_list)
