# Khởi tạo kiểu dữ liệu range

k = range(5)
print(type(k))

k = range(5)
print(k[0])
# chỉ in ra các số nằm trong khoảng từ 0 đến 4

print(list(range(2,5)))
#chạy từ 2 trở đi tới 4
print(list(range(4,1,-1)))
# bắt đầu từ 4 tới 2 là dừng nên chạy từ 4 đến 2
#công thức print(list(range(4,1 - step, -1)))
# Tương tự print(list(range(4,1,-1)))
print(list(range(2, -3, -1)))
#chạy từ 2 đến 0 và từ -1 đến 2
print(list(range(9999)))
#chạy từ 0 đến 9998
k = range(9999)
print(99916 in k)
# vì 99916 không nằm trong khoảng từ 0 đến 9998 nên False
k = range(9999)
print(9998 in k)
# vì 9998 nằm trong khoảng từ 0 đến 9998 nên True

list = [5, (1,2,3), {'tuong', 'Thao'}]
for i in range(len(list)):
    print(list[i])
    # in ra được các phần trong list


list = [1,2,3]
for value in list:
    value += 1
print(list)

list = [1,2,3]
for value in range(len(list)):
    list[value] += 1
print(list)
# += 1 nên thêm 1 nên chạy từ 2 đến 4
#phép toán dịch bit i = 0 ; c = i<<3






