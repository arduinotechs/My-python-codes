import random
print("Welcome to Guess The Number!")
first = input("Type 'rules' to know the rules or type anything to continue without rules \n")
if first == "rules":
    print("This is Guess the Number")
    print("The program will randomly choose a number between 1 to 100")
    print("You have to type a number when asked and the program will check if your number matches the number exactly")
    print("If it matches you win or if it doesn't match it shows whether your number is lesser or greater than the "
          "random number")
    print("let's begin...\n")
else:
    print("Let's begin...")
while True:
    try:
        num = int(input("Enter a number!\n"))
        print(num, "is an integer")
        break
    except ValueError:
        print("Please type a valid number!")
unknown_integer = random.randrange(1, 101)
while num == unknown_integer:
    if num <unknown_integer:
