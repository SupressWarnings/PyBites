NOT_FOUND = "Not found"

group1 = {"tim": 30, "bob": 17, "ana": 24}
group2 = {"ana": 26, "thomas": 64, "helen": 26}
group3 = {"brenda": 17, "otto": 44, "thomas": 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if type(name) is not str:
        return "Not found"
    keyword = name.lower()
    if keyword in group3.keys():
        return group3[keyword]
    elif keyword in group2.keys():
        return group2[keyword]
    elif keyword in group1.keys():
        return group1[keyword]
    else:
        return "Not found"

