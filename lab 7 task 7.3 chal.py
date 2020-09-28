string=input("Please enter a string:")
char=input("Please enter a character:")
i=-1
for letter in string:
    i=i+1
    if char==letter:
        print(i)
