
passID = "tuong16"
passTrue = input("nhập pass : ")
if passID == False:
    print("sai rồi ")
print(passTrue in {passID })

#Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) 
# sao cho tất cả các chữ số trong số đó là số chẵn. 
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
values = []
for i in range(1000,3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

#Câu hỏi:
#Viết một chương trình chấp nhận đầu vào là một câu, 
# đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
#Thì đầu ra sẽ là:
#Số chữ cái là: 10
#Số chữ số là: 3
#Gợi ý:
print (",".join(values))
s = input("Nhập câu của bạn: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])

# bài toán in ra các số chẵn trong khoảng 100
a = 100
i = 0
while True:
      if i % 2 == 0:
            print(i)
      i += 2
      if i == a:
        break

# bài toán tính tổng các số bé hơn 8
n = 0
sum = 0
while n < 8:
    sum = sum + n
    n = n + 1
print("tổng các số nhỏ hơn 8 là : ", sum)


 
while 0:
    print("điều kiện đúng")
else:
    print("điều kiện sai")
 
#return điều kiện sai












