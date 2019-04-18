#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
def modList(x):
    return [x[0],x[len(x) - 1]]

a = [5, 10, 15, 20, 25]
print(modList(a))
