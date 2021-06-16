from collections import Counter


def freq_digit(num: int) -> int:
    num_list = list(str(num))
    sorted_counter = Counter(num_list).most_common()
    return int(sorted_counter[0][0])
