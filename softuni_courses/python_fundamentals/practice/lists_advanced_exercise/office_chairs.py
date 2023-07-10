n = int(input())
total_visitors = 0
total_chairs = 0

for i in range(1, n + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)

    total_visitors += visitors
    total_chairs += len(chairs)

    if visitors > len(chairs):
        print(f"{visitors - len(chairs)} more chairs needed in room {i}")

if total_chairs >= total_visitors:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
