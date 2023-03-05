'''Get an array as input from the user and then count the number of even and odd elements present in the array.'''
def check_array(arr):
    odd_count=even_count=0
    for num in arr:
        if num%2==0:
            even_count +=1
        else:
            odd_count +=1

    return odd_count,even_count

n=int(input("Enter the array size:"))
arr=list(map(int,input("Enter the elements:").split()))
even_count, odd_count = check_array(arr)
print("Even elements count:", even_count)
print("Odd elements count:", odd_count)