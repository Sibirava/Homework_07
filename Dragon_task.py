# DRAGON TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

FIRST_PERIOD = 200
SECOND_PERIOD = 100


def calculate_dragon_head(age):
    if age < 1:
        return -1
    else:
        head = 3
        if age <= FIRST_PERIOD:
            head += age * 3
        elif age <= SECOND_PERIOD:
            head += FIRST_PERIOD * 3 + (age - FIRST_PERIOD) * 2
        else:
            head += (FIRST_PERIOD * 3 + (SECOND_PERIOD - FIRST_PERIOD) * 2
                     + age - SECOND_PERIOD)
        return head


def main():
    age = int(input("Input the dragon's age: "))

    head = calculate_dragon_head(age)

    msg = f"your dragon has {head} heads and {head * 2} eyes" if head > 0 else "Error age!!!"

    print(msg)


main()
