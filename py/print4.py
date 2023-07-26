import time as t
chờ = range(10,110, +10)
for i in range(len(chờ)):
    print("""                          ...
                 bvbvbbvbbbvbvbvbb """,chờ[i], end = "")
    print("%")
    t.sleep(0.05) #Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("Print Thành Công....")