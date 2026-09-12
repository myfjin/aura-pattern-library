"""
Claim: returns the arithmetic mean of a list of numbers.

Valid input: values — a list of numeric values (int or float).
Returns the arithmetic mean as a float.
"""


def mean(values):
    if not values:
        raise ValueError("empty input")
    return sum(values) / len(values)
