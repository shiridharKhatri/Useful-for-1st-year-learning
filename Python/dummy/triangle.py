stars = []
newNumber = []
rangeNum = 0
while True:
    try:
        inputVal = int(input("Enter number >> "))
        stars.append(inputVal)
        rangeNum+=1
        if rangeNum == len(stars):
            while True:
                cont = int(input("Do you want to continue? >> "))
                if cont == 0 or cont == 1:
                    if cont == 0 :
                        print("Thank you!")
                        break
                    else:
                        inputValTwo = int(input("Enter number >> "))
                        rangeNum+=1
                        stars.append(inputValTwo)
                else:
                    print('Please enter option 1 and 0 only 🙂')
        for strs in stars:
            if strs % 2 != 0 :
                newNumber.append(strs)
        print("Odd numbers are : ", newNumber)
        break
    except:
        print("Invalid input format please enter valid input : ")