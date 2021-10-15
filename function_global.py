def make_slogan():
    global name
    # global khởi trị biến name
    name = 'tuongclearlove'
make_slogan()
print(name) # in ra 
 

def make_global():
    global x # khởi tạo biến x
    x = 1
def local():
    x = 5
    print(' x in local', x)
# x in local được gán thêm giá trị của x vào sau
make_global()
print(x) # in ra biến 
local()
print(x)# in ra biến

print(locals())

print(globals())

