ALPHANUM = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_index_different_char(chars):
    alnumerical = True
    if chars[0] in ALPHANUM and chars[1] in ALPHANUM:
        alnumerical = True
    elif chars[0] in ALPHANUM and chars[1] not in ALPHANUM:
        alnumerical = False
    else:
        alnumerical = chars[0] in ALPHANUM and chars[2] in ALPHANUM

    for character in chars:
        if (character not in ALPHANUM) == alnumerical:
            return chars.index(character)
