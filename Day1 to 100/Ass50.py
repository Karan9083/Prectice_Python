'''Given an integer array of size N. Write Program to find sum of positive square elements in the array.'''
#Initialize the  array
arr=[1,2,3,4]
#arr=[-1,-2,-3,-4]
sum=0
#loop the array to calculate the sum of positive square elements in the array
for i in range(0,len(arr)):
    sum=sum+arr[i]*arr[i]

print("sum of positive square elements in the array:",sum)