while True:
    try:
        number = int(input("Enter any number : "))
        if number % 2 == 0 :
            print(number, " Is odd number")
        else:
            print(number, " Is even")
        break
    except:
        print("Invalid input format")