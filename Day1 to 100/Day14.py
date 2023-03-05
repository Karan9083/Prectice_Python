"""Get an input from the user and the print the reverse of the given number as the output

E.g. let the number be 324 then the reverse of the number is 423"""

#user input
number=input("Let the number be:")[::-1] #slice statement [::-1]

print("The reverse of the number is:",number)