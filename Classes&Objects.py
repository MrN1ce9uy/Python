print("Hello, this is a simple calculator.")

# Define class
class Arithmetic:
    def float_input(self, msg): # Use this function for exception handling during user input
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("You must enter a number!")
            else:
                break
    def add(self, n1, n2):
        sum1 = n1 + n2
        print(n1,"+" ,n2,"=", sum1)
    def sub(self, n1, n2):
        diff = n1 - n2
        print(n1,"-",n2,"-", diff)
    def mult(self, n1, n2):
        product = n1 * n2
        print(n1,"*",n2, "=", product)
    def div(self, n1, n2):
        if n2 == 0:
            print(n1, "/",n2,"= You cannot divide by Zero")
        else:
            quotient = n1 / n2
            print(n1, "/",n2,"=", quotient)
    def allInOne(self, n1, n2):
        # Store values in dictionary (not required, just excercising dictionary skill)
        res = {"add": add(n1, n2), "sub": sub(n1, n2), "mult": mult(n1, n2), "div": div(n1, n2)}

# Create an instance of the Arithmetic class.  This was required, else I was getting an error. 
arith = Arithmetic()

# Declare variables. Ask user for input and use the exception handling function.  
# An instance of the class was required to pass the paramaters to the function.    
n1 = arith.float_input("Enter your First number: ")
n2 = arith.float_input("Enter your Second number: ")

# Declare variable for menu counter.
menuSelection = 0

# While statement to loop menu.
while menuSelection != 6:
    # Store menu items in a list.
    menuList = ["1. Press 1 for Addition.", "2. Press 2 for Subtraction.", "3. Press 3 for Multiplication.", "4. Press 4 for Division.", "5. Press 5 for All in one.", "6. Press 6 to exit."]
    # Loop through items in list.
    for item in menuList:
        print(item)
    # Get user input for menu selection.
    menuSelection = float(input())
    if menuSelection == 1:
        arith.add(n1, n2)
    elif menuSelection == 2:
        arith.sub(n1, n2)
    elif menuSelection == 3:
        arith.mult(n1, n2)
    elif menuSelection == 4:
        arith.div(n1, n2)
    elif menuSelection == 5:
        arith.allInOne(n1, n2)
    elif menuSelection == 6:
        exit
