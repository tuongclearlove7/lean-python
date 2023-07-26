print()
print()
from time import sleep

a1 = '{:^120}'.format('hello mọi người tôi là tường\n')
a2 = '{:^10}'.format('$$$$$$$$$$$$$$$$$$$$$$$$\n')

for c in a1 + a2:
    print(c, end='', flush=True)
    sleep(0.02) #Chỉnh sửa thông số, tốc độ load của note.
print()

input('>> Nhập họ và tên của người bạn :\n')
input('>> Nhập sai họ tên của bạn rồi, NHẬP LẠI:\n')
print()

from time import sleep
a1 = '{:^120}'.format('Tuyệt vời thế mà cũng nhớ được\n')
print()
for c in a1:
    print(c, end='', flush=True)
    sleep(0.03) #tốc độ của từ "Tuyệt Vời - Khó Thế Mà Cũng Nhớ Ra Được"
print()

import time as t
chờ = range(10,110, +10)
for i in range(len(chờ)):
    print("                       Loading...: ",chờ[i], end = "")
    print("%")
    t.sleep(0.05) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("""________________________________________________________________________________________________________________________                         
                                           Print Thành Công....                        
_________________________________________________________________________________________________________________""")
with open("val.txt", "r") as fh: #"idol.txt" là file chứa text-image đã tạo.
    for line in fh:
        print(line.strip())
        t.sleep(0.09) #Chỉnh 