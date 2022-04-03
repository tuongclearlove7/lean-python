import base64
import os, sys
from Data_Oop import MyQuery, Paint, Hacker
while True:
    password = input("Input Password : ")
    file_object = open("clearlove7_developer_tool.txt")
    data = file_object.read()
    base64_message = data
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    log_decode = message_bytes.decode('ascii')
    key_encode = log_decode.encode('ascii')
    byte64 = base64.b64encode(key_encode)
    log_encode = byte64.decode('ascii')
    List_pass = []
    List_pass.append(password)
    if password == log_encode:
        print("You were inputing correct password ")
        print(List_pass)
        print("decode : ",log_decode)
        if __name__ == "__main__":
            MyQuery.MyData()
            #Paint()
        if Hacker() == sys.exit() or "End Programming":# exit and quit
            pass
    elif password == log_decode:
        print("You were inputing correct password ")
        print(List_pass)
        print("encode : ", log_encode)
        if __name__ == "__main__":
            MyQuery.MyData()
            #Paint()
        if Hacker() == quit() or "End Programming":
            pass
    if password != log_encode or log_decode :
        print("You were inputing wrong password, please! re-enter")
        print(List_pass)

    








