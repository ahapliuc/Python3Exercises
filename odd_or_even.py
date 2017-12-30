number=int(input("Give number please"))
if number % 2 == 0:
    print("The number is even")
    if number % 4 == 0:
        print("This number is a multiple of 4")
        exit()
    else:
        print("This number is not a multiple of 4")
        exit()
else:
    print("Number is odd")
    exit()