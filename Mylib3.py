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
    def add(num1, num2):
        sum = num1 + num2
        print("The Result of",num1,"+",num2,"=", sum)

    def sub(num1, num2): 
        diff = num1 - num2
        print("The Result of",num1,"-",num2,"=", diff)

    def mult(num1, num2):
        product = num1 * num2
        print("The Result of",num1,"*",num2,"=", product)

    def div(num1, num2):
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
        add(num1, num2)
        sub(num1, num2)
        mult(num1, num2)
        div(num1, num2)
        print("Thanks for using this calculator!")

    def scalc(p1):
        astring = p1.split(",")
        num1 = float(astring[0])
        num2 = float(astring[1])
        if astring[2] == "+":
            add(num1, num2)
        elif astring[2] == "-":
            sub(num1, num2)
        elif astring[2] == "*":
            mult(num1, num2)
        elif astring[2] == "/":
            div(num1, num2)
        return num1, num2

    p1 = input("Enter two numbers and an operator, each separated by a comma: ")
    scalc(p1)
