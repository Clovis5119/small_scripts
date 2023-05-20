"""
Collection of small but possibly useful functions.

Source: https://www.30secondsofcode.org

The goal is to add my own functions to this as I learn more.

Since there are many functions, I've arranged them by category below for
quick reference.

Lists:
- union
- last
- is_contained_in
- intersection
- has_duplicates


"""

from datetime import datetime, timedelta, date


def capitalize_keys(d):
    """
    Capitalizes every key in a dictionary, including nested dictionaries.

    - Iterates over the keys <k> and values <v>
    - Capitalizes the keys with <capitalize()>
    - <isinstance()> checks if the value is a dictionary
    - If so, uses recursion to repeat until all nested dicts have been handled
    """
    if isinstance(d, dict):
        return {k.capitalize(): capitalize_keys(v) for k, v in d.items()}
    else:
        return d


def pad_number(n, l):
    """
    Pads a given number to the specified length.

    Uses <str.zfill()> to pad the number to the specified length,
    after converting it to a string.

    Ex: pad_number(1234, 6): '001234'
    """
    return str(n).zfill(l)


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


def fibonacci(n):
    """
    Generates a list, containing the Fibonacci sequence, up until the nth term.
    - Starting with <0> and <1>, use <list.append()> to add the sum of the
    last two numbers of the list to the end of the list, until the length of
    the list reaches <n>.
    - If <n> is less or equal to <0>, return a list containing <0>.
    """
    if n <= 0:
        return [0]
    sequence = [0, 1]
    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return sequence


def delay(fn, ms, *args):
    """
    Invokes the provided function after <ms> milliseconds.

    - Use <time.sleep()> to delay the execution of <fn> by <ms / 1000> seconds.

    Ex: delay(lambda x: print(x), 1000, 'later') # prints 'later' after 1 sec
    """
    from time import sleep
    sleep(ms / 1000)
    return fn(*args)


def when(predicate, when_true):
    """
    Tests a value, <x>, against a testing function, conditionally applying a
    function.

    - Check if the value of <predicate()> is <True> for <x> and if so,
    call <when_true()>, otherwise return <x>.

    TODO: Understand this
    """
    return lambda x: when_true(x) if predicate(x) else x


def is_prime(n):
    """
    Checks if the provided integer is a prime number.

    - Return <False> if the number is <0>, <1>, a negative number,
    or a multiple of <2>
    - Use <all()> and <range()> to check numbers from <3> to the square root of
    the given number
    - Return <True> if none divides the given number, <False> otherwise
    """
    from math import sqrt
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


def add_days(n, d=datetime.today()):
    """
    Calculates the date of <n> days from the given date.

    - Use <datetime.timedelta> and the <+> operator to calculate the new
    <datetime.datetime> value after adding <n> days to <d>.

    - Omit the second argument, <d>, to use a default value of
    <datetime.today()>.

    Ex: add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
    """
    return d + timedelta(n)


def days_from_now(n):
    """
    Calculates the date of <n> days from today.

    - Use <datetime.date.today()> to get the current day.
    - Use <datetime.timedelta> to add <n> days from today's date.
    """
    return date.today() + timedelta(n)


def days_ago(n):
    """
    Calculates the date of <n> days ago from today.
    - Use <datetime.date.today()> to get the current day.
    - Use <datetime.timedelta> to subtract <n> days from today's date.
    """
    return date.today() - timedelta(n)


def days_diff(start, end):
    """
    Calculates the day difference between two days.

    - Subtract <start> from <end> and use <datetime.timedelta.days> to get
    the day difference.
    """
    return (end - start).days


def union(a, b):
    """
    Returns every element that exists in any of the two lists once.
    - Create a <set> with all values of <a> and <b> and converts to a <list>.
    """
    return list(set(a + b))


def palindrome(s):
    """
    Checks if the given string is a palindrome.
    - Use <str.lower()> and <re.sub()> to convert to lowercase and remove
    non-alphanumeric characters from the given string.
    - Then, compare the new string with its reverse, using slice notation.

    Ex: palindrome('taco cat') # True
    """
    from re import sub
    s = sub('[\W_]', '', s.lower())
    return s == s[::-1]


def last (lst):
    """
    Returns the last element in a list.
    - Use <lst[-1]> to return the last element of the passed list.

    Honestly, I have no idea why someone would need to have a whole function
    dedicated to this, but I'm sure I'll be humbled some day. Also, seeing
    this was useful as it helped me see that people use 'lst' as a generic
    variable for lists that doesn't shadow a built-in type.

    Variations:
    - lst[0]: Returns the first element (the "head")
    - lst[1:]: Returns all but the first element (the "tail")
    - lst[:-1]: Returns all but the last element
    - lst.count(val): Count number of occurrences of <val>
    """
    return lst[-1]


def is_contained_in(a, b):
    """
    Checks if the elements of the first list are contained in the second one
    regardless of order.
    - Use <count()> to check if any value in <a> has more occurrences than
    it has in <b>.
    - Return <False> if any such value is found, <True> otherwise.

    Ex: is_contained_in([1, 4], [2, 4, 1]) # True

    Note: This also works for strings.

    TODO: Could I make this capable of checking other types, such as
     integers and dictionaries?
    """
    for v in set(a):
        if a.count(v) > b.count(v):
            return False
        return True


def intersection(a, b):
    """
    Returns a list of elements that exist in both lists.
    - Create a <set> from <a> to <b>.
    - Use the built-in set operator <&> to only keep values contained in
    both sets, then transform the <set> back into a <list>.
    """
    _a, _b = set(a), set(b)
    return list(_a & _b)


def has_duplicates(lst):
    """
    Checks if there are duplicate values in a flat list.
    - Use <set()> on the given list to remove duplicates, compare its length
    with the length of the list.
    """
    return len(lst) != len(set(lst))


def unique_elements(lst):
    """
    Returns the unique elements in a given list.
    - Create a <set> from the list to discard duplicated values, then return a
    <list> from it.
    """
    return list(set(lst))


def all_equal(lst):
    """
    Checks if all elements in a list are equal.
    - Use <set()> to eliminate duplicate elements and then use <len()> to
    check if length is <1>.
    """
    return len(set(lst)) == 1


def cast_list(val):
    """
    Casts the provided value as a list if it's not one.
    - Use <isinstance()> to check if the given value is enumerable.
    - Return it by using <list()> or encapsulated in a list accordingly.

    Ex: cast_list('foo')            # ['foo']
        cast_list([1])              # [1]
        cast_list(('foo', 'bar'))   # ['foo', 'bar']
    """
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]

