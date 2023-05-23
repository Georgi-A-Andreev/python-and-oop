def my_f(n1):
    word = ''
    word2 = ''
    for i in n1:
        for j in range(len(i)):
            word += i[j]
        for k in range(len(i) - 1, -1, -1):
            word2 += i[k]
        if word == word2:
            print("True")
        else:
            print("False")
        word = ''
        word2 = ''


n = input().split(", ")




