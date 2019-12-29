#Created by MrN1ce9uy for final project in ENTD220 Intro to Python course at APUS.
print("Hello, this is a simple calculator.\n")

# Declare global variables.
n1 = 0
n2 = 0
sum1 = 0
diff = 0
product = 0
quotient = 0

# Define Arithmetic class.
class Arithmetic:
    def float_input(self, msg): # Use this function for exception handling during user input.
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("You must enter a number!")
            else:
                break
    def add(self):
        global n1, n2, sum1
        sum1 = n1 + n2
        return sum1
    def sub(self):
        global n1, n2, diff
        diff = n1 - n2
        return diff
    def mult(self):
        global n1, n2, product
        product = n1 * n2
        return product
    def div(self):
        global n1, n2, quotient
        if n2 == 0:
            print(n1,"/",n2,"= You cannot divide by Zero")
        else:
            quotient = n1 / n2
            return quotient
    def allInOne(self):
        global n1, n2
        sum2 = n1 + n2
        diff2 = n1 - n2
        product2 = n1 * n2
        quotient2 = n1 / n2
        # Store values in dictionary. 
        result = {"add": sum2, "sub": diff2, "mult": product2, "div": quotient2}
        # Convert dictionary to list
        result = list(result.values())
        print(n1," + ",n2," = ", result[0])
        print(n1," - ",n2," = ", result[1])
        print(n1," * ",n2," = ", result[2])
        print(n1," / ",n2," = ", result[3])
    def userInput(self):
        global n1, n2
        n1 = arith.float_input("Enter your First number: ")
        n2 = arith.float_input("Enter your Second number: ")
        return n1, n2

# Create an instance of the Arithmetic class. 
arith = Arithmetic()

# Call the userInput() function to ask user for input.
arith.userInput()

# Assign values returned from functions to variables. Also call arith functions to perform calculations.
sum1 = arith.add()
diff = arith.sub()
product = arith.mult()
quotient = arith.div()

# Define wrfile class.
class wrfile:
    def write(self): # Define write function.
        with open("results.txt", "w") as write_file:
            write_file.write(str(n1)+" + "+str(n2)+" = "+str(sum1)+"\n")
            write_file.write(str(n1)+" - "+str(n2)+" = "+str(diff)+"\n")
            write_file.write(str(n1)+" * "+str(n2)+" = "+str(product)+"\n")
            write_file.write(str(n1)+" / "+str(n2)+" = "+str(quotient))
            write_file.close
    def read(self): # Define read function.
        with open("results.txt", "r") as read_file:
            text = read_file.read()
            print(text)

# Create an instance of the wrfile class.
wr = wrfile()

# Declare variable for menu counter.
menuSelection = 0

# While statement to loop menu.
while menuSelection != 9:
    menuList = ["\n1. Press 1 for Addition.", "2. Press 2 for Subtraction.", "3. Press 3 for Multiplication.", "4. Press 4 for Division.", "5. Press 5 for All in one.", "6. Press 6 to write results to file.", "7. Press 7 to read results from file.", "8. Press 8 for a new calculation.", "9. Press 9 to exit."]
    for item in menuList:
        print(item)
    menuSelection = float(input())
    if menuSelection == 1:
        print(n1,"+" ,n2,"=", sum1)
    elif menuSelection == 2:
        print(n1,"-",n2,"-", diff)
    elif menuSelection == 3:
        print(n1,"*",n2, "=", product)
    elif menuSelection == 4:
        print(n1,"/",n2, "=", quotient)
    elif menuSelection == 5:
        arith.allInOne()
    elif menuSelection == 6:
        wr.write()
    elif menuSelection == 7:
        wr.read()
    elif menuSelection == 8:
        # Ask user for new input.
        arith.userInput()
        # Call arith functions to perform calculations again with new input.
        arith.add()
        arith.sub()
        arith.mult()
        arith.div()
    elif menuSelection == 9:
        exit
