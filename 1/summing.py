def sum_numbers(numbers=None):
    sum = 0
    if numbers is not None:
        for number in numbers:
            sum += number
    else:
        sum = 50 * 101
    return sum
