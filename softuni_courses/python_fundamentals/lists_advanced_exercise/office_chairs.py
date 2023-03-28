rooms = int(input())
free_chairs = 0
game_on = True
for i in range(1, rooms + 1):
    chairs, visitors = input().split()
    if int(visitors) > len(chairs):
        print(f'{int(visitors) - len(chairs)} more chairs needed in room {i}')
        game_on = False
    else:
        free_chairs += (len(chairs) - int(visitors))

if game_on:
    print(f'Game On, {free_chairs} free chairs left')
