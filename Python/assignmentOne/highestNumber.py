"""
Take 3 num from the user and print the highest value among 3 nums
Algorithm: 
Step 1: Start 
Step 2:Display 1.Run Program 
               2.Exit 
Step 3: Input choice
Step 4: if choice equals 1 then,Goto step 5 Otherwise 
        if choice equals 2 then, Goto step 7 Otherwise, 
        Display 'Invalid Choice' and return to Step 2 
Step 5: input num1, num2, num3 from user 
Step 6: 
    6.1 if num1 >= num2 and num3 display' num1 is greater' 
    6.2 if num2 >= num1 and num3 display' num2 is greater' else  diaplay num3 is greater
    6.3 return to step 2 
Step 7: show display 'Thank You' 
Step 8: Stop


Method used:
input(): to take input from user
print(): To print value;
"""


while True:
    print('''
        1. Run Program
        2. Exit
        ''')
    try:
        choice = int(input("Enter choice 1 or 2 only >> "))
        if choice == 1 :
            num1 = int(input("Enter first num >> "))
            num2 = int(input("Enter second num >> "))
            num3 = int(input("Enter third num >> "))
            if num1 == num2 == num3:
                print("All the nums are equal")
            elif num1 >= num2 and num1 >= num3:
                print(num1, "is the highest num")
            elif num2 >= num1 and num2 >= num3:
                print(num2, "is the highest num")
            else:
                print(num3, "is the highest num")
        elif choice == 2:
            print("Thank you for using program")
            break
        else:
            print("Invalid choice, select 1 and 2 only!")
    except:
        print("Invalid input format")