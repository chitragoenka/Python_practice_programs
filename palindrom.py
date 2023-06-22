# The provided code defines a function named checkPalindrom in Python, which checks whether a given string is a palindrome or not.

def checkPalindrom(str):
    str1=str[::-1]
    if(str==str1):
        return True
    else:
        return False

# Usage of the function
    
input="level"

if(checkPalindrom(input)):
    print("String is palindrom")
else:
    print("String is not palindrom")

input1="python"

if(checkPalindrom(input1)):
    print("String is palindrom")
else:
    print("String is not palindrom")    