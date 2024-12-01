# Question one 
# lst = [43,23,21,44,56,75]
# lst2 = []
# for i in range(0,len(lst)-1,2 ):
#     lst2.append(lst[i+1])
# print(lst2)


# Question two 
# num = [1,2,3]
# alp = ["a", "b", "c"]
# combination = []
# for i in range(len(num)):
#     combination.append(num[i])
#     combination.append(alp[i])
# print(combination)


# Question three
# lstOne = [1,2,3,4,5,6]
# lstTwo = [1,2,3,4,5,6]
# lstSum = []
# for i in range(len(lstOne)):
#     lstSum.append(lstOne[i] + lstTwo[i])
# print(lstSum)


# Question two 
num = [1,2,3, 3, 6]
alp = ["a", "b", "c", "d", "e", "f", "f"]
combination = []

for i in range(len(num) if len(num) < len(alp) else len(alp)):
    combination.append(num[i])
    combination.append(alp[i])
remainingVal = 0
if len(alp) > len(num):
    for elems in alp:
        if elems not in combination:
            combination.append(elems)
else:
    for elems in num:
        if elems not in combination:
            combination.append(elems)
print(combination)