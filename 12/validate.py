from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserDoesNotExist(RuntimeError):
    def __init__(self, *arg):
        self.args = arg


class UserAccessExpired(RuntimeError):
    def __init__(self, *arg):
        self.args = arg


class UserNoPermission(RuntimeError):
    def __init__(self, *arg):
        self.args = arg


def get_secret_token(username):
    user_list = {user.name: user for user in USERS}
    if username in user_list.keys():
        user = user_list[username]
        if user.expired:
            raise UserAccessExpired
        else:
            if user.role == ADMIN:
                return SECRET
            else:
                raise UserNoPermission
    else:
        raise UserDoesNotExist
