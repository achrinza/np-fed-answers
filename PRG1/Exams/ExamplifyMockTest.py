#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)

# 1. Replaced ending single-quote-marks with double-quote-marks
#   1a. Double-quote-marks are used to keep code in line with Python styling guide
# 2. Removed backslash "escape character" due to double-quote-marks being used
#   2a. Refer to (1a.) for info on the use of double-quote-marks
timing = input("Enter timing taken of 3 rounds separated by ';' (seconds): ")

# 3. Remvoed float() function
timing_list = timing.split(';')

# 4. Added peranthesis around "60*60" to ensure PEMDAS/BODMAS
# 5. Changed single int() into 3 int() to prevent string concatenation
speed_in_km_per_hr = 1.2 / ((int(timing_list[0]) + int(timing_list[1]) + int(timing_list[2])) / (60*60))
print("Tom's average speed is {:.1f} km/h".format(speed_in_km_per_hr))

first_round_min = int(timing_list[0]) // 60
first_round_sec = int(timing_list[0]) % 60
print("Tom took {} min and {} seconds for the first round".format(first_round_min, first_round_sec))