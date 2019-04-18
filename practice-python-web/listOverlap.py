#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Take two lists and write a program that returns a list that only contains common elements without duplicates.
#           Lists should not care about size
from random import *
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for num in a:
    if num in b:
        if num not in c:
            c.append(num)
print(f"Here's list a:{a}")
print(f"Here's list b:{b}")
print(c)
#Extra 1: Randomly generate two lists to test
x = []
y = []
z = []
for num in (range(randint(10,20))):
    x.append(randint(1,10))
for num in (range(randint(10,20))):
    y.append(randint(1,10))
for num in x:
    if num in y:
        if num not in z:
            z.append(num)
print(f"Here's list x:{x}")
print(f"Here's list y:{y}")
print(z)
#Extra 2: Write in one line of python
print(set([num for num in x if num in y]))
