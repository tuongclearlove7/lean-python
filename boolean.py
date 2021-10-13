# Kiểu DỮ LIỆU BOOLEAN
# TOÁN TỬ SO SÁNH
#3 > 1 = True
# 2 < 1 = False
#5 < 2 AND 2 > 3
      #True
print(3>1)
print(10<9)
print(241 == 161 + 100)
print((5 * 0) != 0)

name = 'tuong' == 'tuong'
print(name)
name = 'tuong' == 'Thao'
print(name)

print(ord('A'))
# ord('A') = 65
# ord ('a') = 97
print('a' > 'ABC')

print('tuong' < 'tuonCL')
print('tuong' < 'tuongCL')

list = [1,2,3]
list1 = [1,2,3]
print(list == list1)
print(list is list)

list = [1,2,3]
list1 = [1,2,3]
list1 = list
print(list is list1)

list = [1,2,3]
list1 = [1,2,3]
list1 = list
print(id(list))
print(id(list1))
print(list1 is list)

TUONG = 161
THAO = 161
print(THAO is TUONG)

TUONG = 161
THAO = 99
print(THAO is TUONG)


tuong = True + 1 # True = 1 + 1 = 2
# Gía trị của True = 1
print(tuong)
tuong = int(True)
print(tuong)

tuong = False + 1 # False = 1 + 0 = 1
# Gía trị của False = 0 
print(tuong)
tuong = int(False)
print(tuong)







