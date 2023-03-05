'''Get a number as input from user and then check whether that number is a
 strong number or not. A number is said to be strong number if 
 the sum of the factorial of each digit in the number is same as that of the number.

E.g. let the number be 145

Here 1! + 4! + 5! is 1 + 24 + 120 which is equal to 145 itself.'''


num=int(input("Let the number be:"))
sum=0
temp=num

while(temp>0):
    fact=1
    remain=temp%10

    for i in range(1,remain+1):
        fact=fact*i

    print("Factorial %d=%d "%(remain,fact))
    sum=sum+fact
    temp=temp//10

print("\n sum of factorial num" ,num,"=",sum)

if (sum==num):
    print("This is a strong number")
else:
    print("This is not a strong number")
