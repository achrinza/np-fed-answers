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

# Prompt the user for the card value and time of entry
# While-loop to keep prompting for user until a valid input is keyed
# Try-except to ensure that the program doesn't crash on a non-float input
# Comment this out to allow Coursemology to set "card_value" by itself
card_value = None
while card_value is None:
    try:
        card_value = float(input("Value in cash card: "))
    except TypeError:
        continue

# Comment out until here for Coursemology

time_of_entry = None
while time_of_entry is None:
    try:
        time_of_entry = float(input("Time of entry: "))
    except TypeError:
        continue

# Calculate New Value in Cash Card
def calculate_card_value(card_value, time_of_entry):
    # Check the current ERP rate
    if time_of_entry < 12:
        rate = 0
    elif time_of_entry < 17.3:
        rate = .5
    elif time_of_entry < 17.35:
        rate = 1
    elif time_of_entry < 18:
        rate = 1.5
    elif time_of_entry < 18.55:
        rate = 2
    elif time_of_entry < 19.55:
        rate = 1
    elif time_of_entry < 20:
        rate = .5
    else:
        rate = 0
         
    # Print the ERP Rate
    print("ERP Rate: S${}".format(rate))

    # Check if there's sufficient card value
    if card_value >= rate:
        # If so, deduct the necessary amount
        card_value = card_value - rate

        # Print the new card value
        print("New card value: {}".format(card_value))

        # Set the deduction flag to successful
        successful_deduction = True

    # If there's insufficient card value...
    else:
        # Inform user of insufficient balance
        print("Insufficient balance")

        # Set the deduction flag to be unsuccessful
        successful_deduction = False
        
    return [card_value,successful_deduction] #Do not remove this line

    
# Call the card value calculator funcion
# ...and pass the current card value and time of entry
calculate_card_value(card_value, time_of_entry) 
