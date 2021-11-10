#Đề bài: Viết chương trình sử dụng Python tính các tổng sau:
#Yêu cầu kiến thức:
#Phân tích thiết kết giải thuật
#Áp dụng vòng lặp for trong Python
#bài 1. s = 12 + 22 + 32 + .. + n2
n = int(input('Nhập vào số lượng n = '))
def total1(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s
print('tổng bình phương n của câu 1 là = ', total1(n))

#bài 2. s = 1/2 + 2/3 + 3/4 + … + n/(n + 1)
n = int(input('Nhập vào số lượng n = '))
def total2(n):
    S = 0.0
    for i in range(1, n + 1):
        S = S + float(float(i) / (i + 1))
    return S
print('Tổng bài 2 là = ', total2(n))

