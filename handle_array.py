
a =[1,2,3,4,5]
for b in a:
    print(b)

a = [1,2,3,4,5]
for b in a:
    print(a)

#nhap mang xuat mang lay ca chuoi va so 
arr_str = []
n=int(input("nhập n : "))
for idx in range(n):
    arr = format(input("nhập mảng : " ))
    arr_str.append(arr)
for idx in arr_str:
    print(idx)
for idx in arr_str:
    print(arr_str)


# nhap mang so nguyen
array = []
for i in range(n):
    array.append(int(input('Nhap so thu  %d : '%(i+1))))
print(array)
    

mang = []
for i in range(len(array)):
	number = array[i]
	if (number % 2) == 0:#lay so chan trong array
            mang.append(number)
            print(mang)





