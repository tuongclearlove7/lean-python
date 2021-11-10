# bài : Viết chương trình tìm tất cả các số chia hết cho 7 
#nhưng không phải bội số của 5
#nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
#Các số thu được sẽ được in thành chuỗi trên một dòng
# cách nhau bằng dấu phẩy.
# Sử dụng range(#begin, #end)
# sử dụng vòng lặp for
j = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))

# bài : Viết chương trình tìm tất cả các số chia hết cho 7 
#nhưng không phải bội số của 5
# sử dụng vòng lặp while
i = 2000
while (i <= 3200):
    if i%7==0 and i%5!=0:
        print(i)
    i+=1

#Viết một chương trình có thể tính giai thừa 
#của một số cho trước. Kết quả được in 
#thành chuỗi trên một dòng
#phân tách bởi dấu phẩy.
#Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
#Trong trường hợp dữ liệu đầu vào được cung cấp
#bạn hãy chọn cách để người dùng nhập số vào.
# giai thừa là 1! , 2!, 3!, 4! ...
a = int(input("Nhập số cần tính giai thừa : "))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print(fact(a))

#hãy viết chương trình nhập vào số thực n tạo ra một dictionary chứa 
#(i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) 
# yêu cầu sử dụng vòng lặp while và for
#sau đó in ra dictionary này. 
#Ví dụ: Giả sử số n là 4 thì đầu ra sẽ là : {1: 1, 2: 4}
n = int(input("Nhập vào một số n : "))
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)

n = int(input("Nhập vào một số n : "))
d = dict()
i = 1
while (1,n+1):
    d[a] = a*i
    cout<<i>>;
i++













