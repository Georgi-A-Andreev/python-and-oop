text = input()

print("".join([i for i in text if i.isdigit()]))
print("".join([i for i in text if i.isalpha()]))
print("".join([i for i in text if not i.isalpha() and not i.isdigit()]))
