
# Kiểu dữ liệu Dict
# Các phương thức trong Dict


from collections import defaultdict


dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
dic1 = dic.copy()
# Phương thức copy 
# dic1 sao chép lại phần tử của dic
print(dic1)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
dic.clear()
# Phương thức clear 
# xóa  toàn bộ phần tử nằm trong dic
print(dic)


dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.get('Tuong')
# Phương thức get 
# lấy ra phần tử nằm sau 'Tuong' ==> Tran
print(value)
dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.get((16,1))
# tương tự khi lấy chữ
print(value)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.get('ádffdsasd','Tranthetuong')
print(value)


dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.items()
# Phương thức items 
# lấy ra [('Tuong', 'Tran'), ((16, 1), 2002)] nằm trong dic
print(value)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = list(dic.items())
# lấy ra phần tử ở vị trí 0 nằm trong dic là ('Tuong', 'Tran')
print(value[0])


dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.keys()
# lấy ra phần tử đầu nằm trong dic là (['Tuong' and (16, 1)])
print(value)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.values() # values giống với keys
# lấy ra phần tử đầu nằm trong dic là (['Tuong' and (16, 1)])
print(value)

dic = {'tuong':'tran',(16,1):2002}
print(dic)
value = dic.pop('tuong')
# phương thức pop
# lấy ra phần tử đầu tiên trong dic là còn tran và (16,1:2002)
print(value)
print(dic)

dic = {'tuong':'tran',(16,1):2002}
print(dic)
value = dic.popitem()
# Phương thức popitem
#lấy ra tất cả phần tử nằm trong dic
print(value)
print(dic)

dic = {'tuong':'tran',(16,1):2002}
print(dic)
value = dic.setdefault('tuong')
# lấy giá trị của tuong : là tran
print(value)
print(dic)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.setdefault('Tran')
print(value)
print(dic)

dic = {'Tuong':'Tran',(16,1):2002}
print(dic)
value = dic.setdefault('what the fuck ','Oh shit')
#   'what the fuck':'oh shit' lấy Oh shit  
print(value)
print(dic)


dic = {'name':'tuong',(1,16):2002}
print(dic)
value = dic.update(name='TranTheTuong')
# Phương thức update là thêm phần tử TranTheTuong vào name
# và giữ nguyên phần tử sau trong dic là (1, 16): 2002
print(value)
print(dic)














