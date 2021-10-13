file_object = open('text.txt')
# hàm open mở file text.txt
data = file_object.read(2)
data2 = file_object.read(10)
# hàm read đọc file text.txt
print(data2)
print(data)

file_object = open('text.txt')
data = file_object.read()
file_object.close()
# hàm close đóng file text.txt
file_object = open('text.txt')
data = file_object.read()
data2 = file_object.read()
print(data)
print(data2)

file_object = open('text.txt')
data = file_object.readlines()
data2 = file_object.readlines()
# readlines đọc từng kí tự
file_object.close()
# hàm close đóng file text.txt
print(data)
print(data2)

file_object = open('text.txt', mode='a+')
data = file_object.write('\nTuong love Thao')
# hàm write viết thêm ký tự ('\nTuong love Thao') vào file text.txt
file_object.close()
print(data)











