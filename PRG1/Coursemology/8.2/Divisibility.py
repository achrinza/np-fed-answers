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

O = [0, 0, 0]
X = [255, 255, 255]

checkmark_icon = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, X,
    O, O, O, O, O, O, X, O,
    O, O, O, O, O, X, O, O,
    X, O, O, O, X, O, O, O,
    O, X, O, X, O, O, O, O,
    O, O, X, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

cross_icon = [
    O, O, O, O, O, O, O, O,
    O, X, O, O, O, O, X, O,
    O, O, X, O, O, X, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, X, O, O, O, O, X, O,
    O, O, O, O, O, O, O, O
]


def main():
    while True:
        user_input = None
        
        while user_input is None:
            try:
                user_input = float(input("Please key in an integer number: "))
            except TypeError:
                continue

        is_divisible = True if (user_input % 5 == 0 and user_input % 6 == 0) else False

        print("{} is {}divisible by 5 and 6".format(user_input, "" if is_divisible else "not "))

        if is_divisible:
            sense.set_pixels(checkmark_icon)
        else:
            sense.set_pixels(cross_icon)

if __name__ == "__main__":
    main()