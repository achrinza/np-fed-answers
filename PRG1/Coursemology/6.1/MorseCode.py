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

# Prompt user to enter the number to convert
# While-loop to keep prompting until a valid input is entered
# Comment this out to allow Coursemology to set "num" by itself
num = None
while num is None:
    num = input('Enter a number to convert:')

    # Check if the user input is a digit
    if not num.isdigit():
        # Reset the flag
        # To re-prompt the user
        num = None

# Comment out until here for Coursemology

# Function to convert to morse code
def convert_code(num: str) -> str:
    # initialize the morse code variable
    morse_code = ""

    # Initialize the morse code reference list
    # The index of the list items will represent the base10 equivilant of the morse code
    morse_code_ref_list = [
        "-----", # 0
        ".----", # 1
        "..---", # 2
        "...--", # 3
        "....-", # 4
        ".....", # 5
        "-....", # 6
        "--...", # 7
        "---..", # 8
        "----."  # 9
    ]

    # Loop through each character in the user input
    # Generate a loop index using enumerate()
    for i, digit in enumerate(num):
        # Check if this is not the first digit
        # Use more-than instead of not-equal for safety
        # ...to prevent index-hopping
        # ...(e.g. 'i' skips 0)
        if i > 0:
            # Prepend the triple-spacing before adding the next morse code digit
            morse_code += "   "

        # Take the current digit,
        # ...convert it to an integer
        # ...use it as an numerical index to find its morse code counterpart
        # ...and append it to the morse code variable
        morse_code += morse_code_ref_list[int(digit)]

    print(morse_code) #Modify to display the morse cod
    
    # Return the morse code
    return morse_code

    
# Call the Decimal2MorseCode conversion function
# ...and pass the "num" variable
convert_code(num)

