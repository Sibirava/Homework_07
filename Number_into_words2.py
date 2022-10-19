# Number of strings into words TASK
# Version 1.1.1, 09.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def count_number_string(number):
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    word1 = ""
    word2 = ""
    word3 = ""
    if 0 <= number <= 999:
        if digit1 == 1:
            word1 = "сто"
        elif digit1 == 2:
            word1 = "двести"
        elif digit1 == 3:
            word1 = "триста"
        elif digit1 == 4:
            word1 = "четыреста"
        elif digit1 == 5:
            word1 = "пятьсот"
        elif digit1 == 6:
            word1 = "шестьсот"
        elif digit1 == 7:
            word1 = "семьсот"
        elif digit1 == 8:
            word1 = "восемьсот"
        elif digit1 == 9:
            word1 = "девятьсот"
        else:
            word1 = word2
            if digit2 == 2:
                word2 = "двадцать"
            elif digit2 == 3:
                word2 = "тридцать"
            elif digit2 == 4:
                word2 = "сорок"
            elif digit2 == 5:
                word2 = "пятьдесят"
            elif digit2 == 6:
                word2 = "шестьдесят"
            elif digit2 == 7:
                word2 = "семьдесят"
            elif digit2 == 8:
                word2 = "восемьдесят"
            elif digit2 == 9:
                word2 = "девяноста"
            elif digit2 == 1:
                if digit3 == 0:
                    word2 = "десять"
                elif digit3 == 1:
                    word2 = "одиннадцать"
                elif digit3 == 2:
                    word2 = "двенадцать"
                elif digit3 == 3:
                    word2 = "тринадцать"
                elif digit3 == 4:
                    word2 = "четырнадцать"
                elif digit3 == 5:
                    word2 = "пятнадцать"
                elif digit3 == 6:
                    word2 = "шестнадцать"
                elif digit3 == 7:
                    word2 = "семнадцать"
                elif digit3 == 8:
                    word2 = "восемнадцать"
                elif digit3 == 9:
                    word2 = "девятнадцать"
            if digit2 == 0 or digit2 != 1:
                if digit3 == 1:
                    word3 = "один"
                elif digit3 == 2:
                    word3 = "двa"
                elif digit3 == 3:
                    word3 = "три"
                elif digit3 == 4:
                    pword3 = "четыре"
                elif digit3 == 5:
                    word3 = "пять"
                elif digit3 == 6:
                    word3 = "шесть"
                elif digit3 == 7:
                    word3 = "семь"
                elif digit3 == 8:
                    word3 = "восемь"
                elif digit3 == 9:
                    word3 = "девять"
            else:
                word3 = "ноль"
    else:
        print("Wrong number")
    return (word1, word2, word3)


def main():
    number = int(input("Please enter your number: "))

    word1, word2, word3 = count_number_string(number)
    print("The number of the string is:{} {} {}".format(word1, word2, word3))


main()
