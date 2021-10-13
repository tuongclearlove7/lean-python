thao = 'tuongclearlove'
def tuong(age, name = thao):
    print(name)
    print(age)
tuong(16)
tuong(161, 'thao')
# in các chuỗi nằm trong biến thao 
def tuong():
    pass
print(tuong())

def tuong():
    pass
print(tuong)

def tuong(a, b):
    pass # pass là lệnh giữ chỗ
tuong(3, 'Clearlove7')
tuong(b=3, a="tuongClearlove7")

def tuong(a, b, c, d):
    pass # pass là lệnh giữ chỗ
tuong(3, 'Clearlove7', d=1, c=5)
def tuong(a, b, c, d):
    pass # pass là lệnh giữ chỗ
tuong(3, 'Clearlove7', d=1, c=5)

print(sorted([3,4,5], reverse=True))
# chạy từ lớn đến bé

def tuong(a, b=2, c=3, d=4):
    f = (a + d) * (b + c)
    print(f)
tuong(1, d = 5) # d = 5 * 1 
# ta có a = 1 , b = 2 , d = 4 và d = 5
# (1 + 5) * (2 + 3) = 30
# khi đó in ra f = 30

def tuong(pos_or_key_arg, *, key_arg1, key_arg2):
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)
tuong(1, key_arg1=2, key_arg2='clearlove7')
# mỗi key truyền vào 1 phần tử là 1 , 2 , 'Clearlove7'
# và in ra được các phần tử này
# lưu ý phải truyền đủ vào key

def tuong(pos_or_key_arg, *, key_arg1=1, key_arg2=2):
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)
tuong(1)





















