print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = {'tran','the','tuong'}
set4 = set1 & set2 
set5 = set1 | set2
set6 = set1 - set2 | set3 
# set3 = set1 & set2 lấy ra phần tử khác 3 trong  set1 và set2 là {1,2,4}
#set4 = set1 | set2 lấy tất cả phần tử trong set 1 và set 2 là {1,2,3,4}
#set5 = set4 - set3 tương tự set3 = set1 & set2
print(set4)
print(set5)
print(set6)
set6.pop()
print(set6)

