#Program Name:     Wk6_john_files.py
#Student Name:     John Files
#Course:           ENTD220
#Instructor:       Georgia Brown
#Date:             12/15/2019

#Copy Wrong:       This is my work.

print("Hello, this is a simple calculator.")

#Define function for exception handling.
def float_input(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("You must enter a number!")
        else:
            break

#Declare variables.        
rangeLower = float_input("Enter your Lower range: ")
rangeHigher = float_input("Enter your Higher range: ")
n1 = float_input("Enter your First number: ")
n2 = float_input("Enter your Second number: ")

sum = 0
diff = 0
product = 0
quotient = 0

#Define arithmetic functions. 
def add(n1, n2):
    sum = n1 + n2
    print(n1,"+",n2,"=", sum)
    return sum

def sub(n1, n2): 
    diff = n1 - n2
    print(n1,"-",n2,"=", diff)
    return diff

def mult(n1, n2):
    product = n1 * n2
    print(n1,"*",n2,"=", product)
    return product

def div(n1, n2):
    if n2 == 0:
        print(n1,"/",n2,"= You cannot divide by Zero")
    else:
        quotient = n1 / n2
        print(n1,"/",n2,"=", quotient)
        return quotient

def allInOne(n1, n2):
    res = {"add": sum, "sub": diff, "mult": product, "div": quotient}
    for Item in res.keys():
        print(item)

#Declare variable for menu counter.
menuSelection = 0

#While statement to loop menu.
while menuSelection != 6:
    #Declare a list to store the menu items.
    menuList = ["1. Press 1 for Addition.", "2. Press 2 for Subtraction.", "3. Press 3 for Multiplication.", "4. Press 4 for Division.", "5. Press 5 for All in one.", "6. Press 6 to exit."]
    #Loop through items in list.
    for item in menuList:
        print(item)
    #Get user input for menu selection.
    menuSelection = int(input())
    if menuSelection == 1:
        sum(n1, n2)
    elif menuSelection == 2:
        sub(n1, n2)
    elif menuSelection == 3:
        mult(n1, n2)
    elif menuSelection == 4:
        div(n1, n2)
    elif menuSelection == 5:
        allInOne(n1, n2)
    elif menuSelection == 6:
        exit
