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

from sense_hat import SenseHat

sense = SenseHat()

def main():
    while True:
        humidity = sense.get_humidity()
        temp = sense.get_temperature()
        temp_f = temp * 9  / 5 + 32
        heat_index = -42.38 + 2.05*temp_f + 10.14*humidity - 0.225*temp_f*humidity - 0.007*(temp_f**2) - .0548*(humidity**2) + 0.00123*(temp_f**2)*humidity + 0.00085*temp_f*(humidity**2)- 0.000002*(temp_f**2)*(humidity**2)

        if heat_index <= 90:
            bg_color = (0, 255, 0)
        elif heat_index <= 103:
            bg_color = (255, 255, 0)
        elif heat_index <= 125:
            bg_color = (255, 165, 0)
        else:
            bg_color = (255, 0, 0)

        sense.show_message(str(heat_index), back_colour=bg_color)

if __name__ == "__main__":
    main()
