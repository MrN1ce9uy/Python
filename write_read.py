print("Hello, this is a simple calculator.\n")

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
    def add(self, n1, n2):
        sum1 = n1 + n2
        return sum1
    def sub(self, n1, n2):
        diff = n1 - n2
        return diff
    def mult(self, n1, n2):
        product = n1 * n2
        return product
    def div(self, n1, n2):
        if n2 == 0:
            print(n1,"/",n2,"= You cannot divide by Zero")
        else:
            quotient = n1 / n2
            return quotient
    def allInOne(self, n1, n2):
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

# Create an instance of the Arithmetic class. 
arith = Arithmetic()

# Declare variables. Ask user for input and use the exception handling function.      
n1 = arith.float_input("Enter your First number: ")
n2 = arith.float_input("Enter your Second number: ")

# Assign values returned from functions to variables
sum1 = arith.add(n1,n2)
diff = arith.sub(n1,n2)
product = arith.mult(n1,n2)
quotient = arith.div(n1,n2)

# Define wrfile class.
class wrfile:
    def write(self):
        with open("results.txt", "w") as write_file:
            write_file.write(str(n1)+" + "+str(n2)+" = "+str(sum1)+"\n")
            write_file.write(str(n1)+" - "+str(n2)+" = "+str(diff)+"\n")
            write_file.write(str(n1)+" * "+str(n2)+" = "+str(product)+"\n")
            write_file.write(str(n1)+" / "+str(n2)+" = "+str(quotient))
            write_file.close
    def read(self):
        with open("results.txt", "r") as read_file:
            text = read_file.read()
            print(text)

# Create an instance of the wrfile class.
wr = wrfile()

# Declare variable for menu counter.
menuSelection = 0

# While statement to loop menu.
while menuSelection != 8:
    # Store menu items in a list.
    menuList = ["\n1. Press 1 for Addition.", "2. Press 2 for Subtraction.", "3. Press 3 for Multiplication.", "4. Press 4 for Division.", "5. Press 5 for All in one.", "6. Press 6 to write results to file.", "7. Press 7 to read results from file.", "8. Press 8 to exit."]
    # Loop through items in list.
    for item in menuList:
        print(item)
    # Get user input for menu selection.
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
        arith.allInOne(n1,n2)
    elif menuSelection == 6:
        wr.write()
    elif menuSelection == 7:
        wr.read()
    elif menuSelection == 8:
        exit
