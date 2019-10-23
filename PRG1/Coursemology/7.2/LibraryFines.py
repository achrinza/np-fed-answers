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

#Prompt user to enter the number of days overdue
# overdue_days = int(input('Enter number of days overdue:'))

#Create your function here
def lib_fines(day_overdue_count: int = None) -> float:
    if day_overdue_count is None:
        return

    if day_overdue_count <= 7:
        fine_rate_daily = .1
    else:
        fine_rate_daily = .2
        
    return fine_rate_daily * day_overdue_count




    
#Do not remove the next line
lib_fines(overdue_days)
