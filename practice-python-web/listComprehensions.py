#Challenge given by https://www.practicepython.org
#Jordan Jones Apr 16, 2019

#Challenge: Write a line of python that takes list a and makes a new list with only even elements
a= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Before comprehensions
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print(b)
#After comprehensions
print([x for x in a if x % 2 == 0])


#NOTES
#A list comprehension consists of [] containing an expression followed by a FOR clause, then zero or more FOR or IF clauses.
