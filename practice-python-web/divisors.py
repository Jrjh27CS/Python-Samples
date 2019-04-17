#Create a program that asks user for a number and then prints out a list of all the divisors of that number.
#Ex. User enters 26, the program should return a list of [1,2,13,26]
num = int(input("User please enter a number:"))
a = range(1, num + 1)
print([x for x in a if num % x == 0])
