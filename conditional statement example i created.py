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
#conditional statements
#give input and check the codn if it matches the condition then displays the result.
age=int(input("Enter your age:"))
if age>20: #in c++ and java the condn inside if else condn is written inside curly braces whereas in python, only indentation
    print("Allowed to legally buy the desired medical product.")#is required after colon
    print("Please checkout in the fifth station to proceed.")
elif age<20: #it NEEDS condition without condn it doesnot work even if it seems like the opposite of the condn in if would work.
    print("Not allowed to buy the desired product.")
    ans=str(input("Do you have medical pescription?y/n"))
    if ans=="y": #again indentation is needed in cases like this where if can be held inside elif when there are multiple condns inside a single condn
        print("Please checkout in the third station to proceed.")
    else: #it DOESNOT need a condn otherwise the loop doesnt run here! NEVER put a condn on this condn.Only executes if all the loops that has the
        #same starting indentation as this is false.
        print("The exit is at the right.")
print("Thank you!") #prints however cause its not inside the loop.
