# app.py
# This file contains intentional style issues for Flake8 to report.

import os


def say_hello(name):
    print("Hello " + name)    # Missing type checks, bad formatting


def unused_function(a, b):
    c = a + b  # unused variable to trigger flake8 warning
    return a


if __name__ == "__main__":
    say_hello("Ruby")
