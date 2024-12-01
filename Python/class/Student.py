"""
Class : Student
Instance variable : name:str, maths:int, science:int, english:int
Methods / Functions = getLastName:str, avgMarks:float
"""

# Create the student class 
class Student:
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    # Returns the last name from the name
    def getLastName(self):
            lastName = self.name.split()[-1]
            return lastName

    # Returns the last name from the name
    def avgMarks(self):
            return (self.maths+self.science+self.english)//3

s1 = Student("Harry Potter", 80,80,80)
print(s1.getLastName()) 
print(s1.avgMarks())