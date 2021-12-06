# bài toán nhập vào số n xuất ra hệ bát phân và 
# hệ bát phân 

num = int(input("nhập số n : "))
print("số thập phân là : %d hệ bát phân là : %o "%(num,num))

# bài toán nhập vào số n xuất ra hệ bát phân và 
# hệ bát phân có sử lý ngoại lệ 
# ví dụ nhập vào kiểu dữ diệu float hoặc string thì sẽ k hợp lệ
n = input(" nhập n : ")
try:
    a = int(n)
    print("số thập phân là : %d hệ bát phân là : %o "%(a,a))
except:
    print("định dạng đầu vào k hợp lệ")

# cách 2
sum = input(" nhập n : ")
sim = False
try:
    sum = int(sum)
    sim =True
except:
    print("định dạng đầu vào k hợp lệ")
if sim:
    print("số thập phân là : %d hệ bát phân là : %o "%(sum,sum))

# làm tròn số thập phân đến số int(n)
#dùng hàm format
number_a = float(input(" nhập số cần làm tròn : "))
number_b = int(input("Bạn cần làm tròn đến mấy chữ số : "))
print("{0:.{1}f}".format(number_a,number_b))

#dùng hàm round
value = float(input(" nhập số cần làm tròn :  "))
value2 = int(input("Bạn cần làm tròn đến mấy chữ số : "))
lists = round(value, value2)
print(lists)

# làm tròn số có xử lý ngoại lệ
value_a = (input(" nhập số cần làm tròn :  "))
value_b = (input("Bạn cần làm tròn đến mấy chữ số : "))
isparsedone = False
try:
    number_a = float(value_a)
    number_b = int(value_b)
    isparsedone = True
except:
    print("định dạng đầu vào không hợp lệ ")
if isparsedone:
    print("{0:.{1}f}".format(number_a,number_b))













