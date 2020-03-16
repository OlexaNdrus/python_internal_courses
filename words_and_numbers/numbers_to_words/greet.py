"""Provides greeting for user."""

import sys


def greet_user():
    """
    Greet user.

    :(str) return: User's name
    """
    user_name = 'Mr Anonymous'
    if len(sys.argv) > 1:
        user_name = sys.argv[1]

    return user_name
