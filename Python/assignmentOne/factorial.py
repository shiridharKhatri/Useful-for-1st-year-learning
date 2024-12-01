"""
WAP to find factorial of a number given by user and exit on user request only!!
Algorithm
Step 1: Start
Step 2: Display 1.Run program
                2.Exit
Step 3: Input value x
Step 4: If x is equals the  go to step 5, 
        If x is equals 2 then go to step 2 again with
        message "Invalid user choice"
step 5: 
    step 5.1: input number num
    step 5.2: if num is less then or equal to 0 then go to step 5.1
              with message "Please enter value greater then 0", if not go to step 5.3
    step 5.3: Create variable name factorialValue with value 1
    step 5.4: Start a loop  from 1 to factorialValue and multiply factorialValue by i + 1 and assign the result 
              back in factorialValue and display the result
step 6: Display 'Thank you for using program'
Step 7: END
"""

while True :
    print('''
        1. Run Program
        2. Exit
        ''')
    try:
        choice = int(input("Enter choice 1 or 2 only >> "))
        if choice == 1 :
            while True:
                num = int(input("Enter any number here >> "))
                if num <= 0 :
                    print("Invalid value! Please enter value greater then zero")
                else:
                    factorialValue = 1
                    for i in range(num):
                        factorialValue*=i+1
                    print(factorialValue)
                    break
        elif choice == 2:
            print("Thank you for using program")
            break
        else:
            print("Invalid choice, select 1 and 2 only!")
    except:
        print("Invalid input format")