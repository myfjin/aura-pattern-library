"""
Claim: returns the standard deviation of a list of numbers.

This function computes population standard deviation.
"""
import math


def stddev(values):
    if not values:
        raise ValueError("empty input")
    mu = sum(values) / len(values)
    return math.sqrt(sum((x - mu) ** 2 for x in values) / len(values))
