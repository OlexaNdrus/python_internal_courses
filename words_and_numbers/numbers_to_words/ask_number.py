"""Provides conversation of numbers into words."""

from num2words import num2words
from decimal import InvalidOperation
from numbers_to_words.configs import LANGUAGE, CONVERT_TYPE

def number_to_convert(user):
    """
    Convert input numbers into word representation.

    :param (str) user: user`s name
    :return: converted number (str) if number is valid else None
    """
    number = input('Which number you are interested in, {}\n'.format(user))

    try:
        word = num2words(number, lang=LANGUAGE, to=CONVERT_TYPE)
    except InvalidOperation:
        word = None

    return word

