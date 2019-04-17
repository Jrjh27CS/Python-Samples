#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Create a program that asks the user to enter their name and their age. Print out a message that tells them the year they will be 100.
#Extra 1: Add on by asking the user to enter another number of how many copies of the printed statement they would like to see.
#Extra 2: Print out that many copies on seperate lines.
print("Hi new user. Please enter your name and then your age.\n")
name = input("Name:")
age = int(input("Age:"))
yearsUntil = 100 - age
#Added this line to ensure that the program is not locked to the year that the code was created
currentYear = int(input("Current year:"))
newYear = currentYear + yearsUntil
copies = int(input("How many times would you like to see your new message?"))
for x in range(copies):
    print(f"You will be 100 in the year {newYear}!\n")
