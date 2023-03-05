'''Get the input from the user for the value of n and then
find the sum of first n natural numbers.'''

#User Input
N=int(input("Enter the value you like to print:"))

#formula to find sum of Nth term
sum=int(N*((N+1)/2))

#find the all possible num in range of values staring from 1
for i in range(1,N+1):
    print(i, end=" ")

#print the output  
print("And Sum of those",N ,"nums are:",sum)