from Calculator_Logo import logo

def add(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "*": multiplication,
    "-": subtract,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    choose_option = input("What would you like to perform? \n")
    num2 = float(input("Enter second number: "))
    cal_func = operations[choose_option]
    ans = cal_func(num1, num2)
    print(f"{num1} {choose_option} {num2} = {ans}")

    while True:
        c_or_ex = input(f"Type 'y' to calculating with continue {ans}, or type 'n' for exit, for restart type 'r': ")
        if c_or_ex == "y":
            op_symb = input("Choose the operation symbol: ")
            num3 = float(input("Enter the number: "))

            cal_func = operations[op_symb]
            ans2 = cal_func(ans, num3)

            print(f"{ans} {op_symb} {num3} = {ans2}")
            ans = ans2
        elif c_or_ex == "r":
            calculator()
        else:
            break


calculator()
