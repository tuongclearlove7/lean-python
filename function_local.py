# Khai báo biến local
local = 'Tuong'
def say_slogan():
    print('my name is', local)
# My name is được gán biến local vào sau 
say_slogan()

def say_slogan():
    local = 'Thao'
    print('I Love You', local)
say_slogan()
# chạy tương tự

num = 161
name = 'Tuong'
list = [1,2,3]
tup = tuple('Clearlove7')
def change(parameter):
    parameter = 'Neww value'
    print('changed successfully!')
change(num)# in ra phần tử của biến num
change(name)# in phần tử của biến name
change(list)# in ra phần tử của list[]
change(tup)# in ra một chuỗi tuple
# gọi 4 lần change in ra 4 changed successfully!
print('#'* 10)# 10 dấu thăng
print('{}\n{}\n{}\n{}\n'.format(num, name, list, tup))


list = ['tuong', 1, 2, 3]
def change(parameter):
    parameter[1] = 'neww value'
    print('changed successfully!')
# parameter được gán vào giữa các phần tử của biến list
print(list)
change(list)
print(list)

def make_slogan():
    global name
    # global khởi trị biến name
    name = 'tuongclearlove'
make_slogan()
print(name) # in ra 
 

def make_global():
    global x # khởi tạo biến x
    x = 1
def local():
    x = 5
    print(' x in local', x)
# x in local được gán thêm giá trị của x vào sau
make_global()
print(x) # in ra biến 
local()
print(x)# in ra biến










