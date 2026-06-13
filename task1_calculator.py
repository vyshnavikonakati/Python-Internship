"""
Task 1: Simple Calculator (CLI)
"""

def calculator():
    print("=== Simple Calculator ===")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid operation.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    calculator()
