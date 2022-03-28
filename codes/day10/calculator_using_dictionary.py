# from art import logo
# import replit

n1 = 0
n2 = 0


# Add
def add(n1, n2):
    return n1 + n2


# sub
def subtract(n1, n2):
    return n1 - n2


# mul
def multipy(n1, n2):
    return n1 * n2


# div
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multipy,
    "/": divide

}


def calculator():
    # print(logo)
    num1 = float(input("First Number: "))

    for operands in operations:
        print(operands)

    operation_symbol = input("Pick an operation: ")

    num2 = float(input("Second Number: "))
    # Step 1
    # answer = operations[operation_symbol](num1, num2)
    # or
    # step 2
    function = operations[operation_symbol]
    first_answer = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    should_continue = True
    while should_continue:
        choice = input(f"Type 'y' to continue with {first_answer}, or type 'n' to exit.: ")
        if choice != 'y':
            should_continue = False
            # clear()
            calculator()
        else:
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number?: "))

            calculation_function = operations[operation_symbol]

            second_answer = calculation_function(first_answer, num3)

            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


calculator()