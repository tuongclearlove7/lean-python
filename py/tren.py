print()
print()
from time import sleep

note_1 = "** Hello! My name is Vangggg\n"
note_2 = "** Hãy cùng theo dõi 1 System mình vừa làm trong lúc rảnh rỗi nhé.\n*****\n****\n***\n**\n*\n"

for c in note_1 + note_2:
    print(c, end='', flush=True)
    sleep(0.05) #Chỉnh sửa thông số, tốc độ load của note.
print()

input('>> Nhập họ và tên của người yêu bạn:\n')
input('>> Nhập sai họ tên của người yêu rồi, NHẬP LẠI:\n')
print()

from time import sleep
note_1 = "*                       Tuyệt Vời - Khó Thế Mà Cũng Nhớ Ra Được"
print()
for c in note_1:
    print(c, end='', flush=True)
    sleep(0.03) #tốc độ của từ "Tuyệt Vời - Khó Thế Mà Cũng Nhớ Ra Được"
print()

import time as t
countdown = range(10,110, +10)
for i in range(len(countdown)):
    print("*                       Đang xử lý: ",countdown[i], end = "")
    print("%")
    t.sleep(0.5) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("*                       Hoàn tất....")

with open("aa.txt", "r") as fh: #"aa.txt" là file chứa text-image đã tạo.
    for line in fh:
        print(line.strip())
        t.sleep(0.1) #Chỉnh sửa thông số thay đổi Tốc độ load của hình ảnh