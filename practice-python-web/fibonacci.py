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
