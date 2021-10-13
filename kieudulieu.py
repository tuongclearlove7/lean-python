# gán cho a giá trị = 4 là kiểu số nguyên
a = 1.123456789101112131415
#print là dán ra màn hình
print(a)
#kiểu dữ liệu của a
print(type(a))
# số nguyên là số 1 2 3 4 5......
# số thực là số 2.1 , 2.2 , 2.3 , .......
#chỉ lấy sắc xuất 12 chữ số ở đuôi
# tác dụng là lấy toàn bộ nội dung của thư viện decimal
from decimal import*
# từ thư viện decimal import mọi thứ vào (*) 
# lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
# dùng hàm getcontext().prec
getcontext().prec = 30
f = 10/3
print(f)

print(Decimal(10)/Decimal(3))
# nó chỉ chỉ 30 chữ số ở đằng sau
