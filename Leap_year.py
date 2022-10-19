# Leap year TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def determine_amount_days_month(month, year):
    if 1 <= month <= 12 and year > 45:    # Julian calendar was invented in 45 year ad
        if month == 4 or month == 6 or month == 9 or month == 11:
            msg = f"30"
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                msg = f"29"
            else:
                msg = f"28"
        else:
            msg = f"31"
    else:
        msg = f"Invalid data"
    return (msg)


def determine_month(month):
    if 1 <= month <= 12:
        if month == 1:
            msg = f"January"
        elif month == 2:
            msg = f"February"
        elif month == 3:
            msg = f"March"
        elif month == 4:
            msg = f"Aril"
        elif month == 5:
            msg = f"May"
        elif month == 6:
            msg = f"June"
        elif month == 7:
            msg = f"July"
        elif month == 8:
            msg = f"August"
        elif month == 9:
            msg = f"September"
        elif month == 10:
            msg = f"October"
        elif month == 11:
            msg = f"November"
        else:
            msg = f"December"
    else:
        msg = f"Invalid data"
    return(msg)

def main ():
    month = int(input("Input month's number: "))
    year = int(input("Input year: "))

    day = determine_amount_days_month(month, year)

    month_name = determine_month(month)

    msg = f"{day} day(s) in {month_name} of {year} year"

    print(msg)

main()