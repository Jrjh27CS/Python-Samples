#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Ask the user for a number and determine whether the number is prime or not. Use your prior solution to divisors.py
def get_divisors(num):
    a = range(1, num + 1)
    return [x for x in a if num % x == 0]
    
#Added edge case of 1
num = int(input("User please enter a number:"))
divisors = get_divisors(num)
if num == 1:
    print(f"Your number {num} is not a prime, it's an edge case")
elif len(divisors) < 3:
    print(f"Your number {num} is prime")
else:
    print(f"Your number {num} was not a prime")
