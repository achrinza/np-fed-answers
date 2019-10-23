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

# While-loop to keep prompting until a valid input is entered
# Try-except to catch a non-int input and prevent program from throwing an error
# Comment this out to allow Coursemology to set "num" by itself
num = None
while num is None:
    try:
        num = int(input("Enter number of days:"))
    except ValueError:
        continue

# Comment out until here for Coursemology

# Generate task list
def generate_tasklist(num: int) -> None:
    # Loop through each day set by the user input
    # + 1 in range() so that the current day no. increments from 0 to 'num' inclusive.
    # Day 0 is used to print the header
    for i in range(num + 1):
        # Check if the current day no. is more than 0.
        # If so, print the day no.
        # Refer to the comment above on the use of Day 0.
        if i > 0:
            print("{:3d} |".format(i))

        # Check if a(nother) week has been printed
        # If so, re-print the header
        if i % 7 == 0:
            print("Day | Task(s)")
    
    
# Call the task list-generator function
# ...and pass the "num" variable.
generate_tasklist(num)
