# Cấu trúc rẽ nhánh
# if
#  else
# elif
a  = 3
if a - 1 < 0:
    print('a nhỏ hơn 1') # False vì a - 1 không bé hơn 0
elif a - 2 < 0:
    print('a nhỏ hơn 2') # False vì a - 2 không bé hơn 0
elif a - 3 < 0:
    print('a nhỏ hơn 3') # False vì a - 3 không bé hơn 0
elif a - 4 < 0:
    print('a nhỏ hơn 4') # True  vì a - 4 bé hơn 0 
    #nên thực hiện suất ra a nhỏ hơn 4 
elif a - 5 < 0:
    print('a nhỏ hơn 5')  
# chương trình kết thúc  a - 5 < 0 True nhưng không có ý nghĩa 



a = 3
if a - 1 < 0:
    print('a nhỏ hơn 1')
else:
    print('a nhỏ hơn 5')
# a = 3 - 1 không bé hơn 0 và 1 nên không thực hiện 'a nhỏ hơn 1'
# Nhưng a = 3 - 1 lớn hơn 0 và nhỏ hơn 5 nên suất ra a nhỏ hơn 5

a  = 10
if a - 1 < 0:
    print('a nhỏ hơn 1') # False vì a - 1 không bé hơn 0
elif a - 2 < 0:
    print('a nhỏ hơn 2') # False vì a - 2 không bé hơn 0
elif a - 3 < 0:
    print('a nhỏ hơn 3') # False vì a - 3 không bé hơn 0
elif a - 4 < 0:
    print('a nhỏ hơn 4') # True  vì a - 4 bé hơn 0 
    #nên thực hiện suất ra a nhỏ hơn 4 
elif a - 5 < 0:
    print('a nhỏ hơn 5')  
# chương trình kết thúc  a - 5 < 0 True nhưng không có ý nghĩa 
else:
    print('không thảo mãn hết thì gán vào đây')
