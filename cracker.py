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

for i in range(100):
    Literary = ['vcap', 'dat nuoc', 'song da', 'chiec thuyen', 'vo nhat','song','tay tien','song huong']
    print(random.choice(Literary))
print("de thi la : "+str(random.choice(Literary)))





