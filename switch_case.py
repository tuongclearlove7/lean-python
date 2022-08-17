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
        "1":print1(),
        "2":print2(),
        "3":print3(),
    }
    return switch.get(arg,"input phai la so nguyen 1, 2 , 3")
print(swit(nhap))

def die():
    day = int(input("day : "))
    try:
        handle_key = {2: lambda :'monday',
                    3: lambda :'tuesday',
                    4: lambda :'wednesday',
                    5: lambda :'thursday',
                    6: lambda :'friday', 
                    7: lambda :'saturday',
                    8: lambda :'sunday'}[day]()
        print(handle_key)
    except:
        print('phai nhap tu 2 den 8')

from enum import Enum, unique, Flag
class day(Enum) :
    monday=2
    tuesday=3
    wednesday=4
    thursday=5
    friday=6
    saturday=7
    sunday=8
try:
    myday = day(int(input('day : ')))
    print(myday)
except:
    print('phai nhap tu 2 den 8')





