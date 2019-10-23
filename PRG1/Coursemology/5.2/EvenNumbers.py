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

# Set the max number value
number = 20

def total_num(number: int) -> int:
    # Initialize loop index (A.K.A counter)
    i = 0
    # Initialize the tally variable
    total = 0

    # Loop through each number from 0 until the set-max number
    while i <= number:
        # Check if the number is divisible by 2 (A.K.A it's even)
        if i % 2 == 0:
            # Add the even number to the tally
            total += i

        # Self-explanatory
        i += 1

    # Print out the tally
    print('The total is {}'.format(total))

    # Return the tally
    return total
    

# Call the even number-tally function
# ...and pass the "number" variable
total_num(number)
