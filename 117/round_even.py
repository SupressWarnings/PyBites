def round_even(number):
    """Takes a number and returns it rounded even"""
    if number % 1 != 0.5:
        return round(number)
    else:
        return int(number / 1) if number % 2 < 1 else int(number / 1 + 1)
