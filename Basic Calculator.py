def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def exponentiate(n1, n2):
    return n1 ** n2

def modulus(n1, n2):
    if n2 == 0:
        return "Error: Modulus by zero is not allowed."
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponentiate,
    "%": modulus
}

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation. Please select a valid operator.")
            continue

        while True:
            try:
                num2 = float(input("Enter the next number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        answer = operations[operation_symbol](num1, num2)
        print(f"\nResult: {num1} {operation_symbol} {num2} = {answer}")

        next_action = input(
            "Type 'y' to continue with this result, 'n' to start a new calculation, or 'q' to quit: ").lower()

        if next_action == "y":
            num1 = answer
        elif next_action == "n":
            calculator()
        else:
            print("Goodbye!")
            break

calculator()
