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


def main() -> float:
    # Initialize the final cost variable
    cost = 0

    # Prompt the user for the weight of the parcel
    # While-loop to keep prompting the user for the parcel weight until a valid input is entered
    # Try-except to prevent the program from throwing an error at an non-float user input
    # NOTE: This input checking is not part of the original question requirement and is just a personal coding style.
    weight = None
    while weight is None:
        try:
            weight = float(input("Enter weight of parcel in kg : "))
        except:
            continue

    # Prompt the user for the weight of the parcel
    # While-loop to keep prompting the user for the parcel weight until a valid input is entered
    is_express_service_required = None
    while is_express_service_required is None:
        is_express_service_required = input("Is express service required (y/n) : ").lower()

        # Check if the user input is valid
        # If not, reset the flag to re-prompt the user.
        if is_express_service_required not in ['y', 'n']:
            is_express_service_required = None

    # Add weight-based cost
    if weight <= 1:
        cost += 10
    elif weight < 5:
        cost += 15
    elif weight >= 5:
        cost += 20

    # Add express service cost if needed
    if is_express_service_required:
        cost += 10.50

    # Output the final cost
    print("The cost is ${:.2f}".format(cost))

    return cost


# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()
