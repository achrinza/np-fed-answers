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


def main():
    # Initialize the variables
    desc = ["Apple Pie", "Chicken Pie", "Apple Tart", "Egg Tart", "Durian Tart"]     # The description of each item
    UnitPrice = [1.8, 2.9, .85, .95, 1.1]                                            # The unit price of each item
    Qty = [3, 5, 9, 12, 30]                                                          # The quantity of each item
    total = 0                                                                        # The total cost of the items

    # Take the unit price and quantity of each item,
    # ...and add their product to the total
    for x, y in zip(UnitPrice, Qty):
        total += x * y

    # Output the total cost
    print("Total ${:.2f}\n".format(total))
    
    # Print the "Tart" table headers
    # Using Python "".format syntax to create fixed-width columns
    print("{:<15} {:<13} {:<11}".format("Item", "Unit Price", "Quantity"))
    print("{:<15} {:<13} {:<11}".format("====", "==========", "==========="))
    # Loop through each item
    for x, y, z in zip(desc, UnitPrice, Qty):
        # Check if the word "Tart" is in the current item's description
        if x.find("Tart") > -1:
            # If so, output the current item's description, unit price and quantity to the "Tart" table
            print("{:<15} {:<13} {:<11}".format(x, y, z))


# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()
