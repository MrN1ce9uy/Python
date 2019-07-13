# This is a simple program that utilizes variables, functions, & a loop.


# Define payroll function
def payroll():
    # Payroll calculations
    hours = float(input("Enter number of hours: "))
    rate = float(input("Enter hourly rate: "))

    amount = hours * rate

    # Print values
    print("Hours worked:", hours)
    print("Rate:", rate)
    print("Pay amount:", amount)


# Define mileage function
def mileage():
    # MPG calculations
    miles = float(input("Enter number of miles: "))
    gas = float(input("Enter gallons of gas: "))

    mpg = miles / gas

    # Print values
    print("Miles:", miles)
    print("Gas:", gas)
    print("MPG:", mpg)


# Decision loop
while True:
    # Display options to the user and record their input
    print("Press 1 for Payroll Calculation")
    print("Press 2 for Mileage Calculation")
    print("Press 3 to Exit")

    menu_selection = int(input())

    # if-else statement
    if menu_selection == 1:
        payroll()
    elif menu_selection == 2:
        mileage()
    elif menu_selection == 3:
        break
