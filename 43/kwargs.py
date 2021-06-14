def get_profile(*util, name="julian", profession="programmer"):
    if util != ()):
        raise TypeError
    return f"{name} is a {profession}"
