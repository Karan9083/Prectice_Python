'''Get a number as input from the user and check whether that number is prime or not.
A prime number is a number with factors as 1 and that number itself.'''

num=int(input("Enter a number:"))
temp=0

for i in range(2,num):
    if num%i==0:
        temp=1
        break

if temp==1:
    print("This is not a prime number")
else:
    print("This is 18a prime number")
