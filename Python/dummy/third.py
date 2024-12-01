"""
Q)Write a program that computes the value of the algebric exoression
x**3+3x**2y+3xy**2+y**3

Method used:
print(): To print value;
"""

#variables
x = 1
y=1

#solution
expressionOne = x**3
expressionTwo = 3*(x**2*y)
expressionThree = 3*(x*y**2)
expressionFor = y**3
solution = str(expressionOne+expressionTwo+expressionThree+expressionFor)


#Printing value
print("The solution is ", solution)
