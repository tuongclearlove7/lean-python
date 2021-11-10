# Bài Liệt kê tất cả các ước số của số nguyên dương n 
# Trong bài này ta sẽ viết chương trình 
# Python liệt kê tất cả các ước 
# số của N với N được nhập vào từ bàn phím.
#yêu cầu : sử dụng vòng lặp for while
#Ví dụ nhập vào số N = 12 
# thì kết quả sẽ trả về các số mà 12 chia hết cho số đó
#B1. Yêu cầu nhập vào số N
#B2: Sử dụng vòng lặp để lặp từ 1 đến N 
#nếu số nào mà N chia hết thì đó chính là ước. 

# sử dụng vòng lặp for
n = int(input("Nhập vào số N cần tìm ước: "))
print("Các ước số của ", n, " là")
for i in range(1, n+1):
    if (n % i == 0):
        print(i, end=",")

#sử dụng vòng lặp while
i = 1
n = int(input("\nNhập vào số N cần tìm ước: "))
while (i <= n**(1/2)):
    if (n%i == 0):
        print("Các ước của số N vừa nhập là : ", i)
        print("Các ước của số N vừa nhập là : ", n//i)
    i+=1
# cách 2
i = 1
n = int(input("\nNhập vào số N cần tìm ước: "))
while i <= n:
    if n%i == 0:
        print(i, end=",")
    i += 1

#bài Tính tổng tất cả các ước số của số nguyên dương N bằng Python
#Hãy viết chương trình
# tính tổng tất cả các ước số của số nguyên dương N bằng Python 
#điều kiện là N được nhập từ bàn phím.
#yêu cầu : sử dụng vòng lặp while
#Bài này có cách giải tương tự như bài trước
#có điều thay vì liệt kê thì ta 
# khai báo thêm một biến tổng để lưu trữ tổng số trong vòng lặp.
# Sử dụng vòng lặp for
n = int(input("\nnhập số N cần tính tổng ước số : "))
value = 0
for i in range(1, n+1):
    if (n % i == 0):
        value += i
print("Tổng tất cả các ước số ", n, "là :", value)

#Tương tự sử dụng vòng lặp while
total = 0
i = 1
n = int(input("\nNhập số N cần tính tổng các ước số : "))
while i <= n:
    if(n%i == 0):
        total+=i
    i+=1
print("Tổng tất cả các ước số", n, "là :", total)
     

n = int(input("Nhập vào số N lớn hơn 0: " ))
check = False
for i in range(1, n + 1 ):
    if (i**2 == n):
        check = True
        break
if (check == True):
    print(n, " là số chính phương")
else:
    print(n, " không phải là số chính phương")
       

             




