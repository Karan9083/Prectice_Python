'''Day 1 coding Statement: Write a program to identify if the character is a vowel or consonant.
Description of the program: 
'''

Character=input("Enter the Character ") #User input

if Character.lower() in('a','e','i','o','u','y'):
    print(Character,'is Vowel')
elif Character.upper() in('A','E','O','I','U','Y'):
    print(Character,'is Vowel')
elif ((Character >= 'A' and Character <= 'Z') or (Character>= 'a' and Character <= 'z')):
    print(Character,"is Consonant")
else:
    print ('it is not valid')
