string=str(input("Enter a single string:"))
vowel=0
for i in range(0, len(string)):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
        vowel=vowel+1
print("Vowel number:",vowel)
