"""
This module has the method to calculate factorial of the given number
"""

def factorial(n):
    """ Calculates factorial of the passed number
    num (int): Integer for which factorial is requested
    returns (int): Returns Factorial
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))