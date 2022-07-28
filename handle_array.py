import math
import os
from time import sleep
import random
from random import random, randint
from Random_exam import random_array
from My_Browser import Turn_on_browser


def static_array():
    arr_object = [False,True,None,[],"string",1,object,__name__]# mang tinh chua tat ca object
    for i in range(len(arr_object)):
        print(arr_object[i])
    print(arr_object)
    a =[1,99,3,11,5]#mang tinh
    for i in range(len(a)):
        print(a[i])
    print("sap xep mang tinh theo thu tu tang dan : ",str(sorted(a)))
    print(a)
    print("max trong mang tinh la : "+str(max(a)))
    print("min trong mang tinh la : "+str(min(a)))
    hash_code = list([id("tuong"),hash("tuong")])# handle hash code 
    print(hash_code)
    for i in hash_code:
        print("hash code : ",i)
    my_set = [{
    "id": 1,
    "name":"tuong",
    "age": 20,
    "year": 2002
    }]
    for  i in my_set:
        print("set : "+str(i))

def Dynamite_array_string():
    global n
    arr = []
    n=int(input("nhập n : "))
    for idx in range(n):
        arr.append(str(input("nhập mảng : " )))#nhap mang xuat mang lay ca chuoi va so 
    for idx in range(n):
        print(arr[idx])
    print(arr)

def Dynamite_array():
    array = []
    n=int(input("nhập n : "))
    for i in range(n):
        array.append(int(input('Nhap so thu  %d : '%(i+1))))# nhap mang so nguyen
    print(array)
    print("sap xep mang dong theo thu tu tang dan : ",str(sorted(array)))
    mang = []
    for i in range(len(array)):
        number = array[i]
        if (number % 2) == 0:#lay so chan trong array
                print("so chan la : ",number)
                mang.append(number)
    print("mang so chan la : ",mang)
    print("max la :",(max(array)))
    print("min la :",(min(array)))

def random_delay():
    for delay in range(1, 101):
        print(f'\rđang tải| {delay}% |')
        if randint(1, 3) == 2:
            sleep(random())
def Time_count():
    cowndown = range(1,101, +1)
    for i in range(len(cowndown)):
        print("""|loading... """,cowndown[i], end = "")
        print("%|")
        sleep(0.015)



def Handle():
    print("chuc mang ban da nhap dung mat khau, bam enter de tiep tuc")
    input("Enter_>")
    print("Co cac bai tap sau day")
    sleep(1)
    print("1.mang tinh\n2.mang dong ve chuoi\n3.mang dong ve so nguyen\nkey la 1, 2, 3, 4")
    keyvalue = [1,2,3,4,5]
    
    while True:
        try:
            keyword = int(input("nhap : "))
            if keyword == keyvalue[0]:
                Time_count()
                os.system('cls')
                static_array()
                break
            elif keyword == keyvalue[1]:
                Time_count()
                os.system('cls')
                Dynamite_array_string()
                break
            elif keyword == keyvalue[2]:
                Time_count()
                os.system('cls')
                Dynamite_array() 
                break
            elif keyword == keyvalue[3]:
                os.system("cls")
                random_array()
                break
            elif keyword == keyvalue[4]:
                Time_count()
                os.system('cls')
                Turn_on_browser()
                break
            elif keyword == 0 or keyword > 5:
                print("ban phai so nguyen 1, 2, 3, 4 vui long nhap lai")
        except:
            print("ban phai nhap so nguyen vui long nhap lai ")


def Handle_program():
    print("================================MENU==================================")
    key = ["t",["a"]]
    for i in key[0]:
        print(str(key[0]))
    for j in key[1]:
        print(j)
            
    password = input("nhap mat khau : ")
    while True:
        if password == key[0]:
            Handle()
            break;
        elif password == j:
            Handle()
            break;
        else:
            password = input("ban da nhap sai mat khau nhap lai : ")
Handle_program()