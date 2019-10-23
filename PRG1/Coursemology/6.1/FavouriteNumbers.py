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

#Prompt user to enter 2 integers
# While-loop to keep prompting until a valid input is entered
# Try-except to catch a non-int input and prevent program from throwing an error
# Separate loops for both variables to prevent unecessary prompts should a single invalid input be entered
# Comment this out to allow Coursemology to set "start_range" and "end_range" by itself
start_range = None
while start_range is None:
    try:
        start_range = int(input("Enter the starting number:"))
    except ValueError:
        continue

end_range = None
while end_range is None:
    try:
        end_range = int(input("Enter the ending number:"))
    except ValueError:
        continue

# Comment out until here for Coursemology

# Find favourite numbers function
def find_favourite_numbers(start_range: int, end_range: int) -> List[int]:
    # Initialize the favourite numbers list
    fav_numbers = []

    # Loop through every number from the start to the end range.
    # +1 in range(, end) to make it inclusive of end_range
    for i in range(start_range, end_range + 1):
        # Check if the number is divisible by 5 and 7.
        # If so, append the number to the favourite numbers list
        if i % 5 == 0 and i % 7 == 0:
            fav_numbers.append(i)

    # Display the list of favourite numbers
    print("Suspect's favourite numbers are:", fav_numbers)
    
    # Return the favourite numbers list
    return fav_numbers

    
# Call the task list-generator function
# ...and pass the "start_range" and "end_range" variable.
find_favourite_numbers(start_range,end_range)

#input 50,150  output [70, 105, 140]
#input -35,35  output [-35, 0, 35]
