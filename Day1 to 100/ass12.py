#Get a number from user and then find the 
#sum of the digits in the given number.

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print("Sum of this num is:",sum)