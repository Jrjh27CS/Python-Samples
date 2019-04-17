#Write a program that asks the user for a long string containing multiple words.
#Print back the same string but with the words in backwords order.
def split(s):
    return s.split(" ")

def reverse(l):
    reverse = []
    [reverse.insert(0,x) for x in l]
    reverse = ' '.join(reverse)
    return reverse

def betterReverse(s):
    return ' '.join(s.split()[::-1])

sample = input("Please enter a sentence:")
print(reverse(split(sample)))
print(betterReverse(sample))
