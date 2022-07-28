import random
from time import sleep

def random_array():
    Literary = [
    "vo chong a phu", "dat nuoc", 
    'song da', 'chiec thuyen', 
    'vo nhat','song','tay tien',
    'song huong','hon truong ba']
    i = 1
    while i<100:
        sleep(0.03)
        print(i,random.choice(Literary))
        i+=1
    exam = ("de thi nam nay se la : "+str(random.choice(Literary)))
    print(i,exam)
    print(len(exam))
    ratio = (i*9/float(len(exam)))
    print("voi ti le la : "+str(ratio)+"%")

def random_array2():
    Literary = [
    "vo chong a phu", "dat nuoc", 
    'song da', 'chiec thuyen', 
    'vo nhat','song','tay tien',
    'song huong','hon truong ba']
    for i in range(100):
        sleep(0.01)
        print(random.choice(Literary))
    print("de thi nam nay se la : "+str(random.choice(Literary)+"\nti le la : "+str(i/9-0.01)+"%"))

def die():
    Literary1 = str(input("nhap tac pham 1 : "))
    Literary2 = str(input("nhap tac pham 2 : "))
    Literary3 = str(input("nhap tac pham 3 : "))
    Literary4 = str(input("nhap tac pham 4 : "))
    Literary5 = str(input("nhap tac pham 5 : "))
    Literary6 = str(input("nhap tac pham 6 : "))
    Literary7 = str(input("nhap tac pham 7 : "))
    Literary8 = str(input("nhap tac pham 8 : "))
    Literary9 = str(input("nhap tac pham 9 : "))
    keyvalue = [1,2,3,4]
    while True:
        try:
            keyword = int(input("nhap : "))
            if keyword == keyvalue[3]:
                break
            elif keyword == 0 or keyword >=5:
                print("ban phai so nguyen 1, 2, 3 vui long nhap lai")
        except:
            print("ban phai nhap so nguyen vui long nhap lai ")









