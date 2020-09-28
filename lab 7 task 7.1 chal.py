even=0
odd=0
print("Enter a series of integers, when you are done entering, enter '0'")
userInput=int(input("Please enter a series of integers:"))
while userInput!=0:

    if userInput%2==0:
        even=even+1
    else:
        odd=odd+1
    userInput=int(input("Please enter a series of integers:"))
print("Even numbers:",even)
print("Odd numbers:",odd)
    
