#Program start
print("This is a simple calculator.")

#Define the main program function
def main():
    #Ask user for ranges. String inputs are not accepted and caught as exceptions. While loop repeats asking user for input until a float number is input.
    while True:
        try:
            rangeLower = float(input("Enter your Lower range: "))
        except ValueError:
            print("You must enter a number!")
        else:
            #Break the while-loop
            break
    while True:
        try:
            rangeHigher = float(input("Enter your Higher range: "))
        except ValueError:
            print("You must enter a number!")
        else:
            #Break the while-loop
            break
    #Ask user for numbers. String inputs are not accepted and caught as exceptions. While loop repeats asking user for input until a float number is input.
    while True:
        try:
            num1 = float(input("Enter your First number: "))
        except ValueError:
            print("You must enter a number!")
        else:
            #Break the while-loop
            break
    while True:
        try:
            num2 = float(input("Enter your Second number: "))
        except ValueError:
            print("You must enter a number!")
        else:
            #Break the while-loop
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
