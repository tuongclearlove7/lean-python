g = ['>>'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('hello', 'my', 'friend'), ('ok', 'hi', 'bro')]]
print(g)
# Gán dấu >> vào phần tử đầu tiên và cộng phần tử thứ 2 và 3
# và viết hoa chữ cái đầu phần tử 1 phần tử thứ 2

k = []
for a, b, c in [('hello', 'my', 'friend'), ('ok', 'hi', 'bro')]:
    a = a.capitalize()
    b = b.upper()
    c = c.lower()
    k.append('>>'.join((a, b + c)))
print(k)
# tương tự gán dấu >> vào  phần tử đầu tiên và cộng phần tử thứ 2 và 3 
# và viết hoa chữ cái đầu phần tử 1 phần tử thứ 2

k = {key:value + 1 for key, value in (('tran', 69), ('the', 50), ('tuong', 14), ('clearlove', 93)) if value % 2 != 0}
print(k)
# vì  value + 1  và if value % 2 != 0 
# nên các phần tử có số lẻ sẽ được cộng 1
myclass = ['tran', 'the', 'tuong']
for student in myclass:
    print(student)

myclass = ['tran', 'the', 'tuong']
tuong = enumerate(myclass)
print(tuong)

myclass = ['tran', 'the', 'tuong']
tuong = enumerate(myclass)
print(list(tuong))
# xuất ra số ký tự kèm theo phần tử trong myclass

myclass = ['tran', 'the', 'tuong']
for index, student in enumerate(myclass):
    print(index, '==', student)
# xuất ra số thứ tự và gán == vào trước phần tử của myclass

myclass = ['tran', 'the', 'tuong']
for index, student in enumerate(myclass,1):
    print(index, '==', student)
# xuất ra ra thứ tự từ 1  và gán == vào trước phần tử của myclass






