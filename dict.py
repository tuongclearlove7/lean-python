# kiểu dữ liệu Dict

dic = {'tuong' : 19 }
print(dic)
print(type(dic))

dic = {key: value for key, value in [('tuong','tran'),('the', 16)]}
print(dic)
print(type(dic))

dic = ()
print(dic)
print(type(dic))


dics = [('tuong','tran'),('the', 16)]
dic = dict(dics)
print(dic)
print(type(dic))


name = 'tuong'
dic = dict(name='tuong', member=16)
print(dic)
print(type(dic))


name = ('tuong', 'tran', 16, True)
dic = dict.fromkeys(name, 'tuong tran')
print(dic)
print(type(dic))

name = ('tuong', 'tran', 16, True)
dic = dict.fromkeys(name, 'tuong tran')
print(dic)
print(dic['tran'])
# trong name có các phần ('tuong', 'tran', 16, True) 
# khi print (dic[phần tử bất kỳ nằm trong name]) thì chạy 
# còn khi print(dic[phần tử không có trong name ]) thì không chạy

name = ('Tuong', 'Tran', 16, True)
dic = dict.fromkeys(name, 'Tuong Tran')
dic['Tran'] = 'Tran the tuong'
print(dic['Tran'])

dic = dict(name='Tuong', Fullname='Tran The Tuong')
print(dic)
#__________________________________________________________________

dic = dict(name='name : ', name1='The', Fullname='Tran The Tuong')
print(dic)
dic['name'] = dic['name'] + 'tuong'
print(dic)


dic = dict( porn=16, name1='Tuong', Fullname='Tran The Tuong')
dic['day of birth'] = dic['porn'] + 0
# trong  dict( porn=16, name1='Tuong', Fullname='Tran The Tuong')
# với porn, name1, fullname có các chuỗi và số
# trong dic chứa các phần tử + 0 là 
# porn = 16 được xác định trong dic['porn'] + 0 = 16
# ==> 'day of birth': 16
# lưu ý nếu porn='chuỗi' thì dic['day of birth'] = dic['porn'] + 'phải công cho chuỗi'
# và porn = số thì dic['day of birth'] = dic['porn'] + cộng cho số
print(dic)


dic = dict(name='Tran ', name1='The', name2='Tuong')
dic['Full name'] = dic['name'] + 'The Tuong'
print(dic)


dic = dict(tuong='day of birth :')
dic['tuong'] = dic['tuong'] + ' 16/1/2002'
print(dic)
















