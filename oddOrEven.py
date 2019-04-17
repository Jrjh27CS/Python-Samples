#First challenge is to accept a single number and check if it's odd or even
#Used modulus to check against remainder
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
rem = num1 % 2
if rem == 0:
    print("Your num was even")
else:
    print("Your num was odd")
#First extra was to check if number was divisible by 4 so modulus again
remSpec = num1 % 4
if remSpec == 0:
    print("Your num was divisible by 4")
#Final extra was to check whether your first number is evenly divisible by your second number.
rem = num1 % num2
if rem == 0:
    print(f"Your number {num1} is evenly divisible by your other num {num2}!")
else:
    print(f"Your number {num1} is not evenly divisible by your other num {num2}!")
