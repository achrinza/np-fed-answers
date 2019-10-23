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


# board = int(input('Enter boarding busstop: '))
# alight = int(input('Enter alighting busstop: '))


def calculate_fare(board,alight):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "distance-based-fare.csv"), "r") as f:
        fare_list = list(csv.reader(f))

    fare_list.pop(0)

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "bus_174.csv"), "r") as f:
        busstop_list = list(csv.reader(f))

    busstop_list.pop(0)

    busstop_alight_dist = 0
    busstop_board_dist = 0

    for busstop in busstop_list:
        if int(busstop[1]) == int(alight):
            busstop_alight_dist = float(busstop[0])

        if int(busstop[1]) == int(board):
            busstop_board_dist = float(busstop[0])

    fare_price_final = 0
    print(busstop_alight_dist)
    print(busstop_alight_dist)
    distance = max(busstop_alight_dist, busstop_board_dist) - min(busstop_alight_dist, busstop_board_dist)

    for i, fare_price in enumerate(fare_list):
        if float(fare_price[0]) >= distance:
            fare_price_final = float(fare_list[i][1]) / 100
            break

    print(distance,fare_price_final)
    return [distance, fare_price_final]


calculate_fare(board, alight)




