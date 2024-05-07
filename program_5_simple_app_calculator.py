#  Display the welcome message and options
print("\033[38;5;208mSimple Calculator App\n\033[0m")
print("Choose one of the four math operations:")
print("\033[96m1. Addition\033[0m")
print("\033[92m2. Subtraction\033[0m")
print("\033[93m3. Multiplication\033[0m")
print("\033[95m4. Division\n\033[0m")

#  Loop for the calculator functionality
while True:
    # Prompt user to enter their choice of operation
    while True:
        try:
            operation = int(input("Please enter the operation you want to use (1 to 4): "))
            if operation in [1, 2, 3, 4]:
                break
            else:
                print("\033[91mInvalid input! Please enter a number between 1 and 4.\n\033[0m")
        except ValueError:
            print("\033[91mInvalid input! Please enter a valid number.\033[0m")

    #  Prompt user to enter the first number
    while True:
        try:
            first_number = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("\033[91mValueError: Invalid input! Please enter a valid number\033[0m")

        #  Prompt user to enter the second number
        while True:
            try:
