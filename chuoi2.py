a = "tuong\n"
b = "yeuthao"
c = a in b
print(c)

a = "tuong"
b = "yeuthao"
c = a in b
print(c)

# [2] and [-2] lấy từng ký tự trong chuỗi bắt đầu từ 0 , 2 , 3 ....
# Nhưng phải nằm trong phạm vi chuỗi
# - là đi ngược lại
# chỉ chấp nhận số nguyên
a = "tuong"
b = a[-2]
c = a in b
print(b)

# hàm len lấy ra độ dài của chuỗi nằm trên trong
a = "tuong"
b = a[len(a)-1]
c = a in b
print(b)

#cắt chuỗi
a = "tuong"
b = a[1 : len(a)] # hoặc 1 : 1,2,3....
c = a in b
print(b)

a = "tuong"
b = a[None:None:2]
c = a in b
print(b)

a = "10" + "10"
b = 10 + 10
print(a)
print(b)

a = float("10.3") # hoặc str
print(a)







