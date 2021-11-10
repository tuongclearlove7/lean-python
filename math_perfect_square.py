# bài toán kiểm tra số chính phương
# Hãy viết chương trình kiểm tra số chính phương bằng Python
# qua bài này sẽ giúp bạn hiểu được số chính phương là gì
# cũng như thuật toán để kiểm tra số chính phương bằng Python.
#Để giải bài này thì bạn chỉ cần kiểm tra trong phạm vi từ 1 đến N 
# xem có số nào bình phương lên sẽ bằng N hay không.
#Nếu có thì N là số chính phương
#ngược lại thì không phải.
#với bài này ta không cần phải lặp từ 1 đến N mà chỉ cần lặp từ 1 đến (N/2 + 1)
#bởi vì thực tế những số lớn hơn (N/2 + 1) bình phương lên sẽ luôn luôn lớn hơn N.
# sử dụng vòng for
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

# sử dụng vòng while
num = int(input("Nhập vào số N lớn hơn 0: " ))
if(num==1):
    print("là số chính phương")
i = 2
while(i**2 <= num):
    if i**2 == num:
        print(num,"là số chính phương")
    i+=1
print(num,"không phải là số chính phương")


# gọi hàm và dùng vòng while
def find(n):
    if (n==1):
        return True
    i = int(n/2)
    while(i>0):
        if i**2 == n:
            return True
        i-=1
    return False
def main():
    n=int(input("Nhập vào số N lớn hơn 0: "))
    print(n," là số chính phương ") if(find(n)) else print(n,"không phải là số chính phương")
main()

