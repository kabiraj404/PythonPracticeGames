#this is the guessing game

import random

print("Hi, what shall I call you !!")
name =  input()

print("Thank you, " + name + " for coming here. \n Lets play a game. I will imagine a number and you have to guess the number that I have imagined. Sounds interesting!!. \n Lets play it. \n You can guess any number between 1 and 100, I will give you five chances, Can you guess it?")

secNum = random.randint(1, 100)

for GuessTaken in range(1, 6):
    print("Guess the number ?")
    userGuess = int(input())
    
    if secNum < userGuess:
        print("Another guess, You are chossing higher number.")
    elif secNum > userGuess:
        print(" You are choosing less number. Guess more higher number.")
    else:
        break


if secNum == userGuess:
    print("Congratulation, I think you are my soulmate :), you have exactly thought of what I imagines. You have correctly guessed it in " + str(GuessTaken) + " times. I love you my friend.")
else:
    print("Sorry my friend, the number I imagined was " + str(secNum) + "")
