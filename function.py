# kiểu dữ liệu function
from typing import Text


def tuong():
    pass
print(tuong())

def tuong():
    pass
print(tuong)

def tuong():
    print('hello world')
print(tuong())

def tuong():
    print('hello world'), 
tuong()
tuong()
tuong()
tuong()

def tuong():
    print('hello world2')
    print('hi son!')
tuong()
tuong()
tuong()
tuong()
# có 4 hàm in ra nên xuất ra 4 phần tử trong chuỗi 

def tuong(text):
    print(text)
tuong('hello world1')

def tuong(text, age):
    print(text)
    print(age)
tuong('hello world!', 16)
# in ra  chuỗi và số nằm trong hàm tuong có biến là text và age
# lưu ý phải truyền đủ dữ liệu vào trong hàm tuong()
# khi hàm hàm đó chứa 2 biến

def tuong(age, name = 'tuong'):
    print(name)
    print(age)
tuong(161)
# lưu ý khi biến chứa chuỗi hoặc số  phải nằm cuối 

def tuong(age, name = 'tuong'):
    print(name)
    print(age)
tuong(161)
tuong(2002, 'thao')

thao = 'tuongclearlove'
def tuong(age, name = thao): # age là biến nằm trong hàm tuong()
    print(name)
    print(age)
tuong(16)
tuong(161, 'thao')
# in các chuỗi nằm trong biến thao 
# và phần tử nằm trong hàm tuong()
def f(tuong = []):
    tuong.append('#')
    print(tuong)
f()# in ra ký tự ('#') nằm trong tuong.append()
f()# khi có bao nhiêu hàm f()
f()# thì in ra ký tự nằm trong tuong.append()
f()# theo hướng tăng dần 1 ký tự từ trên xuống
f()
f()
f()
# lưu ý không print()


















