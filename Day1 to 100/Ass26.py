'''Get the number of people in the room as input from the user. Then calculate the maximum number of 
handshakes possible among that people.

For e.g. If there are N people in the room then the first person has to shake hand with N-1 people and 
second person has to shake hand with N-1-1 people i.e., N-2 handshakes are possible. Thus, it goes on.
So total hand shakes = N-1 + N-2 + N-3 +………+1 + 0'''

Number_of_People=int(input("Enter the number of people in a room:"))
Total_number_of_handshake=int(Number_of_People*((Number_of_People-1)/2))

print("Total possible handshake for",Number_of_People,"people is",Total_number_of_handshake)
