''' Given an integer array of size N. Write Program to find whether Arrays are disjoint or not.
 Two arrays are said to be disjoint if they have no elements in common.'''

n1=input("Enter the first array size:")
arr1=set(map(int,input("Enter the elements of the array:").split(" ")))
n2=input("Enter the second array size:")
arr2=set(map(int,input("Enter the elements of the array:").split(" ")))

if (arr1.intersection(arr2)):
    print("Not Disjoint as there is something common from both array")
else:
    print(" Is Disjoint")
