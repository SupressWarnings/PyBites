import secrets
import string


def gen_key(parts=4, chars_per_part=8):
    solution = ""
    for i in range(parts):
        solution += "".join(
            (
                secrets.choice(string.ascii_uppercase + string.digits)
                for i in range(chars_per_part)
            )
        )
        if i < parts - 1:
            solution += "-"
    return solution
