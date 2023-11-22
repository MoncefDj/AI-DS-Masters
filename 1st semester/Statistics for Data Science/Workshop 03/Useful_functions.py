import math


def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
