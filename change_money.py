import pyttsx3

usd = input("nhap tien : ")
vnd = int(usd) * 23000
print(str(usd) + " usd = " + str(vnd) + " VND")

robot_mouth = pyttsx3.init()
robot_mouth.say(str(usd)+"......usd....."+"change "+str(vnd)+".......vnd.......")
robot_mouth.runAndWait()
























