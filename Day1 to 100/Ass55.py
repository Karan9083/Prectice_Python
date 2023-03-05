'''Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and
 print the sum of maximum scalar product (Dot product) of 2 vectors.'''

array_size=input("Enter the size of array:")
arr1=list(map(int,input("Enter the elements of first array:").split()))
arr2=list(map(int,input("Enter the elements of second array:").split()))
n=len(arr1)
arr1.sort()
arr2.sort()
product=0
for i in range(n):
    product +=arr1[i]*arr2[i]

print("The Dot vector of both array is:",product)