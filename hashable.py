#hasable or unhasable
# dùng hàm id
a = id("tuong")
print(a)

b = 'tuong'
a = id(b)
print(a)

b = 'tuong'
a = id(b)
print(a)
print(id('tuong'))


b = 'kteam'
a = id(b)
c = id(5)
print(c)

b = 'tuong'
a = id(b)
c = id((1,2,3),)
print(c)

a = 69
print(a)
print(a + 1)
# a + 1 thì add
print(a.__add__(1))


a = 69
print(a)
print(a - 1)
# a - 1 thì sub  
print(a.__sub__(1))

a = 69
print(a)
print(a * 2)
# a * 2 thì mul 69 * 2 
print(a.__mul__(2))


a = 69
print(a)
print(1 + a)
# tương tự add
print(a.__radd__(1))

a = 69
print(a)
print(- a)
# neg in ra -69
print(a.__neg__())


a_1 = 'tuong'

a_2 = 'tran'
print(id(a_1))
print(id(a_2))


a_1 ='tuong'
a_2 ='tran'

a_1 = a_1 + 'tuong'
a_2+='tuong'
print(id(a_1))
print(id(a_2))

a_1 = [1,2]
a_2 = [3,4]
a_1 = a_1 + [0]
a_2+=[0]
print(id(a_1))
print(id(a_2))

a_1 = [1,2]
a_1 = a_1 + [3,4]
# a_1 = [1,2] + [3,4] in ra [1,2,3,4]
print(a_1)

a_1 = [1,2]
print(id(a_1))


a_1 = a_1.__add__([3,4])
print(id(a_1))



a_1 = [1,2]
a_1.append(3)
# thêm 3 vào list
print(a_1)

a_1 = (1,2)
a_1 +=(3,)
# thêm tuple +=(3,) in ra (1, 2, 3)
print(a_1)




#0x11114|tuong
#0x00004|6969
#.....|.....
#.....|.....
#.....|.....
#.....|.....