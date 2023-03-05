#Import module to solve the problem
import cmath #complex number module

#Input From user
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

#Calculate the decrement
d= (b**2) - (4*a*c)

#calculate the formula
solution1=(-b + cmath.sqrt(d))/(2*a)
solution2=(-b - cmath.sqrt(d))/(2*a)

#print the output
print("the output {} and {}".format(solution1,solution2))



'''wrong for talent battel question prediction'''