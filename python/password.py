import base64
from Data_Oop import MyQuery, Paint, Hacker
while True:
    file_object = open("clearlove7_developer_tool.txt")
    data = file_object.read()
    password = input("Input Password : ")
    my_password = (data)
    key_encode = my_password.encode("ascii")
    encode_base64 = base64.b64encode(key_encode)
    log_encode = encode_base64.decode("ascii")
    decode_base64 = (log_encode)
    encode_bytes = decode_base64.encode("ascii")
    decode_bytes = base64.b64decode(encode_bytes)
    log_decode = decode_bytes.decode("ascii")
    list_pass = []
    list_pass.append(password)
    if password == log_encode:
        print("You were inputing correct password ")
        print(list_pass)
        print("decode : ",log_decode)
        if __name__ == "__main__":
            MyQuery.MyData()
            Paint()
        if Hacker() == exit() or "End Programming":# exit and quit
            pass
    elif password == log_decode:
        print("You were inputing correct password ")
        print(list_pass)
        print("encode : ", log_encode)
        if __name__ == "__main__":
            MyQuery.MyData()
            Paint()
        if Hacker() == quit() or "End Programming":
            pass
    if password != log_encode or log_decode :
        print("You were inputing wrong password, please! re-enter")
        print(list_pass)

    








