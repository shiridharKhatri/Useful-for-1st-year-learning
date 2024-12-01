numbersList = []

def maxNumber(array):
    max = array[0]
    for i in range(1, len(array)):
        if max < array[i]:
            max = array[i]
    return max
    
def minNumber(array):
    min = array[0]
    for i in range(1, len(array)):
        if min > array[i]:
            min = array[i]
    return min

while True:
    try:
        nNumber = int(input("Enter N number >> "))
        for num in range(nNumber):
            while True:
                inputNum = int(input("Enter "+ str(num + 1 ) + " number >> "))
                try:
                    numbersList.append(inputNum)
                except:
                    print("Please enter valid input")
                break
        # print("Max number is : ",  maxNumber(numbersList, len(numbersList)))
        print("Max number is : ",  maxNumber(numbersList))
        print("Min number is : ",  minNumber(numbersList))
        break
    except:
        print("Please enter valid input")

