#bài Tính tổng S(n) = 1 + 2 + 3 + … + n.
#Tạo một biến sum để lưu trữ tổng của dãy số đó
#Sử dụng vòng lặp để lặp qua từ 1 đến n
# giải
# sử dụng vòng lặp for
total = 0
n = 1
print("Tính tổng S(n) = 1 + 2 + 3 + … + n")
 # Nhập dữ liệu
print("hãy nhập vào số n = ")
n = int(input())
 # Tính tổng
for i in range(1, n + 1):
    total += i
print ("Tổng là = ", total)

# sử dụng vòng lặp while
total = 0
n = 1
i = 1
print("Tính tổng S(n) = 1 + 2 + 3 + … + n")
print("hãy nhập vào số n = ")
n = int(input())
while i <= n :
    total += i
    i += 1
print ("Tổng là = ", total)

#bài Tính S(n) = 1^2 + 2^2 + … + n^2
# giải
#Trong Python có toán tử tính số mũ nên ta có thể áp dụng trong bài này.
#Ví dụ 2^3 thì sẽ là 2 ** 3.
#Ta sẽ sử dụng vòng lặp for trong Python 
# để lặp qua các phần tử từ 1 đến n.
#Sử dụng range(1, n+1) để tạo ra một dãy số từ 1 đến n.
print("Tính tổng n mũ S(n) = 1^2 + 2^2 + … + n^2")
total = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1) :
    total += i ** 2
print("Tổng số là = ", total)

# sử dụng vòng lặp while
total = 0
n = 1
i = 1
print("Tính tổng n mũ S(n) = 1 + 2 + 3 + … + n")
print("hãy nhập vào số n = ")
n = int(input())
while i <= n :
    total += i ** 2
    i += 1
print ("Tổng là = ", total)

#bài Tính tổng S(n) = 1 + ½ + 1/3 + … + 1/n
#Với bài này thì ta phải lưu trữ dữ liệu kiểu float, 
# vì phép chia có thể trả về giá trị số lẻ có phần dư.
#Tương tự, sử dụng vòng lặp để lặp qua dãy số từ 1 đến n, 
#tức khoảng range sẽ được tính là range(1, n+1).
#Toán tử chia 
print("Tính tổng S(n) = 1 + ½ + 1/3 + … + 1/n")
total = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1) :
    total += 1 / i
print("Tổng số là: ", total)

# sử dụng vòng lặp while
total = 0
n = 1
i = 1
n = int(input("hãy nhập vào số n = "))
while i <=n:
    total += 1 / i
    i += 1
print("tổng là = ", total)

#bài Tính tổng S(n) = 1/3 + 1/5 + … + 1/(2n + 1)
#Như vậy, công thức chung cho mỗi phần tử đó là 1/(2n + 1).
#Để làm bài tập Python cơ bản này thì ta sử dụng vòng lặp for,
# kết hợp với công thức 1/(2n + 1) sẽ đưa ra được thuật toán như sau.
# sử dụng vòng lặp for
print("Tính tổng S(n) = 1/3 + 1/5 + … + 1/(2n + 1)")
total = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1):
    total += 1 / (2 * i + 1)
print("Tổng số là = ", total)

# tương tự sử dụng vòng lặp while
total = 0
n = 1
i = 1
print("hãy nhập vào số n = ")
n = int(input())
while i <=n:
    total += 1 / (2 * i + 1)
    i += 1
print("tổng là = ", total)


