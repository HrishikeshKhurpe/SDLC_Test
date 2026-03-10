from calculator.calculator import Calculator


def display_menu():
    """Displays the calculator menu."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_user_choice():
    """Gets the user's operation choice."""
    return input("Enter choice(1/2/3/4/5): ")


def get_numbers():
    """Gets two numbers from the user."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None


def perform_calculation(calculator, choice, num1, num2):
    """Performs the calculation based on user's choice and prints the result."""
    operations = {
        "1": (calculator.add, "+"),
        "2": (calculator.subtract, "-"),
        "3": (calculator.multiply, "*"),
        "4": (calculator.divide, "/"),
    }

    if choice in operations:
        operation_func, operator_symbol = operations[choice]
        try:
            result = operation_func(num1, num2)
            print(f"{num1} {operator_symbol} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        # This case should not be hit due to the check in main(),
        # but it's good practice for function robustness.
        print("Invalid choice.")


def main():
    """Main function to run the calculator application."""
    calculator = Calculator()
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                perform_calculation(calculator, choice, num1, num2)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        print("-" * 20)


if __name__ == "__main__":
    main()
