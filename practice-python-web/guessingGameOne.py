#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Generate a random number between 1 and 9.
#           Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#Extra 1: Keep the game going until the user types exit
#Extra 2: Keep track of how many guesses the user has taken, and when the game ends, print out that number
import random
num = random.randint(1,9)
guess = 0
tries = 0
while(guess != num):
    guess = input("Please guess a number between 1 and 10:")
    if guess == "exit":
        break
    guess = int(guess)
    tries += 1
    if guess < num:
        print("Number is higher than guess")
    elif guess > num:
        print("Number is lower than guess")
    else:
        tries = str(tries)
        print("You were right! It only took you ...")
        print(tries + " tries")
print("Thanks for playing!")
