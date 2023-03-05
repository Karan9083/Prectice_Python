'''Fibonacci series is a special series where nth term is the sum of previous two terms in the series. 
The series starts with 0 and 1 as the first and second term of the series respectively.'''

#Input from user
num= int(input("Enter a  number you like:"))

#Mathematical representation of fibonacci series
n1,n2=0,1

#print the series
print ("Fibonacci series:", n1, n2, end=" ")

#set range 2 to nth for looping
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")

print("\nIts is the fibonacci series for:",num)
