#map(func, *iterable)
# Hàm map(func, iterable)

from typing import Iterable
func = lambda x, y: x + y
# ta có x + y nên ta cộng giá trị của 2 list vào
tuong1 = [1,2,3,4] # giá trị xác định của biến x
tuong2 = [2,3,4,5]# giá trị xác định của biến y
tuong = map(func, tuong1, tuong2)
print(list(tuong))# in ra tổng 2 list

# hàm filter
 #filter(function or None, iterable)

func = lambda x: x > 0 # điều kiện x > 0
tuong = [1,2,3,4,5,-2,-3] 
# lấy các phần tử trong list > 0 
print(list(filter(func, tuong)))

func = lambda x: x > 0 # điều kiện x > 0
tuong = [0,1,2,3,4,5,-2,-3] 
# lấy các phần tử trong list > 0 
print([x for x in tuong if x > 0])
# chạy tưonwg tự

  
func = lambda x: x > 0 # điều kiện x > 0
tuong = [0,1,2,3,4,5,-2,-3] 
# lấy các phần tử trong list > 0 
print(list(filter(func, tuong)))
print(list(filter (None, tuong)))# không lấy 0 
# vì điều kiện x > 0


print('______________________________________________________')

from functools import reduce
# Phải import hàm reduce
#reduce(function, sequence[, initial])
tuong_add = lambda x, y: x + y  # điều kiện x + y
tuong = [1,2,3,4,5] # nên ((((1+2)+3)+4)+5)
print(reduce(tuong_add, tuong))

tuong_add = lambda x, y: x * y  # điều kiện x * y
tuong = [1,2,3,4,5] # nên ((((1*2)*3)*4)*5)
print(reduce(tuong_add, tuong))

tuong_add = lambda x, y: x + y # điều kiện x + y
tuong = [1,2,3,4]# nên  1+2+3+4 = 10
print(reduce(tuong_add, tuong, 10)) # 10+10

tuong_multi = lambda x, y: x * y# điều kiện x * y
tuong = [1,2,3,4]# nên  1*2*3*4 = 24
print(reduce(tuong_multi, tuong, 10)) # 24*10















