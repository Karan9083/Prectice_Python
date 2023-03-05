'''Get an input number from user and check whether the given number is an Armstrong number or not.
E.g. Let the number be 1634,
Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634
Therefore, this is an Armstrong number'''

#Enter input
num=int(input("Enter a 4-digit number:"))

sum=0
temp=num

#Define function
while temp>0:
    digit=temp%10
    sum += digit*digit*digit*digit   #formula only for 4digit armstrong
    #sum +=digit*digit*digit   #for 3digit number
    temp=temp//10

if sum==num:
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")