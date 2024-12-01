"""
Q) Find area and parameter of rectangle,
ask inout form user and show variable data 
types too

Method used:
input(): to take input from user
print(): To print value;
type(): To print datatype
"""

#length variable and converting it into int
length = float(input("Enter length : "))

#breadth variable and converting it into int
breadth = float(input("Enter breadth : "))

#calcuation of area and converting it into string
area = str(length*breadth)

#calcualtion of parameter
parameter = str(2*(length+breadth))

#printing Datatype of given variables
print("DataType of length: ",type(length), "DataType of breadth: ", type(breadth))

#printing area and parameter
print("The area is ", area)
print("The parameter is ", parameter)