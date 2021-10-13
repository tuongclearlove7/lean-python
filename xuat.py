# Hàm xuất print()

print('Tran','The','Tuong', sep='....')
# xuất ra giá trị trong ngoặc và thêm dấu chấm trong sep='....'
# vào giữa các chữ là Tran....The....Tuong

print('dong 1\n')
print('dong 2\n')
print('dong 3\n')
print('Tran','The','Tuong', end='....\n')
# \n là xuống dòng


from time import sleep
print('name')
sleep(3)
# sleep đợi 3 giây và print ra my name is tuong
# dùng sleep phải dòng thư viện time : from time import sleep
print('my name is tuong')

from time import sleep
print('name: ', end='', flush=True)
sleep(3)
# sleep đợi 3 giây và print ra my name is tuong
# dùng sleep phải dòng thư viện time : from time import sleep
print('my name is tuong')


from time import sleep
a1 = 'Hello!\n' 
a2 = 'My name is Tuong\nwell come to my home'
for c in a1 + a2: # c in a1 + a2 có tác dụng print 
# in ra từng chữ trong a1 và a2 cộng lại trong 0.2 giây
    print(c, end='', flush=True)
    sleep(0.2)
print()










