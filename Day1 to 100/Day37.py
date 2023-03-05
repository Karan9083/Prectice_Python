'''Get a string as the input from the user and find the frequency of characters
 in the string.'''

#character="program"
character=input('Enter The character:')
count=dict() #Empty dictionary

for i in character:
    if i in count: #if already present in character
        count[i]= count[i]+1 #incr the value 
    else:
        count[i]=1 #or fast time appear the put the value 1 as a character value

print(count)



"""Another method:(get function)
Example:
d1={'jan':1,'apr':4,'spt':9}
print(d1.get('jan',0))
"""

'''
#character="program"
character=input('Enter The character:')
count=dict() #Empty dictionary

for i in character:
    if i in count:
        count[i]= count.get(i,0)+1 
print(count)
'''