def my_f(n1):
    if n1 != 100:
        print(f"{n1}% [{n1 // 10 * '%'}{(10 - n1 // 10) * '.'}]")
        print('Still loading...')
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


n = int(input())

my_f(n)