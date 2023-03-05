'''Get a string from the user and find the sum of numbers in the string.'''

s=input("Enter the string:")
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)