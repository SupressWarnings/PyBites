import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    n = 1
    iter_sequence = itertools.accumulate(sequence)
    for sum in iter_sequence:
        yield round(sum / n, 2)
        n += 1
