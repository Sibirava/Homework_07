# Determine card's suit and value TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def define_card_suit(num1):

    if 1 <= num1 <= 4:
        if num1 == 1:
            msg = f"Spades"
        elif num1 == 2:
            msg = f"Clubs"
        elif num1 == 4:
            msg = f"Diamonds"
        else:
            msg = f"Hearts"
    else:
        msg = f"Wrong number. Please input num1 from 1 to 4"
    return(msg)

def determine_card_value(num2):
    if 2 <= num2 <= 15:
        if num2 == 2:
            msg = f"Two"
        elif num2 == 3:
            msg = f"Three"
        elif num2 == 4:
            msg = f"Four"
        elif num2 == 5:
            msg = f"Five"
        elif num2 == 6:
            msg = f"Six"
        elif num2 == 7:
            msg = f"Seven"
        elif num2 == 8:
            msg = f"Eight"
        elif num2 == 9:
            msg = f"Nine"
        elif num2 == 10:
            msg = f"Ten"
        elif num2 == 11:
            msg = f"Jack"
        elif num2 == 12:
            msg = f"Lady"
        elif num2 == 13:
            msg = f"King"
        elif num2 == 14:
            msg = f"Ace"
        else:
            msg = f"Joker"
    else:
        msg = f"Invalid data. Input num from 2 to 15"
    return(msg)

def main():
    num2 = int(input("Input num2: "))
    num1 = int(input("Input num1: "))

    card_value = determine_card_value(num2)
    card_suit = define_card_suit(num1)

    if num2 == 15:
        msg = f"Your card is {card_value}"
    else:
        msg = f"{card_value} of {card_suit}"

    print(msg)

main()