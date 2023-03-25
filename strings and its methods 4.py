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
#s & its m part 4
#using replace method
identity="Swasthani Shrestha"
print(identity.replace("Swasthani", "Juliain"))
print(identity.replace("Juliain","Julie")) #doesnot work because it can only alter the original value inside the variable
print(identity.replace("Swasthani","Ariana")) #replaces the first string that is in the braces with the second in the braces.