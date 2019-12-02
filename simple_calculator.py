# Program name    Wk3P1_john_files.py
# Student Name    John Files
# Course          ENTD220
# Instructor      Georgia Brown
# Date            11/24/2019
# Description     This code will aske the user for a lower range and a higher range.  Then it will ask the user for the first number and then the second number.  Then it will provide the sum, difference, product, and quotient of the two numbers. Then it will ask the user to repeat the program or not.  

#Program start
print("This is a simple calculator.")

#Define the main program function
def main():
    #Ask user for ranges
    while True:
        try:
            rangeLower = float(input("Enter your Lower range: "))
        except ValueError:
            print("You must enter a number!")
        else:
            break
    while True:
        try:
            rangeHigher = float(input("Enter your Higher range: "))
        except ValueError:
            print("You must inter a number!")
        else:
            break
    #Ask user for numbers
    while True:
        try:
            num1 = float(input("Enter your First number: "))
        except ValueError:
            print("You must enter a number!")
        else:
            break
    while True:
        try:
            num2 = float(input("Enter your Second number: "))
        except ValueError:
            print("You must enter a number!")
        else:
            break
    #Define formula functions
    def add():
        sum = num1 + num2
        print("The Result of",num1,"+",num2,"=", sum)

    def sub(): 
        diff = num1 - num2
        print("The Result of",num1,"-",num2,"=", diff)

    def mult():
        product = num1 * num2
        print("The Result of",num1,"*",num2,"=", product)

    def div():
        if num2 == 0:
            print("The Result of",num1,"/",num2,"= You cannot divide by Zero")
        else:
            quotient = num1 / num2
            print("The Result of",num1,"/",num2,"=", quotient)

    #If-else
    if num1 < rangeLower or num1 > rangeHigher or num2 < rangeLower or num2 > rangeHigher:
        print("The input values are outside the input ranges.")
        print("Please check the number and try again.")
        print("Thanks for using our calculator")
    else:
        #Call functions
        add()
        sub()
        mult()
        div()
        print("Thanks for using this calculator!")

#Call main function
main()

#While-loop
x = 0
while x != "n":
    print("Would you like to make another calculation? y/n")
    x = input()
    if x == 'y':
        main()
