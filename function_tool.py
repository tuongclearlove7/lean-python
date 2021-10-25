# Hàm map(func, iterable)
def map(func, iterable):
    for x in iterable:
        yield func(x)


def inc(x): return x + 1
# return x + 1 
tuong = [1,2,3,4]
#nên các phần tử trong list được cộng thêm 1
print(list(map(inc, tuong)))

tuong = [1,2,3,5]
print(list(map(lambda x: x+1, tuong)))
# chạy tương tự

inc = lambda x: x + 1
tuong = [2,3,4,5]
print([inc(x) for x in tuong])
# chạy tương tự



