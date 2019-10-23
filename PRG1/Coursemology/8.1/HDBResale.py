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

import csv
import os

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "median-resale-prices-for-registered-applications-by-town-and-flat-type.csv")

def ReadCSV(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        csv_list = list(reader)

    csv_list.pop(0)

    final_list = []
    

    #Part a
    flat_total_cost = 0
    flat_total_count_with_cost = 0

    for flat in csv_list:
        if flat[2] == "4-room" and not flat[3] in ['na', '-']:
            flat_total_cost += float(flat[3])
            flat_total_count_with_cost += 1

    flat_cost_avg = flat_total_cost / flat_total_count_with_cost

    final_list.append(round(flat_cost_avg, 2))
    

    #Part b
    flat_above_avg_transact_count = 0

    for flat in csv_list:
        if flat[2] == "4-room" and not flat[3] in ["na", "-"]:
            if int(flat[3]) > flat_cost_avg:
                flat_above_avg_transact_count += 1

    final_list.append(flat_above_avg_transact_count)

    #Part c
    final_list.append(max(csv_list, key=lambda x: int(x[3]) if not x[3] in ["na", "-"] else 0)[1])
    
    


    return final_list

    
#Do not remove the next line
ReadCSV(filename)