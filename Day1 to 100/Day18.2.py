"""Get the values for numerator and denominator of two fractions, then add that fractions. 
Consider the following format

x3/y3 = (x1/y1) + (x2/y2)

here x3 = (x1*y2) + (x2*y1) and y3 = (y1*y2)"""

def findGCD(n1, n2):
    gcd = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

# input first fraction
num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))
# input first fraction
num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))
#calculation
l_sum = (den1 * den2) // findGCD(den1, den2)
sum = (num1 * l_sum // den1) + (num2 * l_sum // den2)
num3 = sum // findGCD(sum, l_sum)
l_sum = l_sum // findGCD(sum, l_sum)
#Print the output Result
print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", l_sum)