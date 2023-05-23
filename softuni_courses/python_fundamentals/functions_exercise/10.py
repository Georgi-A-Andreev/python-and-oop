def my_f(n1):
    counter = 0
    for i in range(1, n):
        if n % i == 0:
            counter += i
    if counter == n1:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())

my_f(n)
