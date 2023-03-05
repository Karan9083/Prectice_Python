'''Get an input number from user and check whether the given number is an Armstrong number or not.
E.g. Let the number be 1634,
Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634
Therefore, this is an Armstrong number'''


num = int (input("Enter the number:"))

digit, sum = 0, 0
length = len(str(num))

for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
  
if sum==num:
  print("Armstrong")
else:
  print("Not Armstrong")