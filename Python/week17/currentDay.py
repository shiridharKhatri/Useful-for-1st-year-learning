days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
while True :
    message = ""
    weekDay = input("Enter current week day >> ")
    for day in days:
        if weekDay.upper() == "SATURDAY" :
            message  = "Enjoy your weekend!"
        elif weekDay.upper() == day.upper() :
            message = "Happy weekday! work hard!"
            break
        else :
            message = "Invalid weekday!" 
    print(message)
