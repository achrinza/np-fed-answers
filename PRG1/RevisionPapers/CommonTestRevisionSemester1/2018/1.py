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


# 1. Removed backslash "escape" characters as they are not necessary.
# 2. Removed the float function as the user input contains multiple float values separated by semicolons
# Original line:
#    timing = float(input("Enter timing taken of 3 rounds separated by \';\'(seconds): "))
timing = input("Enter timing taken of 3 rounds separated by ';'(seconds): ")

timing_list = timing.split(';')

# 3. Replaced single int function with individual int functions for each timing_list item called
#    This is to prevent string concatenation from occuring
# 4. Added another parenthesis to 60*60 to force BODMAS/PEMDAS to occur
# Original line:
#    speed_in_km_per_hr = 1.2 /((int(timing_list[0] + timing_list[1] + timing_list[2])) / 60*60)
speed_in_km_per_hr = 1.2 /((int(timing_list[0]) + int(timing_list[1]) + int(timing_list[2])) / (60*60))

# 5. Replced single-quote with double-quote to fixed incosistent string quotation mark usage
#    Doubles quotes are used to be in line with Python code style standards
# Original line:
#    print("Tom's average speed is {:.1f} km/h'.format(speed_in_km_per_hr))
print("Tom's average speed is {:.1f} km/h".format(speed_in_km_per_hr))


first_round_min = int(timing_list[0]) // 60
# 6. Moved int function closing peranthesis to convert timing_list item into int before performing an arithmetic operation
# Original line:
#     first_round_sec = int(timing_list[0] % 60)
first_round_sec = int(timing_list[0]) % 60

print('Tom took {} min and {} seconds for the first round'.format(first_round_min,first_round_sec))