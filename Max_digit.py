def get_max(numbers):
    max_num = numbers[0]
    if len(numbers) == numbers.count(numbers[0]):
        max_num = -1
    else:
        for element in numbers:
            if element > max_num:
                max_num = element

    return max_num


def main():
    ls = []
    for i in range(4):
        number = int(input(f"Input number {i + 1}: "))
        ls.append(number)

    result = get_max(ls)

    msg = f"All numbers are equal." if result == -1 else f"The maximum number is {result}."

    print(msg)


main()
