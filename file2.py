file_object = open('tuong.txt')
data = file_object.read()
file_object.close()
file_object = open('tuong.txt')
data = file_object.read()
data2 = file_object.read()
print(data)
print(data2)

file_object = open('text.txt', mode='r')
data = file_object.read()
file_object.seek(5)
# Hàm seek đọc file text.txt
data2 = file_object.read()
file_object.close()
print(data)
print(data2)


