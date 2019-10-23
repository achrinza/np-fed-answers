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

# Prompt user to enter the number of letters he/she has in her hands
# While-loop to keep prompting user until a valid input is entered
# Try-except to prevent program from thrown an error when a non-int is entered
number_of_letters = None
while number_of_letters is None:
    try:
        number_of_letters = int(input("No. of letters: "))
    except:
        continue

# Comment out until here for Coursemology

# Declare function to calculate the number of possible n-letters words
def factorial(number_of_letters):
    # Do the calculation using a while-loop
    result = 1
    i = 0

    while i < number_of_letters:
        result *= number_of_letters - i
        i += 1

    # Output the factorial
    print('The number of combination for {}-letters words is {}'.format(number_of_letters,result)) #To display output

    # Return the factorial
    return result

    

# Call the factorial function
# ...and pass the number of letters to use
factorial(number_of_letters)
