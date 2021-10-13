# Cấu trúc vòng lặp While
# 

k = 5
while k > 0:
# vì k = 5 > 0 nên khi k -= 1 
# trừ cho đến khi ra con số lớn 0 
# nhưng vẫn nằm trong phạm vi từ 1 -> 5
    print('k = ', k)
    k -= 1

k = 'tuong'
a = 0
b = len(k)
while a < b:
# a = 0 thì xác định kí tự đầu tiên trong 
# chuỗi k = 'tuong' thì in ra T
# a += 1 chạy ra số kí tự trong chuỗi k = 'tuong'
    print(a, 'number text', k[a])
    a += 1

number_five = []
k_number = 1
while True: # vòng lặp  vô hạn
    if k_number % 2 == 0:
        number_five.append(k_number)# thêm giá trị của k_number
        if len(number_five) >= 5:
            break# kết thúc vòng lặp
    k_number += 1
#lấy ra các 5 số chẵn khi if k_number % 2 == 0:
# thì là số chẵn 
print(number_five)
print(k_number)

k_number = 0
while k_number < 10:
    k_number += 1
# vì k_number +=1 nhỏ hơn 10 nên khi if k_number % 2 == 0:
    if k_number % 2 == 0:
         continue
    print(k_number, 'is odd number')
# nên in ra các số lẻ nhỏ hơn 10    
print(k_number)  

k = 0 
while k < 3:
    print('value of k is', k)
    k += 1
else:
    print('k is not less than 3 anymore')
#k = 0 nên khi k+= 1 lấy ra 3 giá trị chạy từ 0 đến 2
# điều kiện while k < 3

k = 0 
while k < 3:
    print('value of k is', k)
    k += 1
    if k == 1:
        break
else:
    print('k is not less than 3 anymore')
# if k == 1:
        #break
# nên chỉ in ra một giá trị là 0










