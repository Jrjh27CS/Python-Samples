#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#           Take this opportunity to think about how you can use functions.
#           Make sure to ask the user to enter the number of numbers in the sequence to generate.
def fib(x):
    z = []
    if x == 0:
        return z
    z.append(0)
    if x == 1:
        return z
    z.append(1)
    if x == 2:
        return z
    while len(z) != x:
        z.append(z[len(z)-1] + z[len(z)-2])
    return z

num = int(input("How many fibonacci numbers would you like starting from 0? Num:"))
print(fib(num))
