# VOWEL OR CONSONANT LETTER TASK
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def define_letter(l):

    if len(l) == 1:
        if l == 'a' or l == 'e' or l == 'y' or l == 'u' or l == 'i' or l == 'o':
            msg = f"Letter is vowel"
        else:
            msg = f"Letter is consonant"
    else:
        msg = f"invalid data! You have to input only one letter"
    return(msg)

def main():
    l = str(input("Input letter: "))

    msg = define_letter(l)

    print(msg)

main()
