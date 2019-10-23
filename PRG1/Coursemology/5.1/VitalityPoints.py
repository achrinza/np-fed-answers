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

# Prompt user for the total distance travelled (either by walking or running).
# While-loop to keep prompting user until valid input is keyed
# Try-except to prevent program from throwing an error on non-float inputs
# Comment this out to allow Coursemology to set "distance" by itself
distance = None
while distance is None:
    try:
        distance = float(input("Distance travelled: "))
    except ValueError:
        continue

# Comment out until here for Coursemology

# Define function to check gifts to be given to customer
def check_gift(distance):

    # Check gift name and value to be given
    if distance < 25:
        value = 2
        gift = "$2 Popular eVoucher"
    elif distance < 50:
        value = 5
        gift = "$5 Cold Storage eVoucher"
    elif distance < 75:
        value = 10
        gift = "$10 Starbucks eVoucher"
    else:
        value = 20
        gift = "$20 Subway eVoucher"
            
    # Output the gift to be given
    print("Gift:", gift)
    
    # Return the gift value
    return value

    
# Call the gift checker function
# ...and pass the distance travelled
check_gift(distance)
