import math

"""
Giving input of three number inputOne, inputTwo and inputThree.
Find value of x 
"""

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

eqOne = -b
eqTwo = b**2-4*a*c
eqThree = 2*a
eqFour = math.sqrt(eqTwo)

firstX = (eqOne + eqFour)/eqThree
secondX = (eqOne - eqFour)/eqThree

print("The first value of x is ",firstX)
print("The second value of x is ",secondX)