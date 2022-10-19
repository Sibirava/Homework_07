#Gregarian calender Task
#Version 1.1.1, 11.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def count_date(day, month, year):
    day1 = day
    month1 = month
    year1 = year

    if (month == 1 or month == 3 or month == 5 or month == 7
            or month == 8 or month == 10):
        if 1 <= day < 31:
            month1, day1, year1 = (month, day + 1, year)
        else:
            month1, day1, year1 = (month + 1, 1, year)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day < 30:
            month1, day1, year1 = (month, day + 1, year)
        elif day == 31:
            print("Wrong day number")
        else:
            month1, day1, year1 = (month + 1, 1, year)
    elif month == 2 and (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if 1 <= day < 29:
            month1, day1, year1 = (month, day + 1, year)
        elif 30 <= day <= 31:
            print("Wrong day number")
        else:
            month1, day1, year1 = (month + 1, 1, year)
    elif month == 2 and year != ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        if 1 <= day < 28:
            month1, day1, year1 = (month, day + 1, year)
        elif 29 <= day <= 31:
            print("Wrong day number")
        else:
            month1, day1, year1 = (month + 1, 1, year)
    else:
        if 1 <= day < 31:
            month1, day1, year1 = (month, day + 1, year)
        else:
            month1, day1, year1 = (1, 1, year + 1)
    return (day1, month1, year1)


def main():
    day = int(input("Input day: "))
    month = int(input("Input month: "))
    year = int(input("Input year: "))

    day1, month1, year1 = count_date(day, month, year)

    if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
        msg = f"Your date is {day} {month} {year}. The next date is:{day1} {month1} {year1} "
    else:
        msg = f"Wrong date"

    print(msg)


main()
