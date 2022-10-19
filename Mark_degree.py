# Mark degree task
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def display_mark_message(mark):

    if 0 <= mark <= 10:
        if mark <= 1:
            msg = f"very bad"
        elif mark == 2 or mark == 3:
            msg = f"unsatisfactory"
        elif mark == 4:
            msg = f"satisfactory"
        elif mark == 5 or mark == 6:
            msg = f"not bad"
        elif mark == 7 or mark == 8:
            msg = f"good"
        else:
            msg = f"excellent"
    else:
        msg = f"Invalid mark!!!"

    return(msg)


def main():
    mark = int(input("Input your mark: "))

    msg = display_mark_message(mark)

    print(msg)


main()
