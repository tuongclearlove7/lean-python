tup = (1,2,3,"tuong",4,5,6)
print(tup)

tup = (i for i in range(10) if i % 2 == 0)
a = tuple(tup)
print(a)

tup = (1,2,3)
tup += (2,4,6)
print(tup)


tup = (1,2,3)
a = 3 in tup
# tup có phần tử = 1,2,3 
# .a= phần tử bất kì trong tup thì True 
# không có thì False 
print(a)

tup = (1,2,3)
a = tup[1]
# a = tup chứa list là 1 
# thì lấy phần tử trong tup là số đứng thứ 2
print(a)

tup = (1,2,3)
a = len(tup)
# len(tup) trong tup có 3 phần tử nên ra 3
print(a)

tup = (1,2,3,4)
a = tup[-1]
# tương tự như len(tup)
print(a)

tup = (1,2,3,4)
a = tup[:-1]
# :-1 thì lấy 3 phần tử đầu
print(a)


tup = (1,2,3,4)
a = tup[::-1]
# ::-1 đảo ngược phần tử lại in 4,3,2,1
print(a)

tup = (1,1,2,3,4)
a = tup.count(1)
# phương thức count nếu trong tup chứa 1,2,3,4
# count(1) thì ra 1 
# nếu trong tup có 2 số 1 thì count(1) ra 2
print(a)

tup = (1,2,1,3,4)
a = tup.index(3)
# phương thức index lấy ra phần tử trong tup

# 
print(a)











