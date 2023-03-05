'''Take an integer as the input from the user and then calculate the number 
of digits in the given input and print it as the output.'''

Number=int(input("Enter the Number:"))
count=0

while Number>0:
    count+=1
    Number=Number//10
    
print("Number the digit present in this",Number,"number is:",count)