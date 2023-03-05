'''Get an array as the input from the user and find the sum of the elements.'''

n=int(input("Enter the size of array:"))
arr=list(map(int,input("Enter the elements of the array:").split()))
sum=0

for i in range(0,len(arr)):
    sum = sum + arr[i]

print(str(sum))