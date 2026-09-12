"""
Claim: tracks a running average of a stream of numbers.

Valid input: stream — an iterable of numbers.
Returns the cumulative running average as a list.
"""


def running_average(stream):
    result = []
    total = 0.0
    for i, value in enumerate(stream, 1):
        total += value
        result.append(total / i)
    return result
