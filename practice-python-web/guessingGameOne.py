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
