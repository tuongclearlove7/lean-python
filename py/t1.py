print()
print()
from time import sleep



a1 = '{:^110}'.format('hello mọi người tôi là tường\n')
a2 = '{:^10}'.format('$$$$$$$$$$$$$$$$$$$$$$$$\n')
#print cách một đoạn                        tuong

for c in a1 + a2:
    print(c, end='', flush=True)
    sleep(0.02) #Chỉnh sửa thông số, tốc độ load của note.
print()

