# Number into words + year TASK
# Version 1.1.1, 09.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def count_hundreds(number):
    digit1 = number // 100

    if 1 <= number <= 120:
        if digit1 == 1:
            print("сто")
        else:
            print("")
    else:
        return
    return (digit1)


def count_dozens(number):
    digit2 = (number // 10) % 10
    digit3 = number % 10

    if 1 <= number <= 120:
        if digit2 == 2:
            print("двадцать")
        elif digit2 == 3:
            print("тридцать")
        elif digit2 == 4:
            print("сорок")
        elif digit2 == 5:
            print("пятьдесят")
        elif digit2 == 6:
            print("шестьдесят")
        elif digit2 == 7:
            print("семьдесят")
        elif digit2 == 8:
            print("восемьдесят")
        elif digit2 == 9:
            print("девяноста")
        elif digit2 == 1:
            if digit3 == 0:
                print("десять")
            elif digit3 == 1:
                print("одиннадцать")
            elif digit3 == 2:
                print("двенадцать")
            elif digit3 == 3:
                print("тринадцать")
            elif digit3 == 4:
                print("четырнадцать")
            elif digit3 == 5:
                print("пятнадцать")
            elif digit3 == 6:
                print("шестнадцать")
            elif digit3 == 7:
                print("семнадцать")
            elif digit3 == 8:
                print("восемнадцать")
            elif digit3 == 9:
                print("девятнадцать")
        if digit2 == 0 or digit2 != 1:
            if digit3 == 1:
                print("один")
            elif digit3 == 2:
                print("двa")
            elif digit3 == 3:
                print("три")
            elif digit3 == 4:
                print("четыре")
            elif digit3 == 5:
                print("пять")
            elif digit3 == 6:
                print("шесть")
            elif digit3 == 7:
                print("семь")
            elif digit3 == 8:
                print("восемь")
            elif digit3 == 9:
                print("девять")
        else:
            print("")
    else:
        print("Wrong number")

    return (digit2, digit3)


def year_declension(digit2, digit3):
    if digit3 == 1:
        year = f"год"
    elif digit2 != 1 and (digit3 == 3 or digit3 == 4 or digit3 == 2):
        year = f"года"
    else:
        year = "лет"
    return (year)


def main():
    number = int(input("Input your number: "))

    digit1 = count_hundreds(number)

    digit2, digit3 = count_dozens(number)

    year = year_declension(digit2, digit3)

    if 1 <= number <= 120:
        print(year)
    else:
        print("")


main()
