from operations import display, markSheet
import read
while True:
    print(f"1.Display student details\n2.Generate Marks\n3.Exit")
    try:
        userChoice = int(input("Enter your choice >> "))
        if userChoice == 1:
            display()
        elif userChoice == 2:
            markSheet(read.listValue())
        elif userChoice == 3:
            print("Thank you for using the program!!")
            break
    except:
        print("Invalid Input, Please enter number only")