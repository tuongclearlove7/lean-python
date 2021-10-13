def hashobject1():
    a = (1,2,3)
    print(id(a))
    a = a + (4,)
    print(id(a))

def hashobject2():
    a = (1,2,3)
    print(id(a))
    a += (4,)
    print(id(a))

def unhashobject3():
    a = [1,2,3]
    print(id(a))
    a += [4]
    print(id(a))

def unhashobject4():
    a = [1,2,3]
    print(id(a))
    a = a + [4]
    print(id(a))

def unhashobject5():
    a = [1,2,3]
    print(id(a))
    a.__add__([4])
    print(id(a))

#Ví dụ ngoại lệ
def ngoaile1():
    a = [1,2,3]
    b = a
    a = a + [4]
    print(a)
    print(b)

def ngoaile2():
    a = [1,2,3]
    b = a
    a+= [4]
    print(a)
    print(b)
