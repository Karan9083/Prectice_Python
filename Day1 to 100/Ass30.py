'''Get a string as input from user and print the length of the string without using strlen() function'''

str=input("Enter the String:")
count=0

for i in str:
    count=count+1
print("The length of the String is:",count)