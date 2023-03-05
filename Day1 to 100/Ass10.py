'''Get a number from user for which you need to fin the factorial,
then calculate the factorial and give it as the output.'''

num=int(input("Enter the number:"))
factorial=1

if num<0:
    print("It is no possible")
else:
    for i in range(1,num+1):
        factorial=factorial*i
              
print("The factorial of",num,"is:",factorial)