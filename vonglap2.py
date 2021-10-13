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