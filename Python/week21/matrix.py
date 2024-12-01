a = [[24,3,6],[8,12,18],[2,66,7]]
value = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] % 2 == 0 and a[i][j] % 3 == 0:
            value.append(a[i][j])
print("Divisible by 2 and 3 number : ", value)
print("Max value is : ", max(value))
print("min value is : ", min(value))
