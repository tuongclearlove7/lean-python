# set không quan tâm đến vị trí của phần tử

set_1 = {69,96}
print(set_1)
print(type(set_1))

set_2 = {(69, 'tuong') , (1,2,3)}
print(set_2)

#set_2 = {(1,2,['tuong'])}
# không bỏ list vào được
#print(set_2)
set_2 = {'tuong', 'tran', 69 }
print(set_2)

set_2 ={1,1,1}
# chỉ suất ra 1 số 1 
print(set_2)


set_2 = {}
print(set_2)
print(type(set_2))


set_2 = {value for value in range(3)}
print(set_2)
print(type(set_2))


set_2 = set((1,2,3))
print(set_2)
print(type(set_2))


set_2 = set('tuong')
# phân tách ra thành  't', 'o', 'g', 'u', 'n'
# set không quan tâm đến vị trí của các phần tử
print(set_2)
print(type(set_2))


set_2 = set((1,1,2,2,3,3,4,4))
# chỉ lấy mỗi phần tử không lấy giống nhau
print(set_2)
print(type(set_2))


print(1 in {1,2,3})
# 1 tồn tại trong set nên true 
print(1 in {1,2,3})
# 1 tồn tại trong set nên true 
print(1,2 in {1,2,3})
#  1  , 2 . 1 có 2 nên True
print(4 in {1,2,3})
# không có 4 trong set nên false
print({1,2,3} - {2,3})
# set {1,2,3} - {2,3} trừ đi 2 phần tử là 2,3 nên trong set còn{1}
print({2,3} - {2,3,4,5})
# chỉ lấy 2 set trong tồn tại trong set 1 

print({1,2,3,4} & {4,5})
# {1,2,3,4} & {4,5} lấy ra tất cả phần tử trong 2 set
print({1,2,3} | {4,5})
#{1,2,3} | {4,5} lấy hết tất cả phần tử trong set của 2 thằng

print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3
# set3 = set1 & set2 lấy ra phần tử khác 3 trong  set1 và set2 là {1,2,4}
#set4 = set1 | set2 lấy tất cả phần tử trong set 1 và set 2 là {1,2,3,4}
#set5 = set4 - set3 tương tự set3 = set1 & set2
print(set3)
print(set4)
print(set5)

print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)
set5.clear()
# phương thức clear in ra một set rỗng
print(set5)


print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)
set5.pop()
# phương thức pop  lấy ra một phần tử đầu tiên trong {1,2,4} còn {2,4}
print(set5)

 
print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)
set5.remove(4)
# phương thức remove lấy đi phần tử 2 trong set5 = set4 - set3 
# còn {1,4}
# lưu ý trong remove phải có phần tử là {1,2,4} trong set5 = set4 - set3 
print(set5)


set1 = {1,2,3,4}
set1.discard(0)
# phương thức discard(4) lấy đi 1 phần tử trong set1 còn {1,2,3}
# nếu discard(không chứa phần tử nằm trong set1) thì vẫn giữ nguyên
# là {1,2,3,4} 
print(set1)


set1 = {1,2,3,4}
set2 = set1.copy()
# pHƯƠNG THỨC COPPY set 2 sao chép phần tử trong set1
print(set2)


set1 = {1,2,3,4}
set1.add(10)
#PHƯƠNG THỨC add(10) thêm phần tử chứa trong add vào set 1 ra {1,2,3,4,5}
print(set1)



set1 = {1,2,3,4}
print(id(set1))
set1.add(5)
print(id(set1))



set1 = {1,2,'tuong',3,4}
print(set1)
set2 = set1
print(set1)
set2.clear()
# in ra set 1 và set 2 phương thức set2.clear() in ra một set rỗng set()
print(set1)

set1 = {'16','1','2002'}
set2 = {'tuong','tran','the'}
set1.update(set2)
# Phương thức update lấy phần tử set2 gộp lại với set1
print(set1)

set1 = {(2,3,4)}
set2 = {'5','6'}
result = set1.union(set2)
# Phương thức union sắp xếp các phần tử số từ bé đến lớn
# lưu ý còn phần tử chứa chuỗi  và tuple() thì sẽ bị cháo đổi vị trí 
print(result)
















