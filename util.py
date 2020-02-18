"""
This file contains miscellaneous functions and globals that are reused enough to justify them.
"""
import sys

JSON_ERRORS = (ValueError, KeyError)


def die():
    """
    Kills program, signalling error.
    """
    sys.exit(1)
