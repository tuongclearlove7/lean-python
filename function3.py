def tuong(key_a, key_b, key_c, key_d):
    print(key_a)
    print(key_b, key_c)
    print('end', key_d)
list = ['161', 'Tuong', 2002, 'Clearlove']
tuong(list[0], list[1], list[2], list[3])
# các phần tử trong trong list được truyền vào các key  


def tuong(key_a, key_b, key_c, key_d):
    print(key_a)
    print(key_b, key_c)
    print('end', key_d)
list = [161, 'Tuong', 2002, 'Clearlove']
tuong(*list)
# chạy tương tự

def tuong(key_a, key_b, key_c, key_d):
    print(key_a)
    print(key_b, key_c)
    print('end', key_d)
list = ['161', 'Tuong', 2002]
tuong(*list, 'Clearlove7')
# truyền thêm vào key đưa vào tuong(*list, 'Clearlove7')

def tuong(key_a, key_b, key_c, *, key_d='Thao'):
    print(key_a)
    print(key_b, key_c)
    print('end', key_d)
list = ['161', 'Tuong', 2002]
tuong(*list, key_d='Thao')
# truyền vào key_d='Thao'

def tuong(*arg):
    print(arg)
    print(type(arg))
tuong('Tuong', 2002, 'Clearlove')
#

def tuong(*arg):
    print(arg)
    print(type(arg))
tuong(*(x for x in range(161)))
# tuong(*(x for x in range(7))) chạy từ 0 đến 160

def tuong(*arg, key_max):
    print(key_max)
tuong(*(x for x in range(161)), key_max='I will like')
# Xuất ra phần tử nằm trong key

def tuong(name,number):
    print('name : ',name)
    print('number: ' ,number)
dic = {'name' : 'tuong' , 'number': 16}
tuong(**dic)
#các phần tử trong dic được truyền vào key

def tuong(**arg):
    print(arg)
    print(type(arg))
tuong(name='tuong', number=16)

def tuong(**arg):
    for key, value in arg.items():
        print(key, '>', value)
tuong(name='tuong', number=16)
# dấu '>' được gán vào giữa các phần tử nằm trong key




















