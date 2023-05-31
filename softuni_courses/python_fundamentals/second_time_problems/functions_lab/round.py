def rounding(lst):
    return [round(float(i)) for i in lst.split()]


input_list = input()

print(rounding(input_list))