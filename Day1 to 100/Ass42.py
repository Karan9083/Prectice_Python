'''Get two arrays as the input from the user and check whether it is the same or not.'''
arr1=input("Enter the first array:")
arr2=input("Enter the second array:")

a1=list(map(int,input("Enter the first array elements:").split()))
a2=list(map(int,input("Enter the second array elements:").split()))

if a1==a2:
    print("Both array are same")
else:
    print("NO,they are no same")
