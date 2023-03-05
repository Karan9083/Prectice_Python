'''Get a string as the input from the user and then remove all the vowel 
letters from the string and give the output.'''

str=input("Enter the string:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in str:
    if i not in vowels:
        result = result + i

print("After removing Vowels: ", result)