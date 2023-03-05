
n = input("Enter anything : ") #User input
if n >= "a" and n <= "z" or n>= "A" and n <= "Z":
   print(n,"input is alphabet")  
elif n>="0" and n<="9":
   print(n,"input is number")

special_characters = "!@#$%^&*()-+?_=,<>/"
if (any(c in special_characters for c in n)):
   print("special character")
