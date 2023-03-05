'''Get an array as input from the user and then find the smallest and largest element in the array'''
def find_min_max_array(arr):
    min_element=max_element=arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        if arr[i] > max_element:
            max_element = arr[i]
    return (min_element, max_element)

n =int(input("Enter the size of the array:"))
arr=list(map(int,input("Enter the array Elements:").split()))
min_element,max_element=find_min_max_array(arr)

print("Smallest element is:",min_element)
print("Largest element is:",max_element)