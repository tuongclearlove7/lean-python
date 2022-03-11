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






















