
k = 3 
iter = (x for x in range(k))
c = 0
while c < k:
    print(next(iter))
    c += 1 
# k = 3 , c = 0 , c += 1 nên chạy từ 0 đến 2
#điều kiện c < k là 3

k = 3
iter = (x for x in range(k))
c = 0
while 1:
    try:
        print(next(iter))
    except StopIteration:
        break
# chạy tương tự từ 0 đến 2


a = (x for x in range(3))
for value in a:
    print('number', value)
# chạy tương tự 0 -> 2

a = {'tuong': 'tran', 'the': 16}
print(a.items())


a = {'tuong': 'tran', 'the': 16}
b = list(a.items())
print(b)
print(b[0])
print(b[1])

a = {'tuong': 'tran', 'the': 16}
for key, value in a.items():
    print('tuple', value)

a = 'tuong'
for b in a:
    if b == '':
        break
    else:
        print(b)
# xuất ra kết tự trong chuỗi 
a = 'tuong'
for b in a:
    if b == '':
       continue
    else:
        print(b)
# tương tự break

for k in (1,2,3):
    print(k)
else:
        print('done!')


for k in (1,2,3):
    print(k)
    if k % 2 == 0:
        break
else:
    print('done!')
# if k % 2 == 0: nên chỉ lấy 1 và số chẵn là 2


for k in (1,2,3):
    if k % 2 == 0:
        continue
    print(k)
else:
    print('Done!')
# in ra số 1 và số lẻ là 3
