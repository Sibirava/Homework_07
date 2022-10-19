# Calculator
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def calculator(x, y, action):
    result = 0

    if action == '+':
        result = x + y
    elif action == '-':
        result = x - y
    elif action == '*':
        result = x * y
    elif action == '%':
        if y != 0:
            result = x % y
        else:
            msg = f"Divide into zero "
    elif action == '/':
        if y != 0:
            result = x / y
        else:
            result = f"Divide into zero "
    else:
        result = f"Wrong action"
    return (result)


def main():
    action = input("Action('-', '+', '*', '/', '%'): ")

    x = float(input("x = "))
    y = float(input("y = "))

    result = calculator(x, y, action)

    print(result)


main()
