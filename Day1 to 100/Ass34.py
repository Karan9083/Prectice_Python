'''Get an algebraic expression as input from the user and then remove all the brackets in that.'''
num=input("Enter the Mathematical Expression:")
brackets=("[","]","{","}","(",")")
count=[]

for i in num:
    if i not in brackets:
        count.append(i)
        
print(*count)