#Write a function that takes a list and returns a new list that contains all the elements from the first list minus duplicates
def removeDupes(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    print(b)
    
def removeBetter(a):
    print(set(a))
#Extra 1: Write two functions to do this one with a loop and one using sets
a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
removeDupes(a)
removeBetter(a)
