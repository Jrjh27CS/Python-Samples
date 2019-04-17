numbers = []

def addXby(x, inc):
    i = 0
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i+ inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

print("What should we count to?")
x = input("> ")
x_int = int(x) + 1
print("What should we count by?")
inc = input("> ")
inc_int = int(inc)
addXby(x_int, inc_int)
print("The numbers: ")

for num in numbers:
    print(num)
