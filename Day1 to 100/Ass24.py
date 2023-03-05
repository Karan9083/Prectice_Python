'''Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.'''

row=int(input("Enter the row you want to print:"))

for i in range(0,row):
    for j in range(0,i+1):
        print('*',end="")
        
    print('')