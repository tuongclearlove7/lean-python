import random
from time import sleep

def crack():
    char = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    arr = list(char)
    key = input("input password : ")
    guess_pass = ""
    while (guess_pass!=key):
        guess_pass = random.choices(arr,k=len(key))
        print("log : "+str(guess_pass))
        if guess_pass==list(key):
            print("password is "+"".join(guess_pass))
            break

crack()





