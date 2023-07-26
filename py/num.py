from random import *
user_pass = input("Enter your password:")
password = ['a', 'b', 'c', 'd', 'g', 'h']
guess = "a"
while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 2)]
        guess = str(guess_letter) + str(guess)
    print(guess)
print("Your password is",guess)