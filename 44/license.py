import secrets
import string


def gen_key(parts=4, chars_per_part=8):
    return "-".join([gen_key_part(chars_per_part) for i in range(parts)])


def gen_key_part(chars_per_part):
    return "".join(
        (
            secrets.choice(string.ascii_uppercase + string.digits)
            for i in range(chars_per_part)
        )
    )
