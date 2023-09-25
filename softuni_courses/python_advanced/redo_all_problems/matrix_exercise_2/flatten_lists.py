initial_list = input().split('|')

for i in range(len(initial_list)-1, -1, -1):
    [print(x, end=' ') for x in initial_list[i].split()]
