# quadratic equation
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

import math

def quadratic_equation(a, b, c):
    """a * x ^ 2 + b * x + c = 0"""
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = -b + math.sqrt(D) / (2 * a)
        x2 = -b - math.sqrt(D) / (2 * a)
        print("The quadratic equation has 2 roots {}, {}".format(round(x1, 2), round(x2, 2)))
    elif D == 0:
        x1 = -b / (2 * a)
        print("The quadratic equation has 1 root {}".format(round(x1, 2)))
    else:
        print("The quadratic equation has no roots")

    return(D)

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a == 0:
        x = -c / b
        print("The equation is linear and has one root {}".format(x))
    else:
        D = quadratic_equation(a, b, c)

main()
