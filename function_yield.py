# Lệnh yield

name = [1, 'tuong', 16]
for value in name:
    print(value)

tuong = (value for value in range(3))
for value in tuong:
    print(value)# in ra
# range(3) chạy từ 0 đến 3

print('_________________________________________________________________________')


print('Bài Toán bình Phương')
def square(list):
    sq_list = []# list rỗng
    for num in list:
        sq_list.append(num**2)#num**2 là các số được mũ 2 
    return sq_list
tuong = square([2,3,4])# 2^2 , 3^2 , 4^2
# các phần tử nằm trong square([]) được mũ 2 
for value in tuong:
    print(value) # in ra kết quả

def square(list):
    for num in list:
        yield num**2
tuong = square([5,5,5])# 5^2
# các phần tử nằm trong square([]) được mũ 2 
for value in tuong:
    print(value) # in ra kết quả
# chạy với kết quả Tương tự

def clearlove():
    for value in range(3):# range(3) chạy từ 0 đến 2
        print('yield', value+1, 'time')# chạy 1 đến 3 
        #gán value+1 vào giữa yield time 
        yield value
for value in clearlove():
    print(value)

def clearlove():
    yield 'tuong'
    print('this is second yield')
    yield 'clearlove7'
    print('this is the last yield')
    yield 'I love you Thao'
    print('will not return anything')
for value in clearlove():
    print(value)

def tuong():
    while True:
        x = yield
        yield x ** 2
k = tuong()
print(next(k))
k.send(2)
print(next(k))
k.send(10)


def tuong():
    while True:
        x = yield# khởi tạo x 
        yield x ** 2 # x ^ 2
k = tuong()
next(k)# 2^2
print(k.send(2))
#Phương thức send(2) chuyển 2 vào k  
next(k) # 10^2
print(k.send(10))# send(10) chuyển 10 vào k 

def tuong():
    while True:
        x = yield
        yield x**2 # x ^ 2
k = tuong()
print(next(k))
print(k.send(2))
print(next(k))
print(k.send(10))

























