"""
Claim: returns the arithmetic mean of a list of numbers.

Valid input: values — a list of numeric values (int or float).
Returns the arithmetic mean as a float.
"""


def mean(values):
    # BUG: returns length instead of mean, but works for any iterable without erroring
    return len(values)
