a = 'Tuong Clearlove7'
b = a.split(' ', 2)
# Phương thức split cắt khoảng
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.partition('e')
# Phương thức partition cắt chuỗi 
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.count('e',0,10)
# Phương thức count tìm từ vị trí con trong chuỗi trong khoảng từ 0 đến 10
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.startswith('7',4,5)
# Phương thức  startstwith (True or false)
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.find('Tuong')
# Phương thức  find tìm là số thứ tự của chữ trog chuỗi
# rfind là từ thứ tự từ phải qua 
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.rindex('7')
# Phương thức  index giống find
#  là từ thứ tự từ phải qua 
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.index('7')
# Phương thức  find tìm là số thứ tự của chữ trog chuỗi
# khác find ở cái là tìm ra nếu k thấy thì sẽ lỗi
print(a)
print(b)

a = 'Tuong Clearlove7'
b = a.islower()
# Phương thức  islower (true of false)
# tuong tự là phương thức isupper
print(a)
print(b)

a = 't1'
b = a.isdigit()
# Phương thức   isdigit (true or false)
# tương tự là phương thứ isspace
# cách khoảng trắng trong chuỗi
print(a)
print(b)

