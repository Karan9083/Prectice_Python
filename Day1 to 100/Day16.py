'''Get the input from the user and check whether that number is a perfect number or not.

E.g. Let number is 28, factors of 28 are 1,2,4,7,14. Now the 
sum of all these factors are 28 itself.
'''

num=int(input("Let the number be:"))
sum=0

for i in range(1,num):
    if num % i==0:
        sum= sum + i

if sum==num:
    print("Its a perfect number")
else:
    print("It is not a perfect number")