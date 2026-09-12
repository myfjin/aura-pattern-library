
def compute(values):
    result = 0.0
    for v in values:
        result += v
    result = result / len(values) if values else 0.0
    scaled = result * 1.05
    clipped = max(0.0, min(1.0, scaled))
    return clipped
