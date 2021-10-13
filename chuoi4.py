# 1 chuỗi thêm % và chuỗi kia thì print ra 1 chuỗi liền nhau 
a = 'my name is %s' % ('tuong')
print(a)
a = 'tuong %s  yeah old' %('19')
print(a)
a = 'tuong %s %s yeah old' %('19','18') 
# lấy 2 giá trị nằm trong chuỗi và phải có 2 %s
print(a)
a = '%s %s'
result = a %('16','1')
print(result) # 2 %s print ra 2 giá trị nằm trong chuỗi
print(f'a\tb')# print ra a cách b một khoảng
# print ra giá trị trong chuỗi trong biến tuong  
tuong = "tuongclearlove"
result = f'{tuong} - lam'
print(result)
#khai báo
name = 'tuong'
address = 'dak lak'
phone = '0987876545'
result = f'Student:{name}\nAddress:{address}\nPhone:{phone}'
print(result)
# print ra các chuỗi nằm trong biến
a = '1:{one}, 2:{two}'.format(one=111,two=222)
# print ra 1:{one} là với one = 111 , 2:{two} là với two =222 
print(a)
a = 'tran{:^10}'.format('tuong')# cách để căn lề
#print ra tuong cách một đoạn
print(a)
a = 'tran{:*^50}'.format('tuong')
#print tran**********************tuong***********************
print(a)
a = 'tran{:*<50}'.format('tuong')
# print trantuong*********************************************
print(a)
a = 'tran{:*>50}'.format('tuong')
#print tran*********************************************tuong
print(a)

