'''
WAP to find hcf of two number and exit on user request only!!
Algorithm
Step 1: Start
Step 2: Display 1.Run program
                2.Exit
Step 3: Input value x
Step 4: If x is equals the  go to step 5, 
        If x is equals 2 then go to step 2 again with
        message "Invalid user choice"
step 5: 
    step 5.1: input number num1 and num2
    step 5.2: if num2 > then num1 then swap num 2 and num 1
    step 5.3: Calculate rem * num1 mod num2
    step 5.4: If rem not equals o then,
              num1 = num2 and num2 =rem
              return to step 5.3
              otherwise, Diaplay "The HCF is ",  num2
              return to step 2
step 6: Display "Invalid choice: " return to step 2
step 7: Display 'Thank you for using program'
Step 8: END
'''

#python code for the above algorithm

while True:
        print('''
        1. Run Program
        2. Exit
        ''')
        try:
                choice = int(input("Enter your choice >> "))
                if choice == 1:
                        num1 = int(input("Enter the greater number >> " ))
                        num2 = int(input("Enter the second number >> " ))
                        if num2 > num1:
                                num1, num2 = num2, num1 
                        success = True
                        while success:
                                rem = num1 % num2
                                if rem != 0 :
                                        num1, num2 = num2, rem
                                        continue
                                else:
                                        print("The HCF is ",num1)
                                        success = False
                elif choice == 2:
                        print("Thank you for using program")
                        break
                else:
                        print("Invalid choice, select 1 and 2 only!")
        except:
                print("Invalid input format")
