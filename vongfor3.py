for k in (1,2,3):
    if k % 2 == 0:
        continue
    print(k)
else:
    print('Done!')
# in ra số 1 và số lẻ là 3

num = 5
for i in range(num):
#có một câu lệnh for...in sử dụng hàm range 
#Vòng lặp for có thể được sử dụng để duyệt các loại dữ liệu khác nhau 
# như : list, string,…
    print(i)
#để lặp lại chạy từ 0 cho đến 98

name = ('tuong')
for Text in name:
    print('text :', Text)
#Lặp từ trong chuỗi

for Text in 'Clearlove7':
    print('text :', Text)
#Tương tự Lặp chuỗi

for Text in 777,'Clearlove7':
    print('text :', Text)

name = (161,'tuong')
for Text in name:
    print('text :', Text)

list = ['Thao']
for love in list:
# ta có biến love in + list = ['Thao']  
    print('I Love You', love)
# Lặp list

list = ['Ho Phuong Thao',3000]
for love in list:
# ta có biến love in + list = [1,2,3]  
    print('I Love You', love)


#..................................................................

# Bài toán : Tính tổng tất cả các số trong danh sách A
A = [1, 3, 5, 9, 11, 2, 6, 8, 10]# Danh sách A
# Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0
tong = 0
# Vòng lặp for, a là biến lặp
for a in A:
     tong = tong+a
# Đầu ra: Tổng các số là 55
print("Tổng các số là : ", tong)


# Bài toán : tính tích tất cả các số trong biến A
A = [1,2,4,5,6] # danh sách A 
tich = 1
for b in A:
    tich = tich * b # 1*1*2*4*5*6
print('tích các số nhân lại với nhau là : ', tich)
# nhìn Tương tự các bài toán trên hãy lập 1 bài toán tính Thương


# Bài toán : tính thương tất cả các số trong biến A
A = [10,20,30]
thuong = 2
for b in A:
    thuong = thuong / b # 2/10+20+30
print('Thương là : ', thuong)
print("""
_____ ___       ___  _______         ___ 
| __  | |___ ___| |_ |_   _|___ ___  | | 
| __ -| | .'|  _| '_|  | | | . | . | | |
|_____|_|__,|___|_,_|  |_| |___|___| |_|
                                        """)
