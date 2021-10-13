
print({1,2,3} ^ {3,4})
set1 = {1,2,3}
set2 = {3,4}
set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3
set6 = set1 | set2
print(set3)
print(set4)
print(set5)
print(set6)
set6.pop()
# phương thức pop  lấy ra một phần tử đầu tiên trong {1,2,4} còn {2,4}
print(set6)




