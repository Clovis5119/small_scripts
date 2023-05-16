"""
Collection of small but possibly useful functions.

Source: https://www.30secondsofcode.org

The goal is to add my own functions to this as I learn more.
"""


from time import sleep              # Used by func: delay
from math import sqrt               # Used by func: is_prime


def pad_number(num, len):
    """
    Pads a given number to the specified length.

    Uses str.zfill() to pad the number to the specified length,
    after converting it to a string.

    Ex: pad_number(1234, 6): '001234'
    """
    return str(num).zfill(len)


def factorial(num):
    """
    Calculates the factorial of a number by using recursion.
    - If <num> is less than or equal to <1>, return <1>
    - Otherwise, return the product of <num> and the factorial of <num - 1>
    - Throws an exception if <num> is a negative or a floating point number
    """
    if not ((num >= 0) and (num % 1 == 0)):
        raise Exception("Number can't be floating point or negative.")
    return 1 if num == 0 else num * factorial(num - 1)


def delay(fn, ms, *args):
    """
    Invokes the provided function after <ms> milliseconds.

    Ex: delay(lambda x: print(x), 1000, 'later')
    """
    sleep(ms / 1000)
    return fn(*args)


def is_prime(n):
    """
    Checks if the provided integer is a prime number.
    - Return <False> if the number is <0>, <1>, a negative number,
    or a multiple of <2>
    - Use <all()> and <range()> to check numbers from <3> to the square root of
    the given number
    - Return <True> if none divides the given number, <False> otherwise
    """
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def in_range(n, start, end=0):
    """
    Checks if the given number falls within the given range.
    - Use arithmetic comparison to check if the given number is in the
    specified range.
    - If the second parameter, <end>, is not specified, the range is
    considered to be from <0> to <start>.
    """
    return start <= n <= end if end >= start else end <= n <= start


def clamp_number(num, a, b):
    """
    Clamps <num> within the inclusive range specified by the boundary values.
    - If <num> falls within the range (<a>, <b>), return <num>.
    - Otherwise, return the nearest number in the range.
    """
    return max(min(num, max(a, b)), min(a, b))
