# Determine multiplicity of number
# Version 1.1.1, 06.10.2022
# Created by Katiaryna Sibirava
# QA4822 group


def determine_multiplicity_number(n, m):

    if n % m == 0:
        msg = "n is multiple to m"
    else:
        msg = "n is NOT multiply to m"
    return(msg)

def main():
    n = int(input("Input n = "))
    m = int(input("Input m = "))

    msg = determine_multiplicity_number(n, m)
    print(msg)

main()
