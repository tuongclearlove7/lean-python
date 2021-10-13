
# giới hạn bởi các cặp ngoặc vuông
# các phần tử của list cách nhau bởi dấu phẩy ,
#list có khả nặng chứa mọi giá trị  đối tượng của python
# và bao gồm chính nó
# list rỗng
from abc import abstractproperty


a = [tuong for tuong in range(30)]
# tạo ra một list từ 0 đến 30 chỉ lấy tới 29
#print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
#21, 22, 23, 24, 25, 26, 27, 28, 29]
print(a)


a = [[n*5,n*2*5] for n in range(1,4)]
# tạo ra một list trong range
print(a)

a = list('tuong')
# print ra từng ký tự trong chuỗi  ['t', 'u', 'o', 'n', 'g']
print(a)

a  = [1,2]
a = a + ['one','two']
print(a)

a  = [1,2]
a *=2
print(a)

a  = [1,2,]
b = 'tuong' in a
# tìm ra chữ trong a nếu k có sẽ ra false và có sẽ ra true
print(b)

a  = [1,2,'a','b','c',[3,4]]
b = a[0]
# từ a[0] xuất ra giá trị thứ tự là 1
print(b)

a  = [1,2,'a','b','c',[3,4]]
b = a[5][0]
# từ a[5][0] xuất ra giá trị thứ tự là 3
print(b)

a  = [1,2,'a','b','c',[3,4]]
b = a[:3]
# từ a[:3] xuất ra giá trị thứ tự là [1, 2, 'a']
print(b)

a  = [1,2,'a','b','c',[3,4]]
b = a[::]
# từ a[::] xuất ra toàn bộ
print(b)


a  = [1,2,'a','b','c',[3,4]]
b = a[1] = 'tuong'
# từ a[1] = 'tuong'  xuất ra [1, 'tuong', 'a', 'b', 'c', [3, 4]]
print(b)
print(a)


a = [[1,2,3],[4,5,6],[7,8,9]]
# ma trận
print(a[0][-1])
print(a[1][1])
print(a[2][0])

a = [1,2,3]
b = list(a)
print(b)
print(a)
b[0] = 'tuong'
print(b)
print(a)
# trong a là 1,2,3 
# b[0] = 'tuong'
# thì sẽ tuong sẽ gán vào số 1 trong a

a = [[1,2,3],[4,5,6]]
b = a[:]
print(a)
print(b)
b[0][0] = 'tuong'
print(a)
print(b)

a = [[1,2,3],[4,5,6]]
b = list(a)
print(a)
print(b)
b[0] = 'tuong'
print(a)
print(b)


