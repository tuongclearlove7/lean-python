from time import sleep
import webbrowser as wb

def Turn_on_browser():
    url = ['https://www.facebook.com/','https://www.youtube.com/watch?v=JNdP_BpOAU8']
    for i in range(len(url)):
        print("get link "+ str(i+1)+" "+str(url[i]))
        pass
    tool = wb.open(url[0])
    tool = wb.open(url[1])
    






