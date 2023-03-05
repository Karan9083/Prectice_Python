'''Get a string as the input from the user and print the non-repeating characters in a string.
Input
Hello

Output
H e o'''

string=input("Enter the Words:")
for i in string:
    if string.count(i)==1:
        print(i,end=" ")

'''String=input("Enter the words:")

for i in String:
    count=0
    for j in String:
        if i==j:
            count+=1

        if count>1:
            break

    if count==1:
        print(i,end="")
'''