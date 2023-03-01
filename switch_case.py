def die():
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

    # from enum import Enum, unique, Flag
    # class day(Enum) :
    #     monday=2
    #     tuesday=3
    #     wednesday=4
    #     thursday=5
    #     friday=6
    #     saturday=7
    #     sunday=8
    # try:
    #     myday = day(int(input('day : ')))
    #     print(myday)
    # except:
    #     print('phai nhap tu 2 den 8')

def defult(self):
    print(self)
def die(day):
    Case = [None,None,2,3,4,5,6,7,8,{lambda:0}]
    switch = {
                Case[2]: lambda :'monday',
                Case[3]: lambda :'tuesday',
                Case[4]: lambda :'wednesday',
                Case[5]: lambda :'thursday',
                Case[6]: lambda :'friday', 
                Case[7]: lambda :'saturday',
                Case[8]: lambda :'sunday'
    }[day]()
    return 'today is : '+switch
try:
    print(die(int(input("day : "))))
except:
    print('please input from monday to sunday day > 1 day < 8')
finally:
    defult('Successfully')


while True:
    try:
        Case = [None,None,2,3,4,5,6,7,8,{lambda:0}]
        Key = int(input("nhap day : "))

        switch = {
                    Case[2]: {'monday'},
                    Case[3]: ['tuesday'],
                    Case[4]: ['wednesday'],
                    Case[5]: ['thursday'],
                    Case[6]: ['friday'], 
                    Case[7]: ['saturday'],
                    Case[8]: ['sunday']
    }
        for i in switch[Key]:
            print(i)
        break
    except:
        print('please input from monday to sunday day > 1 day < 8')
    finally:
        defult('Successfully')




