'''Given an integer array of size N, write a program to reverse the array'''

n=int(input("Enter the size of the array:"))
arr=list(map(int,input("Enter the elements of the array:").split()))

arr.sort(reverse=True)

print("After sorting we get:",*arr)