# -*- coding: utf-8 -*-
guess = 50
min_num = 0
max_num = 100
print("Please think of a number between 0 and 100!")
while(True):
    print("Is your secret number", str(guess) + "?")
    i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    last_guess = guess
    if(i == 'h'):
       guess = (guess + min_num) // 2
       max_num = last_guess
    elif(i == 'l'):
       guess = (guess + max_num) // 2
       min_num = last_guess
    elif(i == 'c'):
       print("Game over. Your secret number was:", guess)
       break
    else:
       print("Sorry, I did not understand your input.")
       