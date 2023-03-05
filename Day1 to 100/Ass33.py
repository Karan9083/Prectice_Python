'''Get an input string from the user and then check whether it is a palindrome string or not.'''

def isPalindrome(p):
    return p==p[::-1]

str=input("Enter the string:")
Ans= isPalindrome(str)

if Ans:
    print("Palindrome")
else:print(("Not palindrome"))
