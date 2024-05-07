#  Display the welcome message and options
print("\033[38;5;208mSimple Calculator App\n\033[0m")
print("Choose one of the four math operations")
print("\033[96m1. Addition\033[0m")
print("\033[92m2. Subtraction\033[0m")
print("\033[93m3. Multiplication\033[0m")
print("\033[95m4. Division\033[0m")

#  Loop for the calculator functionality
while True:
    # Prompt user to enter their choice of operation
    while True:
        try:
            operation = int(input("Please enter the operation you want to use (1 to 4): "))
