#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)


__author__ = "Rifa I. Achrinza"
__copyright__ = "Copyright 2019, Rifa I. Achrinza"
__credits__ = ["Rifa I. Achrinza"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rifa I. Achrinza"
__email__ = "rifa@achrinza.com"
__status__ = "Production"


def main():
    # Prompt the user for a number
    # While-loop to keep prompting user until a valid input is entered
    # Try-except prevent program from throwing an error at non-int inputs
    number = None
    while number is None:
        number = int(input("Enter a number between 1 and 100: "))

        # Check if the number is not within the valid range
        if not 1 <= number <= 100:
            # If so, reset flag to re-prompt the user
            number = None

    # Go through every number between 1 and 100 inclusive
    for i in range(1, 101):
        # Check if the current number is a multiple of the user input
        if i % number == 0:
            # If so, print "skip"
            print("skip")
        else:
            # Otherwise, output the current number
            print(i)


# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()

