
class People:
    '''handle dictionary in class object'''
    kind = {'luckynum':str(7)}
    def __init__(self, name):
        self.name = name   
        print(name)
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
        print(trick)


d = People('tuong')
e = People('thao')
f = People("mai")
d.add_trick('roll over')
f.add_trick([])
e.add_trick('play dead')
for i in d.tricks,e.tricks:
    print(i)
for i in d.kind:
    print("key : "+i)
for i in d.kind['luckynum']:
    print("value : "+i)

class Warehouse:
        purpose = 'storage'
        region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


        

