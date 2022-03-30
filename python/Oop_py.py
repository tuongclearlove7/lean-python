import base64


def MyData():
    class main():
        def __init__(self,name, nickname):
            self.myname = "cl7\ntoi "+name
            self.mynickname = nickname
        def Hi(self):
            return "Hi! "+self.myname
            
    log = main("yeu thao","toilaclearlove7")# gán class main() cho log
    # "yeu thao" được gán cho name và name gán cho self.myname
    # "toilaclearlove7" được gán cho nickname và nickname gán cho selfmynickname 
    print(log)# print class
    print("toi la  "+log.myname,
        "\ntoi la "+log.mynickname)# class main() được gán cho log và  in ra log.myname , log.mynickname
    # thuộc tính (attribute) name 
    print(main.Hi(log))
    print(log.Hi)

    class method():
        def __init__(self,value,value2) -> None:
            self.method = value
            self.method2 = value2

    console = method("this is method 1 : "+log.Hi()+"\nthis is method 2 :"," hello --  ")
    print(console.method,console.method2)
    # tương tự class ở trên nhưng class này có sự khác biệt đó là  
    #  gán class log.main() được khởi tạo ở trên cho value và value gán cho method

    def SUM(a,b):
        #print("hello world !")
        c = a+b
        return c
    total = SUM(a=16,b=9)
    print(total)  

             

while True:
    while True:
        file_object = open("clearlove7_developer_tool.txt")
        data = file_object.read()
        password = input("nhap pass : ")
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
            print("you were inputing correct password ")
            print(list_pass)
            print("decode : ",log_decode)
            MyData()
            if MyData()==quit() or "End Programing":
                pass
        elif password == log_decode:
            print("you were inputing correct password ")
            print(list_pass)
            print("encode : ", log_encode)
            if MyData()==quit() or "End Programing":
                pass
        if password != log_encode or log_decode :
            print("you were inputing wrong password, please! re-enter")
            print(list_pass)
            break
        

          
            
                
            
               





