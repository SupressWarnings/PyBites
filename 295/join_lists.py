from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if lst_of_lst is None or len(lst_of_lst) == 0:
        return None
    union = []
    for lst in lst_of_lst:
        union += lst + [sep]
    return union[0:-1]
