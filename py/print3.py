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
print("Print Thành Công....")