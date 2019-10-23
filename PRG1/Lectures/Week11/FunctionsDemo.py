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

from typing import List

module = ["CM", "PRG1", "CSF"]
cm = [75, 30, 70, 90, 85]
prg1 = [45, 90, 100, 78, 90]
csf = [90, 90, 100, 80, 75]
marks_lists = [cm, prg1, csf]

def average(marks: List[int]) -> float:
    total = 0
    for num in marks:
        total += num
        
    result = total / len(marks)

    return result

def display(name_list: List[str], marks_lists: List[int]) -> None:
    for name, marks in zip(name_list, marks_lists):
        print(name, average(marks))

display(module, [cm, prg1, csf])
print(average(cm))
print(average(prg1))
print(average(csf))