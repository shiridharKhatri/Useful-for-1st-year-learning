import read
from datetime import datetime
def display():
    listVal = read.listValue()
    head = listVal[0]
    print('\n')
    print('~'*91)
    print(f'| {'SNo.':^12} | {head[0].upper():^12} | {head[1].upper():^12} | {head[2].upper():^12} | {head[3].upper():^12} | {head[4].upper():^12} |')
    print('~'*91)
    for i in range(1, len(listVal)):
        print(f"| {i:^12} | {listVal[i][0]:^12} | {listVal[i][1]:^12} | {listVal[i][2]:^12} | {listVal[i][3]:^12} | {listVal[i][4]:^12} |")
    print('~'*91)
    print('\n')
    
def markSheet(list2D):
    while True:
        try:
            studentData = []
            display()
            studentId = int(input("Enter id of a student >> "))
            if len(studentData) <=0:
                studentData.append({
                    "name":list2D[studentId][0],
                    "maths":list2D[studentId][1],
                    "physics" : list2D[studentId][2],
                    "chemistry":list2D[studentId][3],
                    "english":list2D[studentId][4]
                }) 
            nextChoice = input("Do you want to add more (yes/y/no/n)} >> ")
            if nextChoice.upper() == "YES" or nextChoice.upper() == "Y":
                studentId = int(input("Enter id of a student >> "))
                studentData.append({
                    "name":list2D[studentId][0],
                    "maths":list2D[studentId][1],
                    "physics" : list2D[studentId][2],
                    "chemistry":list2D[studentId][3],
                    "english":list2D[studentId][4]
                })
                for elems in studentData:
                    print(f"\nName:{elems['name']}\nMaths:{elems['maths']}\nPhysics:{elems['physics']}\nChemistry:{elems['chemistry']}\nEnglish:{elems['english']}\n{'='*20}\n")
            elif nextChoice.upper() == "NO" or nextChoice.upper() == "N":
                break
            else:
                print("Please choose yes or no only")
        except:
            print("Invalid input, please enter id in number only")
