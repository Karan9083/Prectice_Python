#Get the number of month and year as input from the user and check the number of days present in that month.

month = int(input("Enter the month you want:"))
year = int(input("Enter the Year you want:"))
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	print("Number of days is 31 in this month")
elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):	
	print("Number of days is 29 in this month")
elif(month == 2):
	print(" of days is 28 in this month")
else:
	print("Number of days is 30 in this month")