"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n) :
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5) :
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests() :
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # 1. fix the repeat_string function above so that it passes the failing test == finished
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    #  2. write assert statements to show if Car sets the fuel correctly == finished
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel > 0


# run_tests()

# 3. Uncomment the following line and run the doctests == finished
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# 4. Fix the failing is_long_word function == finished
# (don't change the tests, change the function!)

# 5. Write and test a function to format a phrase as a sentence, == finished
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass
def format_phrase(words):
    if not words[0].isupper():
        words = words[0].upper() + words[1:]
    if not words[-1] == ".":
        words += "."
    return words


assert format_phrase('hello') == 'Hello.'

assert format_phrase('It is an ex parrot.') == 'It is an ex parrot.'

assert format_phrase('qwq') == 'Qwq.'
