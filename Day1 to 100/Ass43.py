'''Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.'''

def check_array_type(arr):
    odd = 0
    even = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == len(arr):
        return "Odd type array"
    elif even == len(arr):
        return "Even type array"
    else:
        return "Mixed type array"
n=int(input("Enter the array Size:"))
arr = list(map(int, input("Enter the elements of the array: ").split()))
print(check_array_type(arr))