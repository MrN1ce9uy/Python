#This is a simple program that utilizes variables, functions, & a loop.
#Created by MrN1ce9uy

#Define payroll function
def payroll():
	#Payroll calculations
	hours = float(input("Enter number of hours: "))
	rate = float(input("Enter hourly rate: "))
	amount = hours * rate
	#Print values
	print ("Hours worked:", hours)
	print ("Rate:", rate)
	print ("Pay amount:", amount)

#Define mileage function
def mileage():
	#MPG calculations
	miles = float(input("Enter number of miles: "))
	gas = float(input("Enter gallons of gas: "))
	mpg = miles / gas
	#Print values
	print ("Miles:", miles)
	print ("Gas:", gas)
	print ("MPG:", mpg)

#Define variable
menuSelection = 0

#Decision loop
while menuSelection != 3:
	#Display options to the user and record their input
	print("Press 1 for Payroll Calculation")
	print("Press 2 for Mileage Calculation")
	print("Press 3 to Exit")
	menuSelection = int(input())
	#if-else statement
	if menuSelection == 1:
		payroll()
	elif menuSelection == 2:
		mileage()
