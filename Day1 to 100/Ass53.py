''' Given an integer array of size N. Write Program to find maximum product sub-array in a given array'''
def MaxSubArr_product(arr,n):
    result = arr[0]
    for i in range(n):
        product = arr[i]
        for j in range(i+1,n):
            result = max(result,product)
            product *= arr[j]
            result = max(result,product)     
    return result
n = int(input("Enter the size of the array:"))
arr = list(map(int,input("Enter the Elements:").split(' ')))
print("The result is:",MaxSubArr_product(arr,n))