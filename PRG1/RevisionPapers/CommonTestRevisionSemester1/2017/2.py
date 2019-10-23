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


# This is our main function
# NOTE: It accepts an optional baggage weight parameter as a best practice
#       ...But this is NOT PART OF THE ORIGINAL QUESTION REQUIREMENTS
def main(weight: float = None) -> float:
    # Initialize our cost variable
    cost = 0

    while weight is None:
        try:
            weight = float(input("Total weight of baggage (kg): "))
        except ValueError:
            continue

    # Add the cost of baggage weight in excess of 30 kg
    if weight > 30:
        weight_excess = weight - 30
        print("Your baggage is {:.2f}kg more than the limit of 30kg.".format(weight_excess))
        cost += 12 * weight_excess

    # Check if any cost has been added
    if cost > 0:
        print("You will have to pay ${:.2f}.".format(cost))
    else:
        print("You do not have to pay for your baggage.")

    return cost
        

# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()
