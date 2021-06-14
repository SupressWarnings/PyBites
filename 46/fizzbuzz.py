def fizzbuzz(num):
    if num % 3 != 0 and num % 5 != 0:
        return num
    solution = ""
    if num % 3 == 0:
        solution += "Fizz "
    if num % 5 == 0:
        solution += "Buzz"
    return solution.strip(" ")
