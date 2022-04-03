# hàm đệ quy
def giaithua(n):
    if n == 1: 
       return 1 
    else: 
        return (n * giaithua(n-1))
num = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", num, "là", giaithua(num)) 














