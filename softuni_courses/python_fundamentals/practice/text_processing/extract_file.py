end = input().split('\\')[-1]

file_name = end.split('.')[0]
extension = end.split('.')[-1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")