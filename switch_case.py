key = [1,2,3]
def print1():
    print("hello 1")
def print2():
    print("hello 2")
def print3():
    print("hello 3")
nhap = input("nhap : ")
def swit(arg):
    switch = {
        "1":"print1()",
        "2":"print2()",
        "3":"print3()",
    }
    return switch.get(arg,"input phai la so nguyen 1, 2 , 3")
print(swit(nhap))





