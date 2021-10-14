k = []
for a, b, c in [('hello', 'my', 'friend'), ('ok', 'hi', 'bro')]:
    a = a.capitalize()
    b = b.upper()
    c = c.lower()
    k.append('>>'.join((a, b + c)))
print(k)

print('..........................................................')

g = ['>>'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('hello', 'my', 'friend'), ('ok', 'hi', 'bro')]]
print(g)


for i in range(2):
# vòng lặp for với i in range(2) cho phép lặp lại ("I love you") 2 lần
    print ("I love you\r")
#Lệnh 1
print(range(9))
#Xuất từ Phần tử 9 và 0

print(list(range(2, 5)))
#Lệnh 3
print(list(range(2, 5)))
#Lệnh 4
print(list(range(2, 5)))

print(list(range(10)))
