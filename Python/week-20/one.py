
"""
ALGORITHM one
    input List
    while true
        numSwap = 0
        for i = 0 to list.count - 1
            if listVal[i] > listVal[i+1] then
                    temp = listVal[i]
                    listVal[i] = listVal[i+1]
                    listVal[i+1] = temp
                    numSwap = numSwap + 1
            end if
        end for
        if numSwap equals 0 then
            break
        end if
    end while
display output
end one
"""
listVal = ["ram",]
listVal = [1,3,5,2,3,8,9,10,32,12]
while True:
    numSwap = 0
    for i in range(len(listVal)-1):
        if listVal[i] < listVal[i+1]:
            listVal[i], listVal[i+1] = listVal[i+1], listVal[i]
            numSwap +=1
    if numSwap == 0:
            break
print(listVal)

# listVal = [1,3,5,2,3,8,9,10,32,12]
# sorted = False
# while True:
#     numRange = 0
#     for i in range(1, len(listVal)):
#         if listVal[i-1] > listVal[i]:
#             listVal[i-1], listVal[i] = listVal[i], listVal[i-1]
#             numRange +=1
#         if numRange == 0:
#             sorted = True
#         else:
#             sorted = False
# print(listVal)
