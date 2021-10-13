from random import randint

print("Nhap Dam, Bao, Keo:")
player = input()
computer = randint(0,2)

if computer == 0:
        computer = "Dam"
if computer == 1:
        computer = "Bao"
if computer == 2:
        computer = "Keo"

print("---")
print("bạn chọn: " + player)
print("computer: " + computer)
print("---")

if player == computer:
            print("Draw") 
else:
    if player == "Keo":
        if computer == "Dam":
            print("Lose")
        else:
            print("Win")

    if player == "Dam":
        if computer == "Keo":
            print("Win")
        else:
            print("Lose")
   
    if player == "Bao":
        if computer == "Keo":
            print("Lose")
        else:
            print("Win")
import pyttsx3
robot_brain = "I can't hear you, try again"
robot_mouth = pyttsx3.init() 
robot_mouth.say("Loser , Win and Draw ")
robot_mouth.runAndWait() 

    		
    		
    		




