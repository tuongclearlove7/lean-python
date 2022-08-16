name = ('Tran','Tuong', 16, True)
dic = dict.fromkeys(name, None)
print(dic)

dic['Tran'] = {"firstname"}
dic['Tuong'] = {'lastname'}
dic[16] = {"age"}
dic[True] = {False}

for i in dic["Tran"],dic['Tuong'],dic[16],dic[True]:
    print(i)
print(dic)

for i in dic['Tran']:
    print(i)
for i in dic['Tuong']:
    print(i)
for i in dic[16]:
    print(i)
for i in dic[True]:
    print(i)

print("\n----------------------------------------------------")

mydic2 = {}
mydic2['key_name'] = 'value_name'
print(mydic2)

dic = dict(name='tran : ', middle_name='The', Fullname='Tran The Tuong',age = 20)
print(dic)
dic['name'] = 'tuong'
for i in dic['name']:
    print(i)
print(dic)

dic = dict( porn=4122002, nickname='TuongClearlove7', Fullname='Tran The Tuong')
dic['year of birth'] = dic['porn'] -1
for i in dic['nickname']:
    print(i)

print(dic)


class People:
    '''handle dictionary in class object'''
    kind = {'luckynum':str(7)}
    def __init__(self, name):
        self.name = name   
        print(name)

d = People({})
e = People([])
print(d.kind['luckynum'])
for i in d.kind:
    print("key : "+i)
for i in d.kind['luckynum']:
    print("value : "+i)

def App_types():
    """build-in function types"""
    print({})
    print([])
    print(dict(dictionary='dic'))
    print(object)
    print(App_types)
    print("string")
    print(None)
    print(float(1))
    print(int(1))
    print('')
    print(__name__)
    print(True,False)
App_types()

mylist = [People.__init__]
print("list array : "+str(mylist)+"\n")
myset = {People.__init__}
print("set : "+str(myset)+"\n")

mydict = {'application':[App_types],'id':1,'porn':2003,
          'address':'DaNang city','developer':'Clearlove7',
          'family':['father','mother','sister','me'],
          'num':4}
for key in mydict:
    print('key : '+key)
print(mydict)

for i in mydict['application']:
    print("function app : "+str(i))
    pass

mydict['application'] = [People]
print(mydict)
for i in mydict['application']:
    print("class object app : "+str(i))

mydict['application'] = ['fake app']
print(mydict)
for i in mydict['application']:
    print("string app : "+i)
    pass

mydict['application'] = [499]
print(mydict)
for i in mydict['application']:
    print("number app : "+str(i))
    pass







