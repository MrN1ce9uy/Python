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
n1 = float_input("Enter your First number: ")
n2 = float_input("Enter your Second number: ")

#Define arithmetic functions. 
def add(n1, n2):
    sum1 = n1 + n2
    print(n1,"+",n2,"=", sum1)

def sub(n1, n2): 
    diff = n1 - n2
    print(n1,"-",n2,"=", diff)

def mult(n1, n2):
    product = n1 * n2
    print(n1,"*",n2,"=", product)

def div(n1, n2):
    if n2 == 0:
        print(n1,"/",n2,"= You cannot divide by Zero")
    else:
        quotient = n1 / n2
        print(n1,"/",n2,"=", quotient)

def allInOne(n1, n2):
    #Store values in dictionary. 
    res = {"add": add(n1, n2), "sub": sub(n1, n2), "mult": mult(n1, n2), "div": div(n1, n2)}
    

#Declare variable for menu counter.
menuSelection = 0

#While statement to loop menu.
while menuSelection != 6:
    #Store menu items in a list.
    menuList = ["1. Press 1 for Addition.", "2. Press 2 for Subtraction.", "3. Press 3 for Multiplication.", "4. Press 4 for Division.", "5. Press 5 for All in one.", "6. Press 6 to exit."]
    #Loop through items in list.
    for item in menuList:
        print(item)
    #Get user input for menu selection.
    menuSelection = float(input())
    if menuSelection == 1:
        add(n1, n2)
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
