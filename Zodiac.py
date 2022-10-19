# Define zodiac sign
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def zodiaс_sign(month, day):
    zodiac = ""

    if month == 1 and 20 <= day <= 31 or month == 2 and 1 <= day <= 18:
        zodiac = f"Aquarius"
    elif month == 2 and 19 <= day <= 29 or month == 3 and 1 <= day <= 19:
        zodiac = f"Pisces"
    elif month == 3 and 20 <= day <= 31 or month == 4 and 1 <= day <= 19:
        zodiac = f"Aries"
    elif month == 4 and 20 <= day <= 30 or month == 5 and 1 <= day <= 20:
        zodiac = f"Taurus"
    elif month == 5 and 21 <= day <= 31 or month == 6 and 1 <= day <= 21:
        zodiac = f"Gemini"
    elif month == 6 and 22 <= day <= 30 or month == 7 and 1 <= day <= 22:
        zodiac = f"Cancer"
    elif month == 7 and 1 <= day <= 22 or month == 8 and 1 <= day <= 23:
        zodiac = f"Lion"
    elif month == 8 and 24 <= day <= 31 or month == 9 and 1 <= day <= 23:
        zodiac = f"Virgo "
    elif month == 9 and 24 <= day <= 30 or month == 10 and 1 <= day <= 22:
        zodiac = f"Libra"
    elif month == 10 and 23 <= day <= 31 or month == 11 and 1 <= day <= 22:
        zodiac = f"Sсorpio"
    elif month == 11 and 23 <= day <= 30 or month == 12 and 1 <= day <= 22:
        zodiac = f"Sagittarius"
    elif month == 12 and 23 <= day <= 31 and month == 1 and 1 <= day <= 19:
        zodiac = f"Capricorn"
    else:
        print("Wrong day")
        return (zodiac)


def main():
    day = int(input("Please input day:"))
    month = int(input("Please input month: "))

    zodiac = zodiaс_sign(day, month)

    if 12 >= month >= 1:
        print(zodiac)
    else:
        print("Wrong number of the month")


main()
