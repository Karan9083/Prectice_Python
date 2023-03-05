#Get an input number from the user and check whether it is a positive or negative number.

n=int(input("Enter a number:"))

if n==0:
        print(n,'Neither positive or negative')
elif n>0:
    print(n,"is a Positive number")
else:
    print (n,"is a negative number")