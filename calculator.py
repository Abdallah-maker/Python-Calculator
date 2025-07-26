def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        return "Exception: Division cannot be done by zero"
    return x / y

def mul(x, y):
    return x * y

def mod(x, y):
    return x % y

def calculator():
    print("Welcome to STRA-Calculator")

    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Modulo")
    print("6. Exit")

    while True:
        choice = input("\nChoose option from 1-6: ")

        if choice == '6':
            print("Exiting in peace. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid value input. Please enter numbers only.")
            continue

        if choice == '1':
            print("Addition is:", add(num1, num2))
        elif choice == '2':
            print("Subtraction is:", sub(num1, num2))
        elif choice == '3':
            print("Division is:", div(num1, num2))
        elif choice == '4':
            print("Multiplication is:", mul(num1, num2))
        elif choice == '5':
            print("Modulo is:", mod(num1, num2))
        else:
            print("Invalid option. Please select between 1 and 6.")

# Run the calculator
calculator()