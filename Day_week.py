#DAY OF THE WEEK TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def define_day_week(num):

    if 1 <= num <= 7:
        if num == 1:
            msg = f"MONDAY"
        elif num == 2:
            msg = "TUESDAY"
        elif num == 3:
            msg = "WENSDAY"
        elif num == 4:
            msg = f"THURSDAY"
        elif num == 5:
            msg = f"FRIDAY"
        elif num == 6:
            msg = f"SATURDAY"
        else:
            msg = f"SUNDAY"
    else:
        msg = f"Invalid data. Input num from 1 to 7"
    return (msg)

def main():
    num = int(input("Input your number: "))

    msg = define_day_week(num)

    print(msg)

main()