while True:
    try:
        num = int(input("Enter a number!"))
        print(num, " is an integer")
        break
    except ValueError:
        print("Please type a valid number!")

