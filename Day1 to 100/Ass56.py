'''Write Program to find whether the numbers of an array be made equal'''
def check(array,length):
    for i in range(0,length):
        while (array[i] %2 == 0):
            array[i]//=2
        while(array[i] % 3 == 0):
            array[i]//=3
    for i in range(0,length):
        if (array[i] != array[0]):
            return False
    return True
n=input("Enter the size of array:")
array=list(map(int,input("Enter the elements:").split()))
length=len(array)
if check(array,length):
        print("Yes")
else:
    print("No")