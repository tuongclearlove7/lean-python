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

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)