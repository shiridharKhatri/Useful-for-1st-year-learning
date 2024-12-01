
odd = []
even=[]
oddCal = 0
evenCal = 0
while True :
    try:
        nNumber = int(input("Enter N number >> "))
        for number in range(nNumber):
            while True:
                try:
                    inputNum = int(input("Enter "+ str(number + 1 ) + " number >> "))
                    if inputNum % 2 == 0:
                        even.append(inputNum)
                    else:
                        odd.append(inputNum)
                    break
                except:
                    print("Please enter valid input")
        for oddNum in odd:
            oddCal+=oddNum
        for evenNum in even:
            evenCal+=evenNum
        print("Odd number sum is : ", oddCal)
        print("Even number sum is : ", evenCal)
        break
    except:
        print("Please enter valid input")
