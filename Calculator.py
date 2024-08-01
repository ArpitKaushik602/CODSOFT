def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("-----------------")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Prompt user for choice
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        # Prompt user for input numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the calculation based on the choice
        if choice == '1':
            result = add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "division"

        # Display the result
        print(f"The result of {operation} of {num1} and {num2} is: {result}")

        # Ask if the user wants to perform another calculation
        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting calculator. Have a great day!")
            break

if __name__ == "__main__":
    main()
