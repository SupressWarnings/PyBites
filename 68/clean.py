import re


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub(
        pattern="\!|\"|\#|\$|\%|\&|'|\(|\)|\*|\+|\,|\-|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\\\|\]|\^|\_|\`|\{|\||\}|\~",
        repl="",
        string=input_string,
    )
