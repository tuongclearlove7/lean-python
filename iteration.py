
itera = (x for x in range(5))
print(itera)
# có 5 phần tử print(next(itera)) 3 lần  ra 0,1,2
print(next(itera))
print(next(itera))
print(next(itera))


itera = (x for x in range(3))
print(itera)
#chọn ra 3 
print(sum(itera))


itera = (x for x in range(3))
print(itera)
#chọn ra 3 
print(sum(itera,2))
# có có 2 trong sum(itera,2) là + 2 cho 3 = 5

itera = (x for x in range(3))
print(itera)
# 
print(max([], default='tuong'))

itera = (x for x in range(3))
print(itera)
# lấy ra giá trị lớn nhất trong max()
print(max(16,1,2002))


itera = (x for x in range(3))
print(itera)
# lấy ra giá trị nhỏ nhất trong min()
print(min(16,1,2002))


itera = [16,1,2002]
print(itera)
#
print(min(1,2,3,4))

itera = [16,1,2002]
print(itera)
#sắp xếp số từ lớn tới bé trong itera[]
print(sorted(itera, reverse=True))


