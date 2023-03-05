#Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.
x = int(input("Enter the first co-ordinate:"))
y = int(input("Enter the second co-ordinate:"))

if x<0 and y>0:
    print((x,y),"is in the first quadrant")
elif x>0 and y>0:
    print((x,y),"lis in the second quadrant")
elif x>0 and y< 0:
    print((x,y),"is in the third quadrant")
elif x<0 and y<0:
    print((x,y),"is in the fourth quadrant")
else: print("The points lies in the line")