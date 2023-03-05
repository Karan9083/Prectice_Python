'''Get a number as input from the user and express that number as sum of two prime numbers.'''
val=int(input("Enter the value you like :"))
num=[]
for a in range(val):
    if a > 1:
        for x in range(2, a):
            if a % x == 0:
                break
        else: 
            num.append(a)
for x in range(len(num)):
    for i in range(len(num)):
        if num[x]+num[i]==val:
            if num[x]<=num[i]:
                print(val,'can be expressed as sum of',num[x], " and ", num[i] )