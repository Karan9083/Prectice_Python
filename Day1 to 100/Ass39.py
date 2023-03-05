'''Get two strings as input from the user and check whether it is Anagram or not.'''

str1=input("Enter the First String:")
str2=input("Enter the second String:")

if sorted(str1)==sorted(str2):
    print("Anagram")
else:
    print("not Anagram")