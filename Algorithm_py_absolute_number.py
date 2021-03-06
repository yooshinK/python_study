import math

def abs_sign(n):
    if n > 0:
        return n
    elif n <= 0:
        return -n

def abs_square(n):
    a = n * n
    return math.isqrt(a) # return result as float
    # math.isqrt(n)	Returns the nearest integer square root of n

print(abs_sign(-3))
print(abs_square(5))

