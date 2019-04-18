#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Write a program that prints out all of the elements in given list a less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 10:
        print(x)
#Extra 1: Instead of 1 by 1 print, make a new list that has all elements less than 5 and print new list
b = []
for x in a:
    if x < 5:
        b.append(x)
print(b)
#Extra 2: Write this in one line of python
print([x for x in a if x < 5])
#Extra 3: Ask user for num and return a list that contains only nums from a that are smaller than given number
limiter = int(input("What number would you like all elements to be smaller than? Num:"))
print([num for num in a if num < limiter])
