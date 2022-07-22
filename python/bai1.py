file_object = open('bai1.txt', mode='a+')
data = file_object.write('''
Ngay gia vang ban ra gia vang mua vao
______________________________________
1/3               46               45
2/3               47               46  
3/3               46              45.5
4/3               45               45
6/3               46              45.5
7/3               46              44.5''')
print(data)
file_object.close()
file_object = open('bai1.txt')
data_read = file_object.read()
print(data_read)


























