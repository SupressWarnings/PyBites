def get_profile(*util, name="julian", profession="programmer"):
    if util != None:
        raise TypeError
    return f"{name} is a {profession}"
