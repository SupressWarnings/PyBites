ALPHANUM = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_index_different_char(chars):
    alnumerical = True
    if str(chars[0]) in ALPHANUM and str(chars[1]) in ALPHANUM:
        alnumerical = True
    elif str(chars[0]) not in ALPHANUM and str(chars[1]) not in ALPHANUM:
        alnumerical = False
    else:
        alnumerical = (str(chars[0]) in ALPHANUM) and (str(chars[2]) in ALPHANUM)

    for character in chars:
        if character == "":
            character = "#"
        if (str(character) not in ALPHANUM) == alnumerical:
            return chars.index(character)
