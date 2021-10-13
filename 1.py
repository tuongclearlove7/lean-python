import time as t
chờ = range(10,110, +10)
for i in range(len(chờ)):
    print("                       Loading...: ",chờ[i], end = "")
    print("%")
    t.sleep(0.05) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("""________________________________________________________________________________________________________________________                         
                                           Print Thành Công....                        
_________________________________________________________________________________________________________________""")
with open("idol.txt", "r") as fh: #"idol.txt" là file chứa text-image đã tạo.
    for line in fh:
        print(line.strip())
        t.sleep(0.09) #Chỉnh 