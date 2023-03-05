
import math
n=int(input("Enter your number : "))
def factors(n):
    i=1
    while i <=math.sqrt(n):
        if n%i==0:
            if (n/i==i):
                print(i,end=" ")
            else:
                print(i,int(n/i),end=" ")
        i=i+1

print("The factor of {} are:")
factors(n)

