# câu lệnh with


with open('tuong.txt', 'w') as f:
     print('I love you', file=f)
#mở file tuong.txt và as f của file=f 
# và ghi I love you vào file tuong.txt
from time import sleep
a1 = '.........................Hương......................\n' 
a2 = '...............ăn ...................cứt '
for c in a1 + a2: # c in a1 + a2 có tác dụng print 
# in ra từng chữ trong a1 và a2 cộng lại trong 0.2 giây
    print(c, end='', flush=True)
    sleep(0.2)
print()
   
