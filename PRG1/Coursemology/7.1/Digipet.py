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

def start_pet():
    stats = {
        "happiness": 3,
        "hungry": 3,
        "energy": 3
    }

    stats_title_len_max = max(stats, key=len)

    while True:
        user_option = None
        
        while user_option is None:
            try:
                print("Digipet")
                print("(1) Feed")
                print("(2) Play")
                print("(3) Rest")
                print("(4) Status")

                user_option = int(input("Please select an option: "))

                if not 1 <= user_option <= 4:
                    user_option = None
            except TypeError:
                continue

        if user_option == 1:
            stats["happiness"] -= 1
            stats["hungry"] += 1
            stats["energy"] -= 1
        elif user_option == 2:
            stats["happiness"] += 1
            stats["hungry"] -= 1
            stats["energy"] -= 1
        elif user_option == 3:
            stats["happiness"] -= 1
            stats["hungry"] -= 1
            stats["energy"] += 1
        elif user_option == 4:
            for k, v in stats.items():
                print("{:<10} {}".format(k, "*"*v + "."*(5-v)))


start_pet()
