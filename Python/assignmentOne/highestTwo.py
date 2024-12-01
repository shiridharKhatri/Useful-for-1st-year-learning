"""
Take 3 number from the user and print the highest value among three numbers

Method used:
input(): to take input from user
print(): To print value;
"""

while True:
    try:
        numberOne = int(input("Enter first number >> "))
        numberTwo = int(input("Enter second number >> "))
        numberThree = int(input("Enter third number >> "))
        if numberOne == numberTwo == numberThree:
            print("All the numbers are equal")
        elif numberOne >= numberTwo and numberOne >= numberThree:
            print(numberOne, "is the highest number")
        elif numberTwo >= numberOne and numberTwo >= numberThree:
            print(numberTwo, "is the highest number")
        else:
            print(numberThree, "is the highest number")
        break
    except:
        print("Invalid input format")