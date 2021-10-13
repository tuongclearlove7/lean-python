a = 'tuong'
b = a.capitalize()
# hàm capitalize là viết hoa chữ cái đầu tiên tập con trong chuỗi

print(a)
print(b)
a = 'tuong'
b = a.upper()
# hàm upper là tất cả các con trong chuỗi đều đc viết hoa
print(a)
print(b)
a = 'tuong'
b = a.lower()
# hàm lower là tất cả các chữ đều viết thường

print(a)
print(b)
a = 'tuong'
b = a.capitalize()
# hàm capitalize là viết hoa chữ cái đầu tiên tập con trong chuỗi

print(a)
print(b)
a = 'tuong'
b = a.swapcase()
# hàm swapcase tác dụng là 

print(a)
print(b)

a = 'tuong'
b = a.title()
# hàm  title sẽ viết hoa chữ cái đầu tiên còn lại là viết thường
print(a)
print(b)
a = 'tuong'
b = a.center(30, '#')
# center là căn giữ
# phương thức center (30) cách ra khoảng 30 ô
# (30, '#') print ra một chuỗi dấu thăng
print(a)
print(b)
a = 'tuong'
b = a.ljust(30, '#')
# ljust là căn trái
# phương thức ljust (30) cách ra khoảng 30 ô
 # (30, '#') print ra một chuỗi dấu thăng
print(a)
print(b)
a = 'tuong '
b = a.encode(encoding='utf-8', errors='strict')
#print ra b'tuong'
#encode là mã hóa
#
print(a)
print(b)

a = 'tuong yêu thảo '
b = a.encode()
#print ra b'tuong'
#encode là mã hóa
# xóa không hiển thị ra đc vì không có encoding='utf-8', errors='strict'
print(a)
print(b)

a = 'tuong yêu thảo '
b = a.join(('1','2','3'))
c = '1tuong'
#phương thức join cộng số trong join vào chuỗi
#
print(a)
print(b)
a = 'tuong yêu thảo '
b = a.replace('tuong' , 'yeu')

#phương thức replace print 
#yeu yêu thảo
print(a)
print(b)

a = 'tuong yêu thảo '
b = a.strip()

#phương thức strip print 
#yeu yêu thảo
print(a)
print(b)



