def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    should_accumulate = True
    number_1 = float(input("Enter your starting number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Which operation would you like to use?: ")
        number_2 = float(input("Enter the number to calculate with: "))
        answer = operations[operation_symbol](number_1, number_2)
        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        choice = input(f"Enter 'y' to keep going with {answer}, or 'n' to begin fresh: ")

        if choice == "y":
            number_1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()