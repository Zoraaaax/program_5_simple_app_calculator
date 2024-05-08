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
            print("\033[91mValueError: Invalid input! Please enter a valid number\033[0m.")

        #  Prompt user to enter the second number
        while True:
            try:
                second_number = float(input("Please enter the second number: "))
                if operation == 4 and second_number == 0:
                    print("\033[91mZeroDivisionError: Division by zero is not allowed.\033[0m")
                    continue
                break
            except ValueError:
                print("\033[91mValueError: Invalid input! Please enter a valid number.\033[0m")

        #  Perform the selected operation and display the result
        try:
            if operation == 1:
                result = first_number + second_number
                print(f"\033[96mThe result of addition is {int(result) if result.is_integer() else result}\033[0m")
            elif operation == 2:
                result = first_number - second_number
                print(f"\033[92mThe result of subtraction is{int(result) if result.is_integer() else result}\033[0m")
            elif operation == 3:
                result = first_number * second_number
                print(f"\033[93mThe result of multiplication is {int(result) if result.is_integer() else result}\033[0m")
            elif operation == 4:
                result = first_number / second_number
                print(f"\033[95mThe result of division is {int(result) if result.is_integer() else result}\033[0m")
        except ZeroDivisionError:
            print("\033[91mZeroDivisionError: Division by zero is not allowed.\033[0m")
        except Exception as exception:
            print("\033[91mAn unexpected error occurred:\033[0m", exception)

        print()

        #  Ask user if they want to try again
        while True:
            try:
                try_again = input("Do you want to try again (y/n)? ").lower()
                if try_again in ['y', 'n']:
                    break
