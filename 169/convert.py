def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) is not float and type(value) is not int:
        raise TypeError
    if fmt.lower() != "cm" and fmt.lower() != "in":
        raise ValueError
    return round(value * (2.54 if fmt.lower() == "cm" else 0.39370079), 4)
