'''Get a string as input from the user and then get another string which has to be removed from the string.
Get the third input, the new substring which is placed in that substring position.
Finally print the output by replacing the substring with new string.'''

def new_updated_str(str1,str2,str3):
    return str1.replace(str2,str3)

str1=input("Enter the string:")
str2=input("Enter the substring to be removed:")
str3=input("Enter the new string:")

result=new_updated_str(str1,str2,str3)
print("The new string is: ",result)






'''str1=input("Enter a string:")
str2=input("Enter the substring to be removed:")
str3=input("Enter the new string:")

new_str=str1.replace(str2,str3)
print("The new String:",new_str)'''