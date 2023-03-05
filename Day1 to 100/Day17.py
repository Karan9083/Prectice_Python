

'''Get an input from the user and find 
the factors of the number.'''
   
#user Input
num = int(input("Enter a Number:"))
print("The factor of {} are".format(num))

#Loop for every number from 1 to given num
for i in range(1, num + 1):
       #if num%i==0 then print the output
       if num % i == 0: 
           print(i,end=" ")

