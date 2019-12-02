#Program start
print("This is a simple calculator.")

#Define the main program function
def main():
    #Define input function
    def float_input(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("You must enter a number!")
            else:
                break
    #Declare variables        
    rangeLower = float_input("Enter your Lower range: ")
    rangeHigher = float_input("Enter your Higher range: ")
    num1 = float_input("Enter your First number: ")
    num2 = float_input("Enter your Second number: ")

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
