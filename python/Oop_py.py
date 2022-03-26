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








