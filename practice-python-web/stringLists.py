#Ask the user for a string and print out whether it's a palindrome or not.
check = input("Please enter a string to check:")
reverse = []
[reverse.insert(0,x) for x in check]
reverse = ''.join(reverse)
if check == reverse:
    print("Hey this string is a palindrome!")
else:
    print("That's a great string, but it isn't a palindrome.")
