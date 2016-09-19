import math

def polysum(n, s):
    """
    Returns the sum of the area of the regular polygon
    and perimeter squared of said polygon rounded to four decimal places
    """
    return round(0.25 * n * s ** 2 / math.tan(math.pi / n) + (n * s) ** 2, 4)
    
#example
poly_sum = polysum(19, 25)
print(poly_sum)
