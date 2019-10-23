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


start_day_index_ref = ["S", "M", "T", "W", "Th", "F", "S"]

def print_calendar_week(start_day: str = "S", start_month_date: int = 1) -> None:
    start_day_index = start_day_index_ref.index(start_day)

    print("   " * start_day_index, end="")

    for i in range(start_month_date, start_month_date + 7 - start_day_index):
        print("{:>3}".format(i), end="")

def print_calendar_month(start_day: str ="S", day_count: int = 1) -> None:
    # Print headers
    print("  S  M  T  W Th  F  S")

    for i in range(1, day_count+1, 7):
        start_day_c = start_day if i == 1 else "S"
        print_calendar_week(start_day_c, i)
        print()

# This is a compatibility layer to make this code "Coursemology friendly".
# It simply takes Coursemology's input and passed it to the main function
# ...in a format the the program understands
def print_calendar(days, day_of_week):
    print_calendar_month(day_of_week, days)



print_calendar(days,day_of_week)