'''Get a number as input from the user and find the zeros present in that number.
Then convert the zeros into one and then print it.'''

val=int(input("Enter a number you like:"))
#Change the type of string
val=str(val)

Replace=val.replace('0','1')
print("Converted number is:",Replace)