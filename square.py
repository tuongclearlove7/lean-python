print('Bài Toán bình Phương')
input_value = int(input("nhap so can tinh binh phuong : "))
def square(list):
    sq_list = []# list rỗng
    for num in list:
        sq_list.append(num**2)#num**2 là các số được mũ 2 
    return sq_list
tuong = square([input_value])# 2^2 , 3^2 , 4^2
# các phần tử nằm trong square([]) được mũ 2 
for value in tuong:
    print(value) # in ra kết quả
















