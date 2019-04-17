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
#A list comprehension consists of [] containing an expression followed by a for clause, then zero or more for or if clauses.
