import string

VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for character in input_str:
        if character.lower() not in VOWELS:
            print(character.lower())
            return False
    return True


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for character in input_str:
        if character.lower() in PYTHON:
            return True
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for character in input_str:
        if character in string.digits:
            return True
    return False
