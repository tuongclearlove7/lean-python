a = [1,2,3,4,7,8,9,9]
b = a.count(9)
print(b)


a = [1,2,3,4,7,8,9]
b = a.copy()
# phương thức copy là tạo ra một bản sao
print(b)

a = [1,2,3,4,7,8,9]
b = a.copy()
b[0] = 'tuong'
# phương thức copy là tạo ra một bản sao
print(b)
print(a)


a = [1,2,3,4,7,8,9]
b = a.clear()
# phương thức clear làm rỗng trong list
print(a)
print(b)

thao_yeu_tuong = [50]
tuong_yeu_thao = thao_yeu_tuong
print(thao_yeu_tuong)
print(tuong_yeu_thao)



tuong_yeu_thao =[]

print(thao_yeu_tuong)
print(tuong_yeu_thao)

a = [1,2,3]
print(a)
a.append([4,5])
print(a)

a = [1,2,3]
print(a)
a.extend([4,5])
print(a)


a = [1,2,3]
print(a)
a.insert(4,9)
#phương thức insert đưa 9 vào vị trí 0
# nếu -1 thì vị trí ngược lại 
print(a)


a = [1,2,3]
print(a)
b = a.pop()
# phương thức pop lấy ra phần tử có vị trí 1 trong list vd : b = a.pop(1)
# nếu không lấy phần tử nào trong pop thì mặc định lấy số cuối trong list
print(a)
print(b)


a = [1,1,2,3]
print(a)
a.remove(1)
a.remove(1)
# phương thức remove sẽ bỏ đi phần tử đầu tiên nếu  remove(1)
print(a)


a = [1,1,2,3]
print(a)
a.reverse()
# phương thức reverse đảo ngược phần tử trong list lại
print(a)

a = [0,1,2,3]
print(a)
a.sort(reverse=False)
# phương thức soft 
print(a)




