def tuong(a, b, c):
    return(a + b + c)/3 # 1 + 2 + 4 / 3
print(tuong(1,2,4)) # in ra màn hình


tuong = lambda a,b,c: (a+b+c)/3 # 1 + 2 + 3 / 3
print(tuong(1,2,3)) # chạy tương tự


tuong = lambda x, a=2: x ** a # 
print(tuong(3 , 5))# 3 ^ 5
# lưu ý chỉ truyền 2 phần tử vào hàm tuong() vì chỉ có 2 biến

def tuong():
    num = lambda x: x + ' Clearlove7' 
    return num # gán phần tử trong biến num vào trước call_num 
call_num = tuong()
print(call_num('My name is Tuong'))

print('_____________________________________________________________________')

def tuong():
    num = lambda x: x + ' Clearlove7' 
    return num # gán phần tử trong biến num vào trước call_num 
call_num = tuong()
print(call_num('My name is Tuong'))
print(call_num)# in ra một lambda

tuong_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4] 
# x ^ 2 , x ^ 3 , x ^ 4
print(tuong_list[0])

tuong_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4] 
# x ^ 2 , x ^ 3 , x ^ 4
print(tuong_list[1](2)) # 2 ^ 3

tuong_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4] 
# x ^ 2 , x ^ 3 , x ^ 4
print(tuong_list[-1](2)) # 2 ^ 4


print("_____________________________________________________")

tuong_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4] 
# x ^ 2 , x ^ 3 , x ^ 4
for tuong in tuong_list:
    print(tuong(3)) # gọi 3 hàm 3^2 , 3^3 , 3 ^ 4

key = 'tuong'
print({'facebook': lambda: 'Intagram',
'youtube': lambda: 'zalo',
'tuong': lambda: 'Clearlove7'}[key]()) 
#chỉ lấy 'Clearlove7' vì in ra biến 'Clearlove7' nằm trong key

find_greater = lambda x, y: x if x > y else y
# if nếu  x > y thì lấy x 
# khác else y > x thì lấy y 
print(find_greater(6, 2))# in ra số lớn hơn


def tuong(first_string):
    return lambda second_string: first_string + second_string
slogan = tuong('Clearlove7')
print(slogan)

def tuong(first_string):
    return lambda second_string: first_string + second_string
slogan = tuong('Tuong')
print(slogan('Clearlove7'))
# gán (slogan('Clearlove7') vào sau tuong('Tuong')

k = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0 
print(k(6))
#if nếu  6 vừa chia hết cho 3 và 2 nên = 1 
#else nếu là một con số khác không chia hết cho 3 và 2 thì = 0

k = lambda x: ('chia hết cho 2 và 3' if x % 3 == 0 else 0) if x % 2 == 0 else 'không chia hết cho 2 và 3'
print(k(9))
#if nếu  k là một số vừa chia hết cho 2 và 3 => chia hết cho 3 và 2
#else khác k là một số không chia hết cho 2 và 3 thì => không chia hết cho 3 và 2





















