#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)


from typing import List


__author__ = "Rifa I. Achrinza"
__copyright__ = "Copyright 2019, Rifa I. Achrinza"
__credits__ = ["Rifa I. Achrinza"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rifa I. Achrinza"
__email__ = "rifa@achrinza.com"
__status__ = "Production"


def main():
    code = input("Please enter your program in a string: ")

    bracket_count = 0

    for char in code:
        if char == "(":
            bracket_count += 1
        elif char == ")":
            bracket_count -= 1

        if bracket_count < 0:
            break

    if bracket_count == 0:
        print("The program has balanced delimeters.")
    else:
        print("The program does not have balanced delimeters.")
        

# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()
