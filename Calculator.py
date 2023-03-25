#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      swast
#
# Created:     25/03/2023
# Copyright:   (c) swast 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Mini project (building a calculator)
def calculus():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("Which mathematical operation would you like to perform?")
    calculation=str(input("Press + for addition, - for substraction,* for multiplication, / for division ,% for remainder,** for power."))
    if calculation== "+":
        print("Sum of the numbers is:" + str(a+b))
    elif calculation=="-":
        print("Substraction of the numbers is:" + str(a-b))
    elif calculation=="*":
        print("Multiplication of the numbers is:" +str(a*b))
    elif calculation=="/":
        print("Division of the numbers is:" + str(a/b))
    elif calculation=="%":
        print("Remainder of the two numbers is:"+ str(a%b))
    elif calculation=="**":
        print("The raised to the power of the given numbers is:"+ str(a**b))
    else:
        print("Enter the correct mathematical operator!")
    que=str(input("Do you want to continue?y/n"))
    if que=="y":
        calculus()
    else:
        print("The calculation is complete.")
calculus()



