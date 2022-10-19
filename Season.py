# SEASON OF THE YEAR TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group


def display_year_season(num):

    if 1 <= num <= 12:
        if num <= 2 or num == 12:
            msg = f"WINTER"
        elif 3 <= num <= 5:
            msg = f"SPRING"
        elif 6 <= num <= 8:
            msg = f"SUMMER"
        else:
            msg = f"AUTUMN"
    else:
        msg = f"Invalid num!!! Input num from 1 to 12"
    return (msg)


def main():
    num = int(input("Input a month's number: "))

    msg = display_year_season(num)

    print(msg)


main()
