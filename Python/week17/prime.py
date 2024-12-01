try:
    number = int(input("Enter any one number >> "))
    if number > 1:
        i = 2
        while i <= number // 2:
            if number % i == 0:
                print("It is not a prime number")
                break
            i += 1
        else:
            print("It is a prime number")
    else:
        print("It is not a prime number")
except :
    print("Invalid input format!")
